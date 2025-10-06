%global import_path github.com/opentofu/opentofu
%global _unpackaged_files_terminate_build 1

Name: opentofu
Version: 1.10.6
Release: alt1
Summary: OpenTofu lets you declaratively manage your cloud infrastructure

Group: Development/Tools
License: MPL-2.0

Url: https://github.com/opentofu/opentofu
Vcs: https://github.com/opentofu/opentofu.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch:  %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang
BuildRequires: /proc

%description
OpenTofu lets you declaratively manage your cloud infrastructure.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/version.dev=no \
                -X main.version=v%{version} "

%golang_prepare

%golang_build cmd/tofu

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Mon Oct 06 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.6-alt1
- New version 1.10.6.

* Mon Jul 14 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.2-alt1
- New version 1.10.2.

* Wed May 07 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.9.1-alt1
- Initial build

