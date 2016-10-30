Summary: IRQ balancing daemon
Name: birq
Version: 1.3.0
Release: alt1
License: BSD
Group: System/Kernel and hardware
Url: http://libcode.org/projects/birq/
Source0: %name-%version.tar
Source1: %name.sysconfig
Source2: %name.service

Patch: %name-%version-%release.patch

%description
birq is a daemon that distributes IRQ load across multiple CPUs

%prep
%setup
%patch -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std
# install config
install -p -D -m 0644 %SOURCE1 %buildroot%_sysconfdir/sysconfig/%name
# install init script
install -p -D -m 0644 %SOURCE2 %buildroot%_unitdir/%name.service

%files
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service
%_sbindir/%name
%doc README doc/%name.md

%changelog
* Sun Oct 30 2016 Terechkov Evgenii <evg@altlinux.org> 1.3.0-alt1
- 1.3.0-5-g89ec6bd
- Initial build for ALT Linux Sisyphus
