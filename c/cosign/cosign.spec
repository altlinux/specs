%global import_path github.com/sigstore/cosign/v3
%global _unpackaged_files_terminate_build 1

%define revision 7914231b348c4057891edeb321772aad3ed04fce

%def_with check

Name:    cosign
Version: 3.1.1
Release: alt1

Summary: Container Signing, Verification and Storage in an OCI registry
License: Apache-2.0
Group:   Development/Tools
Url:     https://github.com/sigstore/cosign

ExclusiveArch: %go_arches

Source: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.26.0
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
%setup -a 1
%patch -p1

%build
RU_PKG=sigs.k8s.io/release-utils/version

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
SOURCE_DATE_EPOCH=$(date +%%s)
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

export LDFLAGS="-X ${RU_PKG}.gitVersion=%{version} -X ${RU_PKG}.gitCommit=%{revision} -X ${RU_PKG}.gitTreeState=release -X ${RU_PKG}.buildDate=${BUILD_DATE}"
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export TAGS="pivkey,pkcs11key"

%golang_prepare
%golang_build cmd/%name

%install
export IGNORE_SOURCES=1
export BUILDDIR="$PWD/.gopath"

%golang_install

%check
%make test

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Wed Jun 10 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.1.1-alt1
- New version 3.1.1.

* Wed Apr 08 2026 Alexander Danilov <admsasha@altlinux.org> 3.0.6-alt1
- New version 3.0.6 (Fixes: CVE-2026-39395).

* Wed Feb 25 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.0.5-alt1
- New version 3.0.5 (Fixes: CVE-2026-24122).

* Fri Jan 30 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 3.0.4-alt1
- New version 3.0.4 (Fixes: CVE-2026-22703).
- Enable tests with no Internet access only.

* Mon Aug 11 2025 Alexey Shabalin <shaba@altlinux.org> 2.5.3-alt1
- New version 2.5.3.
- Disable tests, because need Internet access.

* Tue Aug 20 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.4.0-alt1
- 2.3.0 -> 2.4.0

* Tue Jul 23 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.3.0-alt1
- 2.2.4 -> 2.3.0

* Fri Apr 12 2024 Ivan Pepelyaev <fl0pp5@altlinux.org> 2.2.4-alt1
- Initial build for ALT 

