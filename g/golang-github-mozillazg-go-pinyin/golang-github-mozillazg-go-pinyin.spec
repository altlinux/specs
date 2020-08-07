%def_without check

%global goipath github.com/mozillazg/go-pinyin

Name: golang-github-mozillazg-go-pinyin
Version: 0.18.0
Release: alt1
Summary: Chinese pinyin conversion tool Go version.
Group: Development/Other
License: MIT
Url: https://github.com/mozillazg/go-pinyin
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: go-pinyin-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
%summary.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
%summary.

%prep
%setup -n go-pinyin-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in cmd/pinyin _tools; do
%golang_build $cmd ||:
done

# touch _tools/pinyin-data/pinyin.txt
# go run _tools/gen_pinyin_dict.go _tools/pinyin-data/pinyin.txt pinyin_dict.go
# gofmt -s -w . cmd/pinyin _tools

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
%gotest -v -cover
%endif

%files
%doc LICENSE README.md CHANGELOG.md
%_bindir/*

%files devel
%go_path/src/%goipath

%changelog
* Fri Aug 07 2020 Leontiy Volodin <lvol@altlinux.org> 0.18.0-alt1
- New version.

* Thu Jun 04 2020 Leontiy Volodin <lvol@altlinux.org> 0.17.0-alt1
- Initial build for ALT Sisyphus.
