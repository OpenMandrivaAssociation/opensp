%define lib_major 5
%define lib_name %mklibname %{name} %{lib_major}
%define	sgmlbase %{_datadir}/sgml

Summary: The OpenJade Group's SGML and XML parsing tools
Name: OpenSP
Version: 1.5.2
Release: %mkrel 7
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: BSD
Group: Publishing
Source: http://download.sourceforge.net/openjade/%{name}-%{version}.tar.bz2
Patch0: OpenSP-1.5-prefer-catalog-entries.patch
Patch1: opensp-1.5.2-multilib.patch
Patch2: opensp-1.5.2-nodeids.patch
URL: http://openjade.sourceforge.net/
BuildRequires: xmlto
BuildRequires: docbook-dtd412-xml

%description
This package is a collection of SGML/XML tools called OpenSP. It is a fork from
James Clark's SP suite. These tools are used to parse, validate, and normalize
SGML and XML files.  
     
%package -n %{lib_name}
Summary: Runtime library for the OpenJade group's SP suite
Group: System/Libraries

%description -n %{lib_name}
This is the SP suite's shared library runtime support.  This C++
library contains entity management functions, parsing functions, and
other functions useful for SGML/XML/DSSSL development.

%package -n %{lib_name}-devel
Summary: Libraries and include files for developing OpenSP applications
Group: Development/C
Requires: %{lib_name} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{lib_name}-devel
This contains include files and libraries for OpenSP.
This C++ library contains entity management functions, parsing functions,
and other functions useful for SGML/XML/DSSSL development.

%prep
%setup -q
%patch0 -p1 -b .try_catalogs_first
%patch1 -p1 -b .multilib
%patch2 -p1 -b .nodeids

%build
%configure2_5x --enable-static --enable-http \
 --enable-default-catalog=%{_sysconfdir}/sgml/catalog  \
 --enable-default-search-path=%{sgmlbase} \
 --datadir=%{sgmlbase}/%{name}-%{version}
%make

%install

test "$RPM_BUILD_ROOT" = "/" || rm -rf "$RPM_BUILD_ROOT"
%makeinstall_std

%find_lang sp

#remove unpackaged files
rm -rf $RPM_BUILD_ROOT%{_prefix}/doc  $RPM_BUILD_ROOT%{_docdir}/OpenSP

%clean
test "$RPM_BUILD_ROOT" = "/" || rm -rf "$RPM_BUILD_ROOT"

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -f sp.lang
%defattr(-, root, root)
%doc doc/*.htm ABOUT-NLS AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/*
%{sgmlbase}/%{name}-%{version}/*
%{_mandir}/man1/*


%files -n %{lib_name}
%defattr(-, root, root)
%{_libdir}/libosp.so.%{lib_major}*

%files -n %{lib_name}-devel
%defattr(-, root, root)
%{_libdir}/lib*.so
%{_libdir}/lib*.a
%{_libdir}/lib*.la
%{_includedir}/OpenSP
