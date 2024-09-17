Name: safeeyes
Version: 2.1.6
Release: alt1.2

Summary: Tool for reminding the user to take breaks

License: GPL-3.0-only
Group: Graphics
Url: https://github.com/slgobinath/SafeEyes

# Source-url: https://github.com/slgobinath/SafeEyes/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Patch: remove-distutils-for-python-3.12.patch

#BuildRequires: hicolor-icon-theme
BuildRequires(pre): rpm-build-python3

Requires: typelib(Notify)
Requires: typelib(AyatanaAppIndicator3)

BuildArch: noarch

%description
This utility reminds the user to take breaks whilst they are working
at the computer in an effort to alleviate eye strain (asthenopia).

%prep
%setup
%patch -p2

%build
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/*/*
%python3_sitelibdir/%name/
%python3_sitelibdir/%name-%version-py*.egg-info

%changelog
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
