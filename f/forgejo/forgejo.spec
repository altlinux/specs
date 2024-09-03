%global import_path code.gitea.io/gitea
%global _unpackaged_files_terminate_build 1

Name: forgejo
Version: 8.0.2
Release: alt1

Summary: Self-hosted lightweight software forge

License: MIT
Group: Development/Other
Url: https://forgejo.org
Vcs: https://codeberg.org/forgejo/forgejo.git
Source: %name-%version.tar

Source2: %name.service
Source3: %name.service.d.conf

Patch3: disable-strip.patch

BuildRequires(pre): rpm-macros-golang
BuildRequires: golang >= 1.22 rpm-build-golang
BuildRequires: libpam-devel
BuildRequires: /proc

Requires: git-core

%description
Forgejo is a self-hosted lightweight software forge.
Easy to install and low maintenance, it just does the job

Brought to you by an inclusive community under the umbrella
of Codeberg e.V., a democratic non-profit organization,
Forgejo can be trusted to be exclusively Free Software. It
is a "soft" fork of Gitea with a focus on scaling, federation
and privacy.

%prep
%setup
%patch3 -p1

sed -i \
    -e "s|^APP_NAME = ; Gitea: Git with a cup of tea|APP_NAME = Forgejo: Beyond coding. We Forge.|" \
    -e "s|^RUN_USER =|RUN_USER = forgejo|" \
    -e "s|^HTTP_ADDR = 0.0.0.0|HTTP_ADDR = 127.0.0.1|" \
    -e "s|^;APP_DATA_PATH = data|;APP_DATA_PATH = %_localstatedir/%name/data|" \
    -e "s|^;STATIC_ROOT_PATH =|;STATIC_ROOT_PATH = %_datadir/%name|" \
    -e "s|^;ROOT_PATH =|;ROOT_PATH = %_logdir/%name|" \
    -e "s|^DB_TYPE = mysql|;DB_TYPE = mysql|" \
    -e "s|^HOST = 127.0.0.1:3306|;HOST = 127.0.0.1:3306|" \
    -e "s|^NAME = gitea|;NAME = gitea|" \
    -e "s|^USER = root|;USER = root|" \
    -e "s|^;DB_TYPE = sqlite3|DB_TYPE = sqlite3|" \
custom/conf/app.example.ini

sed -i -e "s|gitea|%name|g" contrib/autocompletion/*_autocomplete

%build
export BUILDDIR="$PWD/.gopath"
export IMPORT_PATH="%import_path"
export GOPATH="$BUILDDIR:%go_path"
export LDFLAGS="-X code.gitea.io/gitea/modules/setting.CustomConf=%_sysconfdir/%name/app.ini \
                -X code.gitea.io/gitea/modules/setting.CustomPath=%_localstatedir/%name/custom \
                -X code.gitea.io/gitea/modules/setting.AppWorkPath=%_localstatedir/%name"
export TAGS="bindata timetzdata sqlite sqlite_unlock_notify pam"
%make all
%gobuild -o %name-environment-to-ini contrib/environment-to-ini/environment-to-ini.go

%install
mkdir -p %buildroot%_localstatedir/%name/custom
mkdir -p %buildroot%_logdir/%name
install -Dm 0755 gitea %buildroot%_bindir/%name
install -Dm 0755 %name-environment-to-ini %buildroot%_bindir/%name-environment-to-ini
install -Dm 0644 %SOURCE2 %buildroot%_unitdir/%name.service
mkdir -p %buildroot%_sysconfdir/systemd/system/%name.service.d
install -Dm 0644 %SOURCE3 %buildroot%_sysconfdir/systemd/system/%name.service.d/port.conf
install -Dm 0660 custom/conf/app.example.ini %buildroot%_sysconfdir/%name/app.ini

# install docs
mkdir -p %buildroot%_man1dir
%buildroot%_bindir/%name docs --man > %buildroot%_man1dir/%name.1

# install completions
install -D -p -m 0644 contrib/autocompletion/bash_autocomplete %buildroot%_datadir/bash-completion/completions/%name
install -D -p -m 0644 contrib/autocompletion/zsh_autocomplete %buildroot%_datadir/zsh/site-functions/_%name

%pre
groupadd -r -f %name 2>/dev/null ||:
useradd -r -g %name -c 'Forgejo daemon' \
        -s /bin/bash  -d %_localstatedir/%name %name 2>/dev/null ||:

%post
%post_service %name

%preun
%preun_service %name
%files
%doc *.md custom/conf/app.example.ini
%_bindir/%name
%_bindir/%name-environment-to-ini
%dir %attr(0750,%name,%name) %_localstatedir/%name
%dir %attr(0750,%name,%name) %_localstatedir/%name/custom
%dir %attr(0770,root,%name) %_logdir/%name
%dir %_sysconfdir/%name
%config(noreplace) %attr(0660,root,%name) %_sysconfdir/%name/app.ini
%dir %_sysconfdir/systemd/system/%name.service.d
%config(noreplace) %_sysconfdir/systemd/system/%name.service.d/port.conf
%_unitdir/%name.service
%_man1dir/*
%_datadir/bash-completion/completions/%name
%_datadir/zsh/site-functions/_%name

%changelog
* Tue Sep 03 2024 Alexey Shabalin <shaba@altlinux.org> 8.0.2-alt1
- 8.0.2.

* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 8.0.1-alt1
- 8.0.1.

* Wed Aug 28 2024 Alexey Shabalin <shaba@altlinux.org> 7.0.7-alt1
- 7.0.7.

* Fri Aug 02 2024 Alexey Shabalin <shaba@altlinux.org> 7.0.6-alt1
- 7.0.6.

* Mon Jul 08 2024 Alexey Shabalin <shaba@altlinux.org> 7.0.5-alt1
- 7.0.5.

* Mon Jul 01 2024 Alexey Shabalin <shaba@altlinux.org> 7.0.4-alt1
- Initial build (based on gitea.spec).
