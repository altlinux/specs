Name:       mako
Version:    1.4
Release:    alt2
Summary:    Lightweight Wayland notification daemon
Provides:   desktop-notification-daemon
Group:      Graphical desktop/Other

License:    MIT
URL:        https://github.com/emersion/mako
Source0:    %name-%version.tar
Patch0:     meson-disable-werror.patch

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  systemd-devel
#BuildRequires: libelogind-devel
BuildRequires:  scdoc
Requires:       dbus

%description
mako is a lightweight notification daemon for Wayland compositors that support
the layer-shell protocol.

%prep
%setup
%patch0 -p1

%build
%meson
%meson_build

%install
%meson_install

rm -f -- \
	%buildroot/%_bindir/makoctl \
	%buildroot/%_man1dir/makoctl.* \


%files
%doc LICENSE README.md
%_bindir/mako
%_datadir/dbus-1/services/fr.emersion.mako.service
%_man1dir/mako.*

%changelog
* Wed Nov 06 2019 Alexey Gladkov <legion@altlinux.ru> 1.4-alt2
- Drop makoctl to avoid logind dependency.

* Wed Aug 07 2019 Alexey Gladkov <legion@altlinux.ru> 1.4-alt1
- New version (1.4).

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Jul 14 2019 Jeff Peeler <jpeeler@redhat.com> - 1.3-1
- Upstream 1.3 release

* Thu Apr 04 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-2
- Fix location of systemd service file

* Sun Mar 17 2019 Timothée Floure <fnux@fedoraproject.org> - 1.2-1
- Let there be package
