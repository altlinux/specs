%global _unpackaged_files_terminate_build 1
# Vendorized go modules
# $ go generate
# $ GO111MODULE=on go mod vendor -v
# $ git add -f vendor
# $ git commit -n --no-post-rewrite -m "add go vendor modules"

Name: clickhouse-backup
Version: 2.1.2
Release: alt1
Summary: Tool for easy ClickHouse backup and restore with cloud storages support
Group: Databases
License: MIT
Url: https://github.com/AlexAkulov/clickhouse-backup/
Source0: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
Tool for easy ClickHouse backup and restore with cloud storages support.

%prep
%setup

%build
export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux

go build -ldflags " \
    -X main.version=$VERSION \
    -X main.commit=$COMMIT \
    -X main.branch=$BRANCH " \
    -o clickhouse-backup/clickhouse-backup \
    ./cmd/clickhouse-backup

%install
%__install -pDm0755 clickhouse-backup/clickhouse-backup %buildroot%_bindir/%name

# generation of the config file
%__install -pdm0750 %buildroot%_sysconfdir/%name
./clickhouse-backup/clickhouse-backup default-config > %buildroot%_sysconfdir/%name/config.yml

%files
%_bindir/%name
%dir %attr(0750,root,root) %_sysconfdir/%name
%attr(0640,root,root) %config(noreplace) %_sysconfdir/%name/config.yml

%changelog
* Tue Nov 01 2022 Anton Farygin <rider@altlinux.ru> 2.1.2-alt1
- 1.6.1 -> 2.1.2

* Tue Aug 30 2022 Anton Farygin <rider@altlinux.ru> 1.6.1-alt1
- 1.4.5 -> 1.6.1

* Thu Jun 23 2022 Anton Farygin <rider@altlinux.ru> 1.4.5-alt1
- 1.4.0 -> 1.4.5

* Fri May 27 2022 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- 1.3.2 -> 1.4.0

* Wed Apr 20 2022 Anton Farygin <rider@altlinux.ru> 1.3.2-alt1
- 1.3.1 -> 1.3.2

* Sun Feb 20 2022 Anton Farygin <rider@altlinux.ru> 1.3.1-alt1
- 1.3.0 -> 1.3.1

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 1.3.0-alt1
- 1.2.2 -> 1.3.0

* Mon Nov 29 2021 Anton Farygin <rider@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Mon Nov 01 2021 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Oct 29 2021 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Tue Oct 12 2021 Anton Farygin <rider@altlinux.ru> 1.1.0-alt1
- first build for ALT
