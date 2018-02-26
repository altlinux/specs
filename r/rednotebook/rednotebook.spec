Name: rednotebook
Version: 1.2.0
Release: alt1.1

Summary: A desktop diary

Group: Office
License: GPLv2+
Url: http://rednotebook.sourceforge.net

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://prdownloads.sf.net/%name/%name-%version.tar

BuildArch: noarch

# for encoding
#Requires: python-module-chardet

Requires: python-module-yaml

# FIXME: Segfaults with pywebkit installed
#Requires: python-module-pywebkitgtk

%add_python_req_skip daywidgets

# Automatically added by buildreq on Sun Oct 24 2010
BuildRequires: python-module-paste python-module-peak

%description
RedNotebook is a desktop diary that makes it very easy for you
to keep track of the stuff you do and the thoughts you have. This
journal software helps you to write whole passages or just facts,
and does so in style.

%prep
%setup

%build
%python_build

%install
%python_install
#%buildroot/%_desktopdir/%name.desktop

%files
%doc AUTHORS CHANGELOG LICENSE README
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.png
%_liconsdir/%name.png
%python_sitelibdir/%name/
%python_sitelibdir/%{name}*.egg-info

%changelog
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

