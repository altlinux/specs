%global import_path github.com/subtrace/subtrace

%define upstream_commit_hash 69ed580

%define upstream_commit_time 2025-03-15T01:14:35Z

%define timestamp %(TZ=UTC LC_TIME=C date +%%Y-%%m-%%dT%%H:%%M:%%SZ)

Name:    subtrace
Version: b271
Release: alt1

Summary: Wireshark for Docker containers
License: BSD-3-Clause
Group:   Other
Url:     https://github.com/subtrace/subtrace

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang golang

ExcludeArch: i586

%description
Subtrace is Wireshark for your Docker containers. 
It lets developers see all incoming and outgoing 
requests in their backend server so that they can 
resolve production issues faster.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

export LDFLAGS="-X subtrace.dev/cmd/version.Release=%version \
                -X subtrace.dev/cmd/version.CommitHash=%upstream_commit_hash \
                -X subtrace.dev/cmd/version.CommitTime=%upstream_commit_time \
                -X subtrace.dev/cmd/version.BuildTime=%timestamp"

%golang_prepare

cd .build/src/%import_path
%gobuild -o subtrace --ldflags "$LDFLAGS"

%install
export BUILDDIR="$PWD/.build"
mkdir -p %buildroot%_bindir
install -Dm 0755 $BUILDDIR/src/%import_path/%name %buildroot%_bindir/%name

%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Wed Mar 19 2025 Aleksandr Gamzin <gamzin@altlinux.org> b271-alt1
- Initial build for Sisyphus
