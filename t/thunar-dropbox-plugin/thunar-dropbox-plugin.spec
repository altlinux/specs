Name: thunar-dropbox-plugin
Version: 0.2.1
Release: alt2

Summary: Dropbox context-menu items for Thunar
License: %gpl3plus
Group: Graphical desktop/XFce

URL: http://www.softwarebakery.com/maato/thunar-dropbox.html
# https://github.com/Maato/thunar-dropbox.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch
# https://github.com/Maato/thunar-dropbox/pull/10
Patch1: libthunar-3.patch

BuildRequires(pre): rpm-build-licenses

BuildRequires: libthunar-devel libgio-devel
# Build with waf > 1.5 is broken
#BuildRequires: waf

# for waf (ALT bug #25802)
BuildRequires: python-modules-logging

Requires: dropbox

%define _unpackaged_files_terminate_build 1

%description
Thunar Dropbox is a plugin for thunar that adds context-menu items from
dropbox.

%prep
%setup
%patch -p1
%patch1 -p1

%build
./waf configure --prefix=%_prefix --libdir=%_prefix/%_lib
./waf build

%install
./waf install --destdir=%buildroot

%files
%doc AUTHORS ChangeLog
%_libdir/thunarx-*/*.so
%_miconsdir/*.png

%changelog
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
