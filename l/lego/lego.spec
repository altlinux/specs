%global import_path github.com/go-acme/lego
%global _unpackaged_files_terminate_build 1

Name: lego
Version: 5.2.2
Release: alt2
Summary: Let's Encrypt/ACME client and library written in Go

Group: Development/Tools
License: MIT

Url: https://go-acme.github.io/lego/
Vcs: https://github.com/go-acme/lego.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches
# Exclude because date and time tests failed.
ExcludeArch: i586

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang >= 1.24.0
BuildPreReq: /proc

%description
Let's Encrypt/ACME client and library written in Go.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-extldflags '-static'"
export CGO_ENABLED=0

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%check
export LDFLAGS="-extldflags '-static'"
export IMPORT_PATH="%import_path"
# Disable trace commands.
setx=
[[ $- = *x* ]] && setx=1
[ -n "$setx" ] && set +x
# Test skip patterns for all packages.
# Patterns must be separated by space.
commonskip="^TestDNSProvider"
# Test skip patterns for specific packages.
# Patterns must be separated by space.
declare -A EXCLUDE_TESTS=(
  # Skip due to network usage.
  ["${IMPORT_PATH}/v5/acme/api/internal/nonces"]="TestNewNonceSource_notHoldingLockWhileMakingHTTPRequests TestManager_getNonce_notHoldingLockWhileMakingHTTPRequests"
  ["${IMPORT_PATH}/v5/providers/dns/cloudns/internal"]="^TestClient_GetZone"
  ["${IMPORT_PATH}/v5/providers/dns/constellix/internal"]="TestTokenTransport_RoundTrip"
  ["${IMPORT_PATH}/v5/providers/dns/dynu/internal"]="TestTokenTransport_RoundTrip"
  ["${IMPORT_PATH}/v5/providers/dns/edgedns"]="^Test_findZone"
  ["${IMPORT_PATH}/v5/providers/dns/gcloud"]="^TestPresent"
  ["${IMPORT_PATH}/v5/providers/dns/yandexcloud"]="^TestNewDNSProvider"
)

ALL_PKGS=($(go list ./...))
code=0
for package in ${ALL_PKGS[@]}; do
  patterns=("$commonskip")

  if [[ -v EXCLUDE_TESTS["$package"] ]]; then 
    for p in ${EXCLUDE_TESTS["$package"]}; do
      patterns+=("$p")
    done
  fi

  skip_pattern=$(IFS='|'; echo "${patterns[*]}")
  skip=
  if [ -n "$skip_pattern" ]; then
    skip="-skip ${skip_pattern}"
  fi
  %gotest $skip $package || code=$((code + $?))
done

# Fail if one of tests failed.
[ $code -gt 0 ] && exit 1

# Enable trace commands back.
[ -n "$setx" ] && set -x

%files
%doc docs/content/*
%_bindir/*

%changelog
* Thu Jun 21 2026 Alexey Romanyuta <r9odt@altlinux.org> 5.2.2-alt2
- Add check section to spec file.
- Exclude i586 architecture.

* Tue Jun 09 2026 Alexey Romanyuta <r9odt@altlinux.org> 5.2.2-alt1
- New version 5.2.2.

* Fri Mar 06 2026 Alexey Romanyuta <r9odt@altlinux.org> 4.32.0-alt1
- New version v4.32.0

* Sat Jul 05 2025 Alexey Romanyuta <r9odt@altlinux.org> 4.24.0-alt1
- Initial build v4.24.0
