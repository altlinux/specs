%global import_path golang.org/x/net

%global commit f73e4c9ed3b7ebdd5f699a16a880c2b1994e50dd
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-golang-x-net
Version: 0
Release: alt6.git%abbrev
Summary: Go supplementary network libraries
License: MIT
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Go supplementary network libraries

%package devel
Summary: golang-golang-x-net
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Go supplementary network libraries

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
%doc AUTHORS README.md LICENSE PATENTS
%go_path/src/*

%changelog
* Wed May 09 2018 Denis Pynkin <dans@altlinux.org> 0-alt6.gitf73e4c9e
- Update

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 0-alt5.gitb417086c
- Update

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 0-alt4.gitf5079bd7
- Update

* Fri Jun 30 2017 Denis Pynkin <dans@altlinux.org> 0-alt3.git1f922427
- Update

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 0-alt2.gita6577fac
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 0-alt1.git4971afdc
- Initial package

