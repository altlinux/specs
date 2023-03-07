Name: rednotebook
Version: 2.29.3
Release: alt1

Summary: A desktop diary

Group: Office
License: GPLv2+
Url: http://rednotebook.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/jendrikseipp/rednotebook/archive/v%version.tar.gz
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-module-yieldfrom

Requires: python3-module-yaml
#Requires: typelib(Gtk)
Requires: libgtk+3-gir
# Requires: typelib(GtkSource)
Requires: libgtksourceview3-gir
# Requires: typelib(WebKit2)
Requires: libwebkit2gtk-gir

%description
RedNotebook is a desktop diary that makes it very easy for you
to keep track of the stuff you do and the thoughts you have. This
journal software helps you to write whole passages or just facts,
and does so in style.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install
%find_lang %name

%files -f %name.lang
%doc CHANGELOG.md README.md
%_bindir/%name
%_desktopdir/%name.desktop
%_datadir/metainfo/rednotebook.appdata.xml
%_iconsdir/hicolor/scalable/apps/rednotebook.svg
# TODO: own dir in datadir
%python3_sitelibdir/%name/
%python3_sitelibdir/%{name}*.egg-info

%changelog
* Wed Mar 08 2023 Vitaly Lipatov <lav@altlinux.ru> 2.29.3-alt1
- new version 2.29.3 (with rpmrb script)
- add requires: libgtksourceview3-gir (ALT bug 45504)
- add requires: libwebkit2gtk-gir

* Sun Sep 11 2022 Vitaly Lipatov <lav@altlinux.ru> 2.25-alt1
- new version 2.25 (with rpmrb script)

* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 2.22-alt1
- new version 2.22 (with rpmrb script)

* Fri Feb 26 2021 Vitaly Lipatov <lav@altlinux.ru> 2.21-alt1
- new version 2.21 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 2.11.1-alt1
- new version 2.11.1 (with rpmrb script)

* Sat Oct 13 2018 Vitaly Lipatov <lav@altlinux.ru> 2.6.1-alt1
- new version 2.6.1 (with rpmrb script)

* Thu Jul 05 2018 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version 2.5 (with rpmrb script)
- python 3, GTK3

* Tue May 09 2017 Vitaly Lipatov <lav@altlinux.ru> 1.15-alt1
- new version 1.15 (with rpmrb script)

* Tue Dec 06 2016 Vitaly Lipatov <lav@altlinux.ru> 1.14-alt1
- new version 1.14 (with rpmrb script)

* Sat Sep 24 2016 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- new version 1.13 (with rpmrb script)

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- new version 1.12 (with rpmrb script)

* Sat Jan 30 2016 Vitaly Lipatov <lav@altlinux.ru> 1.11-alt1
- new version 1.11 (with rpmrb script)

* Sat Aug 15 2015 Vitaly Lipatov <lav@altlinux.ru> 1.9.0-alt1
- new version 1.9.0 (with rpmrb script)

* Mon Dec 08 2014 Vitaly Lipatov <lav@altlinux.ru> 1.8.1-alt1
- new version 1.8.1 (with rpmrb script)

* Wed Apr 02 2014 Vitaly Lipatov <lav@altlinux.ru> 1.8.0-alt1
- new version 1.8.0 (with rpmrb script)

* Sun Aug 04 2013 Vitaly Lipatov <lav@altlinux.ru> 1.7.2-alt1
- new version 1.7.2 (with rpmrb script)

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1.1
- Rebuild with Python-2.7

* Tue Oct 11 2011 Vitaly Lipatov <lav@altlinux.ru> 1.2.0-alt1
- new version 1.2.0 (with rpmrb script)

* Sun Oct 24 2010 Vitaly Lipatov <lav@altlinux.ru> 1.1.1-alt1
- initial build for ALT Linux Sisyphus

* Sun Aug 29 2010 Fabian Affolter <fabian@bernewireless.net> - 1.1.1-1
- Updated to new upstream version 1.1.1

* Sat Aug 14 2010 Fabian Affolter <fabian@bernewireless.net> - 1.1.0-1
- Updated to new upstream version 1.1.0

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jun 26 2010 Fabian Affolter <fabian@bernewireless.net> - 1.0.0-1
- Updated to new upstream version 1.0.0

* Tue May 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.5-2
- Require python-chardet

* Tue May 11 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.5-1
- Update to 0.9.5

* Wed Feb 24 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.3-1
- Update to 0.9.3

* Mon Feb 01 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.2-1
- Update to 0.9.2

* Sun Jan 10 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.1-1
- Update to 0.9.1
- Require pywebkitgtk for new print preview
- Use desktop-file-install

* Fri Dec 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.9.0-1
- Update to 0.9.0

* Thu Nov 19 2009 Fabian Affolter <fabian@bernewireless.net> - 0.8.9-2
- Updated the URL after a request from the upstream maintainer

* Wed Nov 18 2009 Fabian Affolter <fabian@bernewireless.net> - 0.8.9-1
- Updated to new upstream version 0.8.9

* Mon Nov 16 2009 Fabian Affolter <fabian@bernewireless.net> - 0.8.8-1
- Updated to new upstream version 0.8.8

* Tue Sep 29 2009 Fabian Affolter <fabian@bernewireless.net> - 0.8.7-1
- Updated to new upstream version 0.8.7

* Thu Sep 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6.1-1
- Update to 0.8.6.1, fixes #523880

* Thu Sep 17 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6-2
- Fix libglade error with GTK 2.16.6 (#523880)

* Fri Sep 04 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.6-1
- Updated to new upstream version 0.8.6

* Fri Aug 14 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.5-1
- Updated to new upstream version 0.8.5 (fixes #518778)

* Fri Aug 14 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.4-1
- Updated to new upstream version 0.8.4

* Fri Aug 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.3-1
- Updated to new upstream version 0.8.3

* Wed Jul 29 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.2-1
- Updated to new upstream version 0.8.2

* Sat Jul 25 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.1-1
- Updated to new upstream version 0.8.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Fabian Affolter <fabian@bernewireless.net> - 0.8.0-1
- Updated BR python
- Icon cache update added
- Updated to new upstream version 0.8.0

* Wed Jul 15 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.6-1
- Updated to new upstream version 0.7.6

* Mon Jul 06 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.5-1
- Removed the shebang stuff, upstream changed this
- Updated to new upstream version 0.7.5

* Mon Jun 29 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.4-1
- Moved the removing of the shebang to prep section
- Updated to new upstream version 0.7.4

* Thu May 26 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.2-1
- Updated to new upstream version 0.7.2

* Wed May 06 2009 Fabian Affolter <fabian@bernewireless.net> - 0.7.1-1
- Updated to new upstream version 0.7.1

* Wed May 06 2009 Fabian Affolter <fabian@bernewireless.net> - 0.6.9-1
- Updated to new upstream version 0.6.9

* Sun May 03 2009 Fabian Affolter <fabian@bernewireless.net> - 0.6.8-1
- Updated to new upstream version 0.6.8

* Tue Apr 21 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.7-1
- Updated to new upstream version 0.6.7

* Tue Apr 07 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.6-1
- Updated to new upstream version 0.6.6

* Fri Apr 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.5-1
- Updated to new upstream version 0.6.5

* Wed Mar 18 2009 Fabian Affolter <fabian@bernewireless.net> - 0.6.2-1
- Added hicolor-icon-theme as a requirement
- Added icons directory
- Updated to new upstream version 0.6.2

* Sat Mar 07 2009 Fabian Affolter <fabian@bernewireless.net> - 0.6.1-1
- Updated to new upstream version 0.6.1
- Renamed docs, added License file

* Thu Feb 12 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5.5-1
- Updated to new upstream version 0.5.5

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5.2-1
- Updated to new upstream version 0.5.2

* Sat Jan 24 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5.1-1
- Initial package for Fedora

