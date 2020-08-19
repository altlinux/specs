%def_without check

# https://github.com/golang/xerrors
%global goipath         golang.org/x/xerrors
%global forgeurl        https://github.com/golang/xerrors
%global commit          9bdfabe68543c54f90421aeb9a60ef8061b5b544

Name: golang-x-xerrors
Version: 0
Release: alt2.git9bdfabe
Summary: Transition packages for the new Go 1.13 error values
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/golang/xerrors
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: xerrors-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
This package holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.

%package devel
Summary: Transition packages for the new Go 1.13 error values
Group: Development/Other
BuildArch: noarch

%description devel
This package holds the transition packages for the new Go 1.13 error values.
See golang.org/design/29934-error-values.

%prep
%setup -n xerrors-%version

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
%doc README LICENSE PATENTS
%go_path/src/%goipath

%changelog
* Wed Aug 19 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt2.git9bdfabe
- Disabled tests.

* Thu May 7 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git9bdfabe
- Initial build for ALT Sisyphus (thanks fedora for this spec).
