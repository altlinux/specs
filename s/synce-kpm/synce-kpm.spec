Summary: SynCE KDE PDA Manager
Name: synce-kpm
Version: 0.15
Release: alt1.qa1.1
License: GPL2
Group: Communications
Packager: Mobile Development Team <mobile@packages.altlinux.org>
Source: %name-%version.tar.gz
Source1: %name.desktop
Url: http://www.synce.org/
BuildArch: noarch

Requires: python-module-librapi >= 0.14

BuildRequires: python-module-setuptools desktop-file-utils

%description
Device Manager for WM5+ devices for KDE.

%prep
%setup -q

%build
python setup.py build

%install
python setup.py install --root=%buildroot --optimize=2 --record=INSTALLED_FILES

desktop-file-install --dir=%buildroot%_datadir/applications %SOURCE1
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Network \
	--add-category=Office \
	--add-category=PDA \
	%buildroot%_desktopdir/synce-kpm.desktop

%files -f INSTALLED_FILES
%doc AUTHORS README TODO ChangeLog
%_datadir/applications/*.desktop

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.15-alt1.qa1.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.15-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for synce-kpm
  * postclean-03-private-rpm-macros for the spec file

* Mon May 17 2010 Alexey Shabalin <shaba@altlinux.ru> 0.15-alt1
- 0.15
- add desktop file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1.1
- Rebuilt with python 2.6

* Mon Aug 24 2009 Alexey Shabalin <shaba@altlinux.ru> 0.14-alt1
- 0.14

* Tue Mar 03 2009 Alexey Shabalin <shaba@altlinux.ru> 0.13-alt1
- 0.13

* Mon Oct 13 2008 Alexey Shabalin <shaba@altlinux.ru> 0.12-alt1
- 0.12
- cleanup spec

* Tue Jan 29 2008 Eugene V. Horohorin <genix@altlinux.ru> 0.11-alt1
- update to svn 20080129
- initial build for ALT Linux

