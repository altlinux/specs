%global _unpackaged_files_terminate_build 1
%global import_path codeberg.org/git-pages/git-pages

Name:    git-pages
Version: 0.8.1
Release: alt1

Summary: Scalable static site server for Git forges (like GitHub Pages or Netlify)
License: 0BSD
Group:   System/Servers
Url:     https://git-pages.org
Vcs:     https://codeberg.org/git-pages/git-pages.git

Source: %name-%version.tar
Source1: %name-%version-vendor.tar

Source2: %name.service
Source3: %name.sysconfig

ExclusiveArch: %go_arches
ExcludeArch: %ix86

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
export LDFLAGS="-X main.versionOverride=%version"

%golang_prepare

%golang_build .

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install

mkdir -p %buildroot%_localstatedir/%name

sed -i "s|root = '.*'|root = '/var/lib/git-pages'|" conf/config.default.toml
install -Dm 0644 conf/config.default.toml %buildroot%_sysconfdir/%name/config.toml
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -g %name -c 'git-pages daemon' \
        -s /bin/bash  -d %_localstatedir/%name %name 2>/dev/null ||:

%files
%doc README.md
%_bindir/%name
%dir %attr(0750,%name,%name) %_localstatedir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,%name) %_sysconfdir/%name/config.toml
%config(noreplace) %_sysconfdir/sysconfig/%name
%_unitdir/%name.service

%changelog
* Tue Apr 28 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.8.1-alt1
- New version 0.8.1.
- Add sysconfig file (closes ALT#58846).

* Sat Mar 28 2026 Maxim Slipenko <maks1ms@altlinux.org> 0.7.0-alt1
- Initial build.

