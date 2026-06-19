%global _unpackaged_files_terminate_build 1
%global import_path github.com/garethgeorge/backrest
# git rev-parse --short v%version
%global commit_hash a389bbc

Name: backrest
Version: 1.13.0
Release: alt1
Summary: Web UI and orchestrator for restic backup
License: GPL-3.0
Group: Archiving/Backup
Url: https://garethgeorge.github.io/backrest
VCS: https://github.com/garethgeorge/backrest

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: backrest.sysconfig
Source4: backrest.service

Patch: alt-fix-inlang-settings.patch

ExclusiveArch: x86_64

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: npm

Requires: restic

%description
Backrest is a web-accessible backup solution built on top of restic.
Backrest provides a WebUI which wraps the restic CLI and makes it easy
to create repos, browse snapshots, and restore files.

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
# npm --prefix webui install
# git add webui/node_modules -f && git commit -m "Updated node modules."
%setup -a 1 -a 2
%patch -p1

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export BACKREST_BUILD_VERSION=%version

npm --prefix webui run build

%golang_prepare
cd .gopath/src/%import_path/cmd/backrest
go build --ldflags "-X main.version=%version -X main.commit=%commit_hash" -o=backrest .

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_sysconfdir/{backrest,sysconfig} \
         %buildroot%_sharedstatedir/backrest
install -m 0755 .gopath/src/%import_path/cmd/backrest/backrest %buildroot%_bindir/backrest
install -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/backrest
install -m 0644 %SOURCE4 %buildroot%_unitdir/backrest.service
touch %buildroot%_sysconfdir/backrest/config.json

%post
%post_service backrest

%preun
%preun_service backrest

%files
%_bindir/backrest
%_unitdir/backrest.service
%config(noreplace) %_sysconfdir/sysconfig/backrest
%ghost %config(noreplace) %_sysconfdir/backrest/config.json
%dir %_sysconfdir/backrest
%dir %_sharedstatedir/backrest
%doc LICENSE

%changelog
* Fri Jun 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.13.0-alt1
- Updated to version 1.13.0.

* Thu Mar 19 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.1-alt1
- Updated to version 1.12.1.

* Sun Feb 22 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.0-alt1
- Updated to version 1.12.0.

* Tue Feb 03 2026 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.2-alt1
- Updated to version 1.11.2.

* Sun Nov 02 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.10.1-alt1
- Updated to version 1.10.1.

* Fri Aug 29 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.9.2-alt1
- Updated to version 1.9.2.

* Sat Aug 09 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.9.1-alt1
- Updated to version 1.9.1.

* Wed Jul 23 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.8.1-alt1
- Updated to version 1.8.1.

* Sat Mar 08 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.2-alt2
- Fixed cache directory path.

* Sat Feb 22 2025 Alexander Makeenkov <amakeenk@altlinux.org> 1.7.2-alt1
- Initial build for ALT.
