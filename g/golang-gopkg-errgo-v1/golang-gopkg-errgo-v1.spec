%global import_path     gopkg.in/errgo.v1

%global commit c17903c6b19d5dedb9cfba9fa314c7fae63e554f
%global abbrev %(c=%{commit}; echo ${c:0:8})

Name: golang-gopkg-errgo-v1
Version: 0
Release: alt1.git%abbrev
Summary: The errgo package provides a way to create and diagnose errors.
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
The errgo package provides a way to create and diagnose errors. It is compatible
with the usual Go error idioms but adds a way to wrap errors so that they record
source location information while retaining a consistent way for code to inspect
errors to find out particular problems.

%package devel
Summary: The errgo package provides a way to create and diagnose errors.
Group: Development/Other
Requires: golang
Provides: golang(%import_path) = %version-%release

%description devel
The errgo package provides a way to create and diagnose errors. It is compatible
with the usual Go error idioms but adds a way to wrap errors so that they record
source location information while retaining a consistent way for code to inspect
errors to find out particular problems.

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
* Sun May 13 2018 Denis Pynkin <dans@altlinux.org> 0-alt1.gitc17903c6
- Initial package
