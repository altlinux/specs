%define _unpackaged_files_terminate_build 1
%define import_path oss.terrastruct.com/d2

Name: d2
Version: 0.7.1
Release: alt2

Summary: A modern diagram scripting language that turns text to diagrams
License: MPL-2.0
Group: Publishing
Url: https://d2lang.com/
Vcs: https://github.com/terrastruct/d2

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang

%description
%summary.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export LDFLAGS="$LDFLAGS -X %import_path/lib/version.Version=%version"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

%files
%_bindir/d2

%changelog
* Wed Jul 29 2026 Anton Zhukharev <ancieg@altlinux.org> 0.7.1-alt2
- Corrected license tag.

* Wed Jul 29 2026 Anton Zhukharev <ancieg@altlinux.org> 0.7.1-alt1
- Packaged for ALT Sisyphus.
