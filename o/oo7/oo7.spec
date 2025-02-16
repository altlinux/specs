%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.4

%def_disable bootstrap
%def_enable check

Name: oo7
Version: %ver_major.0
Release: alt1

Summary: Secret Service provider
License: MIT
Group: System/Libraries
Url: https://github.com/bilelmoussaoui/oo7

Vcs: https://github.com/bilelmoussaoui/oo7.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version.tar.gz
%else
Source: %name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-build-rust rpm-macros-meson rpm-build-systemd
BuildRequires: meson

%description
This package provides:
- cargo credential provider
- cli: a secret-tool replacement
- client: the client side library
- org.freedesktop.impl.portal.Secret implementation
- org.freedesktop.secrets server implementation

%prep
%setup -n %name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar .cargo/ vendor/}

%build
%rust_build
for d in portal server; do
    pushd $d
    %meson
    %meson_build
    popd
done

%install
%rust_install cargo-credential-%name %name-cli
for d in portal server; do
    pushd $d
    %meson_install
    popd
done

%check
#dbus-run-session %rust_test
for d in portal server; do
    pushd $d
    %__meson_test
    popd
done

%files
%_bindir/cargo-credential-%name
%_bindir/%name-cli
%_libexecdir/%name-daemon
%_libexecdir/%name-portal
%_userunitdir/%name-daemon.service
%_userunitdir/%name-portal.service
%_desktopdir/%name-portal.desktop
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.oo7.service
%_datadir/xdg-desktop-portal/portals/%name-portal.portal
%doc README*

%changelog
* Sun Feb 16 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Wed Jun 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Mon May 06 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Sat May 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Sat Feb 24 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first preview for Sisyphus (0.3.0-5-gad713f5)

