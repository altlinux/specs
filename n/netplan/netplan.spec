Name:    netplan
Version: 1.1.1
Release: alt1

Summary: Backend-agnostic network configuration in YAML
License: GPL-3.0
Group:   System/Configuration/Networking
URL:     https://github.com/canonical/netplan

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires(pre): rpm-macros-meson
BuildRequires:  meson
BuildRequires:  python3-module-pyflakes
BuildRequires:  python3-module-pycodestyle
BuildRequires:  python3-module-coverage
BuildRequires:  pytest3
BuildRequires:  python3-dev
BuildRequires:  python3(cffi)
BuildRequires:  pkgconfig(cmocka)

BuildRequires:  python3(setuptools)
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(yaml-0.1)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  %_bindir/pandoc

Requires:       iproute2
Requires:       python3(cffi)

%add_python3_path %_datadir/%name

Source:  %name-%version.tar

Patch1: netplan-1.1.1-alt-meson.patch
Patch2: netplan-1.1.1-alt-libexec.patch

%description
%summary

%prep
%setup -n %name-%version
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
if [ '%python3_sitelibdir' != '%python3_sitelibdir_noarch' ]; then
    mv %buildroot%python3_sitelibdir_noarch/%name/* -t %buildroot%python3_sitelibdir/%name
    rmdir %buildroot%python3_sitelibdir_noarch/%name
fi
mkdir -p %buildroot%_sysconfdir/%name

%files
%python3_sitelibdir/%name
%_sbindir/%name
%_gen_dir/%name
%_libexecdir/%name
%_libdir/libnetplan.so.1
%_datadir/bash-completion/completions/%name
%_datadir/%name
%_defaultdocdir/%name
%_datadir/dbus-1/system-services/io.netplan.Netplan.service
%_datadir/dbus-1/system.d/io.netplan.Netplan.conf
%dir %_sysconfdir/%name
%doc *.md
%_man5dir/%{name}*
%_man8dir/%{name}*

%changelog
* Wed Nov 20 2024 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.1-alt1
- New version 1.1.1 (Fixes: CVE-2022-4968).

* Tue Jul 02 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.106-alt2
- Fix rebuild using %%_gen_dir

* Mon Apr 24 2023 Mikhail Gordeev <obirvalger@altlinux.org> 0.106-alt1
- New version 0.106.

* Thu Jan 13 2022 Mikhail Gordeev <obirvalger@altlinux.org> 0.103-alt2
- Fix rebuild

* Mon Nov 08 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.103-alt1
- new version 0.103

* Thu Jan 14 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.101-alt1
- new version 0.101

* Thu Mar 19 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.98-alt1
- new version 0.98
- (ALT#37740) fix path to wpa_supplicant

* Thu Aug 15 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.97-alt2
- Remove Requires to systemd and systemd-networkd, it could use NetworkManager

* Fri Jul 26 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.97-alt1
- Initial build for Sisyphus
