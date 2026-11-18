%global import_path github.com/open-policy-agent/opa
%global _unpackaged_files_terminate_build 1
%global upstream_commit ba39415db4b3c90cd68942a74b3cc2223ec2b23c

Name:    opa
Version: 1.22.4
Release: alt1

Summary: Open source, general-purpose policy engine
License: Apache-2.0
Group:   Development/Other
URL:     https://www.openpolicyagent.org
Vcs:     https://github.com/open-policy-agent/opa

Source0: %name-%version.tar
Source1: vendor.tar
Source2: build-tools-vendor.tar

Patch0: %name-%version-i586-support.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.26.0

%description
Open Policy Agent (OPA) is an open source, general-purpose policy engine
that enables unified, context-aware policy enforcement across the entire
stack.

OPA is a graduated project in the Cloud Native Computing Foundation (CNCF)
landscape.

%prep
%setup -a 1

mkdir -p build/tools/vendor
tar -xf %SOURCE2 -C build/tools/vendor

%patch0 -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-buildmode=exe -trimpath -mod=vendor"
export TAGS="opa_wasm"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null || \
            date -u -r "$SOURCE_DATE_EPOCH" "$DATE_FMT" 2>/dev/null || \
            date -u "$DATE_FMT")

export LDFLAGS="-X %import_path/v1/version.Version=%version \
               -X %import_path/v1/version.Timestamp=$BUILD_DATE \
               -X %import_path/v1/version.Hostname=%buildhost \
               -X %import_path/v1/version.Vcs=%upstream_commit"

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1

%golang_install

install -d %buildroot%_datadir/bash-completion/completions
%buildroot%_bindir/%name completion bash \
    > %buildroot%_datadir/bash-completion/completions/%name

install -d %buildroot%_datadir/fish/vendor_completions.d
%buildroot%_bindir/%name completion fish \
    > %buildroot%_datadir/fish/vendor_completions.d/%name.fish

install -d %buildroot%_datadir/zsh/site-functions
%buildroot%_bindir/%name completion zsh \
    > %buildroot%_datadir/zsh/site-functions/_%name

%check
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-buildmode=exe -trimpath -mod=vendor"

%golang_prepare

# Skip AWS SSO credential service tests because they require
# network access to AWS SSO and OIDC endpoints.
%gotest -skip '^TestSSOCredentialService$' \
    -tags=opa_wasm -short ./...

%files
%doc *.md
%_bindir/%name
%_datadir/bash-completion/completions/%name
%_datadir/fish/vendor_completions.d/%name.fish
%_datadir/zsh/site-functions/_%name

%changelog
* Fri Nov 13 2026 Aleksandr Gamzin <gamzin@altlinux.org> 1.22.4-alt1
- Initial build for Sisyphus.
