%global import_path     github.com/armon/go-metrics

%global commit f0300d1749da6fa982027e449ec0c7a145510c3c
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-github-armon-go-metrics
Version: 0
Release: alt0.git%shortcommit
Summary: This library provides a `metrics` package
License: MIT
Group: Development/Other
Url: https://github.com/armon/go-metrics
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
This library provides a `metrics` package which can be used to instrument code,
expose application metrics, and profile runtime performance in a flexible manner.

%package devel
Summary: This library provides a `metrics` package
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

# Auto-detected requirements
Requires:	golang(github.com/hashicorp/go-immutable-radix)

%description devel
This library provides a `metrics` package which can be used to instrument code,
expose application metrics, and profile runtime performance in a flexible manner.

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 0-alt0.gitf0300d17
- Initial package
