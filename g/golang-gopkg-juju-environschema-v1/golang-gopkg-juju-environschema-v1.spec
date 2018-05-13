%global import_path     gopkg.in/juju/environschema.v1

%global commit 7359fc7857abe2b11b5b3e23811a9c64cb6b01e0
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-gopkg-juju-environschema-v1
Version: 0
Release: alt1.git%abbrev
Summary: This package allows the specification of Juju environment config schema.
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
This package allows the specification of Juju environment config schema.

%package devel
Summary: This package allows the specification of Juju environment config schema.
Group: Development/Other
Requires: golang
Requires: golang(github.com/juju/errors)
Requires: golang(github.com/juju/schema)
Requires: golang(github.com/juju/utils/keyvalues)
BuildRequires: golang(github.com/juju/utils/keyvalues)
BuildRequires: golang(github.com/juju/schema)
BuildRequires: golang(github.com/juju/errors)

Provides: golang(%import_path) = %version-%release

%description devel
This package allows the specification of Juju environment config schema.

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
%doc README.md LICENCE
%go_path/src/*

%changelog
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.git7359fc78
- Initial package

