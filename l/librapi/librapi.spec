# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: /usr/bin/pyrexc gcc-c++ pkgconfig(dbus-1) pkgconfig(dbus-glib-1) pkgconfig(libsynce) python-devel
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%{!?python_sitearch: %define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}

Name:           librapi
Version:        0.15.2
Release:        alt2_10
Summary:        Library to connect to Pocket PC devices

Group:          System/Libraries
License:        MIT
URL:            http://www.synce.org
Source0:        http://download.sf.net/synce/librapi2-%{version}.tar.gz
Patch0:         librapi2-dso.patch

BuildRequires:  libsynce-devel >= 0.15.1
BuildRequires:  python-module-Pyrex
BuildRequires:  libdbus-devel libdbus-glib-devel
BuildRequires:  libudev-devel
BuildRequires:  libtool

# Provide an upgrade path from the monilithic synce package
Provides:       synce = %{version}-%{release}
Obsoletes:      synce <= 0.9.1-10
Source44: import.info

%description
The RAPI library is an open source implementation that works like RAPI.DLL,
available on Microsoft operating systems. The library makes it possible to make
remote calls to a computer running Pocket PC.
In order to use librapi, a daemon that the Pocket PC client connects to must be
running on the computer using librapi.

%package devel
Summary: Development libraries and header files for librapi
Group: Development/C
Requires: %{name} = %{version}
Requires: pkgconfig

%description devel
This package contains the header files and link libraries for librapi

%package -n python-module-rapi
Summary: Python bindings to librapi (part of SynCE)
Group: Development/Python
Requires: %{name} = %{version}

%description -n python-module-rapi
This package contains the python bindings to librapi, a component
of the SynCE PocketPC connection framework.
The python module to import is named "pyrapi2"


%prep
%setup -q -n librapi2-%{version}
%patch0

# Prevent configure from killing CFLAGS
sed -i -e 's,^\(CFLAGS=\"\"\),#\1,' configure*
# Fix up timestamps to avoid re-running autotools
touch -r aclocal.m4 configure*

%build
%configure \
--disable-hal-support \
--enable-udev-support \
--disable-static --disable-rpath
make LIBTOOL=/usr/bin/libtool %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.{la,a}
rm -f $RPM_BUILD_ROOT%{python_sitelibdir}/pyrapi2.{la,a}

%files
%doc BUGS ChangeLog README README.contributing TODO
%{_bindir}/*
%{_libdir}/librapi.so.2*
%{_mandir}/man1/*

%files devel
%doc README.design
%{_includedir}/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*

%files -n python-module-rapi
%{python_sitelibdir}/pyrapi2.so


%changelog
* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.15.2-alt2_10
- update to new release by fcimport

* Tue Nov 17 2015 Igor Vlasenko <viy@altlinux.ru> 0.15.2-alt2_7
- rebuild

* Thu Mar 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.15.2-alt2
- resurrected from orphaned

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15.2-alt1.1
- Rebuild with Python-2.7

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Wed Feb 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.15.1-alt1
- 0.15.1
- build withouth hal support
- disable versioning

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.1
- Rebuilt with python 2.6

* Fri Aug 21 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14
- add versioning

* Sun Mar 01 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13.1-alt1
- 0.13.1
- rename python package to python-module-librapi
- removed pre/post scripts

* Sun Oct 05 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12
- fix link with python

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.11-alt1.1
- Rebuilt with python-2.5.

* Wed Jan 09 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- 0.11

* Thu Jan 03 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt3
- update to SVN 20080102 version

* Fri Dec 07 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt2
- update to SVN 20071207 version

* Mon May 14 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.10.0-alt1
- 0.10.0
- buildreq updated
- removed old hack with chrpath

* Fri Jan 12 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Tue May 02 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt4
- pcp fix on x86_64 (patch by Andrzej Szombierski)

* Sun Feb 26 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt3
- x86_64 support

* Tue Feb 21 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt2
- FUR support

* Sun Jul 24 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Wed Sep 01 2004 Michael Shigorin <mike@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Sun Apr 25 2004 Michael Shigorin <mike@altlinux.ru> 0.8.9-alt1
- 0.8.9

* Thu Dec 18 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt4
- worked around changed behaviour of chrpath regarding non-ELF input

* Wed Dec 17 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt3
- removed *.la *and* uploaded -proper- packages, oops :-)

* Fri Nov 28 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt2
- removed *.la and devel-static subpackage

* Fri Nov 07 2003 Michael Shigorin <mike@altlinux.ru> 0.8.1-alt1
- built for ALT Linux

