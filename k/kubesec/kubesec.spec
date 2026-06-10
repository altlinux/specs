%define _unpackaged_files_terminate_build 1
%define import_path github.com/controlplaneio/kubesec

Name: kubesec
Version: 2.14.2
Release: alt2

Summary: Security risk analysis for Kubernetes resources
License: Apache-2.0
Group: Development/Other
Url: https://kubesec.io
Vcs: https://github.com/controlplaneio/kubesec

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
Kubesec is a security risk analysis tool for Kubernetes resources.
It inspects Kubernetes manifests and assigns a score based on security
best practices, helping detect risky configurations before they are applied.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/controlplaneio/kubesec/v2/cmd.version=%version \
-X github.com/controlplaneio/kubesec/v2/cmd.commit=%version-%release \
-X github.com/controlplaneio/kubesec/v2/cmd.date=$(date -u +'%%Y-%%m-%%d')"

%golang_prepare
cd .build/src/%import_path/
%golang_build .

%install
ln -sf %_licensedir/Apache-2.0 LICENSE
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
$BUILDDIR/bin/kubesec completion bash | install -Dm644 /dev/stdin "%buildroot%_datadir/bash-completion/completions/kubesec"
$BUILDDIR/bin/kubesec completion zsh | install -Dm644 /dev/stdin "%buildroot%_datadir/zsh/site-functions/_kubesec"
$BUILDDIR/bin/kubesec completion fish | install -Dm644 /dev/stdin "%buildroot%_datadir/fish/vendor_completions.d/kubesec.fish"
$BUILDDIR/bin/kubesec completion powershell | install -Dm644 /dev/stdin "%buildroot%_datadir/powershell/completions/kubesec.ps1"

%golang_install

%files
%_bindir/kubesec
%_datadir/bash-completion/completions/kubesec
%_datadir/zsh/site-functions/_kubesec
%_datadir/fish/vendor_completions.d/kubesec.fish
%_datadir/powershell/completions/kubesec.ps1
%doc --no-dereference LICENSE 
%doc README.md 

%changelog
* Wed May 06 2026 Maxim Tulskiy <tulskijms@altlinux.org> 2.14.2-alt2
- Added shell completion files (bash, zsh, fish, powershell) (Closes: #58636).
- Fixed version info embedding via ldflags (Closes: #58635).

* Tue Aug 27 2025 Maxim Tulskiy <tulskijms@altlinux.org> 2.14.2-alt1
- Initial build for ALT Sisyphus.
