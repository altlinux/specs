%global import_path github.com/gosexy/gettext

%global commit d0176d33a571755ef6cd36796750ad48c9d21ee8
%global abbrev %(c=%{commit}; echo ${c:0:8})


Name: golang-github-gosexy-gettext
Version: 0
Release: alt1.git%abbrev
Summary: Go bindings for GNU gettext
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
Go bindings for GNU gettext, an internationalization and localization
library for writing multilingual systems.

%package devel
Summary: Go bindings for GNU gettext
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Go bindings for GNU gettext, an internationalization and localization
library for writing multilingual systems.

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

rm -rf -- %buildroot/%go_path/src/%import_path/examples
rm -rf -- %buildroot/%go_path/src/%import_path/xgettext


%files devel
%doc README.md LICENSE
%go_path/src/*

%changelog
* Tue Feb 16 2016 Denis Pynkin <dans@altlinux.ru> 0-alt1.gitd0176d33
- Initial package

