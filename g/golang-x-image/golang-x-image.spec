%def_without check

# This package does not create any elf file
%global debug_package %nil

%global goipath  golang.org/x/image
%global commit   58c23975cae11f062d4b3b0c143fe248faac195d

Name: golang-x-image
Version: 0
Release: alt1.git58c2397
Summary: Go supplementary image libraries
Group: Development/Other

License: BSD-3-Clause
Url: https://github.com/golang/image
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: %url/archive/%version/image-%version.tar.gz

BuildRequires(pre): rpm-build-golang
# BuildRequires: golang(golang.org/x/text/encoding/charmap)
BuildRequires: golang-x-text-devel

%description
This package holds supplementary Go image libraries.

%package devel
Summary: Go supplementary image libraries
Group: Development/Other
BuildArch: noarch

%description devel
This package holds supplementary Go image libraries.

%prep
%setup -n image-%version

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

%check
%if_with check
export GOPATH="%go_path"
%gotest
%endif

%files devel
%doc example AUTHORS CONTRIBUTING.md CONTRIBUTORS README.md LICENSE PATENTS
%go_path/src/%goipath

%changelog
* Thu Apr 16 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git58c2397
- Initial build for ALT Sisyphus (thanks fedora for this spec).
