%global import_path gopkg.in/yaml.v2

%global commit 51d6538a90f86fe93ac480b35f37b2be17fef232
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-gopkg-yaml-v2
Version: 2.2.2
Release: alt1.git%abbrev
Summary: YAML support for the Go language
License: Apache v.2
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch

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
* Fri Jan 11 2019 Denis Pynkin <dans@altlinux.org> 2.2.2-alt1.git51d6538a
- Update

* Fri Feb 02 2018 Denis Pynkin <dans@altlinux.org> 2.0-alt6.gitd670f940
- Update

* Sat Jul 29 2017 Denis Pynkin <dans@altlinux.org> 2.0-alt5.git25c4ec80
- Update

* Mon Mar 13 2017 Denis Pynkin <dans@altlinux.org> 2.0-alt4.gita3f3340b
- Update

* Fri Nov 25 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt3.gita5b47d31
- Update
- License has been changed to Apache 2.0

* Thu Mar 10 2016 Denis Pynkin <dans@altlinux.org> 2.0-alt2.gita83829b6
- Update

* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 2.0-alt1.gitf7716cbe
- Initial package

