%define _unpackaged_files_terminate_build 1
%define import_path github.com/alibaba/open-code-review

%define bash_completionsdir %_datadir/bash-completion/completions
%define fish_completionsdir %_datadir/fish/vendor_completions.d
%define zsh_completionsdir %_datadir/zsh/site-functions

Name: open-code-review
Version: 1.12.9
Release: alt1

Summary: An AI-powered code review CLI tool
License: Apache-2.0
Group: Development/Tools
Url: https://open-codereview.ai/
Vcs: https://github.com/alibaba/open-code-review

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch0: %name-%version-alt.patch

Requires: git
BuildRequires(pre): rpm-build-golang

%description
OpenCodeReview is an AI-powered command-line code review tool. It reads Git
diffs, sends changed files to a configurable LLM through an agent with tool-use
capabilities, and produces structured review comments with line-level precision.

It supports workspace, branch-range and single-commit review modes, as well as
full-file repository scanning.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
%golang_prepare

cd .build/src/%import_path
export VERSION="%version"
export GIT_COMMIT="v%version"
export BUILD_DATE="$(date -u +%%Y-%%m-%%dT%%H:%%M:%%SZ)"
export LDFLAGS="-X main.Version=$VERSION -X main.GitCommit=$GIT_COMMIT -X main.BuildDate=$BUILD_DATE"
%golang_build cmd/opencodereview

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1
%golang_install

# rename to well-known name
mv %buildroot%_bindir/opencodereview %buildroot%_bindir/ocr

# generate completions
mkdir -p %buildroot%bash_completionsdir
mkdir -p %buildroot%fish_completionsdir
mkdir -p %buildroot%zsh_completionsdir
%buildroot%_bindir/ocr completion bash > %buildroot%bash_completionsdir/ocr
%buildroot%_bindir/ocr completion fish > %buildroot%fish_completionsdir/ocr.fish
%buildroot%_bindir/ocr completion zsh > %buildroot%zsh_completionsdir/_ocr

%files
%_bindir/ocr
%bash_completionsdir/ocr
%fish_completionsdir/ocr.fish
%zsh_completionsdir/_ocr

%changelog
* Thu Sep 24 2026 Artem Krasovskiy <aibure@altlinux.org> 1.12.9-alt1
- updated from 1.12.3 to 1.12.9

* Wed Sep 16 2026 Anton Zhukharev <ancieg@altlinux.org> 1.12.3-alt1
- Packaged for ALT Sisyphus.
