%def_without check

%global goipath         honnef.co/go/tools
%global forgeurl        https://github.com/dominikh/go-tools
%global tag             2020.1.4

Name: golang-honnef-tools
Version: 2020.1.4
Release: alt1
Summary: Collection of static analysis tools for working with Go code

License: BSD-3-Clause and MIT and Apache-2.0
Group: Development/Other
Url: https://github.com/dominikh/go-tools
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: go-tools-%version.tar.gz

BuildRequires(pre): rpm-build-golang
BuildRequires: golang golang-tools-devel
# BuildRequires: golang(github.com/BurntSushi/toml) golang(github.com/google/renameio) golang(github.com/kisielk/gotool) golang(github.com/rogpeppe/go-internal/modfile) golang(golang.org/x/mod/module)
BuildRequires: golang-x-mod-devel golang-github-rogpeppe-internal-devel golang-github-kisielk-gotool-devel golang-github-google-renameio-devel golang-github-burntsushi-toml-devel
#BuildRequires: golang(golang.org/x/tools/go/analysis)
#BuildRequires: golang(golang.org/x/tools/go/analysis/analysistest)
#BuildRequires: golang(golang.org/x/tools/go/analysis/passes/inspect)
#BuildRequires: golang(golang.org/x/tools/go/ast/astutil)
#BuildRequires: golang(golang.org/x/tools/go/ast/inspector)
#BuildRequires: golang(golang.org/x/tools/go/buildutil)
#BuildRequires: golang(golang.org/x/tools/go/gcexportdata)
#BuildRequires: golang(golang.org/x/tools/go/loader)
#BuildRequires: golang(golang.org/x/tools/go/packages)
#BuildRequires: golang(golang.org/x/tools/go/types/objectpath)
#BuildRequires: golang(golang.org/x/tools/go/types/typeutil)
#BuildRequires: golang(golang.org/x/tools/refactor/importgraph)

%description
honnef.co/go/tools/... is a collection of tools and libraries for working with
Go code, including linters and static analysis, most prominently staticcheck.

%package devel
Summary: Collection of static analysis tools for working with Go code
Group: Development/Other
BuildArch: noarch

%description devel
honnef.co/go/tools/... is a collection of tools and libraries for working with
Go code, including linters and static analysis, most prominently staticcheck.

%prep
%setup -n go-tools-%version
mv gcsizes/LICENSE LICENSE-gcsizes
mv lint/LICENSE LICENSE-lint

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

mkdir -p -- %buildroot/%go_root/bin
for f in %buildroot/%_bindir/*; do
        [ -x "$f" ] || continue
        f="${f##*/}"
        what="$(relative %_bindir/$f %go_root/bin/$f)"
        ln -s -- "$what" %buildroot/%go_root/bin/$f
done

%if_with check
%check
# https://github.com/dominikh/go-tools/issues/687
%gotest -d unused
%endif

%files
%doc LICENSE LICENSE-gcsizes LICENSE-lint LICENSE-THIRD-PARTY README.md
%_bindir/*
%go_root/bin/*

%files devel
%go_path/src/%goipath

%changelog
* Tue May 19 2020 Leontiy Volodin <lvol@altlinux.org> 2020.1.4-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
