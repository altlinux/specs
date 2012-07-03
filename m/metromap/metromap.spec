Name: metromap
Version: 0.1.4
Release: alt1

Summary: Metro (subway) navigator
License: GPL
Group: Office

Url: http://metromap.antex.ru
Source: %url/%name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
BuildRequires: python-devel >= %_python_version

# FIXME: not exactly elegant
Requires: %name-map-Moscow = %version

%description
A simple pygtk+2 program to help finding paths
in metro (subway) maps.

%define metromap_subpackage() \
%package map-%1 \
Summary: metro map for %2 \
Group: Office \
PreReq: %name = %version-%release \
AutoReqProv: no \
\
%description map-%1 \
This package contains metro map for %2 city. \
\
%files map-%1 \
%_datadir/%name/data/%{1}*

%define space %nil %nil

%metromap_subpackage Berlin Berlin
%metromap_subpackage Kiev Kiev
%metromap_subpackage London London
%metromap_subpackage Moscow Moscow
%metromap_subpackage New-York New%{space}York
%metromap_subpackage Paris Paris
%metromap_subpackage Petersburg St.%{space}Petersburg

%define python_libdir %_libdir/python%_python_version
%define python_site_packages_dir %python_libdir/site-packages

%prep
%setup -n %name-%version
rm -f modules/MapDisplayGC.py*
rm -rf tests

%build
mv data/Peter{,s}burg.pmz 

%install
make install DESTDIR=%buildroot%prefix
%find_lang %name

%files -f %name.lang
%_bindir/*
%dir %_datadir/%name
%dir %_datadir/%name/data
%dir %_datadir/%name/modules/
%_datadir/%name/modules/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%doc doc/AUTHORS doc/NEWS doc/README doc/README.data doc/TODO

%changelog
* Tue Feb 14 2012 Michael Shigorin <mike@altlinux.org> 0.1.4-alt1
- 0.1.4:
  + python-2.7 fixes
  + updated map-{Moscow,Petersburg,Kiev}
  + thx upstream for notification ;-)
- major spec cleanup (thx raorn@ for ruby-dbi.spec again)
- renamed Peterburg data file to Petersburg

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.3-alt1.1
- Rebuild with Python-2.7

* Sat Sep 24 2011 Michael Shigorin <mike@altlinux.org> 0.1.3-alt1
- 0.1.3
  + added New York and Paris

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt5.1
- Rebuilt with python 2.6

* Thu Jul 23 2009 Michael Shigorin <mike@altlinux.org> 0.1.2-alt5
- applied repocop patch

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 0.1.2-alt4
- added Packager:

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 0.1.2-alt3
- applied repocop patch

* Sun May 04 2008 Michael Shigorin <mike@altlinux.org> 0.1.2-alt2
- added %_datadir/%name/modules/ to package filelist (thx at@)

* Tue Feb 12 2008 Michael Shigorin <mike@altlinux.org> 0.1.2-alt1
- 0.1.2

* Sat Jan 26 2008 Grigory Batalov <bga@altlinux.ru> 0.1.2-alt0.pre3.1.1
- Rebuilt with python-2.5.

* Sat Dec 29 2007 Eugene V. Horohorin <genix@altlinux.ru> 0.1.2-alt0.pre3.1
- 0.1.2pre3

* Tue Jan 16 2007 Michael Shigorin <mike@altlinux.org> 0.1.1-alt2
- changed menu group to "Office" (#10662)
- added Packager:
- spec cleanup
- s/Peterburg/Petersburg/
- added freedesktop menu instead of debian's one

* Sun Aug 14 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.1.1-alt1
- new version

* Sun Jun 19 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.0.9-alt1
- initial build for Sisyphus.

