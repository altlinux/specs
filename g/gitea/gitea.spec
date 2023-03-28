%global import_path code.gitea.io/gitea

%global _unpackaged_files_terminate_build 1
%def_enable tarball

Name:    gitea
Version: 1.19.0
Release: alt1

Summary: Git with a cup of tea, painless self-hosted git service

License: MIT
Group:   Development/Other
Url:     https://gitea.io

# https://github.com/go-gitea/gitea
Source: %name-%version.tar

Source2: gitea.service
Source3: gitea.service.d.conf
Source4: README.ALT

%if_disabled tarball
Patch1: %name-%version.patch
%endif
Patch2: ALT_config.patch
Patch3: disable-strip.patch

BuildRequires(pre): rpm-build-golang
BuildRequires: golang >= 1.19
%if_disabled tarball
BuildRequires: npm >= 6.13.6-alt2 node >= 14.0.0 esbuild node-gyp go-bindata
%endif
BuildRequires: libpam-devel
BuildRequires: /proc

Requires: git-core

%description
The goal of this project is to make the easiest, fastest, and most painless way
of setting up a self-hosted Git service. It is similar to GitHub, Bitbucket,
and Gitlab. Gitea is a fork of Gogs.

%prep
# build the JavaScript and CSS files
# $ npm install
# $ rm -f node_modules/esbuild/bin/esbuild
# $ rm -rf node_modules/esbuild-linux*
# $ git add -f node_modules
# $ git commit -n --no-post-rewrite -m "add node js modules"
# $ go mod vendor
# $ git add -f vendor
# $ git commit -n --no-post-rewrite -m "add go modules by go mod vendor"

%setup
%if_disabled tarball
%patch1 -p1
mkdir -p node_modules/esbuild/bin
ln -s %_bindir/esbuild node_modules/esbuild/bin/esbuild
%else
%patch3 -p1
%endif
%patch2 -p1

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"

TAGS="bindata sqlite sqlite_unlock_notify pam" GITEA_VERSION=%version %make all

%install
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_logdir/%name
install -Dm 0755 %name %buildroot%_bindir/%name
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/systemd/system/gitea.service.d
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/systemd/system/gitea.service.d/port.conf
install -Dm 0660 custom/conf/app.example.ini %buildroot%_sysconfdir/%name/app.ini

# install docs
mkdir -p %buildroot%_man1dir
./gitea docs --man > %buildroot%_man1dir/gitea.1
mkdir -p %buildroot%_docdir/%name
install -Dm 0644 custom/conf/app.example.ini %buildroot%_docdir/%name/default-app.ini
install -Dm 0644 %SOURCE4 %buildroot%_docdir/%name/

# install completions
install -D -p -m 0644 contrib/autocompletion/bash_autocomplete %buildroot%_datadir/bash-completion/completions/gitea
install -D -p -m 0644 contrib/autocompletion/zsh_autocomplete %buildroot%_datadir/zsh/site-functions/_gitea

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -g %name -c 'Gitea daemon' \
        -s /bin/bash  -d %_localstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc *.md
%_docdir/%name
%_bindir/%name
%dir %attr(0750,%name,%name) %_localstatedir/%name
%dir %attr(0770,root,%name) %_logdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0660,root,%name) %_sysconfdir/%name/app.ini
%dir %_sysconfdir/systemd/system/gitea.service.d
%config(noreplace) %_sysconfdir/systemd/system/gitea.service.d/port.conf
%_unitdir/%name.service
%_man1dir/*
%_datadir/bash-completion/completions/gitea
%_datadir/zsh/site-functions/_gitea


%changelog
* Tue Mar 28 2023 Alexey Shabalin <shaba@altlinux.org> 1.19.0-alt1
- 1.19.0

* Mon Jan 23 2023 Alexey Shabalin <shaba@altlinux.org> 1.18.2-alt1
- 1.18.2

* Wed Oct 19 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.3-alt1
- Build new version (Fixes: CVE-2022-42968).

* Mon Sep 26 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.2-alt1
- Build new version.

* Mon Sep 05 2022 Alexey Shabalin <shaba@altlinux.org> 1.17.1-alt1
- Build new version.

* Thu Jul 28 2022 Alexey Shabalin <shaba@altlinux.org> 1.16.9-alt1
- Build new version (Fixes: CVE-2022-38183, CVE-2022-1928).

* Mon May 02 2022 Alexey Shabalin <shaba@altlinux.org> 1.16.7-alt1
- Build new version (Fixes: CVE-2022-30781).

* Sat Apr 23 2022 Alexey Shabalin <shaba@altlinux.org> 1.16.6-alt1
- Build new version (Fixes: CVE-2022-30781, CVE-2022-1058, CVE-2022-0905).
- Build from src tarball.
- Add man page.

* Wed Mar 02 2022 Alexey Shabalin <shaba@altlinux.org> 1.16.2-alt1
- Build new version.

* Sat Jan 22 2022 Alexey Shabalin <shaba@altlinux.org> 1.15.10-alt1
- Build new version.

* Tue Dec 14 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.7-alt1
- 1.15.7 (Fixes: CVE-2021-45330)

* Sun Oct 31 2021 Alexey Shabalin <shaba@altlinux.org> 1.15.6-alt1
- Build new version.

* Fri Jul 30 2021 Alexey Shabalin <shaba@altlinux.org> 1.14.5-alt1
- Build new version.

* Fri Jul 02 2021 Alexey Shabalin <shaba@altlinux.org> 1.14.3-alt1
- Build new version.

* Fri May 28 2021 Alexey Shabalin <shaba@altlinux.org> 1.14.2-alt1
- Build new version.

* Wed Apr 07 2021 Alexey Shabalin <shaba@altlinux.org> 1.13.7-alt1
- Build new version (Fixes: CVE-2021-3382, CVE-2021-29134).

* Fri Dec 11 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.6-alt1
- Build new version (Fixes: CVE-2021-28378, CVE-2020-28991).

* Thu Oct 29 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.5-alt1
- Build new version (Fixes: CVE-2020-14144).

* Fri Sep 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.4-alt1
- Build new version.

* Mon Aug 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.3-alt1
- Build new version.

* Thu Jun 25 2020 Alexey Shabalin <shaba@altlinux.org> 1.12.1-alt1
- Build new version.

* Fri May 29 2020 Alexey Shabalin <shaba@altlinux.org> 1.11.5-alt1
- Build new version (Fixes: CVE-2020-13246).

* Mon Apr 27 2020 Alexey Shabalin <shaba@altlinux.org> 1.11.4-alt2
- update nodejs modules

* Thu Apr 02 2020 Alexey Shabalin <shaba@altlinux.org> 1.11.4-alt1
- Build new version (Fixes: CVE-2021-45327).

* Wed Feb 19 2020 Alexey Shabalin <shaba@altlinux.org> 1.11.1-alt1
- Build new version.

* Tue Feb 11 2020 Grigory Ustinov <grenka@altlinux.org> 1.11.0-alt1
- Build new version.

* Mon Jan 20 2020 Grigory Ustinov <grenka@altlinux.org> 1.10.3-alt1
- Build new version.

* Tue Jan 07 2020 Grigory Ustinov <grenka@altlinux.org> 1.10.2-alt1
- Build new version.

* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 1.10.1-alt1
- Build new version.
- Change building scheme.

* Tue Oct 22 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.4-alt3
- Fix perms on /var/lib/gitea.

* Mon Oct 14 2019 Alexey Shabalin <shaba@altlinux.org> 1.9.4-alt2
- Update spec:
  + disable find debuginfo files
  + %%systemd_unitdir -> %%_unitdir
  + fixed perm /lib/systemd/system/gitea.service
  + fixed perm /etc/systemd/system/gitea.service.d/port.conf
  + fixed perm /var/lib/gitea
  + fixed perm /var/log/gitea
  + add %%preun
  + add comment option to adduser in %%pre

* Mon Oct 14 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.4-alt1
- Build new version.

* Wed Sep 11 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.3-alt1
- Build new version.

* Fri Aug 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt1
- Build new version.
- Add post section.
- Updated config-updater for new building scheme.

* Wed Jul 31 2019 Grigory Ustinov <grenka@altlinux.org> 1.9.0-alt1
- new version 1.9.0
- Changed config file.
- Changed building scheme (thx to obirvalger@).

* Tue Jun 18 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.3-alt1
- new version 1.8.3

* Thu May 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.2-alt1
- new version 1.8.2

* Mon May 13 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.1-alt1
- Build new version.
- Changed config file.

* Tue Apr 23 2019 Grigory Ustinov <grenka@altlinux.org> 1.8.0-alt1
- Build new version.
- Changed config file.

* Mon Apr 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.6-alt1
- Build new version.

* Thu Mar 28 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.5-alt1
- Build new version.

* Tue Mar 19 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.4-alt1
- Build new version.

* Mon Mar 04 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.3-alt1
- Build new version.

* Fri Feb 15 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.2-alt1
- Build new version.

* Fri Feb 08 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.7.1-alt3
- Fix ownership of catalogs
- Fix showing version

* Mon Feb 04 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt2
- Change user _gitea to gitea.

* Fri Feb 01 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt1
- Build new version.

* Wed Jan 30 2019 Grigory Ustinov <grenka@altlinux.org> 1.7.0-alt1
- Build new version.

* Mon Jan 28 2019 Mikhail Gordeev <obirvalger@altlinux.org> 1.6.4-alt1
- Initial build for Sisyphus
