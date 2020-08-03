%def_without check

%global goipath github.com/gosexy/gettext

Name: golang-github-gosexy-gettext
Version: 0.9
Release: alt1
Summary: Go bindings for GNU's gettext
Group: Graphical desktop/Other
License: MIT
Url: https://github.com/gosexy/gettext
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/gettext-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(github.com/jessevdk/go-flags) gettext-tools
BuildRequires: gettext-tools golang-github-jessevdk-flags-devel

%if_with check
# Tests
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(gopkg.in/check.v1)
%endif

%description
Go bindings for GNU gettext, an internationalization and localization library
for writing multilingual systems.

%package -n go-xgettext
Summary: Program for extracting translatable strings from Go programs
Group: Development/Other

%description -n go-xgettext
The go-xgettext program is an implementation of xgettext implemented in go.
It can reliably parse go source files to identify content to translate.

%package -n go-xgettext-devel
Summary: Program for extracting translatable strings from Go programs
Group: Development/Other
BuildArch: noarch

%description -n go-xgettext-devel
The go-xgettext program is an implementation of xgettext implemented in go.
It can reliably parse go source files to identify content to translate.

%package -n go-xgettext-examples
Summary: Examples for go-xgettext
Group: Development/Other
BuildArch: noarch

%description -n go-xgettext-examples
This package provides examples for go-xgettext utility.

%prep
%setup -n gettext-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in go-xgettext; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest -d .
%endif

%files -n go-xgettext
%doc LICENSE README.md
%_bindir/*

%files -n go-xgettext-devel
%go_path/src/%goipath
%exclude %go_path/src/%goipath/_examples

%files -n go-xgettext-examples
%go_path/src/%goipath/_examples

%changelog
* Tue May 12 2020 Leontiy Volodin <lvol@altlinux.org> 0.9-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

