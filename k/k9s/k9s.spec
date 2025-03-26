%define _unpackaged_files_terminate_build 1
%define import_path github.com/derailed/k9s

Name: k9s
Version: 0.40.10
Release: alt1

Summary: Kubernetes CLI To Manage Your Clusters In Style
License: Apache-2.0
Group: Development/Other
Url: https://k9scli.io/
Vcs: https://github.com/derailed/k9s

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
K9s provides a terminal UI to interact with your Kubernetes clusters.
The aim of this project is to make it easier to navigate, observe and manage
your applications in the wild. K9s continually watches Kubernetes for changes
and offers subsequent commands to interact with your observed resources.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/derailed/k9s/cmd.commit=%version-%release
-X github.com/derailed/k9s/cmd.date=$(date -u +'%%Y-%%m-%%d')
-X github.com/derailed/k9s/cmd.version=%version"

%golang_prepare
cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
$BUILDDIR/bin/k9s completion bash | install -Dm644 /dev/stdin "%buildroot%_datadir/bash-completion/completions/k9s"
$BUILDDIR/bin/k9s completion zsh  | install -Dm644 /dev/stdin "%buildroot%_datadir/zsh/site-functions/_k9s"
$BUILDDIR/bin/k9s completion fish | install -Dm644 /dev/stdin "%buildroot%_datadir/fish/vendor_completions.d/k9s.fish"
install -Dm755 $BUILDDIR/bin/k9s "%buildroot%_bindir/k9s"

%golang_install

%files
%_bindir/k9s
%_datadir/bash-completion/completions/k9s
%_datadir/zsh/site-functions/_k9s
%_datadir/fish/vendor_completions.d/k9s.fish
%doc COPYING README.md

%changelog
* Wed Mar 26 2025 Maxim Tulskiy <tulskijms@altlinux.org> 0.40.10-alt1
- Initial build for ALT Sisyphus.

