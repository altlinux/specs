%global import_path     github.com/juju/errors

%global commit c7d06af17c68cd34c835053720b21f6549d9b0ee
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-juju-errors
Version: 0
Release: alt1.git%abbrev
Summary: The juju/errors provides an easy way to annotate errors without losing the orginal error context.
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
The juju/errors provides an easy way to annotate errors without losing the orginal error context.

%package devel
Summary: The juju/errors provides an easy way to annotate errors without losing the orginal error context.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
The juju/errors provides an easy way to annotate errors without losing the orginal error context.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.gitc7d06af1
- Initial package

