%global import_path     github.com/rogpeppe/fastuuid

%global commit 6724a57986aff9bff1a1770e9347036def7c89f6
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-github-rogpeppe-fastuuid
Version: 0
Release: alt1.git%abbrev
Summary: This package provides fast UUID generation of 192 bit universally unique identifiers.
License: BSD
Group: Development/Other
Url: https://godoc.org/%import_path
Source: %name-%version.tar

Packager: Denis Pynkin <dans@altlinux.ru>

ExclusiveArch:  %go_arches
BuildRequires(pre): rpm-build-golang

BuildArch: noarch
BuildRequires: golang-tools

%description
Package fastuuid provides fast UUID generation of 192 bit universally unique
identifiers. It does not provide formatting or parsing of the identifiers (it is
assumed that a simple hexadecimal or base64 representation is sufficient, for
which adequate functionality exists elsewhere).

Note that the generated UUIDs are not unguessable - each UUID generated from a
Generator is adjacent to the previously generated UUID.

It ignores RFC 4122.

%package devel
Summary: This package provides fast UUID generation of 192 bit universally unique identifiers.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
Package fastuuid provides fast UUID generation of 192 bit universally unique
identifiers. It does not provide formatting or parsing of the identifiers (it is
assumed that a simple hexadecimal or base64 representation is sufficient, for
which adequate functionality exists elsewhere).

Note that the generated UUIDs are not unguessable - each UUID generated from a
Generator is adjacent to the previously generated UUID.

It ignores RFC 4122.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.git6724a579
- Initial package
