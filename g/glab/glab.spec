%define _unpackaged_files_terminate_build 1
%define import_path gitlab.com/gitlab-org/cli

%def_with docs

Name: glab
Version: 1.42.0
Release: alt1

Summary: A GitLab CLI tool bringing GitLab to your command line
License: MIT
Group: Development/Other
Url: https://gitlab.com/gitlab-org/cli
Vcs: https://gitlab.com/gitlab-org/cli

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-golang
%if_with docs
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
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
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

pushd .build/src/%import_path
    export LDFLAGS="$LDFLAGS -X main.buildDate=$(date +%%Y-%%m-%%d)"
    export LDFLAGS="$LDFLAGS -X main.version=%version"
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
%_man1dir/*.1.*

%changelog
* Tue Jun 18 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.42.0-alt1
- Updated to 1.42.0.

* Fri Jun 07 2024 Ajrat Makhmutov <rauty@altlinux.org> 1.41.0-alt1
- Updated to 1.41.0.

* Wed May 15 2024 Anton Zhukharev <ancieg@altlinux.org> 1.40.0-alt1
- Updated to 1.40.0.

* Mon Apr 01 2024 Anton Zhukharev <ancieg@altlinux.org> 1.37.0-alt1
- Updated to 1.37.0.

* Wed Dec 20 2023 Anton Zhukharev <ancieg@altlinux.org> 1.36.0-alt1
- Updated to 1.36.0.

* Tue Nov 07 2023 Anton Zhukharev <ancieg@altlinux.org> 1.35.0-alt1
- Updated to 1.35.0.

* Tue Sep 26 2023 Anton Zhukharev <ancieg@altlinux.org> 1.33.0-alt1
- Updated to 1.33.0.

* Tue Aug 22 2023 Anton Zhukharev <ancieg@altlinux.org> 1.32.0-alt1
- Updated to 1.32.0.

* Wed Aug 02 2023 Anton Zhukharev <ancieg@altlinux.org> 1.31.0-alt1
- Updated to 1.31.0.

* Wed May 17 2023 Anton Zhukharev <ancieg@altlinux.org> 1.29.4-alt1
- New version.

* Tue Mar 28 2023 Anton Zhukharev <ancieg@altlinux.org> 1.26.0-alt1
- New version.

* Fri Jan 06 2023 Anton Zhukharev <ancieg@altlinux.org> 1.24.1-alt1
- 1.24.1
- use upstream's way to build docs
- build documetation separately (glab-docs)
- provide markdown docs

* Thu Oct 06 2022 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt2
- build with docs

* Wed Sep 28 2022 Anton Zhukharev <ancieg@altlinux.org> 1.22.0-alt1
- initial build for Sisyphus

