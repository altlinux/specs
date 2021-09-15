%def_without check

%global goipath         github.com/jinzhu/inflection
%global commit          b5281034e75ed100658f8d9d0b2837f3fad4e8b3

Name: golang-github-jinzhu-inflection
Version: 1.0.0
Release: alt3.gitb528103
Summary: Pluralizes and singularizes English nouns
Group: Development/Other
License: MIT
Url: https://github.com/jinzhu/inflection
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: inflection-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Inflection pluralizes and singularizes English nouns.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Inflection pluralizes and singularizes English nouns.

%prep
%setup -n inflection-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

go mod tidy -go=1.17
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
* Wed Sep 15 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt3.gitb528103
- Fixed build with golang 1.17.

* Mon Feb 01 2021 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt2.gitb528103
- Built from git.

* Fri Aug 07 2020 Leontiy Volodin <lvol@altlinux.org> 1.0.0-alt1.git970f05d
- Built from git.

* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git0414036
- Initial build for ALT Sisyphus (thanks fedora for this spec).
