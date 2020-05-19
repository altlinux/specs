%def_without check

%global goipath github.com/rickb777/date

Name: golang-github-rickb777-date
Version: 1.12.5
Release: alt1
Summary: Functionality for working with dates
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/rickb777/date
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/date-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/mattn/goveralls) golang(github.com/rickb777/plural) golang(github.com/sqs/goreturns) golang(golang.org/x/text) golang(golang.org/x/tools)
BuildRequires: golang-github-mattn-goveralls-devel golang-github-rickb777-plural-devel golang-github-sqs-goreturns-devel golang-x-text-devel golang-tools-devel

%description
Package date provides functionality for working with dates.

This package introduces a light-weight Date type that is storage-efficient and convenient for calendrical calculations and date parsing and formatting.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Package date provides functionality for working with dates.

This package introduces a light-weight Date type that is storage-efficient and convenient for calendrical calculations and date parsing and formatting.

%prep
%setup -n date-%version
# remove chromium-browser from requires
sed -i '37,39d; 41d' coverage.sh

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
%doc LICENSE README.md
%go_path/src/%goipath

%changelog
* Thu Jun 04 2020 Leontiy Volodin <lvol@altlinux.org> 1.12.5-alt1
- Initial build for ALT Sisyphus.
