Summary: Simple console clock
Name: tty-clock
Version: 2.3
Release: alt2
License: BSD 3-Clause
Group: Shells
Url: http://github.com/xorg62/tty-clock
Packager: Artyom Bystrov <arbars@altlinux.org>
Source: %name-%version.tar

BuildRequires: libncursesw-devel
Requires: termutils

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
* Tue Mar 31 2020 Artyom Bystrov <arbars@altlinux.org> 2.3-alt2
- Fixed cense tag
- Replaced libncurses
- Add termutils in Requires

* Mon Mar 30 2020 Artyom Bystrov <arbars@altlinux.org> 2.3-alt1
- initial build for ALT Sisyphus
