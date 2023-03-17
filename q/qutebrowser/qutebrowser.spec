%global srcname qutebrowser

Name: %srcname
Version: 2.5.4
Release: alt1
Summary: A keyboard-driven, vim-like browser based on PyQt5 and QtWebEngine
License: GPLv3
Group: Networking/WWW
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://www.qutebrowser.org
Source0: %srcname-%version.tar
BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: asciidoc asciidoc-a2x
BuildRequires: desktop-file-utils python3-module-setuptools rpm-build-python3
#Requires: qt5-qtbase
#Requires: qt5-qtdeclarative
#Requires: python3-module-setuptools
#Requires: python3-qt5
#Requires: python3-qt5-webengine
#Requires: python3-jinja2
#Requires: python3-pygments
#Requires: python3-PyYAML
#Requires: python3-pyPEG2
#Requires: python3-attrs
#Requires: qt5-qtwebengine qt5-qtwebkit python3-qt5-webkit python3-cssutils
Provides: python3(qutebrowser.extensions)
Provides: python3(qutebrowser.components.utils)
#add_python3_req_skip PyQt5.QtWebKit PyQt5.QtWebKitWidgets
%add_python3_req_skip PyQt5.QtWebEngineCore PyQt5.QtWebEngine PyQt5.QtWebEngineWidgets


%description
qutebrowser is a keyboard-focused browser with a minimal GUI. It's based on
Python, PyQt5 and QtWebEngine and free software, licensed under the GPL.
It was inspired by other browsers/addons like dwb and Vimperator/Pentadactyl.

%prep
%setup -n %srcname-%version

%build
# Compile the man page
a2x -f manpage doc/qutebrowser.1.asciidoc

# Find all *.py files and if their first line is exactly '#!/usr/bin/env python3'
# then replace it with '#!/usr/bin/python3' (if it's the 1st line).
find . -type f -iname "*.py" -exec sed -i '1s_^#!/usr/bin/env python3$_#!/usr/bin/python3_' {} +

%python3_build

%install
%python3_install

# install .desktop file
desktop-file-install \
	--add-category="Network" \
	--delete-original \
	--dir=%buildroot%_datadir/applications \
	misc/org.%srcname.%srcname.desktop

# Install man page
install -Dm644 doc/%srcname.1 -t %buildroot%_mandir/man1

# Install icons
install -Dm644 icons/qutebrowser.svg \
	-t "%buildroot%_datadir/icons/hicolor/scalable/apps"
for i in 16 24 32 48 64 128 256 512; do
	install -Dm644 "icons/qutebrowser-${i}x${i}.png" \
		"%buildroot%_datadir/icons/hicolor/${i}x${i}/apps/qutebrowser.png"
done

# Set __main__.py as executable
chmod 755 %buildroot%python3_sitelibdir/%srcname/__main__.py

# Remove zero-length files:
# https://fedoraproject.org/wiki/Packaging_tricks#Zero_length_files
find %buildroot -size 0 -delete

%files
%doc README.asciidoc doc/changelog.asciidoc doc/img/* 
%python3_sitelibdir/%srcname-%version-py?.*.egg-info
%python3_sitelibdir/%srcname
%_bindir/%srcname
%_datadir/applications/org.%srcname.%srcname.desktop
%_man1dir/%srcname.1*
%_datadir/icons/hicolor/scalable/apps/%srcname.svg
%_datadir/icons/hicolor/16x16/apps/%srcname.png
%_datadir/icons/hicolor/24x24/apps/%srcname.png
%_datadir/icons/hicolor/32x32/apps/%srcname.png
%_datadir/icons/hicolor/48x48/apps/%srcname.png
%_datadir/icons/hicolor/64x64/apps/%srcname.png
%_datadir/icons/hicolor/128x128/apps/%srcname.png
%_datadir/icons/hicolor/256x256/apps/%srcname.png
%_datadir/icons/hicolor/512x512/apps/%srcname.png

%changelog
* Sat Mar 18 2023 Ilya Mashkin <oddity@altlinux.ru> 2.5.4-alt1
- 2.5.4

* Sun Feb 19 2023 Ilya Mashkin <oddity@altlinux.ru> 2.5.3-alt1
- 2.5.3

* Fri Jun 24 2022 Ilya Mashkin <oddity@altlinux.ru> 2.5.2-alt1
- 2.5.2

* Fri May 27 2022 Ilya Mashkin <oddity@altlinux.ru> 2.5.1-alt1
- 2.5.1

* Sat Apr 02 2022 Ilya Mashkin <oddity@altlinux.ru> 2.5.0-alt1
- 2.5.0

* Wed Feb 02 2022 Sergey V Turchin <zerg@altlinux.org> 2.4.0-alt2
- no qtwebengine on e2k and ppc64le (see bug#41476)

* Fri Oct 22 2021 Ilya Mashkin <oddity@altlinux.ru> 2.4.0-alt1
- 2.4.0 (Fixes: CVE-2021-41146)

* Thu Jul 29 2021 Ilya Mashkin <oddity@altlinux.ru> 2.3.1-alt1
- 2.3.1

* Tue Jul 20 2021 Ilya Mashkin <oddity@altlinux.ru> 2.3.0-alt4
- Fixing skip reqs for python3 QtWebKit in the correct way (thanks to Vitaly Lipatov, closes: #38837)

* Fri Jul 16 2021 Ilya Mashkin <oddity@altlinux.ru> 2.3.0-alt3
- add BR rpm-build-python3

* Fri Jul 16 2021 Ilya Mashkin <oddity@altlinux.ru> 2.3.0-alt2
- skip reqs for python3 QtWebKit (thanks to Sergey Turchin, closes: #38837)

* Thu Jul 15 2021 Ilya Mashkin <oddity@altlinux.ru> 2.3.0-alt1
- 2.3.0

* Thu Jun 03 2021 Ilya Mashkin <oddity@altlinux.ru> 2.2.3-alt1
- 2.2.3

* Sun May 23 2021 Ilya Mashkin <oddity@altlinux.ru> 2.2.2-alt1
- 2.2.2

* Sat May 01 2021 Ilya Mashkin <oddity@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Wed Apr 21 2021 Ilya Mashkin <oddity@altlinux.ru> 2.2.0-alt1
- 2.2.0

* Tue Apr 13 2021 Ilya Mashkin <oddity@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Fri Mar 19 2021 Ilya Mashkin <oddity@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Tue Feb 16 2021 Ilya Mashkin <oddity@altlinux.ru> 2.0.1-alt1
- 2.0.1

* Mon Jan 11 2021 Ilya Mashkin <oddity@altlinux.ru> 1.14.1-alt1
- 1.14.1

* Thu Oct 29 2020 Ilya Mashkin <oddity@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Fri Jul 12 2019 Ilya Mashkin <oddity@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Sat Apr 27 2019 Ilya Mashkin <oddity@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Sat Oct 20 2018 Ilya Mashkin <oddity@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Thu Oct 11 2018 Ilya Mashkin <oddity@altlinux.ru> 1.5.0-alt1
- Build for Sisyphus

* Wed Oct 03 2018 Timothée Floure <fnux@fedoraproject.org> - 1.5.0-1
- Rebase to 1.5.0

* Mon Sep 03 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.2-1
- Rebase to 1.4.2

* Wed Jul 11 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.1-1
- Rebase to 1.4.1
- Remove patch introduced in 1.4.0-2, since included in upstream release 1.4.1

* Tue Jul 10 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.0-2
- Patch critical CSRF issues with qute://settings/set URL, leading to arbitrary
  code exexution.

* Tue Jul 03 2018 Timothée Floure <fnux@fedoraproject.org> - 1.4.0-1
- Rebase to 1.4.0

* Mon Jul 02 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.3-2
- Rebuilt for Python 3.7

* Fri Jun 22 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.3-1
- Rebase to 1.3.3

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-2
- Rebuilt for Python 3.7

* Tue Jun 12 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.2-1
- Rebase to 1.3.2

* Tue May 29 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.1-1
- Rebase to 1.3.1

* Fri May 04 2018 Timothée Floure <fnux@fedoraproject.org> - 1.3.0-1
- Rebase to 1.3.0

* Tue Mar 20 2018 Timothée Floure <fnux@fedoraproject.org> - 1.2.1-1
- Rebase to 1.2.1

* Mon Mar 12 2018 Timothée Floure <fnux@fedoraproject.org> - 1.2.0-1
- Rebase to 1.2.0

* Mon Mar 05 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.2-1
- Rebase to 1.1.2

* Sun Jan 21 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.1-1
- Rebase to 1.1.1

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.1.0-2
- Remove obsolete scriptlets

* Mon Jan 15 2018 Timothée Floure <fnux@fedoraproject.org> - 1.1.0-1
- Rebase to 1.1.0

* Tue Nov 28 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.4-1
- Rebase to 1.0.4

* Tue Nov 14 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.3-2
- Fix typos in some (weak) Qt dependencies

* Tue Nov 07 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.3-1
- Rebase to 1.0.3
- Fix dependency issue for architectures unsupported by qt5-qtwebengine

* Fri Oct 20 2017 Timothée Floure <timothee.floure@fnux.ch> - 1.0.2-1
- Rebase to 1.0.2
- Remove the deprecated Group tag
- Add the python3-attrs dependency
- Adapt the descriptions and dependencies to the QtWebEngine backend (new default)
- Doc tag: do not package the PKG-INFO file anymore
- Doc tag: package the full HTML documentation instead of sparse asciidoc files

* Tue Mar 14 2017 Tomas Orsava <torsava@redhat.com> - 0.10.1-1
- Rebased to 0.10.1

* Mon Feb 27 2017 Tomas Orsava <torsava@redhat.com> - 0.10.0-1
- Rebased to 0.10.0
- Updated Source URL

* Mon Jan 16 2017 Tomas Orsava <torsava@redhat.com> - 0.9.1-1
- Rebased to 0.9.1

* Mon Jan 02 2017 Tomas Orsava <torsava@redhat.com> - 0.9.0-1
- Rebased to 0.9.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.4-2
- Rebuild for Python 3.6

* Fri Aug 05 2016 Tomas Orsava <torsava@redhat.com> - 0.8.2-1
- New upstream release 0.8.2

* Thu Jul 28 2016 Tomas Orsava <torsava@redhat.com> - 0.8.1-1
- Rebased onto a new upstream version

* Mon Jun 13 2016 Tomas Orsava <torsava@redhat.com> - 0.7.0-1
- Updated to a new version
- Removed soft dependency on `colorama` as it is no longer needed

* Fri May 06 2016 Tomas Orsava <torsava@redhat.com> - 0.6.2-1
- Updated to a new upstream version.
- Remover patches specific to the version 0.6.1

* Wed Apr 27 2016 Tomas Orsava <torsava@redhat.com> - 0.6.1-2
- Added 3 upstream patches from the mailing list to help with PyQT crashes
  until 0.6.2 comes out.

* Tue Apr 12 2016 Tomas Orsava <torsava@redhat.com> - 0.6.1-1
- Updated to a new upstream version.
- Simplified the sed command that replaces shebangs.
- Fixed issue with python3-qt5-webkit not being provided by python-qt5 in f23.

* Wed Mar 02 2016 Rex Dieter <rdieter@fedoraproject.org> 0.5.1-2
- Requires: python3-qt5-webkit

* Mon Feb 22 2016 Tomas Orsava <torsava@redhat.com> - 0.5.1-1
- Let there be package.
