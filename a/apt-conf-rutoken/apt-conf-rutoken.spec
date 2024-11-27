Name: apt-conf-rutoken
Summary: Official repository of Rutoken software for ALT
Version: 1.0
Release: alt1

License: Public-Domain
Group: System/Base
URL: https://www.rutoken.ru/

ExclusiveArch: %ix86 x86_64 aarch64

Source: %name-%version.tar

Requires: apt-https

%description
%{summary}.

Available packages: libnpRutokenPlugin, librtengine1, librtpkcs11ecp and
rtcontrolcenter.

%prep
%setup
%ifarch %ix86
echo "rpm https://repo.rutoken.ru alt/stable/i586 classic" > rutoken.list
%endif
%ifarch x86_64
echo "rpm https://repo.rutoken.ru alt/stable/x86_64 classic" > rutoken.list
%endif
%ifarch aarch64
echo "rpm https://repo.rutoken.ru alt/stable/aarch64 classic" > rutoken.list
%endif

%install
install -Dpm 0644 rutoken.list %buildroot%_sysconfdir/apt/sources.list.d/rutoken.list

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/rutoken.list

%changelog
* Wed Nov 27 2024 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
