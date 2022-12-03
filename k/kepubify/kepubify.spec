# SPEC file for kepubify
#

%global import_path github.com/pgaskin/kepubify

Name:     kepubify
Version:  4.0.4
Release:  alt1

Summary:  EPUBs to KEPUBs converter

Group:    System/Servers
License:  %mit
URL:      https://pgaskin.net/kepubify/
#URL:      https://github.com/pgaskin/kepubify
Packager: Nikolay Fetisov <naf@altlinux.org>

Source0: %name-%version.tar
Source1: vendor.tar
Patch0:  %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires(pre): rpm-build-golang

%description
Kepubify converts EPUBs to KEPUBs (ePub eBook format extension
used by Kobobooks readers).

This package also includes two standalone utilities which
do not depend on kepubify (and don't conflict with Calibre):
- covergen (which pre-generates cover images), and
- seriesmeta (which updates Calibre or EPUB3 series metadata).


%prep
%setup  -n %name-%version
%patch0 -p1

tar xf %SOURCE1

%build
export GO111MODULE=auto
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/kepubify
%golang_build cmd/covergen
%golang_build cmd/seriesmeta


%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install


%files
%doc README.md

%_bindir/*

%changelog
* Sat Dec 03 2022 Nikolay A. Fetisov <naf@altlinux.org> 4.0.4-alt1
- New version

* Thu Feb 10 2022 Nikolay A. Fetisov <naf@altlinux.org> 4.0.3-alt1
- New version

* Fri Oct 15 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.0.1-alt1
- New version

* Sun Jul 11 2021 Nikolay A. Fetisov <naf@altlinux.org> 4.0.0-alt1
- New version
  * Conversion is now 3 to 6 times faster than v3
  * Kepubify can now fix layout issues caused by books without
    a standalone cover page
  * HTML content files with non-standard extensions now work correctly

* Mon Jun 28 2021 Nikolay A. Fetisov <naf@altlinux.org> 3.1.6-alt1
- Initial build for ALT Linux Sisyphus

