Name: purple-plugin-carbons
Version: 0.2.1
Release: alt1

Summary: Message Carbons plugin for libpurple

License: GPLv2+
Group: Networking/Instant messaging
Url: https://github.com/gkdr/carbons

Source: %name-%version.tar
# git://git.altlinux.org/gears/p/purple-plugin-carbons.git
Patch1: %name-%version-%release.patch

BuildRequires: glib2-devel libpurple-devel libxml2-devel

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

%files
%_libdir/purple-2/carbons.so

%changelog
* Wed Mar 06 2019 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus.


