%define _unpackaged_files_terminate_build 1

%global import_path gitlab.com/gitlab-org/cli

Name: glab
Version: 1.22.0
Release: alt2

Summary: A GitLab CLI tool bringing GitLab to your command line
License: MIT
Group: Development/Other
Url: https://gitlab.com/gitlab-org/cli

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)

%description
GLab is an open source GitLab CLI tool bringing GitLab to your terminal
next to where you are already working with git and your code without
switching between windows and browser tabs. Work with issues, merge
requests, watch running pipelines directly from your CLI among other
features.

glab is available for repositories hosted on GitLab.com and self-managed
GitLab instances. glab supports multiple authenticated GitLab instances
and automatically detects the authenticated hostname from the remotes
available in the working Git directory.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

cd .build/src/%import_path
%golang_build cmd/glab

%make SPHINXBUILD=sphinx-build-3 -C docs man

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot%_man1dir/
cd $BUILDDIR/src/%import_path/docs/build/man
install -p -m0644 glab.1 %buildroot%_man1dir/glab.1

%files
%doc LICENSE README.md
%_bindir/%name
%_man1dir/%name.1.*

%changelog
* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt2
- build with docs

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt1
- initial build for Sisyphus

