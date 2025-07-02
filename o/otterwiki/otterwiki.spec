%define module python3-module-%name
%define rootdir /var/www/webapps/%name
%define ident _%name
Name: otterwiki
Version: 2.11.1
Release: alt1
Url: https://otterwiki.com
Group: Networking/WWW
Summary: A minimalistic wiki powered by python, markdown and git
License: MIT
Source: %name-%version.tar.gz
Source1: otterwiki-install.sh
Source2: otterwiki.service
Source3: otterwiki.sh
Source4: mistune.tar.gz
Patch: otterwiki-mistune2.patch
Buildarch: noarch

# Automatically added by buildreq on Wed Jul 02 2025
# optimized out: bash5 libgpg-error openssl-config python3 python3-base python3-dev python3-module-jaraco.context python3-module-jaraco.functools python3-module-jaraco.text python3-module-more-itertools python3-module-packaging python3-module-pkg_resources python3-module-py3dephell python3-module-wheel sh5
BuildRequires: python3-module-pyproject-installer python3-module-setuptools

Requires(pre): webserver-common
Requires: python3(sqlite3) python3(otterwiki)

%description
An Otter Wiki - minimalistic wiki powered by python, markdown and git.
Notable Features

    Minimalistic interface with dark-mode
    Editor with markdown support including tables
    Full changelog and page history
    Customizable Sidebar: Menu and/or Page Index
    User authentication
    Page Attachments
    Extended: tables, footnotes, fancy blocks, alerts and mermaid diagrams.
    Git http server: clone, pull and push the content of your wiki.
    A very cute Otter as logo (drawn by Christy Presler CC BY 3.0)

%package -n %module
Group: Networking/WWW
Summary: %summary, python core module

%description -n %module
%summary

%prep
%setup
%setup -a4
mv mistune %name/
%patch -p1
cat > %name.etcconfig <<@@@
OTTERWIKI_SETTINGS=%rootdir/settings.cfg
OTTERWIKI_LISTEN=127.0.0.1:8080
@@@

%build
%pyproject_build

%install
%pyproject_install
install -D %SOURCE1 %buildroot%_libexecdir/%name-install
install -m 644 -D %SOURCE2 %buildroot%systemd_unitdir/%name.service
install -D %SOURCE3 %buildroot%_bindir/%name
install -m644 -D %name.etcconfig %buildroot%_sysconfdir/%name

%pre
%_sbindir/groupadd -r %ident &>/dev/null ||:
%_sbindir/useradd -r -N -M -g %ident -G webmaster -d %rootdir -s /dev/null %ident  &>/dev/null ||:

%post
su -s /bin/sh -c "%_libexecdir/%name-install %ident %rootdir" %ident

%files -n %module
%python3_sitelibdir_noarch/*

%files
%doc docs settings.cfg.skeleton *.md
%config %_sysconfdir/%name
%_libexecdir/%name-install
%systemd_unitdir/%name.service
%_bindir/%name

%changelog
* Wed Jul 02 2025 Fr. Br. George <george@altlinux.org> 2.11.1-alt1
- Autobuild version bump to 2.11.1

* Wed Jul 02 2025 Fr. Br. George <george@altlinux.org> 2.11.0-alt1
- Initial build
