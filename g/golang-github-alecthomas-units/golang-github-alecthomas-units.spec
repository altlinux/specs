%def_without check

%global goipath         github.com/alecthomas/units
%global commit          f65c72e2690dc4b403c8bd637baf4611cd4c069b

Name: golang-github-alecthomas-units
Version: 0
Release: alt1.gitf65c72e
Summary: Helpful unit multipliers and functions for go
Group: Development/Other
License: MIT
Url: https://github.com/alecthomas/units
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: units-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%if_with check
# Tests
# BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang-github-stretchr-testify-devel
%endif

%description
Helpful unit multipliers and functions for go.

%package devel
Summary: Helpful unit multipliers and functions for go
Group: Development/Other
BuildArch: noarch

%description devel
Helpful unit multipliers and functions for go.

%prep
%setup -n units-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc COPYING README.md
%go_path/src/%goipath

%changelog
* Tue May 12 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.gitf65c72e
- Initial build for ALT Sisyphus (thanks fedora for this spec).

