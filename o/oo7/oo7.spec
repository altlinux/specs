%def_enable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.6
%define beta %nil

%def_enable python
%def_disable bootstrap
%def_enable check

Name: oo7
Version: %ver_major.0
Release: alt1%beta

Summary: Secret Service provider
License: MIT
Group: System/Libraries
Url: https://github.com/bilelmoussaoui/oo7

Vcs: https://github.com/bilelmoussaoui/oo7.git

%if_disabled snapshot
Source: %url/archive/%version/%name-%version%beta.tar.gz
%else
Source: %name-%version%beta.tar
%endif
Source1: %name-%version%beta-cargo.tar

Conflicts: gnome-keyring

BuildRequires(pre): rpm-build-rust rpm-macros-meson rpm-build-systemd rpm-macros-pam %{?_enable_python:rpm-build-python3}
BuildRequires: meson
%{?_enable_python:BuildRequires: python3(wheel) python3(maturin)}

%description
This package provides:
- cargo credential provider
- cli: a secret-tool replacement
- client: the client side library
- org.freedesktop.impl.portal.Secret implementation
- org.freedesktop.secrets server implementation

%package -n python3-module-%name
Summary: Python bindings for oo7 client
Group: Development/Python3
Requires: %name = %EVR
%define pypi_name %{name}_python

%description -n python3-module-%name
Python bindings for oo7 client, providing access to Secret
Service API on Linux. Automatically uses a file-based keyring when
running in a sandboxed environment.

%prep
%setup -n %name-%version%beta %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
[ ! -d .cargo ] && mkdir .cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > .cargo/config.toml
tar -cf %_sourcedir/%name-%version%beta-cargo.tar .cargo/ vendor/}

%build
%rust_build
for d in portal server pam; do
    pushd $d
    %meson
    %meson_build
    popd
done
%{?_enable_python:
pushd python
%pyproject_build
popd}

%install
%rust_install cargo-credential-%name %name-cli
for d in portal server pam; do
    pushd $d
    %meson_install
    popd
done
%{?_enable_python:
pushd python
%pyproject_install
popd}

%check
#dbus-run-session %%rust_test
for d in portal server pam; do
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
%_pam_modules_dir/pam_%name.so
%_userunitdir/dbus-org.freedesktop.impl.portal.desktop.oo7.service
%_datadir/xdg-desktop-portal/portals/%name-portal.portal
# gnome-keyring replacement
%_datadir/dbus-1/services/org.freedesktop.secrets.service
%_userunitdir/dbus-org.freedesktop.secrets.service
%doc README*

%{?_enable_python:
%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%name.pyi
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
}

%changelog
* Sun Feb 22 2026 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Sun Aug 24 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Mon Mar 24 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.3-alt1
- 0.4.3

* Fri Mar 21 2025 Yuri N. Sedunov <aris@altlinux.org> 0.4.2-alt1
- 0.4.2

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

