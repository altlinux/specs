%global _unpackaged_files_terminate_build 1
%global import_path code.gitea.io/tea

Name: gitea-tea
Version: 0.8.0
Release: alt1
Summary: command line tool to interact with Gitea

License: MIT
Group: Development/Other
Url: https://gitea.com/gitea/tea
Vcs: https://gitea.com/gitea/tea.git
Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%description
tea is a productivity helper for Gitea.
It can be used to manage most entities on one or multiple Gitea instances
and provides local helpers like 'tea pull checkout'.
tea makes use of context provided by the repository in $PWD if available,
but is still usable independently of $PWD.
Configuration is persisted in $XDG_CONFIG_HOME/tea.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
cd ${BUILDDIR}/src/%import_path

export VERSION=%version
export COMMIT=%release
export BRANCH=altlinux
export LDFLAGS="-X main.Version=$VERSION"
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Mon Nov 15 2021 Alexey Shabalin <shaba@altlinux.org> 0.8.0-alt1
- Initial build for ALT

