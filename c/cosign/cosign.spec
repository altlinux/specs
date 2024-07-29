%global import_path github.com/sigstore/cosign/v2
%global _unpackaged_files_terminate_build 1

%define revision deed3631520ddeb6cc7d81ace205a97342c8daab

%def_with check

Name:    cosign
Version: 2.3.0
Release: alt1

Summary: Container Signing, Verification and Storage in an OCI registry
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/sigstore/cosign

ExclusiveArch: %go_arches

Source: %name-%version.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: libpcsclite-devel

BuildRequires: /proc

%description
Cosign aims to make signatures invisible infrastructure.

Cosign supports:

* "Keyless signing" with the Sigstore public good Fulcio certificate authority and Rekor transparency log (default)
* Hardware and KMS signing
* Signing with a cosign generated encrypted private/public keypair
* Container Signing, Verification and Storage in an OCI registry.
* Bring-your-own PKI

%prep
%setup
%patch -p1

%build
RU_PKG=sigs.k8s.io/release-utils/version

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
SOURCE_DATE_EPOCH=$(date +%s)
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

export LDFLAGS="-X ${RU_PKG}.gitVersion=%{version} -X ${RU_PKG}.gitCommit=%{revision} -X ${RU_PKG}.gitTreeState=release -X ${RU_PKG}.buildDate=${BUILD_DATE}"
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-tags=pivkey,pkcs11key"

%golang_prepare

%golang_build cmd/%name

%install
export BUILDDIR="$PWD/.gopath"
mkdir -p %buildroot%_bindir

%golang_install

rm -rf -- "%buildroot%go_root"

%check
%make test

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Tue Jul 23 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.3.0-alt1
- 2.2.4 -> 2.3.0

* Fri Apr 12 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.2.4-alt1
- Initial build for ALT 

