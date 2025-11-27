%define _unpackaged_files_terminate_build 1
%global import_path github.com/mark3labs/mcphost

Name: mcphost
Version: 0.31.4
Release: alt1
Summary: A CLI host application for the Model Context Protocol (MCP).
License: MIT and Apache-2.0 and BSD-2-Clause and BSD-3-Clause
Group: Networking/Other
Url: https://github.com/mark3labs/mcphost


Source0: %name-%version.tar
Source1: vendor.tar
Patch: %name-%version-%release.patch
ExcludeArch: i586

BuildRequires(pre): rpm-build-golang
BuildRequires: golang

%description
A CLI host application that enables Large Language Models (LLMs) to interact
with external tools through the Model Context Protocol (MCP). Currently
supports both Claude 3.5 Sonnet and Ollama models.

%prep
%setup -a 1
%autopatch -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export IGNORE_SOURCES=1
%golang_install

%files
%doc *.md
%_bindir/%name

%changelog
* Thu Nov 27 2025 Pavel Shilov <zerospirit@altlinux.org> 0.31.4-alt1
- Update to 0.31.4

* Fri Oct 24 2025 Pavel Shilov <zerospirit@altlinux.org> 0.31.3-alt1
- Initial build for Sisyphus.
