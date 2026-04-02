%define _unpackaged_files_terminate_build 1
%define import_path github.com/nats-io/nsc

Name: nsc
Version: 2.12.2
Release: alt1

Summary: Tool for creating nkey/jwt based configurations
License: Apache-2.0
Group: Development/Tools
Url: https://nats-io.github.io/nsc/
Vcs: https://github.com/nats-io/nsc

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
A tool for creating NATS account and user access configurations.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

export LDFLAGS="-X  main.version=%version"
pushd $BUILDDIR/src/$IMPORT_PATH
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%doc docs README.md LICENSE
%_bindir/%name

%changelog
* Thu Apr 02 2026 Artem Krasovskiy <aibure@altlinux.org> 2.12.2-alt1
- Initial build for Sisyphus.
