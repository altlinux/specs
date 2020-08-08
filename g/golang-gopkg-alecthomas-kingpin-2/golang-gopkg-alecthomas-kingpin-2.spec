%def_without check

%global goipath         gopkg.in/alecthomas/kingpin.v2
%global forgeurl        https://github.com/alecthomas/kingpin

Name: golang-gopkg-alecthomas-kingpin-2
Version: 2.2.6
Release: alt2
Summary: Go command line and flag parser
Group: Development/Other
License: MIT
Url: https://github.com/alecthomas/kingpin
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: kingpin-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/alecthomas/template) golang(github.com/alecthomas/units)
BuildRequires: golang-github-alecthomas-units-devel golang-github-alecthomas-template-devel

%if_with check
# Tests
# BuildRequires: golang(github.com/stretchr/testify/assert) golang(github.com/davecgh/go-spew/spew) golang(github.com/pmezard/go-difflib/difflib) golang(gopkg.in/yaml.v3)
# Notes: build golang(gopkg.in/yaml.v3)
BuildRequires: golang-gopkg-yaml-2-devel golang-github-stretchr-testify-devel golang-github-pmezard-difflib-devel golang-github-davecgh-spew-devel 
%endif

%description
Kingpin is a fluent-style, type-safe command-line parser. It supports flags,
nested commands, and positional arguments.

%package devel
Summary: Go command line and flag parser
Group: Development/Other
BuildArch: noarch

%description devel
Kingpin is a fluent-style, type-safe command-line parser. It supports flags,
nested commands, and positional arguments.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name.

%prep
%setup -n kingpin-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in cmd/* ; do
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

%files
%_bindir/*
%doc COPYING README.md

%files devel
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_examples

%files examples
%go_path/src/%goipath/_examples

%changelog
* Sat Aug 08 2020 Leontiy Volodin <lvol@altlinux.org> 2.2.6-alt2
- Disabled tests.

* Tue May 12 2020 Leontiy Volodin <lvol@altlinux.org> 2.2.6-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

