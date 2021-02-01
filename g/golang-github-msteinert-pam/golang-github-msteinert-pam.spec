%def_with check

%global goipath         github.com/msteinert/pam
%global commit          e61372126161db56aa15734b7575714920c274ac

Name: golang-github-msteinert-pam
Version: 0
Release: alt2.gite613721
Summary: Go wrapper module for the Pluggable Authentication Modules (PAM) API
Group: Development/Other
License: BSD-2-Clause
Url: https://github.com/msteinert/pam
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: pam-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: libpam0-devel
%if_with check
# Tests
BuildRequires: golang(github.com/bgentry/speakeasy)
%endif

%description
Go wrapper module for the Pluggable Authentication Modules (PAM) API.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Go wrapper module for the Pluggable Authentication Modules (PAM) API.

%prep
%setup -n pam-%version
%if_with check
# Tests
sed -i 's|"github.com/msteinert/pam"|"."|' example_test.go
%endif

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path:$BUILDDIR"

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
* Mon Feb 01 2021 Leontiy Volodin <lvol@altlinux.org> 0-alt2.gite613721
- Built from git.

* Mon Jun 01 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.gitf29b9f2
- Initial build for ALT Sisyphus (thanks fedora for this spec).
