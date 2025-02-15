%define _unpackaged_files_terminate_build 1

Name: dualsensectl
Version: 0.7
Release: alt1

Summary: Linux tool for controlling PS5 DualSense controllers

License: GPLv2
Group: System/Configuration/Hardware
Url: https://github.com/nowrep/dualsensectl

Source: %name-%version.tar
Source2: 70-%name.rules

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson cmake gcc-c++
BuildRequires: libdbus-devel
BuildRequires: libhidapi-devel
BuildRequires: pkgconfig(libudev)

%description
%summary

%prep
%setup

%build
%meson
%meson_build -v

%install
DESTDIR=%buildroot meson install -C %_cmake__builddir
install -Dm 755 completion/dualsensectl %buildroot%_datadir/bash-completion/completions/dualsensectl
install -Dm 755 completion/_dualsensectl %buildroot%_datadir/zsh/site-functions/_dualsensectl
install -Dm 644 %SOURCE2 %buildroot%_udevrulesdir/70-%name.rules

%files
%doc README.md LICENSE
%_bindir/%name
%_datadir/bash-completion/completions/dualsensectl
%_datadir/zsh/site-functions/_dualsensectl
%_udevrulesdir/70-%name.rules

%changelog
* Sat Feb 15 2025 Mikhail Tergoev <fidel@altlinux.org> 0.7-alt1
- updated to version 0.7
- updated udev rules
- moved to meson build

* Mon Aug 19 2024 Mikhail Tergoev <fidel@altlinux.org> 0.6-alt1
- 0.6

* Mon Apr 01 2024 Mikhail Tergoev <fidel@altlinux.org> 0.5-alt1
- 0.5

* Thu Dec 07 2023 Mikhail Tergoev <fidel@altlinux.org> 0.4-alt1
- initial build for ALT Sisyphus
