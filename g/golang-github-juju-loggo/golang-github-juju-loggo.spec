%global import_path     github.com/juju/loggo

%global commit 7f1609ff1f3fcf3519ed62ccaaa9e609ea287838
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-loggo
Version: 0
Release: alt1.git%abbrev
Summary: This package provides an alternative to the standard library log package.
License: LGPL v.3
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
This package provides an alternative to the standard library log package.

The actual logging functions never return errors.  If you are logging
something, you really don't want to be worried about the logging
having trouble.

%package devel
Summary: This package provides an alternative to the standard library log package.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
This package provides an alternative to the standard library log package.

The actual logging functions never return errors.  If you are logging
something, you really don't want to be worried about the logging
having trouble.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.git7f1609ff
- Initial package
