%def_with check

%global goipath         github.com/alecthomas/template
%global commit          fb15b899a75114aa79cc930e33c46b577cc664b1

Name: golang-github-alecthomas-template
Version: 0
Release: alt1.gitfb15b89
Summary: Fork of go's text/template adding newline elision
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/alecthomas/template
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: template-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Fork of go's text/template adding newline elision.

%package devel
Summary: Fork of go's text/template adding newline elision
Group: Development/Other
BuildArch: noarch

%description devel
Fork of go's text/template adding newline elision.

%prep
%setup -n template-%version

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

%changelog
* Tue May 12 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.gitfb15b89
- Initial build for ALT Sisyphus (thanks fedora for this spec).

