Name: klavaro
Version: 1.9.3
Release: alt3.1

Summary: Yet another touch typing tutor
License: GPLv3+
Group: Education

Url: http://klavaro.sourceforge.net/en/
Source: http://downloads.sourceforge.net/klavaro/klavaro-%version.tar.bz2
Source1: ru.po
Patch: klavaro-1.9.3-alt-DSO.patch

# Automatically added by buildreq on Wed Feb 23 2011
BuildRequires: intltool libcurl-devel libgtkdatabox-devel

%description
Klavaro is just another free touch typing tutor program. It intends to
be keyboard and language independent, saving memory and time.

%prep
%setup
%patch -p2
cp %SOURCE1 po/
subst 's#/usr/share/icons/hicolor/24x24/apps/klavaro.png#klavaro#' data/klavaro.desktop.in
subst 's/Education/Education;Science;ComputerScience/' data/klavaro.desktop.in

%build
%configure
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/*
%_datadir/klavaro/
%_desktopdir/klavaro.desktop
%_man1dir/*
%_iconsdir/hicolor/*/apps/klavaro.png

%changelog
* Wed Jul 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.3-alt3.1
- Fixed build

* Mon Aug 15 2011 Andrey Cherepanov <cas@altlinux.org> 1.9.3-alt3
- Update Russian translation (closes: #26055)

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.9.3-alt2
- Rebuild with new libgtkdatabox.

* Sun Jul 10 2011 Victor Forsiuk <force@altlinux.org> 1.9.3-alt1
- 1.9.3

* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 1.9.2-alt1
- 1.9.2

* Sun Apr 17 2011 Victor Forsiuk <force@altlinux.org> 1.9.1-alt1
- 1.9.1

* Tue Mar 29 2011 Victor Forsiuk <force@altlinux.org> 1.9.0-alt1
- 1.9.0

* Wed Feb 23 2011 Victor Forsiuk <force@altlinux.org> 1.8.1-alt1
- 1.8.1

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 1.7.5-alt1
- 1.7.5

* Mon Dec 20 2010 Victor Forsiuk <force@altlinux.org> 1.7.4-alt1
- 1.7.4

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.3-alt1
- 1.7.3

* Mon Sep 27 2010 Victor Forsiuk <force@altlinux.org> 1.7.2-alt1
- 1.7.2

* Thu Aug 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Aug 17 2010 Victor Forsiuk <force@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Mar 01 2010 Victor Forsiuk <force@altlinux.org> 1.5.0-alt1
- 1.5.0

* Mon Dec 28 2009 Victor Forsyuk <force@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Dec 14 2009 Victor Forsyuk <force@altlinux.org> 1.4.0-alt1
- 1.4.0

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 1.3.0-alt1
- 1.3.0

* Wed Jul 29 2009 Victor Forsyuk <force@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sat Jan 26 2008 Eugene Ostapets <eostapets@altlinux.ru> 1.0.7-alt1
- first build
