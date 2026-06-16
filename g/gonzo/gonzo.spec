%define _unpackaged_files_terminate_build 1
%define import_path github.com/control-theory/gonzo

Name: gonzo
Version: 0.4.2
Release: alt1

Summary: Gonzo! The Go based TUI log analysis tool
License: MIT
Group: Monitoring
Url: https://gonzo.controltheory.com
Vcs: https://github.com/control-theory/gonzo

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
A powerful, real-time log analysis terminal UI inspired by k9s. Analyze log
streams with beautiful charts, AI-powered insights, and advanced filtering - all
from your terminal

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
export VERSION="%version"
export COMMIT="unknown"
export BUILD_TIME=$(date -u +"%%Y-%%m-%%dT%%H:%%M:%%SZ")
export GO_VERSION=$(go version | cut -d' ' -f3)
export LDFLAGS="-X main.version=${VERSION} -X main.commit=${COMMIT} -X main.buildTime=${BUILD_TIME} -X main.goVersion=${GO_VERSION}"
pushd $BUILDDIR/src/$IMPORT_PATH
%golang_build cmd/gonzo
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Thu Jun 11 2026 Artem Krasovskiy <aibure@altlinux.org> 0.4.2-alt1
- New version 0.4.2.

* Wed Feb 18 2026 Artem Krasovskiy <aibure@altlinux.org> 0.3.1-alt1
- New version 0.3.1.

* Fri Dec 12 2025 Artem Krasovskiy <aibure@altlinux.org> 0.3.0-alt1
- New version 0.3.0.

* Fri Oct 24 2025 Artem Krasovskiy <aibure@altlinux.org> 0.2.1-alt1
- New version 0.2.1.

* Wed Oct 01 2025 Artem Krasovskiy <aibure@altlinux.org> 0.2.0-alt1
- New version 0.2.0.

* Wed Sep 10 2025 Artem Krasovskiy <aibure@altlinux.org> 0.1.7-alt1
- Initial build for Sisyphus.
