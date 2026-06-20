%define import_path github.com/trufflesecurity/trufflehog/v3
%global _unpackaged_files_terminate_build 1

Name: trufflehog
Version: 3.95.6
Release: alt1
Summary: CLI tool to find exposed secrets in source and archives

Group: Development/Tools
License: AGPL-3.0

Url: https://trufflesecurity.com/
Vcs: https://github.com/trufflesecurity/trufflehog.git

Source0: %name-%version.tar
Source1: %name-%version-vendor.tar
Patch: %name-%version-%release.patch

ExclusiveArch: %go_arches
ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang

%description
TruffleHog is a scanning engine that helps find exposed secrets
within e.g. GitHub/GitLab repos, AWS S3 buckets, GCS buckets,
Docker images, Circle CI/Travis CI setups, or in individual files.

%prep
%setup -a1
%autopatch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X %import_path/pkg/version.BuildVersion=%version"
%golang_prepare
%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

%files
%_bindir/%name
%doc *.md

%changelog
* Sat Jun 20 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.95.6-alt1
- New version 3.95.6.

* Tue Jun 02 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.95.5-alt1
- New version 3.95.5.

* Tue May 12 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.95.3-alt1
- New version 3.95.3.

* Tue May 05 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.95.2-alt1
- New version 3.95.2.

* Wed Mar 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.94.0-alt2
- Disable automatic update fetcher (closes: #57990).

* Wed Mar 25 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.94.0-alt1
- New version 3.94.0.

* Wed Feb 11 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.93.2-alt1
- New version 3.93.2.

* Fri Jan 16 2026 Maxim Slipenko <maks1ms@altlinux.org> 3.92.5-alt1
- New version 3.92.5.

* Sun Dec 21 2025 Maxim Slipenko <maks1ms@altlinux.org> 3.92.4-alt1
- New version 3.92.4.

* Mon Nov 17 2025 Maxim Slipenko <maks1ms@altlinux.org> 3.91.0-alt1
- New version 3.91.0.

* Thu Oct 23 2025 Maxim Slipenko <maks1ms@altlinux.org> 3.90.11-alt1
- Initial build.



