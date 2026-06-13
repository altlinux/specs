%define _unpackaged_files_terminate_build 1
%global import_path github.com/ansible/receptor

Name:     receptor
Version:  1.6.5
Release:  alt1

Summary:  Overlay network for distributed work
License:  Apache-2.0
Group:    Development/Tools
Url:      https://github.com/ansible/receptor

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
Receptor is an overlay network intended to ease the distribution of
work across a large and dispersed collection of workers. Receptor nodes
establish peer-to-peer connections with each other via existing networks.
Once connected, the Receptor mesh provides datagram (UDP-like) and stream
(TCP-like) capabilities to applications, as well as robust unit-of-work
handling with resiliency against transient network failures.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="\
    -X github.com/ansible/receptor/internal/version.Version=%version \
    $LDFLAGS \
"

%golang_prepare

pushd "$BUILDDIR"/src/%import_path
%golang_build cmd/receptor-cl
popd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mv %buildroot/%_bindir/receptor-cl %buildroot/%_bindir/receptor

mkdir -p %buildroot%_sysconfdir/receptor
cp packaging/container/receptor.conf %buildroot%_sysconfdir/receptor/receptor.conf

%files
%doc README.md LICENSE.md
%_bindir/receptor
%config(noreplace) %_sysconfdir/receptor/receptor.conf
%dir %_sysconfdir/receptor

%changelog
* Fri Jun 12 2026 Nikita Panov <nexxy@altlinux.org> 1.6.5-alt1
- Initial build for Sisyphus.

