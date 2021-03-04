%def_without check

%global goipath         github.com/jessevdk/go-flags
%global commit          c17162fe8fd74f119ff938c5c67af63e3bac5ded

Name: golang-github-jessevdk-flags
Version: 1.4.0
Release: alt3.gitc17162f
Summary: Go command line option parser
License: BSD-3-Clause
Group: Graphical desktop/Other
Url: https://github.com/jessevdk/go-flags
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/go-flags-%version.tar.gz

BuildRequires(pre): rpm-build-golang
%if_with check
BuildRequires: golang-golang-x-sys-devel
%endif

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
export GO111MODULE="auto"

%golang_prepare

#go mod init github.com/jessevdk/go-flags
cd .build/src/%goipath
%golang_build

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
export GO111MODULE="auto"
%gotest
%endif

%files devel
%doc LICENSE README.md
%go_path/src/%goipath
%exclude %go_path/src/%goipath/examples

%files examples
%go_path/src/%goipath/examples

%changelog
* Thu Mar 04 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt3.gitc17162f
- Disabled tests (unexpected man page).

* Wed Mar 03 2021 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt2.gitc17162f
- Updated from git.
- Enabled tests.

* Wed May 13 2020 Leontiy Volodin <lvol@altlinux.org> 1.4.0-alt1.gitc0795c8
- Initial build for ALT Sisyphus (thanks fedora for this spec).

