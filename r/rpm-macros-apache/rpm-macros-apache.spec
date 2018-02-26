# hey Emacs, its -*- rpm-spec -*-

%define repocop_testdatadir %_datadir/repocop/testdata.d

Name: rpm-macros-apache
Version: 0.2
Release: alt2

Summary: RPM macros to Apache Web server
Summary(ru_RU.KOI8-R): RPM макросы для веб-сервера Apache
License: %asl
Group: Development/Other

Packager: Aleksey Avdeev <solo@altlinux.ru>

# rpm macro definitions
Source1: apache.rpm-macros

BuildPreReq: rpm-build-licenses
BuildPreReq: rpm-macros-webserver-common >= 1.1

Conflicts: rpm-macros-webserver-common < 1.1
Conflicts: apache-devel <= 1.3.41rusPL30.23-alt4.2
Conflicts: apache2-devel <= 2.2.9-alt2
Requires: rpm-macros-webserver-common >= 1.1

BuildArch: noarch

%description
The package provide a set of macros for packaging Web applications
according to the ALT Linux Web Packaging Policy.

%description -l ru_RU.KOI8-R
Макросы для обеспечения сборки пакетов веб серверов и приложений
в соответствии с ALT Linux Web Packaging Policy.


%package -n repocop-unittest-data-%name
Summary: Data file for repocop test platform
Summary(ru_RU.KOI8-R): Данные для тестов repocop
Group: Development/Other

Provides: %repocop_testdatadir/%name

%description -n repocop-unittest-data-%name
The package provide data file for repocop test platform.

%description -n repocop-unittest-data-%name -l ru_RU.KOI8-R
Пакет предоставляет данные для тестов repocop.


%install

install -pD -m644 %SOURCE1 %buildroot%_sysconfdir/rpm/macros.d/%name

mkdir -p %buildroot%repocop_testdatadir/
egrep '^[[:space:]]*%%[^%%[:space:]]+[[:space:]]' %SOURCE1 \
	| sort -r > %buildroot%repocop_testdatadir/%name

%files
%_sysconfdir/rpm/macros.d/%name

%files -n repocop-unittest-data-%name
%repocop_testdatadir/%name

%changelog
* Mon Aug 04 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt2
- Create repocop-unittest-data-%%name subpacage for repocop tests

* Mon Jul 14 2008 Aleksey Avdeev <solo@altlinux.ru> 0.2-alt1
- Readd %%post/%%postun scripts and %%version/%%release macros

* Mon Jul 14 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt1
- Fix Conflicts/Requires

* Sun Jul 13 2008 Aleksey Avdeev <solo@altlinux.ru> 0.1-alt0.1
- First build for ALT Linux
