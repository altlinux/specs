%define _unpackaged_files_terminate_build 1
%define import_path github.com/google/gopacket


Name: golang-gopacket
Version: 1.1.14
Release: alt1%ubt
Summary: Provides packet processing capabilities for Go
License: BSD
Group: Development/Other
Url: https://github.com/google/gopacket

# https://github.com/google/gopacket.git
Source: %name-%version.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-golang
BuildRequires: golang
BuildRequires: golang-tools-devel

%description
Package gopacket provides packet decoding for the Go language.

gopacket contains many sub-packages with additional functionality you may find useful, including:

* layers: You'll probably use this every time.  This contains of the logic
    built into gopacket for decoding packet protocols.  Note that all example
    code below assumes that you have imported both gopacket and
    gopacket/layers.
* pcap: C bindings to use libpcap to read packets off the wire.
* pfring: C bindings to use PF_RING to read packets off the wire.
* afpacket: C bindings for Linux's AF_PACKET to read packets off the wire.
* tcpassembly: TCP stream reassembly

%package devel
Summary: Provides packet processing capabilities for Go
Group: Development/Other
BuildArch: noarch
Requires: golang

%description devel
Package gopacket provides packet decoding for the Go language.

gopacket contains many sub-packages with additional functionality you may find useful, including:

* layers: You'll probably use this every time.  This contains of the logic
    built into gopacket for decoding packet protocols.  Note that all example
    code below assumes that you have imported both gopacket and
    gopacket/layers.
* pcap: C bindings to use libpcap to read packets off the wire.
* pfring: C bindings to use PF_RING to read packets off the wire.
* afpacket: C bindings for Linux's AF_PACKET to read packets off the wire.
* tcpassembly: TCP stream reassembly

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

rm -rf .build/src/%import_path/examples
find .build/src/%import_path -type f ! -name '*.go' -delete

pushd .build/src/%import_path
%golang_build .
popd

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

%files devel
%doc LICENSE AUTHORS README.md
%doc examples
%go_path/src/*

%changelog
* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.14-alt1%ubt
- Initial build for ALT.
