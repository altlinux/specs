%global _unpackaged_files_terminate_build 1
%global import_path github.com/sigstore/policy-controller
%global commit cc75baab1d34d3bae47bde7bd934bf79e5ca3afc

Name: policy-controller
Version: 0.15.1
Release: alt1

Summary: admission controller to enforce policy on a Kubernetes cluster

License: Apache-2.0
Group: System/Configuration/Other

Url: https://docs.sigstore.dev/%name
Vcs: https://github.com/sigstore/%name

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
The %name admission controller can be used to enforce policy on a
Kubernetes cluster based on verifiable supply-chain metadata from cosign.

%prep
%setup

%build
DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
export BUILD_DATE=$(date -u -d "@$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null || \
            date -u -r "$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null || \
            date -u "$DATE_FMT")

export LDFLAGS="-X sigs.k8s.io/release-utils/version.gitCommit=%commit \
                -X sigs.k8s.io/release-utils/version.gitVersion=%version \
                -X sigs.k8s.io/release-utils/version.gitTreeState=clean \
                -X sigs.k8s.io/release-utils/version.buildDate=$BUILD_DATE"
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare
%gobuild -o %name ./cmd/webhook

%install
install -Dm 755 %name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc *.md *.txt CODEOWNERS LICENSE

%changelog
* Tue Jun 09 2026 Aleksandr Gamzin <gamzin@altlinux.org> 0.15.1-alt1
- Initial build for Sisyphus.
