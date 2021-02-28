%set_verify_elf_method fhs=relaxed

Name: dbeaver
Version: 21.0.0
Release: alt1

Summary: Universal Database Manager
Summary(ru_RU.UTF-8): Универсальный менеджер баз данных
License: Apache-2.0
Group: Databases

URL: https://%name.io/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

# https://github.com/%name/%name/archive/%version/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.desktop
Source2: maven-local-repository.tar

BuildRequires: /proc
BuildRequires: java-11-openjdk-headless
BuildRequires: libsecret
BuildRequires: maven-lib
BuildRequires: rpm-build-java
BuildRequires: xmvn-resolve

Requires: java-11-openjdk-headless

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
%setup -b 2

%__rm -rf ~/.m2
%__mv -Tf ../.m2 ~/.m2

%build
mvn -o package

%install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_datadir
%__mkdir_p %buildroot%_desktopdir
%__cp -r product/standalone/target/products/org.jkiss.dbeaver.core.product/linux/gtk/x86_64/%name %buildroot%_datadir
%__install -m 0755 %SOURCE1 %buildroot%_desktopdir/%name.desktop
%__ln_s %_datadir/%name/%name %buildroot%_bindir/%name

%files
%_bindir/%name
%_datadir/%name
%_desktopdir/%name.desktop
%config %_datadir/%name/%name.ini

%changelog
* Sun Feb 28 2021 Nazarov Denis <nenderus@altlinux.org> 21.0.0-alt1
- Version 21.0.0

* Fri Feb 26 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt3
- Add requires on java-openjdk-headless

* Thu Feb 25 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt2
- Build with maven

* Fri Feb 19 2021 Nazarov Denis <nenderus@altlinux.org> 7.3.5-alt1
- Initial build for ALT Linux
