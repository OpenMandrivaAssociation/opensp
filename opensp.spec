%define major 5
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name
%define	sgmlbase %{_datadir}/sgml

Summary: The OpenJade Group's SGML and XML parsing tools
Name: opensp
Version: 1.5.2
Release: 10
License: BSD
Group: Publishing
URL: http://openjade.sourceforge.net/
Source0: http://download.sourceforge.net/openjade/OpenSP-%{version}.tar.bz2
Patch0: OpenSP-1.5-prefer-catalog-entries.patch
Patch1: opensp-1.5.2-multilib.patch
Patch2: opensp-1.5.2-nodeids.patch
BuildRequires: xmlto
BuildRequires: docbook-dtd412-xml
%rename OpenSP

%description
This package is a collection of SGML/XML tools called OpenSP. It is a fork from
James Clark's SP suite. These tools are used to parse, validate, and normalize
SGML and XML files.  
     
%package -n %{libname}
Summary: Runtime library for the OpenJade group's SP suite
Group: System/Libraries
Obsoletes: %{_lib}OpenSP5 < 1.5.2-8

%description -n %{libname}
This is the SP suite's shared library runtime support.  This C++
library contains entity management functions, parsing functions, and
other functions useful for SGML/XML/DSSSL development.

%package -n %{develname}
Summary: Libraries and include files for developing OpenSP applications
Group: Development/C
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: OpenSP-devel = %{version}-%{release}
Obsoletes: %{_lib}OpenSP5-devel < 1.5.2-8

%description -n %{develname}
This contains include files and libraries for OpenSP.
This C++ library contains entity management functions, parsing functions,
and other functions useful for SGML/XML/DSSSL development.

%prep
%setup -qn OpenSP-%{version}
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-http \
	--enable-default-catalog=%{_sysconfdir}/sgml/catalog  \
	--enable-default-search-path=%{sgmlbase} \
	--datadir=%{sgmlbase}/%{name}-%{version}

%make

%install
rm -rf "%{buildroot}"
%makeinstall_std
%find_lang sp5

#remove unpackaged files
rm -rf %{buildroot}%{_prefix}/doc  %{buildroot}%{_docdir}/OpenSP

%files -f sp5.lang
%doc doc/*.htm ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{sgmlbase}/%{name}-%{version}/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libosp.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/OpenSP
