%def_without check

%global goipath github.com/jung-kurt/gofpdf

Name: golang-github-jung-kurt-gofpdf
Version: 2.17.2
Release: alt1
Summary: PDF document generator with high level support for text, drawing and images
Group: Development/Other
License: MIT
Url: https://github.com/jung-kurt/gofpdf
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: gofpdf-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Package Gofpdf implements a PDF document generator with high level support for
text, drawing and images.

%package devel
Summary: Development/Other
Group: Development/Other
BuildArch: noarch

%description devel
Package Gofpdf implements a PDF document generator with high level support for
text, drawing and images.

%prep
%setup -n gofpdf-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

for cmd in makefont; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest
%endif

%files
%doc LICENSE
%doc doc README.md checklist.txt document.md text/20k_c1.txt text/20k_c2.txt
%doc text/countries.txt text/utf-8test.txt text/utf-8test2.txt
%_bindir/*

%files devel
%go_path/src/%goipath

%changelog
* Mon May 18 2020 Leontiy Volodin <lvol@altlinux.org> 2.17.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

