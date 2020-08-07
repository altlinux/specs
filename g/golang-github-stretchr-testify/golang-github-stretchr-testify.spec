%def_without check

%global goipath         github.com/stretchr/testify
%global goaltipaths     gopkg.in/stretchr/testify.v1

Name: golang-github-stretchr-testify
Version: 1.6.1
Release: alt1
Summary: Toolkit with common assertions and mocks
Group: Development/Other
License: MIT
Url: https://github.com/stretchr/testify
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/testify-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/davecgh/go-spew/spew) golang(github.com/pmezard/go-difflib/difflib) golang(github.com/stretchr/objx) golang(gopkg.in/yaml.v2)
#BuildRequires: golang(github.com/ernesto-jimenez/gogen)
BuildRequires: golang-gopkg-yaml-2-devel golang-github-stretchr-objx-devel golang-github-pmezard-difflib-devel golang-github-davecgh-spew-devel

%description
Golang set of packages that provide many tools for testifying
that your code will behave as you intend.
Features include:
 - Easy assertions
 - Mocking
 - Testing suite interfaces and functions

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Golang set of packages that provide many tools for testifying
that your code will behave as you intend.
Features include:
 - Easy assertions
 - Mocking
 - Testing suite interfaces and functions

%prep
%setup -n testify-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in _codegen/ ; do
%golang_build $cmd ||:
done

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
%doc README.md LICENSE
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_codegen

%changelog
* Fri Aug 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.6.1-alt1
- New version.

* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 1.5.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

