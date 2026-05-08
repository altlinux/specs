%define _unpackaged_files_terminate_build 1
%global import_path github.com/F1bonacc1/process-compose

Name: process-compose
Version: 1.110.0
Release: alt1
Summary: Process Compose is a simple and flexible scheduler and orchestrator to manage non-containerized applications.
License: Apache-2.0
Group: Monitoring
Url: https://github.com/F1bonacc1/process-compose

Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: git

Requires: nginx

%description
%summary

%prep
%setup -a 1
%patch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor "

%golang_prepare

#golang_build 
%make_build build

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install
mkdir -p %buildroot%_sysconfdir/xdg/%name
install -p -Dm755 bin/%name %buildroot%_bindir/
install -p -D -m 640 process-compose.yaml %buildroot%_sysconfdir/%name/process-compose.yaml
ln -s %_sysconfdir/%name/process-compose.yaml %buildroot%_sysconfdir/xdg/%name/process-compose.yaml

%check
%make test

%files
%doc *.md
%_bindir/%name
%config(noreplace) %_sysconfdir/%name/process-compose.yaml
%_sysconfdir/xdg/%name/process-compose.*

%changelog
* Fri May 08 2026 Pavel Shilov <zerospirit@altlinux.org> 1.110.0-alt1
- Update to new version 1.110.0.

* Fri Apr 10 2026 Pavel Shilov <zerospirit@altlinux.org> 1.103.0-alt1
- Update to new version 1.103.0.

* Thu Feb 26 2026 Pavel Shilov <zerospirit@altlinux.org> 1.94.0-alt1
- Update to new version 1.94.0.

* Wed Feb 04 2026 Pavel Shilov <zerospirit@altlinux.org> 1.90.0-alt1
- Update to new version 1.90.0.

* Tue Dec 23 2025 Pavel Shilov <zerospirit@altlinux.org> 1.85.0-alt1
- Update to new version 1.85.0.

* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 1.78.0-alt2
- Update non-code file from vendor to meet RF legal constraints.

* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 1.78.0-alt1
- 1.75.2 -> 1.78.0
- Remove non-code file from vendor to meet RF legal constraints.

* Thu Sep 25 2025 Pavel Shilov <zerospirit@altlinux.org> 1.75.2-alt1
- Initial build for Sisyphus.
