%def_without check

%global goipath github.com/teambition/rrule-go

Name: golang-github-teambition-rrule-go
Version: 1.5.0
Release: alt1
Summary: Go library for working with recurrence rules for calendar dates
Group: Graphical desktop/Other
License: MIT
Url: https://github.com/teambition/rrule-go
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/rrule-go-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
The rrule module offers a complete implementation of the recurrence rules documented in the iCalendar RFC. It is a partial port of the rrule module from the excellent python-dateutil library.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
The rrule module offers a complete implementation of the recurrence rules documented in the iCalendar RFC. It is a partial port of the rrule module from the excellent python-dateutil library.

%package examples
Summary: Examples for %name
Group: Development/Other
BuildArch: noarch

%description examples
This package provides examples for %name.

%prep
%setup -n rrule-go-%version

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
%exclude %go_path/src/%goipath/example

%files examples
%go_path/src/%goipath/example

%changelog
* Tue Jun 09 2020 Leontiy Volodin <lvol@altlinux.org> 1.5.0-alt1
- Initial build for ALT Sisyphus.

