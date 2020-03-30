Summary: Simple console clock
Name: tty-clock
Version: 2.3
Release: alt1
License: GPLv2+
Group: Shells
Url: http://github.com/xorg62/tty-clock
Packager: Artyom Bystrov <arbars@altlinux.org>
Source: %name-%version.tar

BuildRequires: libncurses-devel

%description
An analog clock in ncurses

%prep
%setup
chmod -x README

%build
%make_build

%install

install -d -m 755 %buildroot%_bindir
install -m 755 %name %buildroot%_bindir/

%files
%doc README
%_bindir/%name

%changelog
* Mon Mar 30 2020 Artyom Bystrov <arbars@altlinux.org> 2.3-alt1
- initial build for ALT Sisyphus