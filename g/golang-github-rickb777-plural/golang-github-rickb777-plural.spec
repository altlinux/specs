%def_without check

%global goipath github.com/rickb777/plural

Name: golang-github-rickb777-plural
Version: 1.4.1
Release: alt1
Summary: Support for localising plurals in a flexible range of different styles
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/rickb777/plural
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/plural-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n plural-%version

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
* Wed Sep 15 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.1-alt1
- New version (1.4.1).
- Fixed build with golang 1.17.

* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 1.3.0-alt1
- New version (1.3.0).

* Fri Oct 16 2020 Leontiy Volodin <lvol@altlinux.org> 1.2.2-alt1
- New version.

* Fri Jun 05 2020 Leontiy Volodin <lvol@altlinux.org> 1.2.1-alt1
- Initial build for ALT Sisyphus.

