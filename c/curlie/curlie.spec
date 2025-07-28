%define _unpackaged_files_terminate_build 1
%define import_path github.com/rs/curlie

Name: curlie
Version: 1.8.1
Release: alt1

Summary: User-friendly curl wrapper with HTTPie-style syntax and features
License: MIT
Group: Development/Other
Url: https://rs.github.io/curlie/
Vcs: https://github.com/rs/curlie

Source0: %name-%version.tar
Source1: vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-build-golang

%description
Curlie provides the interface of HTTPie but miss the features of curl,
curlie is what you are searching for. Curlie is a frontend to curl that
adds the ease of use of httpie, without compromising on features and
performance. All curl options are exposed with syntax sugar and output
formatting inspired from httpie.

%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
cd .build/src/%import_path
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/curlie
%doc LICENSE README.md

%changelog
* Fri May 23 2025 Maxim Tulskiy <tulskijms@altlinux.org> 1.8.1-alt1
- Initial build for ALT Sisyphus.
