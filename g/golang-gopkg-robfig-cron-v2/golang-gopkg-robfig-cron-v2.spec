%global import_path     gopkg.in/robfig/cron.v2

%global commit be2e0b0deed5a68ffee390b4583a13aff8321535
%global shortcommit %(c=%{commit}; echo ${c:0:8})

Name: golang-gopkg-robfig-cron-v2
Version: 2.0
Release: alt0.git%shortcommit
Summary: Package cron implements a cron spec parser and job runner.
License: MIT
Group: Development/Other
Url: https://gopkg.in/robfig/cron.v2
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

%description
%summary

%package devel
Summary: Package cron implements a cron spec parser and job runner.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
%summary

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
* Thu Jan 10 2019 Denis Pynkin <dans@altlinux.org> 2.0-alt0.gitbe2e0b0d
- Initial package
