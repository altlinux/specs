%global _unpackaged_files_terminate_build 1
%global import_path github.com/navidrome/navidrome
# git rev-parse --short v%version
%global commit_hash c5bb920

Name: navidrome
Version: 0.61.0
Release: alt1
Summary: Modern Music Server and Streamer compatible with Subsonic/Airsonic
License: GPL-3.0
Group: System/Servers
Url: https://www.navidrome.org
VCS: https://github.com/navidrome/navidrome

Source: %name-%version.tar
Source1: vendor.tar
Source2: node_modules.tar
Source3: navidrome.sysconfig
Source4: navidrome.toml
Source5: navidrome.service

# CPU time limit exceeded
ExcludeArch: i586

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: esbuild
BuildRequires: gcc-c++
BuildRequires: npm
BuildRequires: taglib-devel

Requires: ffmpeg
Requires: ffprobe

%description
Navidrome is an open source web-based music collection server and streamer.
It gives you freedom to listen to your music collection from any browser
or mobile device. It's like your personal Spotify!

%prep
%setup -a 1 -a 2
# use system esbuild
ln -sv %_bindir/esbuild ui
sed -i "s/0.27.2/$(rpm -q --qf '%{VERSION}' esbuild)/g" node_modules/esbuild/lib/main.js

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
export CGO_CFLAGS_ALLOW="--define-prefix"
export ESBUILD_BINARY_PATH=./esbuild
npm --prefix ui run build
%golang_prepare
cd .gopath/src/%import_path
go build -gcflags="all=-N -l" -tags=netgo,sqlite_fts5 -ldflags="\
         -X %import_path/consts.gitTag=v%version \
         -X %import_path/consts.gitSha=%commit_hash"

%install
mkdir -p %buildroot%_bindir \
         %buildroot%_unitdir \
         %buildroot%_sysconfdir/sysconfig \
         %buildroot%_sharedstatedir/navidrome
install -m 0755 .gopath/src/%import_path/navidrome %buildroot%_bindir/navidrome
install -m 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/navidrome
install -m 0644 %SOURCE4 %buildroot%_sysconfdir/navidrome.toml
install -m 0644 %SOURCE5 %buildroot%_unitdir/navidrome.service

%pre
%_sbindir/groupadd -r -f navidrome
%_sbindir/useradd -r -g navidrome -s /sbin/nologin \
                  -d %_sharedstatedir/navidrome navidrome 2>/dev/null ||:

%post
%post_service navidrome

%preun
%preun_service navidrome

%files
%_bindir/navidrome
%_unitdir/navidrome.service
%_sysconfdir/sysconfig/navidrome
%config(noreplace) %_sysconfdir/navidrome.toml
%dir %attr(750, navidrome, navidrome) %_sharedstatedir/navidrome

%changelog
* Thu Apr 02 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.61.0-alt1
- Updated to version 0.61.0.

* Sat Feb 14 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.60.3-alt1
- Updated to version 0.60.3.

* Wed Feb 04 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.60.0-alt1
- Updated to version 0.60.0 (fix CVE-2026-25578, CVE-2026-25579).

* Sat Jan 31 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.59.0-alt2
- Fixed build with golang 1.25.6.

* Thu Jan 01 2026 Alexander Makeenkov <amakeenk@altlinux.org> 0.59.0-alt1
- Updated to version 0.59.0.

* Mon Nov 10 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.58.5-alt1
- Updated to version 0.58.5.

* Sun Aug 10 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.58.0-alt1
- Updated to version 0.58.0.

* Sun Jun 01 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.56.1-alt1
- Updated to version 0.56.1 (fix CVE-2025-48948, CVE-2025-48949).
- Excluded i586 arch (CPU time limit exceeded).

* Sun Apr 27 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.55.2-alt1
- Updated to version 0.55.2.

* Wed Mar 19 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.55.1-alt1
- Updated to version 0.55.1.

* Mon Feb 24 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.54.5-alt1
- Updated to version 0.54.5 (fix CVE-2025-27112).

* Sun Dec 29 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.54.3-alt1
- Updated to version 0.54.3 (fix CVE-2024-47062, CVE-2024-56362).

* Thu May 09 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.52.0-alt1
- Updated to version 0.52.0.

* Mon Mar 18 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.51.1-alt1
- Initial build for ALT.
