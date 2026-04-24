%global import_path github.com/varnamproject/govarnam

%global descr Easily type Indic languages on computer and mobile. GoVarnam\
is a cross-platform transliteration library. Manglish -> Malayalam,\
Thanglish -> Tamil, Hinglish -> Hindi plus another 10 languages.\
GoVarnam is a near-Go port of libvarnam.

%define sname varnam
%define oname govarnam
%define abiversion 1

Name: libgovarnam
Version: 1.9.1
Release: alt3

Summary: GoVarnam is a cross-platform transliteration library
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://varnamproject.com
Vcs: https://github.com/varnamproject/govarnam

Source0: %name-%version.tar
Source1: vendor.tar
Patch0: 0001-Removed-build-dependency-on-git.patch
Patch1: 0002-Fixed-erroneous-use-of-or.patch
Patch2: 0003-Added-correct-names-of-library-files.patch
Patch3: 0004-Added-correct-file-paths-for-installing-the-library.patch
Patch4: 0005-Used-https-in-URL-instead-of-http.patch
Patch5: 0006-Installation-moved-to-Makefile-from-install.sh.patch

BuildRequires(pre): rpm-build-golang

BuildRequires: golang
BuildRequires: pkg-config
BuildRequires: libsqlite3-devel

%description
%descr

%package -n libgovarnam%abiversion
Summary: %summary
Group: Graphical desktop/Other

%description -n libgovarnam%abiversion
%descr

%package devel
Summary: Development files for libgovarnam
Group: Development/Other
Requires: libgovarnam%abiversion = %EVR

%description devel
Contains the library and header files needed to develop applications using
%name.

%package -n %{sname}cli
Summary: GoVarnam Command Line Utility (CLI)
Group: Development/Other
Requires: libgovarnam%abiversion = %EVR

%description -n %{sname}cli
%summary.

%prep
%setup -a1
%autopatch -p1
sed -i 's/@GITVERSION@/%version/g' Makefile

%build
export BUILDDIR=$PWD/.build
export IMPORT_PATH=%import_path
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export CGO_CFLAGS="-std=gnu17"
%golang_prepare
cd .build/src/%import_path
%make_build PREFIX=%prefix \
	BINDIR=%_bindir \
	INCLUDEDIR=%_includedir \
	LIBDIR=%_libdir \
	PKGCONFIGDIR=%_pkgconfigdir

%install
cd .build/src/%import_path
%makeinstall_std PREFIX=%prefix \
	BINDIR=%_bindir \
	INCLUDEDIR=%_includedir \
	LIBDIR=%_libdir \
	PKGCONFIGDIR=%_pkgconfigdir

%files -n libgovarnam%abiversion
%_libdir/libgovarnam.so.%{abiversion}*

%files devel
%_includedir/libgovarnam
%_pkgconfigdir/%oname.pc
%_libdir/libgovarnam.so

%files -n %{sname}cli
%_bindir/%{sname}cli

%changelog
* Thu Apr 23 2026 Ulysses Apokin <ulysses@altlinux.org> 1.9.1-alt3
- Fixed FTBFS.

* Mon Sep 08 2025 Ulysses Apokin <ulysses@altlinux.org> 1.9.1-alt2
- Fixed wrong prefix and libdir in pc-file (ALT #54897).
- Used vendoring go modules.
- Corrected as per shared libs policy.

* Tue Apr 08 2025 Ulysses Apokin <ulysses@altlinux.org> 1.9.1-alt1
- Initial build for Sisyphus.
