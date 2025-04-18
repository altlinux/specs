%global import_path github.com/varnamproject/govarnam

%define sname varnam
%define oname govarnam

Name: libgovarnam
Version: 1.9.1
Release: alt1

Summary: GoVarnam is a cross-platform transliteration library
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://varnamproject.com
Vcs: https://github.com/varnamproject/govarnam

Source: %name-%version.tar

BuildRequires(pre): rpm-build-golang

BuildRequires: golang
BuildRequires: pkg-config
BuildRequires: libsqlite3-devel
BuildRequires: golang-github-mattn-go-sqlite3-devel

%description
Easily type Indic languages on computer and mobile. GoVarnam
is a cross-platform transliteration library. Manglish -> Malayalam,
Thanglish -> Tamil, Hinglish -> Hindi plus another 10 languages.
GoVarnam is a near-Go port of libvarnam.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %EVR

%description devel
Contains the library and header files needed to develop applications using
%name.

%package -n %{sname}cli
Summary: GoVarnam Command Line Utility (CLI)
Group: Development/Other
Requires: %name = %EVR

%description -n %{sname}cli
%summary.

%prep
%setup

%build
export GO111MODULE=off
export GOPROXY=off
export GOCACHE=$PWD/.build
export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.Version=v%version -X main.Version=$(date +%%Y%%m%%dT%%H%%M%%S)"
export GOPRIVATE=%go_path
%golang_prepare
cd .build/src/%import_path
%make_build
# To comply with the shared library packaging convention
mv -v %name.so %name.so.%version

%install
mkdir -p %buildroot%_bindir
install -Dpm 0755 .build/src/%import_path/%{sname}cli %buildroot%_bindir

mkdir -p %buildroot%_libdir
install -Dpm 0644 .build/src/%import_path/%name.so.%version %buildroot%_libdir
ln -sf %name.so.%version %buildroot%_libdir/%name.so

mkdir -p %buildroot%_pkgconfigdir
install -Dpm 0644 .build/src/%import_path/%oname.pc %buildroot%_pkgconfigdir

mkdir -p %buildroot%_includedir/%name
install -Dpm 0644 .build/src/%import_path/%name.h \
	%buildroot/%_includedir/%name
install -Dpm 0644 .build/src/%import_path/c-shared.h \
	%buildroot/%_includedir/%name
install -Dpm 0644 .build/src/%import_path/c-shared-util.h \
	%buildroot/%_includedir/%name
install -Dpm 0644 .build/src/%import_path/c-shared-varray.h \
	%buildroot/%_includedir/%name

%files
%_libdir/%name.so.*

%files devel
%_includedir/%name/c-shared.h
%_includedir/%name/c-shared-util.h
%_includedir/%name/c-shared-varray.h
%_includedir/%name/%name.h
%_pkgconfigdir/%oname.pc
%_libdir/%name.so

%files -n %{sname}cli
%_bindir/%{sname}cli

%changelog
* Tue Apr 08 2025 Ulysses Apokin <ulysses@altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus.
