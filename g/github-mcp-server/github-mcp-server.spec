%global _unpackaged_files_terminate_build 1
%global import_path github.com/github/github-mcp-server
%global commit 85598ba6e1256f7ebf4867b95d63b833c4549264

%def_without check
# tests need network access to the GitHub API, not available in the
# build environment.

Name: github-mcp-server
Version: 1.12.2
Release: alt1

Summary: GitHub's official MCP server
License: MIT
Group: Development/Tools

Url: https://github.com/github/github-mcp-server
Vcs: https://github.com/github/github-mcp-server

ExclusiveArch: %go_arches

Source0: %name-%version.tar
Source1: vendor.tar
Source2: ui-dist.tar
Source3: %name-http.user.service
Source4: 50-%name.preset
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
MCP server by GitHub connecting AI tools to the GitHub platform
(repositories, issues, pull requests, Actions, code security);
supports stdio transport spawned per client and an HTTP gateway
mode.

%prep
%setup -a1 -a2
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-s -w -X main.version=%version
-X main.commit=%commit
-X main.date=$(date -u -d "@$SOURCE_DATE_EPOCH" +%%FT%%TZ)"
%golang_prepare
cmd_dir=$BUILDDIR/src/%import_path/cmd/%name
CGO_ENABLED=0 %golang_build $cmd_dir

%install
export BUILDDIR="$PWD/.build"
install -Dm755 $BUILDDIR/bin/%name %buildroot%_bindir/%name
install -Dm644 %SOURCE3 \
	%buildroot%_userunitdir/%name-http.service
install -Dm644 %SOURCE4 \
	%buildroot%_userpresetdir/50-%name.preset

%files
%doc README.md LICENSE
%_bindir/github-mcp-server
%_userunitdir/github-mcp-server-http.service
%_userpresetdir/50-github-mcp-server.preset

%changelog
* Mon Sep 28 2026 Alexandr Shashkin <dutyrok@altlinux.org> 1.12.2-alt1
- Initial build for ALT Sisyphus.
