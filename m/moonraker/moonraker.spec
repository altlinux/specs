%define _unpackaged_files_terminate_build 1
Name:    moonraker
Version: 0.9.3
Release: alt1
Summary: Moonraker - API Web Server for Klipper
License: GPL-3.0-or-later
Group:   Development/Python3
URL:     https://moonraker.readthedocs.io
VCS:     https://github.com/Arksine/moonraker
Source:  %name-%version.tar
Patch:   %name-%version-%release.patch
BuildRequires: rpm-build-python3
BuildRequires: pytest3
BuildRequires: python3-module-pytest
BuildRequires: python3-module-pdm
BuildRequires: python3-module-pdm-backend
BuildRequires: python3-module-pytest-asyncio
BuildRequires: python3-module-pytest-timeout
BuildRequires: python3-module-importlib-metadata
BuildRequires: python3-module-tornado
BuildRequires: python3-module-periphery
BuildRequires: python3-module-lmdb
Requires: klipper
Requires: polkit

BuildArch: noarch

%package -n python3-module-%name
Summary: Moonraker - API Web Server for Klipper
BuildArch: noarch
Group:   Development/Python3

%description
Moonraker as a ready-made solution to work out of the box.
It has systemd services, sockets, and a basic cnfig.

%description -n python3-module-%name
Moonraker is a Python 3 based web server that exposes APIs with which client
applications may use to interact with the 3D printing firmware Klipper.
Communication between the Klippy host and
Moonraker is done over a Unix Domain Socket.
Tornado is used to provide Moonraker's server functionality.

%prep
%setup
%autopatch -p1

%build
export PDM_BUILD_SCM_VERSION=%version
%pyproject_build

%install
%pyproject_install
install -D -m 0644 moonraker.service %buildroot/%_unitdir/moonraker.service
install -D -m 0644 moonraker.conf %buildroot/%_localstatedir/moonraker_data/config/moonraker.conf
install -D -m 0644 moonraker.rules %buildroot/%_datadir/polkit-1/rules.d/moonraker.rules
mkdir -p %buildroot/%_localstatedir/moonraker_data/logs/moonraker
ln -sT %_sysconfdir/klipper/ %buildroot/%_localstatedir/moonraker_data/config/klipper
ln -sT %_logdir/klipper %buildroot/%_localstatedir/moonraker_data/logs/klipper

%post
getent group moonraker-admin >/dev/null || groupadd -r moonraker-admin
if getent passwd klipper >/dev/null 2>&1; then
    if ! groups klipper 2>/dev/null | grep -qw moonraker-admin; then
        usermod -a -G moonraker-admin klipper
    fi
fi

%files -n python3-module-%name
%python3_sitelibdir_noarch/moonraker
%python3_sitelibdir_noarch/moonraker-%version.dist-info

%files
%_bindir/moonraker
%attr(755,klipper,klipper) %dir %_localstatedir/moonraker_data
%attr(755,klipper,klipper) %dir %_localstatedir/moonraker_data/config
%attr(755,klipper,klipper) %dir %_localstatedir/moonraker_data/config/klipper
%attr(755,klipper,klipper) %config(noreplace) %_localstatedir/moonraker_data/config/moonraker.conf
%attr(755,klipper,klipper) %dir %_localstatedir/moonraker_data/logs
%attr(755,klipper,klipper) %_localstatedir/moonraker_data/logs/klipper
%attr(755,klipper,klipper) %dir %_localstatedir/moonraker_data/logs/moonraker
%_datadir/polkit-1/rules.d/moonraker.rules
%_unitdir/moonraker.service
%doc README.md

%changelog
* Tue Oct 21 2025 Arseniy Romenskiy <romenskiy@altlinux.org> 0.9.3-alt1
- Initial build.
