%define tested_version 8.3.24.1667

Name:    1c-preinstall-full
Version: 8.3
Release: alt13

Summary: Set correct environment for 1C:Enterprise platform, including proprietary components
License: GPL-2.0
Group:   System/Libraries
URL:     http://1c.ru/
Packager: Pavel Isopenko <pauli@altlinux.org>

BuildArch: noarch

Requires: 1c-preinstall
Requires: fonts-ttf-ms

%description
This metapackage is intend to deploy correct environment for 1C:Enterprise platform installation.

This package also install Microsoft (tm) fonts are needed by 1C:Enterprise.

Tested with 1C:Enterprise platform version %tested_version

%description -l ru_RU.UTF-8
Метапакет предназначен для развёртывания корректного окружения для платформы 1С:Предприятия.

Также устанавливает шрифты Microsoft (tm), необходимые для отдельных конфигураций.

Проверено с версией платформы 1С:Предприятие %tested_version

%files

%changelog
* Thu Feb 13 2025 Pavel Isopenko <pauli@altlinux.org> 8.3-alt13
- Return to Sisyphus

