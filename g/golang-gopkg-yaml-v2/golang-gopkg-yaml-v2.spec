%global import_path gopkg.in/yaml.v2

%global commit a83829b6f1293c91addabc89d0571c246397bbf4
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-gopkg-yaml-v2
Version: 2.0
Release: alt2.git%abbrev
Summary: YAML support for the Go language
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
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within Canonical (https://www.canonical.com) as
part of the juju (https://juju.ubuntu.com) project, and is based on a
pure Go port of the well-known libyaml (http://pyyaml.org/wiki/LibYAML)
C library to parse and generate YAML data quickly and reliably.

%package devel
Summary: YAML support for the Go language
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within [Canonical](https://www.canonical.com) as
part of the [juju](https://juju.ubuntu.com) project, and is based on a
pure Go port of the well-known [libyaml](http://pyyaml.org/wiki/LibYAML)
C library to parse and generate YAML data quickly and reliably.

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
%doc README.md LICENSE LICENSE.libyaml
%go_path/src/*

%changelog
* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt2.gita83829b6
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 2.0-alt1.gitf7716cbe
- Initial package

