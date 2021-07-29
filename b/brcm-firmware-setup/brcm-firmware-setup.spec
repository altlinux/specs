%define _unpackaged_files_terminate_build 1

Name: brcm-firmware-setup
Version: 0.1
Release: alt1

Summary: brcm firmware file downloader
License: GPLv2+
Group: System/Kernel and hardware
Packager: Dmitry Terekhin <jqt4@altlinux.org>
Url: https://www.altlinux.org/RaspberryPi_firmware
BuildArch: noarch
Source0: %name-%version.tar

%description
The tool will download the brcm firmware from a hardcoded URL
and copy it to the /lib/firmware/brcm directory.

%description -l ru_RU.UTF-8
Данный скрипт загрузит файлы firmware brcm с определённых URL-адресов
и скопирует их в папку /lib/firmware/brcm.

%prep
%setup -q

%install
install -pD -m755 %name %buildroot/%_bindir/%name

%files
%doc README.en
%doc README.ru
%_bindir/%name

%changelog
* Thu Jul 29 2021 Dmitry Terekhin <jqt4@altlinux.org> 0.1-alt1
- Initial build
