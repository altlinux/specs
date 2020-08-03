%def_without check

%global goipath github.com/rogpeppe/go-internal

Name: golang-github-rogpeppe-internal
Version: 1.6.0
Release: alt1
Summary: Selected Go-internal packages factored out from the standard library

License: BSD-3-Clause
Group: Development/Other
Url: https://github.com/rogpeppe/go-internal
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: go-internal-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(gopkg.in/errgo.v2/fmt/errors)
BuildRequires: golang-gopkg-errgo-2-devel

%description
Selected Go-internal packages factored out from the standard library.

%package devel
Summary: Selected Go-internal packages factored out from the standard library
Group: Development/Other
BuildArch: noarch

%description devel
Selected Go-internal packages factored out from the standard library.

%prep
%setup -n go-internal-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

for cmd in cmd/* ; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
# https://github.com/rogpeppe/go-internal/issues/76
%gotest -d imports -d cmd/testscript -d testscript
%endif

%files
%doc LICENSE README.md
%_bindir/*

%files devel
%go_path/src/%goipath

%changelog
* Tue May 19 2020 Leontiy Volodin <lvol@altlinux.org> 1.6.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

