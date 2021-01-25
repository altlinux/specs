%def_without check

%global goipath golang.org/x/text

Name: golang-x-text
Version: 0.3.5
Release: alt1
Summary: Go text processing support
Group: Development/Other

License: BSD-3-Clause
Url: https://github.com/golang/text
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/text-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang-tools-devel
# BuildRequires: golang(golang.org/x/tools/go/buildutil) golang(golang.org/x/tools/go/callgraph) golang(golang.org/x/tools/go/callgraph/cha) golang(golang.org/x/tools/go/loader) golang(golang.org/x/tools/go/ssa) golang(golang.org/x/tools/go/ssa/ssautil)

%description
Text is a repository of text-related packages related to internationalization
(i18n) and localization (l10n), such as character encodings, text
transformations, and locale-specific text handling.

%package devel
Summary: Go text processing support
Group: Development/Other
BuildArch: noarch

%description devel
Text is a repository of text-related packages related to internationalization
(i18n) and localization (l10n), such as character encodings, text
transformations, and locale-specific text handling.

%prep
%setup -n text-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in cmd/*; do
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

# %%files
# %%_bindir/*

%files devel
%doc LICENSE PATENTS AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md
%go_path/src/%goipath

%changelog
* Mon Jan 25 2021 Leontiy Volodin <lvol@altlinux.org> 0.3.5-alt1
- New version (0.3.5).

* Mon Dec 28 2020 Leontiy Volodin <lvol@altlinux.org> 0.3.4-alt1
- New version.

* Mon Aug 10 2020 Leontiy Volodin <lvol@altlinux.org> 0.3.3-alt1
- New version.

* Thu Apr 16 2020 Leontiy Volodin <lvol@altlinux.org> 0.3.2-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
