%define _unpackaged_files_terminate_build 1
%define import_path github.com/anchore/grype

%def_with check

Name: grype
Version: 0.116.0
Release: alt1

Summary: A vulnerability scanner for container images and filesystems
License: Apache-2.0
Group: Development/Tools
Url: https://github.com/anchore/grype
Vcs: https://github.com/anchore/grype
ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar
Source2: .excluded_packages
Source3: list

Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: /proc
%if_with check
BuildRequires: git-core
BuildRequires: openssl
%endif

%description
A vulnerability scanner for container images and filesystems. Finds
vulnerabilities in operating system packages (Alpine, Debian, RHEL and
others) and in language-specific packages (Go, Java, JavaScript,
Python, Ruby and others), and consumes SBOM documents produced by
Syft.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export CGO_ENABLED=0
# consumed by golang-build as `go install -ldflags`
export LDFLAGS="-s -w -X main.version=%version \
		      -X main.gitDescription=v%version \
		      -X main.gitCommit=%(cut -b -8 %SOURCE3) \
                      -X main.buildDate=%(date "+%%Y%%m%%d")"

%golang_prepare

cd .build/src/%import_path
%golang_build ./cmd/grype

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install
ln -sf %_licensedir/Apache-2.0 LICENSE

%check
export GOPATH="$PWD/.build:%go_path"
export GOFLAGS="-mod=vendor"

# the presenter golden files are compared after stripping the `/tmp/...`
# temporary paths they embed, so the tests only match when `t.TempDir()`
# hands out directories directly under /tmp
export TMPDIR=/tmp

# several test suites locate the source tree by shelling out to
# `git rev-parse --show-toplevel`; an empty repository is enough for that
git init -q .

cd .build/src/%import_path

# the exclusion list holds packages that build their fixtures with a
# networked `go build` or drive a container runtime directly
# (docker/podman), neither of which exists in the build environment
go test $(go list ./... | grep -vxFf %SOURCE2)

%files
%doc --no-dereference LICENSE
%doc README.md
%_bindir/%name

%changelog
* Wed Jul 22 2026 Andrey Kuzma <kuzmaav@altlinux.org> 0.116.0-alt1
- Initial build for ALT Sisyphus.
