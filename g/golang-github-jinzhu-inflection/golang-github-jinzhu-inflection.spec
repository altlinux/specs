%def_with check

%global goipath         github.com/jinzhu/inflection
%global commit          04140366298a54a039076d798123ffa108fff46c

Name: golang-github-jinzhu-inflection
Version: 0
Release: alt1.git0414036
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
* Tue Jun 02 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git0414036
- Initial build for ALT Sisyphus (thanks fedora for this spec).
