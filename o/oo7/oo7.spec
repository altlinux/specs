%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define ver_major 0.7
%define beta %nil

%def_enable python
%def_disable bootstrap
%def_enable check

Name: oo7
Version: %ver_major.1
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

BuildRequires(pre): rpm-build-rust rpm-macros-meson rpm-build-systemd rpm-macros-pam %{?_enable_python:rpm-build-python3}
BuildRequires: meson libpam-devel
%{?_enable_python:BuildRequires: python3(wheel) python3(maturin)}

%description
This package provides:
- cargo credential provider
- cli: a secret-tool replacement
- client: the client side library
- kwallet-cli: a simple CLI to read KWallet `.kwl` files
- git-credential: replacement for git-credential-libsecret
- org.freedesktop.impl.portal.Secret implementation
- org.freedesktop.secrets server implementation

%package daemon
Summary: %name daemon
Group: System/Servers
Requires: %name-portal = %EVR
#Conflicts: gnome-keyring

%description    daemon
%name service providing the Secret Service D-Bus API.

%package portal
Summary: %name portal
Group: System/Servers
Requires: xdg-desktop-portal

%description portal
An implementation of the org.freedesktop.impl.portal.Secret interface.

%package -n pam_%name
Summary: A pam module for unlocking keyrings at login time
Group: System/Base
Requires: %name-daemon = %EVR

%description -n pam_%name
The pam_%name package contains a pam module that can
automatically unlock the "login" keyring when the user logs in
and start the %name-daemon.

%package cli
Summary: %name cli tools
Group: System/Base

%description cli
This package provides %name-cli to interact with keyrings.

%package -n cargo-credential-%name
Summary: %name cargo credential provider
Group: System/Base

%description -n cargo-credential-%name
A cargo credential provider built using %name.

%package -n git-credential-%name
Summary: %name cargo credential provider
Group: System/Base

%description -n git-credential-%name
A git credential provider built using %name.

%package kwallet-cli
Summary: Command-line tool for reading KWallet files
Group: System/Base

%description kwallet-cli
Command-line tool for reading KWallet files.

%package -n python3-module-%name
Summary: Python bindings for oo7 client
Group: Development/Python3
Requires: %name-cli = %EVR
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
    %meson -Dbuildtype=release -Dprofile=default
    %meson_build
    popd
done
%{?_enable_python:
pushd python
%pyproject_build
popd}

%install
%rust_install %name-cli cargo-credential-%name git-credential-%name kwallet-cli
for d in portal server pam; do
    pushd $d
    %meson_install
    popd
done
%{?_enable_python:
pushd python
%pyproject_install
popd}

%find_lang %name-daemon

%check
#dbus-run-session %%rust_test
for d in portal server pam; do
    pushd $d
    %__meson_test
    popd
done

%files daemon -f %name-daemon.lang
%_libexecdir/%name-daemon
%_libexecdir/%name-daemon-login
%_userunitdir/%name-daemon.service
%_userunitdir/dbus-org.freedesktop.secrets.service
# gnome-keyring replacement
# b4f53971aec12491767f5867e4577d06e273caca
#%_datadir/dbus-1/services/org.freedesktop.secrets.service
%doc server/README*

%files portal
%_libexecdir/%name-portal
%_userunitdir/%name-portal.service
%_desktopdir/%name-portal.desktop
%_userunitdir/dbus-org.freedesktop.impl.portal.desktop.oo7.service
%_datadir/dbus-1/services/org.freedesktop.impl.portal.desktop.oo7.service
%_datadir/xdg-desktop-portal/portals/%name-portal.portal
%doc portal/README*

%files -n pam_%name
%_pam_modules_dir/pam_%name.so
%doc pam/README*

%files cli
# secret-tool replacement
%_bindir/%name-cli

%files -n git-credential-%name
%_bindir/git-credential-%name
%doc git-credential/README*

%files -n cargo-credential-%name
%_bindir/cargo-credential-%name
%doc cargo-credential/README*

%files kwallet-cli
%_bindir/kwallet-cli
%doc kwallet/cli/README*

%{?_enable_python:
%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%pypi_name-*.dist-info/
#%python3_sitelibdir/%{pyproject_distinfo %pypi_name}
%doc python/README*
}

%changelog
* Wed Nov 11 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1

* Mon Nov 09 2026 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

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

