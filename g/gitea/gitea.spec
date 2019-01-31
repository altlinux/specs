%global import_path code.gitea.io/gitea

Name:     gitea
Version:  1.7.0
Release:  alt1

Summary:  Git with a cup of tea, painless self-hosted git service

License:  MIT
Group:    Development/Other
Url:      https://gitea.io

# https://github.com/go-gitea/gitea
Source:   %name-%version.tar

Source1: gitea.service
Source2: app-%version.ini
Source3: README.ALT

BuildRequires(pre): rpm-build-golang
BuildRequires: golang go-bindata
BuildRequires: libpam0-devel

Requires: git-core

%description
The goal of this project is to make the easiest, fastest, and most painless way
of setting up a self-hosted Git service. It is similar to GitHub, Bitbucket,
and Gitlab. Gitea is a fork of Gogs.

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
install -Dm 0660 %SOURCE2 %buildroot%_sysconfdir/%name/app.ini

# install docs
mkdir -p %buildroot%_docdir/%name
install -Dm 0644 ".gopath/src/%import_path/custom/conf/app.ini.sample" %buildroot%_docdir/%name/default-app.ini
install -Dm 0644 %SOURCE3 %buildroot%_docdir/%name/

%pre
groupadd -rf _%name
useradd -r -g _%name -d %_localstatedir/%name _%name -s /bin/sh ||:

%files
%_bindir/%name
%dir %attr(0770,root,_%name) %_localstatedir/%name
%dir %attr(0770,root,_%name) %_logdir/%name
%dir %_docdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0660,root,_%name) %_sysconfdir/%name/app.ini
%systemd_unitdir/%name.service
%_docdir/%name/default-app.ini
%_docdir/%name/README.ALT
%doc *.md

%changelog
* Wed Jan 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Build new version.

* Mon Jan 28 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.4-alt1
- Initial build for Sisyphus
