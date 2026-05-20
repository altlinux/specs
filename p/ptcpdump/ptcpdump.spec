%global _unpackaged_files_terminate_build 1
%global import_path github.com/mozillazg/ptcpdump

%define revision 773055f60c8fb637358991b134ed3f99e8791192

Name:    ptcpdump
Version: 0.37.0
Release: alt1

Summary: Process-aware, eBPF-based tcpdump
License: MIT
Group:   Monitoring
Url:     https://github.com/mozillazg/ptcpdump

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.23
# clang required for bpf *.o files generation
BuildRequires: clang >= 14
BuildRequires: libpcap-devel
Requires: libpcap


%description
ptcpdump is a tcpdump-compatible packet analyzer powered by eBPF,
automatically annotating packets with process/container/pod metadata when detectable.

%prep
%setup
# remove upstream's bpf object files (will be generated during the build).
find bpf -type f -name "*.o"

%build
PKG=github.com/mozillazg/ptcpdump/internal

# return to project root
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%ifarch x86_64 %ix86
TARGET=amd64 go generate ./...
%elifarch aarch64
TARGET=arm64 go generate ./...
%elifarch %arm
TARGET=arm go generate ./...
%endif

export CGO_ENABLED=1
export GOFLAGS="-trimpath"
%ifarch %ix86
export LDFLAGS="-X ${PKG}.Version=%{version} -X ${PKG}.GitCommit=%{revision} -s -w"
%else
export LDFLAGS="-X ${PKG}.Version=%{version} -X ${PKG}.GitCommit=%{revision} -buildmode=pie -s -w"
%endif
export TAGS="dynamic"

%golang_prepare

cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md LICENSE
%_bindir/%name

%changelog
* Wed May 06 2026 Ivan Pepelyaev <fl0pp5@altlinux.org> 0.37.0-alt1
- Initial build for ALT.

