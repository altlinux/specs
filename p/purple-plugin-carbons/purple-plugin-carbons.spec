Name: purple-plugin-carbons
Version: 0.2.3
Release: alt1

Summary: Message Carbons plugin for libpurple

License: GPLv2+
Group: Networking/Instant messaging
Url: https://github.com/gkdr/carbons

VCS: git://github.com/gkdr/carbons.git
Source: %name-%version.tar
# git://git.altlinux.org/gears/p/purple-plugin-carbons.git
Patch1: %name-%version-%release.patch

BuildRequires: glib2-devel libpurple-devel libxml2-devel
# need for tests
BuildRequires: libcmocka-devel

%description
Implements XEP-0280: Message Carbons as a plugin.

This plugin enables a consistent history view across multiple devices which are
online at the same time.

%prep
%setup
%patch1 -p1

%build
make

%install
make DESTDIR=%buildroot install

%check
make test

%files
%_libdir/purple-2/carbons.so

%changelog
* Thu Dec 09 2021 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.3-alt1
- Updated to v0.2.3.

* Thu Dec 05 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.2-alt2
- Fixed linkage with libjabber.so.0 (added RPATH).

* Mon May 06 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.2-alt1
- Updated to 0.2.2.
- spec: enabled tests (introduced in 0.2.2).

* Wed Mar 06 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.


