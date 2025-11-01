%define _unpackaged_files_terminate_build 1
%define import_path github.com/TecharoHQ/anubis.git

Name: anubis
Version: 1.23.0
Release: alt1

Group: Networking/WWW
Summary: Weighs the soul of incoming HTTP requests using proof-of-work to stop AI crawlers

License: MIT
Url: https://anubis.techaro.lol/
Vcs: https://github.com/TecharoHQ/anubis.git

Source: %name-%version.tar
Patch: %name-%version.patch

ExclusiveArch: x86_64 aarch64 ppc64le riscv64 loongarch64

BuildRequires(pre): rpm-macros-golang rpm-macros-nodejs
BuildRequires: rpm-build-golang golang >= 1.24.2
BuildRequires: npm
BuildRequires: node >= 18 node-devel
BuildRequires: esbuild brotli gzip zstd
BuildRequires: /proc

%description
Anubis weighs the soul of your connection using a sha256 proof-of-work challenge
in order to protect upstream resources from scraper bots.
Installing and using this will likely result in your website not being indexed
by some search engines. This is considered a feature of Anubis, not a bug.
This is a bit of a nuclear response, but AI scraper bots scraping so
aggressively have forced my hand. I hate that I have to do this, but this
is what we get for the modern Internet because bots don't conform to standards
like robots.txt, even when they claim to.

%prep
%setup
%patch -p1

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X github.com/TecharoHQ/anubis.Version=%version"
export NODE_OPTIONS=--max_old_space_size=2048
export PATH="$PATH:$PWD/node_modules/.bin"
pushd lib/challenge/preact
./build.sh
popd
go generate
web/build.sh
xess/build.sh
%golang_prepare
%golang_build cmd/%name
%golang_build cmd/robots2policy

%install
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export IGNORE_SOURCES=1
%golang_install

mkdir -p %buildroot{%_sysconfdir,%_localstatedir}/%name
install -p -m644 run/default.env %buildroot%_sysconfdir/%name/default.env
install -pD -m644 run/anubis@.service %buildroot%_unitdir/anubis@.service

rm -f data/embed.go

%post
%post_systemd %name@*.service

%preun
%preun_systemd %name@*.service

%files
%_bindir/*
%doc LICENSE README.md
%doc docs/docs/CHANGELOG.md
%doc docs/docs/admin/policies.mdx
%doc docs/docs/admin/native-install.mdx
%doc data
%dir %_sysconfdir/%name
%config(noreplace) %_sysconfdir/%name/default.env
%_unitdir/anubis@.service
%ghost %dir %_localstatedir/%name

%changelog
* Sat Nov 01 2025 Alexey Shabalin <shaba@altlinux.org> 1.23.0-alt1
- New version 1.23.0.

* Fri Sep 12 2025 Alexey Shabalin <shaba@altlinux.org> 1.22.0-alt1
- New version 1.22.0.

* Mon Jul 28 2025 Alexey Shabalin <shaba@altlinux.org> 1.21.3-alt1
- New version 1.21.3 (Fixes: CVE-2025-54414).

* Mon Jun 16 2025 Alexey Shabalin <shaba@altlinux.org> 1.19.1-alt1
- New version 1.19.1.

* Wed May 14 2025 Alexey Shabalin <shaba@altlinux.org> 1.18.0-alt1
- New version 1.18.0.

* Mon Apr 14 2025 Alexey Shabalin <shaba@altlinux.org> 1.16.0-alt1
- Initial build in Sisyphus

