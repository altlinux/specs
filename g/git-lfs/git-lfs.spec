%define _unpackaged_files_terminate_build 1
%define import_path github.com/git-lfs/git-lfs/v3

Name: git-lfs
Version: 3.5.1
Release: alt1

Summary: Git extension for versioning large files
License: MIT
Group: Development/Tools
Url: https://git-lfs.com/
Vcs: https://github.com/git-lfs/git-lfs

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: asciidoctor

%description
Git LFS is a command line extension and specification for managing large files
with Git.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd $BUILDDIR/src/$IMPORT_PATH
export LDFLAGS="-X '%import_path/config.Vendor=%vendor'"
%golang_build  .
popd

for page in $(find docs/man -name '*.adoc'); do
  manpage=$(echo $page | sed 's/.adoc/.1/')
  asciidoctor -a reproducible -b manpage -o $manpage $page
done

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

for page in $(find docs/man -name '*.1'); do
  install -pD -m0644 $page %buildroot/%_man1dir/$(basename $page)
done

%files
%doc CHANGELOG.md README.md LICENSE.md
%_bindir/%name
%_man1dir/*.1.*

%changelog
* Wed Apr 24 2024 Artem Krasovskiy <aibure@altlinux.org> 3.5.1-alt1
- Update version

* Tue Jan 23 2024 Artem Krasovskiy <aibure@altlinux.org> 3.4.1-alt2
- Packaged man pages

* Mon Jan 22 2024 Artem Krasovskiy <aibure@altlinux.org> 3.4.1-alt1
- Initial build

