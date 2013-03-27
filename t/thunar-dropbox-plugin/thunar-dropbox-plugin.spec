Name: thunar-dropbox-plugin
Version: 0.2.0
Release: alt3

Summary: Dropbox context-menu items for Thunar
License: %gpl3plus
Group: Graphical desktop/XFce

URL: http://www.softwarebakery.com/maato/thunar-dropbox.html
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

BuildRequires: libThunar-devel libgio-devel
# Build with waf > 1.5 is broken
#BuildRequires: waf

# for waf (ALT bug #25802)
BuildRequires: python-modules-logging

Requires: dropbox

%description
Thunar Dropbox is a plugin for thunar that adds context-menu items from
dropbox.

%prep
%setup
sed -i 's;/lib/;/%_lib/;' wscript

%build
./waf configure --prefix=%_prefix
./waf build

%install
./waf install --destdir=%buildroot

%files
%doc AUTHORS ChangeLog
%_libdir/thunarx-*/*.so
%_miconsdir/*.png

%changelog
* Wed Mar 27 2013 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt3
- Build with local waf..

* Tue Mar 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.2.0-alt2.1
- NMU: waf update.
  build with new waf fails - changed BR: to waf15 compat package.

* Mon Jul 11 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt2
- Requre dropbox.

* Thu Jun 23 2011 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1
- Initial build (based in Fedora spec).
