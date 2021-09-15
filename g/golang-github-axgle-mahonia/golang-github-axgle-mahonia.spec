%def_without check

%global goipath         github.com/axgle/mahonia
%global commit          3358181d7394e26beccfae0ffde05193ef3be33a

Name: golang-github-axgle-mahonia
Version: 0
Release: alt3.git3358181
Summary: Character-set conversion library implemented in Go
Group: Development/Other
License: BSD-3-Clause
Url: https://github.com/axgle/mahonia
Packager: Leontiy Volodin <lvol@altlinux.org>

Source: mahonia-%version.tar.gz

BuildRequires(pre): rpm-build-golang

%description
Mahonia is a character-set conversion library implemented in Go. All data is
compiled into the executable; it doesn't need any external data files.

%package devel
Summary: %summary
Group: Development/Other
BuildArch: noarch

%description devel
Mahonia is a character-set conversion library implemented in Go. All data is
compiled into the executable; it doesn't need any external data files.

%prep
%setup -n mahonia-%version
#sed -i "s|github.com/axgle/mahonia|..|" mahoniconv/mahoniconv.go

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%goipath"
export GOPATH="%go_path"

%golang_prepare

go mod init github.com/axgle/mahonia
for cmd in mahoniconv; do
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
%doc LICENSE README.md
%_bindir/*

%files devel
%go_path/src/%goipath

%changelog
* Tue Sep 14 2021 Leontiy Volodin <lvol@altlinux.org> 0-alt3.git3358181
- Fixed build with golang 1.17.

* Wed Feb 24 2021 Leontiy Volodin <lvol@altlinux.org> 0-alt2.git3358181
- Fixed build.

* Fri May 29 2020 Leontiy Volodin <lvol@altlinux.org> 0-alt1.git3358181
- Initial build for ALT Sisyphus (thanks fedora for this spec).
