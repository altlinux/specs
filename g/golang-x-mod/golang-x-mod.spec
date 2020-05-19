%def_without check

%global goipath         golang.org/x/mod
%global forgeurl        https://github.com/golang/mod

Name: golang-x-mod
Version: 0.3.0
Release: alt1
Summary: Go module mechanics libraries
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/golang/mod
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: mod-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(golang.org/x/crypto/ed25519) golang(golang.org/x/xerrors)
BuildRequires: golang-golang-x-sys-devel golang-golang-x-crypto-devel golang-x-xerrors-devel

%description
This packages holds packages for writing tools that work directly with Go module
mechanics. That is, it is for direct manipulation of Go modules themselves.

%package devel
Summary: Go module mechanics libraries
Group: Development/Other
BuildArch: noarch

%description devel
This packages holds packages for writing tools that work directly with Go module
mechanics. That is, it is for direct manipulation of Go modules themselves.

%prep
%setup -n mod-%version

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

cd .build/src/%goipath
for cmd in gosumcheck; do
%golang_build $cmd ||:
done

%install
export BUILDDIR="$PWD/.build"
export GOPATH="%go_path"
%golang_install

%if_with check
%check
export GOPATH="%go_path"
# sumdb/tlog: needs network
%gotest -d sumdb/tlog
%endif

# %%files
# %%_bindir/*

%files devel
%doc README LICENSE PATENTS
%go_path/src/%goipath

%changelog
* Wed May 20 2020 Leontiy Volodin <lvol@altlinux.org> 0.3.0-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).

