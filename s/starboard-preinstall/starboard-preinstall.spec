%define script_name starboard-fix-install-script

Name: starboard-preinstall
Version: 1.0
Release: alt4

Summary: Script to fixing StarBoardSoftware installation script for ALTLinux
Summary(ru_RU.UTF8): Сценарий для исправления сценария установки StarBoardSoftware под ALTLinux
License: GPL
Group: Education

Source: %name.tar
Packager: Rinat Bikov <becase@altlinux.org>
BuildArch: noarch

Requires: lsb-init
Provides: perl(strict)

%description
Script starboard-fix-install-script  must be used after installation of package
StarBoardSoftware and before start install.sh script of StarBoardSoftware.

%description -l ru_RU.UTF8
Сценарий starboard-fix-install-script, входящий в состав этого пакета, необходимо
запустить после установки пакета StarBoardSoftware и перед запуском сценария 
установки install.sh, входящего в состав пакета StarBoardSoftware.

%prep
%setup -n %name

%install
%__install -pD -m 755 %script_name %buildroot/%_sbindir/%script_name

%files
%_sbindir/%script_name

%changelog
* Fri Mar 4 2011 Rinat Bikov <becase@altlinux.org> 1.0-alt4
- deleted ldconfig from installation script

* Wed Mar 2 2011 Rinat Bikov <becase@altlinux.org> 1.0-alt3
- added fake provides perl(strict)

* Fri Feb 11 2011 Rinat Bikov <becase@altlinux.org> 1.0-alt2
- fixed misprint in changelog

* Fri Feb 11 2011 Rinat Bikov <becase@altlinux.org> 1.0-alt1
- intial build
