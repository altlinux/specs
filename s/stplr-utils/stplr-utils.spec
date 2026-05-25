%global import_path go.stplr.dev/stplr-utils
%global _unpackaged_files_terminate_build 1

Name:    stplr-utils
Version: 0.0.13
Release: alt1

Summary: Utilities for working with stplr and Staplerfile
License: AGPL-3.0-only
Group:   Development/Tools
Url:     https://altlinux.space/stapler/stplr-utils
Vcs:     https://altlinux.space/stapler/stplr-utils.git

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.

%package -n stplr-spec
Summary: A command line tool for writing Staplerfile
Group:   Development/Tools

%description -n stplr-spec
%summary.

%package -n stplr-lint
Summary: A command line tool for linting Staplerfile
Group:   Development/Tools

%description -n stplr-lint
%summary.

%package -n stplr-language-server
Summary: A language server for Staplerfile
Group:   Development/Tools

%description -n stplr-language-server
%summary.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

%golang_build cmd/*

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files -n stplr-spec
%_bindir/stplr-spec

%files -n stplr-lint
%_bindir/stplr-lint

%files -n stplr-language-server
%_bindir/stplr-language-server

%changelog
* Mon May 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.0.13-alt1
- New version 0.0.13.

* Tue Mar 17 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.0.11-alt1
- Initial build.

