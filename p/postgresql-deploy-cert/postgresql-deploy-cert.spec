Name:    postgresql-deploy-cert
Version: 0.6
Release: alt1

Summary: deploy script for postgresql cert config
License: MIT
Group:   Other
Url:     https://git.altlinux.org/gears/p/postgresql-deploy-cert.git

Packager: "Denis Medvedev" <nbr@altlinux.org>

Source: %name-%version.tar

BuildArch: noarch
Requires: deploy

%description
A module for deploy ansible configuration maker for postgresql config

%prep
%setup

%install
mkdir -p %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 postgresql-cert.yml %buildroot%_datadir/deploy/postgresql-cert.yml
install -Dm 0644 *.conf  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 *.acl  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 main.yml  %buildroot/%_datadir/deploy/postgresql-cert/tasks
install -Dm 0644 postgresql.pam  %buildroot/%_datadir/deploy/postgresql-cert/tasks


%files
%_datadir/deploy/postgresql-cert.yml
%_datadir/deploy/postgresql-cert/tasks/*

%changelog
* Thu Jun 27 2024 "Denis Medvedev" <nbr@altlinux.org> 0.6-alt1
- added packages for cluster and checksums

* Mon Jun 03 2024 "Denis Medvedev" <nbr@altlinux.org> 0.5-alt1
- Initial build for ALT
