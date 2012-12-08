%define major 5
%define libname %mklibname %{name} %{major}
%define develname %mklibname -d %name
%define	sgmlbase %{_datadir}/sgml

Summary: The OpenJade Group's SGML and XML parsing tools
Name: opensp
Version: 1.5.2
Release: 12
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
%{sgmlbase}/%{name}-%{version}/doc/*
%{sgmlbase}/%{name}-%{version}/OpenSP/*
%{_mandir}/man1/*

%files -n %{libname}
%{_libdir}/libosp.so.%{major}*

%files -n %{develname}
%{_libdir}/lib*.so
%{_includedir}/OpenSP


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.5.2-9mdv2011.0
+ Revision: 653255
- add more obsoletes
- rename spec file and devel package name
- lowercase the package name
- bunzip2 the aptch

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 1.5.2-7mdv2010.1
+ Revision: 485962
- BR dtd412

  + Christophe Fergeau <cfergeau@mandriva.com>
    - rebuild

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.5.2-5mdv2009.0
+ Revision: 223373
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-4mdv2008.1
+ Revision: 178765
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 21 2007 Christiaan Welvaart <spturtle@mandriva.org> 1.5.2-3mdv2008.0
+ Revision: 42318
- add version to devel provides

* Fri Jun 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.5.2-2mdv2008.0
+ Revision: 37270
- fix major
- new version
- update patches (Frederic Himpe)

* Thu Apr 19 2007 Andreas Hasenack <andreas@mandriva.com> 1.5-12mdv2008.0
+ Revision: 14997
- Import OpenSP



* Sat Sep 02 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.5-1mdv2007.0
- Rebuild

* Sun May 28 2006 Stefan van der Eijk <stefan@eijk.nu> 1.5-11mdk
- %%mkrel

* Fri Apr 14 2006 Christiaan Welvaart <cjw@daneel.dyndns.org> 1.5-10mdk
- patch3: try to find an external DTD's public ID in the local 
          catalogs before dereferencing the system ID

* Thu Nov 03 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.5-9mdk
- Rebuild

* Thu Jun 10 2004 Götz Waschk <waschk@linux-mandrake.com> 1.5-8mdk
- rebuild for broken libstdc++6-devel-3.4.1-0.2mdk

* Thu Jun  3 2004 Montel Laurent <lmontel@n2.mandrakesoft.com> 1.5-7mdk
- Rebuild 

* Mon Nov 24 2003 Stefan van der Eijk <stefan@eijk.nu> 1.5-6mdk
- rebuild 4 reupload (alpha)

* Mon Jul 21 2003 Frederic Crozat <fcrozat@mandrakesoft.com> - 1.5-5mdk
- Rebuild

* Wed Jun 11 2003 Warly <warly@mandrakesoft.com> 1.5-4mdk
- Fix Per Øyvind Karlse patch 0 to be able to build openjade 1.3.2

* Fri Jun 06 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.5-3mdk
- compile with same options as openjade
- Patch1 from RH

* Fri Jun 06 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.5-2mdk
- gcc-3.3 fix from RH (Patch0)

* Mon Feb  3 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 1.5-1mdk
- Initial Mandrake package
