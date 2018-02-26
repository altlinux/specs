Name: rovclock
Version: 0.6e
Release: alt1

Summary: Radeon overclocking utility
License: GPL v2
Group: System/Configuration/Hardware

Url: http://www.hasw.net/linux/
Source: http://www.hasw.net/linux/%name-%version.tar.bz2
Packager: Michael Shigorin <mike@altlinux.org>

ExclusiveArch: %ix86 x86_64

Summary(pl.UTF-8): Narzędzie do zmiany częstotliwości pracy chipsetów Radeon

%description
Radeon overclocking utility

%description -l pl.UTF-8
Narzędzie do zmiany częstotliwości pracy chipsetów Radeon

%prep
%setup -q

%build
%make

%install
install -pD -m755 %name %buildroot%_bindir/%name

%files
%doc ChangeLog README
%_bindir/*

%changelog
* Sun Mar 30 2008 Michael Shigorin <mike@altlinux.org> 0.6e-alt1
- built for ALT Linux
- spec based on PLD rev1.4

