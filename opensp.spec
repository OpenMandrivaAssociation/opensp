%define major	5
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}
%define	sgmlbase %{_datadir}/sgml

Summary:	The OpenJade Group's SGML and XML parsing tools
Name:		opensp
Version:	1.5.2
Release:	17
License:	BSD
Group:		Publishing
Url:		http://openjade.sourceforge.net/
Source0:	http://download.sourceforge.net/openjade/OpenSP-%{version}.tar.bz2
Patch0:		OpenSP-1.5-prefer-catalog-entries.patch
Patch1:		opensp-1.5.2-multilib.patch
Patch2:		opensp-1.5.2-nodeids.patch

BuildRequires:	docbook-dtd412-xml
BuildRequires:	xmlto
BuildRequires:	gettext-devel
%rename OpenSP

%description
This package is a collection of SGML/XML tools called OpenSP. It is a fork from
James Clark's SP suite. These tools are used to parse, validate, and normalize
SGML and XML files.  
     
%package -n %{libname}
Summary:	Runtime library for the OpenJade group's SP suite
Group:		System/Libraries

%description -n %{libname}
This is the SP suite's shared library runtime support.  This C++
library contains entity management functions, parsing functions, and
other functions useful for SGML/XML/DSSSL development.

%package -n %{devname}
Summary:	Libraries and include files for developing OpenSP applications
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This contains include files and libraries for OpenSP.
This C++ library contains entity management functions, parsing functions,
and other functions useful for SGML/XML/DSSSL development.

%prep
%setup -qn OpenSP-%{version}
%apply_patches
#fix build with new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*
autoreconf -fi

%build
%configure2_5x \
	--disable-static \
	--enable-http \
	--enable-default-catalog=%{_sysconfdir}/sgml/catalog  \
	--enable-default-search-path=%{sgmlbase} \
	--datadir=%{sgmlbase}/%{name}-%{version}

%make

%install
%makeinstall_std
%find_lang OpenSP

#remove unpackaged files
rm -rf %{buildroot}%{_prefix}/doc  %{buildroot}%{_docdir}/OpenSP

%files -f OpenSP.lang
%doc doc/*.htm ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{sgmlbase}/%{name}-%{version}/doc/*
%{sgmlbase}/%{name}-%{version}/OpenSP/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libosp.so.%{major}*

%files -n %{devname}
%{_libdir}/lib*.so
%{_includedir}/OpenSP

