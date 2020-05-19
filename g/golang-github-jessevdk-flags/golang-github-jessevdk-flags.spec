%def_without check

%global goipath         github.com/jessevdk/go-flags
%global commit          c0795c8afcf41dd1d786bebce68636c199b3bb45

Name: golang-github-jessevdk-flags
Version: 1.4.0
Release: alt1.gitc0795c8
Summary: Go command line option parser
License: BSD-3-Clause
Group: Graphical desktop/Other
Url: https://github.com/jessevdk/go-flags
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-flags-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Package Flags provides an extensive command line option parser. The flags
package is similar in functionality to the go builtin flag package but provides
more options and uses reflection to provide a convenient and succinct way of
specifying command line options.

%package devel
Summary: Go command line option parser
Group: Development/Other
BuildArch: noarch

%description devel
Package Flags provides an extensive command line option parser. The flags
package is similar in functionality to the go builtin flag package but provides
more options and uses reflection to provide a convenient and succinct way of
specifying command line options.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name package.

%prep
%setup -n go-flags-%version

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
%gotest
%endif

%files devel
%doc LICENSE README.md
%go_path/src/%goipath
%exclude %go_path/src/%goipath/examples

%files examples
%go_path/src/%goipath/examples

%changelog
* Wed May 13 2020 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt1.gitc0795c8
- Initial build for ALT Sisyphus (thanks fedora for this spec).

