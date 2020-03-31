Name: thunar-dropbox-plugin
Version: 0.3.1
Release: alt1

Summary: Dropbox context-menu items for Thunar
License: GPL-3.0-only
Group: Graphical desktop/XFce

URL: http://www.softwarebakery.com/maato/thunar-dropbox.html
# Old upstream
# https://github.com/Maato/thunar-dropbox.git
Vcs: https://github.com/Jeinzi/thunar-dropbox
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: rpm-macros-cmake cmake
BuildRequires: libthunar-devel libgio-devel

Requires: dropbox

%define _unpackaged_files_terminate_build 1

%description
Thunar Dropbox is a plugin for thunar that adds context-menu items from
dropbox.

%prep
%setup
%patch -p1

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%doc AUTHORS ChangeLog
%_libdir/thunarx-*/*.so
%_miconsdir/*.png

%changelog
* Tue Mar 31 2020 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1
- Fixed plugin install path.
- Added Vcs tag.
- Fixed license.
- Switched to cmake.
- Dropped libthunar-3.patch.
- Updated to 0.3.1.

* Tue Aug 21 2018 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt2
- Use _unpackaged_files_terminate_build.
- Port to libthunar-3 patch.

* Wed Apr 29 2015 Mikhail Efremov <sem@altlinux.org> 0.2.1-alt1
- Updated to 0.2.1.

* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt3
- Build with local waf..

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2.1
- NMU: waf update.
  build with new waf fails - changed BR: to waf15 compat package.

* Mon Jul 11 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Requre dropbox.

* Thu Jun 23 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Initial build (based in Fedora spec).
