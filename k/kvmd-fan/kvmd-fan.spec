Name: kvmd-fan
Version: 0.24
Release: alt1

Summary: Fan controller daemon
License: GPLv3
Group: System/Servers
Url: https://github.com/pikvm/kvmd-fan

Source: %name-%version-%release.tar

BuildRequires: libiniparser-devel
BuildRequires: libmicrohttpd-devel
BuildRequires: libgpiod-devel

%description
%summary

%prep
%setup
sed -ri '/^_CFLAGS/ s,$, %optflags -I%_includedir/iniparser,' Makefile

%build
make WITH_WIRINGPI_STUB=yes

%install
install -pm0755 -D kvmd-fan %buildroot%_bindir/kvmd-fan
install -pm0644 -D kvmd-fan.service %buildroot%_unitdir/kvmd-fan.service
install -pm0644 -D /dev/null %buildroot%_sysconfdir/kvmd/fan.ini

%files
%doc README*
%ghost %config(noreplace) %_sysconfdir/kvmd/fan.ini
%_unitdir/kvmd-fan.service
%_bindir/kvmd-fan

%changelog
* Thu Dec 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.24-alt1
- initial
