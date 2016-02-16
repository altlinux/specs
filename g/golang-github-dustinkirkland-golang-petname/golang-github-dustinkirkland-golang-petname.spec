%global import_path     github.com/dustinkirkland/golang-petname

%global commit 2182cecef7f257230fc998bc351a08a5505f5e6c
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-dustinkirkland-golang-petname
Version: 1.11
Release: alt1.git%abbrev
Summary: This utility will generate "pet names", consisting of a random combination
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

# TODO: create a binary
%description
This utility will generate "pet names", consisting of a random combination 
of an adverb, adjective, and proper name.  These are useful for unique hostnames, for instance.

%package devel
Summary: Package provides generation of "pet names", consisting of a random combination 
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Package provides generation of "pet names", consisting of a random combination

%prep
%setup -q

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"

%golang_prepare

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"

%golang_install

rm -rf -- %buildroot/%go_path/src/%import_path/cmd
rm -rf -- %buildroot/%go_path/src/%import_path/debian

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 1.11-alt1.git2182cece
- Initial package for development only

