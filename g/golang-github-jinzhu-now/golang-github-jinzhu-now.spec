%def_without check

%global goipath         github.com/jinzhu/now

Name: golang-github-jinzhu-now
Version: 1.1.4
Release: alt1
Summary: Time toolkit for Go
Group: Development/Other
License: MIT
Url: https://github.com/jinzhu/now
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/now-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Now is a time toolkit for Go.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Now is a time toolkit for Go.

%prep
%setup -n now-%version

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
%doc License README.md
%go_path/src/%goipath

%changelog
* Tue Dec 07 2021 Leontiy Volodin <lvol@altlinux.org> 1.1.4-alt1
- New version (1.1.4).

* Thu Nov 25 2021 Leontiy Volodin <lvol@altlinux.org> 1.1.3-alt1
- New version (1.1.3).

* Tue Sep 21 2021 Leontiy Volodin <lvol@altlinux.org> 1.1.2-alt2
- Fixed build with golang 1.17.

* Fri Mar 26 2021 Leontiy Volodin <lvol@altlinux.org> 1.1.2-alt1
- New version (1.1.2).

* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 1.1.1-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
