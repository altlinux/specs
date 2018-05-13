%global import_path     github.com/spf13/pflag

#global commit ef82de70bb3f60c65fb8eebacbb2d122ef517385
#global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-spf13-pflag
Version: 1.0.1
Release: alt1
Summary: pflag is a drop-in replacement for Go's flag package
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

pflag is compatible with the [GNU extensions to the POSIX recommendations
for command-line options][1]. For a more precise description, see the
"Command-line flag syntax" section below.

%package devel
Summary: pflag is a drop-in replacement for Go's flag package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

pflag is compatible with the [GNU extensions to the POSIX recommendations
for command-line options][1]. For a more precise description, see the
"Command-line flag syntax" section below.

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

%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 1.0.1-alt1
- Initial package

* Sat Dec 09 2017 Igor Vlasenko <viy@altlinux.ru>  0-alt1_0.19.gitc7e63cf
- new version
