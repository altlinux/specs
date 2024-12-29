%global _unpackaged_files_terminate_build 1
%global import_path github.com/navidrome/navidrome
 # git rev-parse --short v%version
%global commit_hash 734eb30ac

Name: navidrome
Version: 0.54.3
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

BuildRequires(pre): rpm-build-golang
BuildRequires: esbuild
BuildRequires: gcc-c++
BuildRequires: golang
BuildRequires: npm
BuildRequires: libtag-devel

Requires: ffmpeg

%description
Navidrome is an open source web-based music collection server and streamer.
It gives you freedom to listen to your music collection from any browser
or mobile device. It's like your personal Spotify!

%prep
# go mod vendor
# git add vendor -f && git commit -m "Updated go vendor modules."
# npm --prefix ui ci
# rm -vf ui/node_modules/{esbuild/bin/esbuild,@esbuild/linux-*/bin/esbuild}
# git add ui/node_modules -f && git commit -m "Updated node modules."
%setup -a 1 -a 2
# use system esbuild
%ifarch x86_64
%define arch_dir x64
%endif
%ifarch i586
%define arch_dir ia32
%endif
%ifarch aarch64
%define arch_dir arm64
%endif
%ifarch loongarch64
%define arch_dir loong64
%endif
%ifarch ppc64le
%define arch_dir ppc64
%endif
mkdir -p node_modules/{esbuild/bin,@esbuild/linux-%arch_dir/bin}
ln -sv %_bindir/esbuild node_modules/esbuild/bin/esbuild
ln -sv %_bindir/esbuild node_modules/@esbuild/linux-%arch_dir/bin/esbuild
sed -i "s/0.21.5/$(rpm -q --qf '%{VERSION}' esbuild)/g" node_modules/esbuild/lib/main.js

%build
export BUILDDIR=$PWD/.gopath
export IMPORT_PATH=%import_path
export GOPATH=$BUILDDIR:%go_path
export GOFLAGS=-mod=vendor
npm --prefix ui run build
%golang_prepare
cd .gopath/src/%import_path
go build -gcflags="all=-N -l" -tags=netgo -ldflags="\
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
* Sun Dec 29 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.54.3-alt1
- Updated to version 0.54.3 (fix CVE-2024-47062, CVE-2024-56362).

* Thu May 09 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.52.0-alt1
- Updated to version 0.52.0.

* Mon Mar 18 2024 Alexander Makeenkov <amakeenk@altlinux.org> 0.51.1-alt1
- Initial build for ALT.
