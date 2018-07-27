%define import_path     github.com/mattn/go-shellwords
%define gopath          %_datadir/gocode
%define commit          f8471b0a71ded0ab910825ee2cf230f25de000f1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name: golang-github-mattn-go-shellwords
Version: 1
Release: alt2.git%shortcommit
Summary: Parse line as shell words
License: MIT
Group: Development/Other
Url: http://%import_path

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires(pre): rpm-build-golang

%description
%summary

%package devel
Requires: golang
Summary: Parse line as shell words (devel files)
Group: Development/Other
Provides: golang(%import_path) = %version-%release

%description devel
%summary

This package contains library source intended for building other
packages which use mattn/go-shellwords

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
%doc LICENSE README.md
%gopath/src/%import_path/*

%changelog
* Fri Jul 27 2018 Vladimir Didenko <cow at altlinux.org> 1-alt2.gitf8471b0
- Spec cleanup

* Fri Jul 27 2018 Vladimir Didenko <cow at altlinux.org> 1-alt2.gitf8471b0
- Initial build.
