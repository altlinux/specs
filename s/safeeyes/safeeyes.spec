Name: safeeyes
Version: 3.3.1
Release: alt1

Summary: Tool for reminding the user to take breaks

License: GPL-3.0-only
Group: Graphics
Url: https://github.com/slgobinath/SafeEyes

# Source-url: https://github.com/slgobinath/SafeEyes/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%add_python3_req_skip pywayland.client pywayland.protocol.wayland.wl_seat

Requires: typelib(Notify)
Requires: typelib(AyatanaAppIndicator3)

BuildArch: noarch

%description
This utility reminds the user to take breaks whilst they are working
at the computer in an effort to alleviate eye strain (asthenopia).

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

install -Dm644 %name/platform/io.github.slgobinath.SafeEyes.desktop %buildroot%_desktopdir/io.github.slgobinath.SafeEyes.desktop
install -Dm644 %name/platform/io.github.slgobinath.SafeEyes.metainfo.xml %buildroot%_datadir/metainfo/io.github.slgobinath.SafeEyes.metainfo.xml
mkdir -p %buildroot%_iconsdir/
cp -a %name/platform/icons/* %buildroot%_iconsdir/

%files
%doc README.md
%_bindir/%name
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_iconsdir/hicolor/*/*/*
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo %name}/

%changelog
* Tue Mar 10 2026 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt1
- new version 3.3.1 (with rpmrb script)
- switch to pyproject build

* Sun Jan 26 2025 Vitaly Lipatov <lav@altlinux.ru> 2.2.3-alt1
- new version 2.2.3 (with rpmrb script)

* Tue Sep 17 2024 Andrey Cherepanov <cas@altlinux.org> 2.1.6-alt1.2
- NMU: added requirements of libayatana-appindicator3-gir (ALT #45647).

* Thu Oct 19 2023 Grigory Ustinov <grenka@altlinux.org> 2.1.6-alt1.1
- NMU: dropped dependency on distutils.

* Tue Aug 01 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1.6-alt1
- new version 2.1.6 (with rpmrb script)

* Thu Mar 09 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1.5-alt1
- new version 2.1.5 (with rpmrb script)

* Thu Mar 09 2023 Vitaly Lipatov <lav@altlinux.ru> 2.1.4-alt1
- initial build for ALT Sisyphus
