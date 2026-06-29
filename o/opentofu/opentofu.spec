%global import_path github.com/opentofu/opentofu
%global _unpackaged_files_terminate_build 1

Name: opentofu
Version: 1.12.3
Release: alt1
Summary: OpenTofu lets you declaratively manage your cloud infrastructure

Group: Development/Tools
License: MPL-2.0

Url: https://github.com/opentofu/opentofu
Vcs: https://github.com/opentofu/opentofu.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch:  %go_arches

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.26.3

%description
OpenTofu lets you declaratively manage your cloud infrastructure.

%prep
%setup
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/version.dev=no \
                -X main.version=v%{version} "

%golang_prepare

%golang_build cmd/tofu

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%doc *.md
%_bindir/*

%changelog
* Sat Jun 20 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.3-alt1
- New version 1.12.3.

* Mon Jun 15 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.2-alt1
- New version 1.12.2.

* Fri May 15 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.12.0-alt1
- New version 1.12.0.

* Mon May 11 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.11.7-alt1
- New version 1.11.7.

* Sun May 10 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.11.6-alt1
- New version 1.11.6.

* Tue Feb 17 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.11.5-alt1
- New version 1.11.5.

* Mon Jan 26 2026 Maxim Slipenko <maks1ms@altlinux.org> 1.11.3-alt1
- New version 1.11.3.

* Sun Dec 21 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.11.2-alt1
- New version 1.11.2.

* Thu Nov 27 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.7-alt1
- New version 1.10.7.

* Mon Oct 06 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.6-alt1
- New version 1.10.6.

* Mon Jul 14 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.10.2-alt1
- New version 1.10.2.

* Wed May 07 2025 Maxim Slipenko <maks1ms@altlinux.org> 1.9.1-alt1
- Initial build

