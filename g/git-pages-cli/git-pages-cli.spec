%global _unpackaged_files_terminate_build 1
%global import_path codeberg.org/git-pages/git-pages-cli

Name:    git-pages-cli
Version: 1.10.0
Release: alt1

Summary: Command-line tool for publishing a site to a git-pages server
License: 0BSD
Group:   Development/Tools
Url:     https://git-pages.org
Vcs:     https://codeberg.org/git-pages/git-pages.git

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

ExclusiveArch: %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
%summary.


%prep
%setup -a1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X main.versionOverride=%version"

%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc README.md
%_bindir/%name

%changelog
* Thu Jun 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.10.0-alt1
- New version 1.10.0.

* Tue Jun 02 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.9.0-alt1
- New version 1.9.0.

* Tue Apr 28 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.8.2-alt1
- New version 1.8.2.

* Sat Mar 28 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.8.0-alt1
- Initial build.

