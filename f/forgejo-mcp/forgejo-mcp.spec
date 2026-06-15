%global _unpackaged_files_terminate_build 1

Name:    forgejo-mcp
Version: 2.29.0
Release: alt1

%global import_path codeberg.org/goern/forgejo-mcp/v%(echo %{version} | cut -d. -f1)

Summary: This Model Context Protocol (MCP) server provides tools and resources for interacting with the Forgejo (specifically Codeberg.org) REST API
License: MIT
Group:   Development/Tools
Url:     https://codeberg.org/goern/forgejo-mcp
Vcs:     https://codeberg.org/goern/forgejo-mcp.git

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
export LDFLAGS="-X main.Version=%version"

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
* Mon Jun 15 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.29.0-alt1
- New version 2.29.0.

* Fri May 29 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.26.0-alt1
- New version 2.26.0.

* Mon May 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.23.1-alt1
- New version 2.23.1.

* Tue May 12 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.22.0-alt1
- New version 2.22.0.

* Sun May 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.21.0-alt1
- New version 2.21.0.

* Mon Mar 16 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.15.1-alt1
- New version 2.15.1.

* Thu Mar 12 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.15.0-alt1
- New version 2.15.0.

* Sun Mar 01 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.12.0-alt1
- New version 2.12.0.

* Wed Feb 11 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.10.0-alt1
- New version 2.10.0.

* Sat Feb 07 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.9.1-alt1
- New version 2.9.1.

* Fri Jan 30 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.7.0-alt1
- New version 2.7.0.

* Sun Jan 18 2026 Maxim Slipenko <maks1ms@altlinux.org> 2.5.0-alt1
- Initial build.

