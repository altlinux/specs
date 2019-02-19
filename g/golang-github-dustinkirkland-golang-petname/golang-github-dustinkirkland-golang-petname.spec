%global import_path     github.com/dustinkirkland/golang-petname

%global commit d3c2ba80e75eeef10c5cf2fc76d2c809637376b3
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-dustinkirkland-golang-petname
Version: 2.8
Release: alt2.git%abbrev
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
* Wed Feb 20 2019 Denis Pynkin <dans@altlinux.org> 2.8-alt2.gitd3c2ba80
- Remove golang-tools from build requires

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 2.8-alt1.gitd3c2ba80
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.5-alt1.git7ff34179
- Update

* Mon Aug 22 2016 Denis Pynkin <dans@altlinux.org> 2.2-alt1.git552e8d4d
- New version

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 1.11-alt1.git2182cece
- Initial package for development only

