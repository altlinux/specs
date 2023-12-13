%define _unpackaged_files_terminate_build 1

Name: dualsensectl
Version: 0.4
Release: alt1

Summary: Linux tool for controlling PS5 DualSense controllers

License: GPLv2
Group: System/Configuration/Hardware
Url: https://github.com/nowrep/dualsensectl

Source: %name-%version.tar
Source2: 70-%name.rules

BuildRequires: libdbus-devel
BuildRequires: libhidapi-devel
BuildRequires: pkgconfig(libudev)

%description
%summary

%prep
%setup
sed -i "s|CFLAGS += -O2 -s -DNDEBUG|CFLAGS += %optflags_default|" Makefile

%build
%make_build

%install
%makeinstall_std
install -Dm 644 %SOURCE2 %buildroot%_udevrulesdir/70-%name.rules

%files
%doc README.md LICENSE
%_bindir/%name
%_datadir/bash-completion/completions/dualsensectl
%_datadir/zsh/site-functions/_dualsensectl
%_udevrulesdir/70-%name.rules

%changelog
* Thu Dec 07 2023 Mikhail Tergoev <fidel@altlinux.org> 0.4-alt1
- initial build for ALT Sisyphus
