%global import_path code.gitea.io/gitea
Name:     gitea
Version:  1.6.4
Release:  alt1

Summary:  Git with a cup of tea, painless self-hosted git service

License:  MIT
Group:    Other
Url:      https://gitea.io

Source:   %name-%version.tar

Source1: gitea.service
Source2: app.ini

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-bindata
BuildRequires: libpam0-devel

Requires: git-core

%description
%summary

%prep
%setup

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

%golang_prepare
cd "$BUILDDIR"/src/%import_path
TAGS="bindata sqlite pam" make generate all

%install
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name
install -Dm 0755 ".gopath/src/%import_path/%name" %buildroot%_bindir/%name
install -Dm 0640 %SOURCE1 %buildroot%systemd_unitdir/%name.service
install -Dm 0660 %SOURCE2  %buildroot%_sysconfdir/%name/app.ini

%pre
groupadd -rf _%name
useradd -r -g _%name -d %_localstatedir/%name _%name -s /bin/sh ||:

%files
%_bindir/%name
%dir %attr(0770,root,_%name) %_localstatedir/%name
%dir %attr(0770,root,_%name) %_logdir/%name
%config(noreplace) %attr(0660,root,_%name) %_sysconfdir/%name/app.ini
%systemd_unitdir/%name.service
%doc *.md

%changelog
* Mon Jan 28 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.4-alt1
- Initial build for Sisyphus
