%define import_path github.com/siderolabs/bldr
%define sha 71a72d9
%define tag v%version

Name: bldr
Version: 0.6.0
Release: alt1
Summary: Tool to build and package software distributions

Group: Development/Tools
License: MPL-2.0

Url: https://github.com/siderolabs/bldr
Vcs: https://github.com/siderolabs/bldr.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang > 1.23.4 
BuildRequires: /proc

%description
bldr is a tool to build and package software distributions.
Build processruns in buildkit(or docker buildx),
build result can be exported as container image.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/internal/version.Name=bldr \
                -X %import_path/internal/version.SHA=%sha \
                -X %import_path/internal/version.Tag=%tag"

%golang_prepare

%golang_build cmd/bldr

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p \
    %buildroot%_datadir/bash-completion/completions \
    %buildroot%_datadir/zsh/site-functions \
    %buildroot%_datadir/fish/vendor_completions.d

%buildroot%_bindir/bldr completion bash > %buildroot%_datadir/bash-completion/completions/bldr
%buildroot%_bindir/bldr completion zsh > %buildroot%_datadir/zsh/site-functions/_bldr
%buildroot%_bindir/bldr completion fish > %buildroot%_datadir/fish/vendor_completions.d/bldr


%files
%_bindir/bldr
%_datadir/bash-completion/completions/bldr
%_datadir/zsh/site-functions/_bldr
%_datadir/fish/vendor_completions.d/bldr
%doc *.md

%changelog
* Tue Jun 02 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.6.0-alt1
- New version 0.6.0.

* Sun Dec 21 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.5.6-alt1
- New version 0.5.6.

* Mon Nov 17 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.5.5-alt1
- New version 0.5.5.

* Mon Oct 06 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.5.4-alt1
- New version 0.5.4.

* Sat Aug 30 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.5.2-alt1
- New version 0.5.2.

* Mon Jul 14 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.5.0-alt1
- New version 0.5.0.

* Fri Apr 18 2025 Maxim Slipenko <maks1ms@altlinux.org> 0.4.1-alt1
- New version 0.4.1.

* Thu Jan 30 2025 Alexey Kostarev <kaf@altlinux.org> 0.3.2-alt1
- Initial build.

