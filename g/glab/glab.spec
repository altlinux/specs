%define _unpackaged_files_terminate_build 1

%global import_path gitlab.com/gitlab-org/cli

%def_with docs

Name: glab
Version: 1.24.1
Release: alt1

Summary: A GitLab CLI tool bringing GitLab to your command line
License: MIT
Group: Development/Other
Url: https://gitlab.com/gitlab-org/cli

Source: %name-%version.tar

ExclusiveArch: %go_arches
BuildRequires(pre): rpm-build-golang

%if_with docs
BuildRequires: python3(sphinx)
BuildRequires: python3(sphinx_rtd_theme)
%endif

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

%package docs
Summary: Documentation for glab (in man-pages and markdown formats)
Group: Documentation
BuildArch: noarch

%description docs
%summary.

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare

pushd .build/src/%import_path
    %golang_build cmd/glab
popd

%if_with docs
go run ./cmd/gen-docs/docs.go --manpage --path .man-pages/
go run ./cmd/gen-docs/docs.go --path .web-pages/
%endif

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot%_man1dir
mv .man-pages/* %buildroot%_man1dir

%files
%doc LICENSE README.md
%_bindir/%name

%files docs
%doc .web-pages/*
%exclude %_docdir/%name-%version/LICENSE
%exclude %_docdir/%name-%version/README.md
%_man1dir/*.1.xz

%changelog
* Fri Jan 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1.24.1-alt1
- 1.24.1
- use upstream's way to build docs
- build documetation separately (glab-docs)
- provide markdown docs

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt2
- build with docs

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt1
- initial build for Sisyphus

