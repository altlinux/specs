%set_verify_elf_method fhs=relaxed

Name: dbeaver
Version: 7.3.5
Release: alt1

Summary: Universal Database Manager
Summary(ru_RU.UTF-8): Универсальный менеджер баз данных
License: Apache-2.0
Group: Databases

URL: https://%name.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://download.%name.com/community/%version/%name-ce-%version-linux.gtk.x86_64-nojdk.tar.gz
Source: %name-ce-%version-linux.gtk.x86_64-nojdk.tar

Requires: java

BuildRequires: libsecret

%description
DBeaver is free and open source universal database tool for developers and database administrators.

*  Usability is the main goal of this project, program UI is carefully designed and implemented.
*  It is free and open-source (ASL).
*  It is multiplatform.
*  It is based on opensource framework and allows writing of various extensions (plugins).
*  It supports any database having a JDBC driver.
*  It may handle any external datasource which may or may not have a JDBC driver.
*  There is a set of plugins for different databases and different database management utilities (e.g. ERD, data transfer, compare, data export/import, mock data generation, etc).
*  It has a great number of features.

%prep
%setup -n %name

%install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_datadir/%name
%__mkdir_p %buildroot%_desktopdir
%__cp -r . %buildroot%_datadir/%name/
%__rm %buildroot%_datadir/%name/%name.desktop
%__install -m 0755 %name.desktop %buildroot%_desktopdir/%name.desktop
%__ln_s %_datadir/%name/%name %buildroot%_bindir/%name

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%config %_datadir/%name/%name.ini

%changelog
* Fri Feb 19 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt1
- Initial build for ALT Linux
