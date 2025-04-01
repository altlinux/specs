%global import_path github.com/crazy-max/diun
%global _unpackaged_files_terminate_build 1
# according to upstreams makefile
# git_version=$(git describe --match 'v[0-9]*' --dirty='.m' --always --tags)
%global git_version v4.29.0-1-ga23713d0.m

Name:    diun
Version: 4.29.0
Release: alt1

Summary: Receive notifications when an image is updated on a Docker registry
License: MIT
Group:   Other
Url:     https://github.com/crazy-max/diun

Source: %name-%version.tar
Source2: %name.service
Source3: %name.sysconfig
Source4: %name.yml
Source5: config.yml

BuildRequires(pre): rpm-macros-golang
BuildRequires: rpm-build-golang
BuildRequires: golang >= 1.23.0
BuildRequires: /proc

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.build"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export GOFLAGS="-mod=vendor"
export LDFLAGS="-X main.version=%git_version"

%golang_prepare

%golang_build cmd

%install
export BUILDDIR="$PWD/.build"
export IGNORE_SOURCES=1

%golang_install
mv -vf -- %buildroot%_bindir/cmd %buildroot%_bindir/diun
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
mkdir -p %buildroot%_localstatedir/%name
install -Dm 0640 %SOURCE4 %buildroot%_sysconfdir/%name/diun.yml
install -Dm 0640 %SOURCE5 %buildroot%_sysconfdir/%name/config.yml

%pre
groupadd -r -f _%name 2>/dev/null ||:
useradd -r -s /dev/null -d %_localstatedir/%name -g _%name -c 'Diun daemon' _%name 2>/dev/null ||:

%preun
%preun_service %name

%post
%post_service %name

%files
%doc README.md CHANGELOG.md
%_bindir/diun
%dir %_sysconfdir/%name
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/diun.yml
%config(noreplace) %attr(0640,root,_%name) %_sysconfdir/%name/config.yml
%config(noreplace) %_sysconfdir/sysconfig/%name
%dir %attr(0750,_%name,_%name) %_localstatedir/%name
%_unitdir/%name.service

%changelog
* Mon Feb 24 2025 Nadezhda Fedorova <fedor@altlinux.org> 4.29.0-alt1
- Initial build for ALT Sisyphus.
