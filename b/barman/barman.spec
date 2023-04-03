Name: barman
Version: 3.5.0
Release: alt1
Summary: Backup and Recovery Manager for PostgreSQL

License: GPL-3.0+
Group: Databases
Url: http://www.pgbarman.org/

Source: https://sourceforge.net/projects/pgbarman/files/%version/%name-%version.tar.gz
Source1: barman.cron
Source2: barman.logrotate

BuildArch: noarch

BuildRequires(pre): python3-module-wheel
BuildRequires: python3-devel python3-module-setuptools
Requires(pre): shadow-utils
Requires: python3-module-argcomplete
Requires: rsync >= 3.0.4

%description
Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%package -n barman-cli
Summary: Client Utilities for Barman, Backup and Recovery Manager for PostgreSQL
Group: Databases

%description -n barman-cli
Client utilities for the integration of Barman in
PostgreSQL clusters.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%package -n python3-module-barman
Summary: The shared libraries required for Barman family components
Group: Databases
Requires: python3-module-setuptools, python3-module-psycopg2 >= 2.4.2, python3-module-argh >= 0.21.2, python3-module-argcomplete, python3-module-dateutil

%description -n python3-module-barman
Python libraries used by Barman.

Barman (Backup and Recovery Manager) is an open-source
administration tool for disaster recovery of PostgreSQL
servers written in Python.
It allows your organization to perform remote backups of
multiple servers in business critical environments to
reduce risk and help DBAs during the recovery phase.

Barman is distributed under GNU GPL 3 and maintained
by 2ndQuadrant.

%prep
%setup

# Change shebang in all relevant executable files in this directory and all subdirectories
find -type f -executable -exec sed -i '1s=^#!%_bindir/\(python\|env python\)[23]\?=#!%__python3=' {} +

%build
%pyproject_build

%install
%pyproject_install
mkdir -p %buildroot%_sysconfdir/cron.d/
mkdir -p %buildroot%_logrotatedir/
mkdir -p %buildroot/var/lib/barman
mkdir -p %buildroot/var/log/barman
mkdir -p %buildroot%_sysconfdir/barman/conf.d
install -pm 644 doc/barman.conf %buildroot%_sysconfdir/barman/barman.conf
install -pm 644 doc/barman.d/* %buildroot%_sysconfdir/barman/conf.d
install -pm 644 %SOURCE1 %buildroot%_sysconfdir/cron.d/barman
install -pm 644 %SOURCE2 %buildroot%_logrotatedir/barman
install -Dpm 644 scripts/barman.bash_completion %buildroot%_datadir/bash-completion/completions/barman
touch %buildroot/var/log/barman/barman.log

%__subst 's|/etc/barman.d|/etc/barman/conf.d|g' %buildroot%_sysconfdir/barman/barman.conf

%files
%doc LICENSE
%doc NEWS README.rst
%_bindir/%name
%_man1dir/%name.1.xz
%_man5dir/%name.5.xz
%config(noreplace) %_sysconfdir/barman/%name.conf
%config(noreplace) %_sysconfdir/cron.d/%name
%config(noreplace) %_logrotatedir/%name
%config(noreplace) %_sysconfdir/barman/conf.d/
%_datadir/bash-completion/completions/barman
%attr(700,barman,barman) %dir /var/lib/%name
%attr(755,barman,barman) %dir /var/log/%name
%attr(600,barman,barman) %ghost /var/log/%name/%name.log

%files -n barman-cli
%doc NEWS README.rst
%_bindir/barman-wal-archive
%_bindir/barman-wal-restore
%_bindir/barman-cloud-restore
%_bindir/barman-cloud-backup
%_bindir/barman-cloud-backup-list
%_bindir/barman-cloud-backup-delete
%_bindir/barman-cloud-backup-keep
%_bindir/barman-cloud-backup-show
%_bindir/barman-cloud-wal-archive
%_bindir/barman-cloud-check-wal-archive
%_bindir/barman-cloud-wal-restore
%doc %_man1dir/barman-wal-archive.1.xz
%doc %_man1dir/barman-wal-restore.1.xz
%doc %_man1dir/barman-cloud-backup.1.xz
%doc %_man1dir/barman-cloud-wal-archive.1.xz
%doc %_man1dir/barman-cloud-backup-list.1.xz
%doc %_man1dir/barman-cloud-backup-delete.1.xz
%doc %_man1dir/barman-cloud-backup-keep.1.xz
%doc %_man1dir/barman-cloud-restore.1.xz
%doc %_man1dir/barman-cloud-wal-restore.1.xz
%doc %_man1dir/barman-cloud-check-wal-archive.1.xz

%files -n python3-module-barman
%doc NEWS README.rst
%python3_sitelibdir/%name-%version.dist-info/
%python3_sitelibdir/%name/

%pre
getent group barman >/dev/null || groupadd -r barman
getent passwd barman >/dev/null || \
    useradd -r -g barman -d /var/lib/barman -s /bin/bash \
    -c "Backup and Recovery Manager for PostgreSQL" barman
exit 0

%changelog
* Mon Apr 03 2023 Leontiy Volodin <lvol@altlinux.org> 3.5.0-alt1
- New version 3.5.0.

* Mon Jan 30 2023 Leontiy Volodin <lvol@altlinux.org> 3.4.0-alt1
- New version (3.4.0).
- Applied patches from master branch.

* Mon Dec 19 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.0-alt1
- New version (3.3.0).

* Mon Oct 24 2022 Leontiy Volodin <lvol@altlinux.org> 3.2.0-alt1
- New version (3.2.0).

* Thu Sep 15 2022 Leontiy Volodin <lvol@altlinux.org> 3.1.0-alt1
- New version (3.1.0).

* Mon Jul 11 2022 Leontiy Volodin <lvol@altlinux.org> 3.0.1-alt1
- New version (3.0.1).

* Fri Mar 11 2022 Leontiy Volodin <lvol@altlinux.org> 2.19-alt1
- New version (2.19).

* Tue Jan 25 2022 Leontiy Volodin <lvol@altlinux.org> 2.18-alt1
- New version (2.18).

* Wed Dec 01 2021 Leontiy Volodin <lvol@altlinux.org> 2.17-alt1
- New version (2.17).

* Fri Oct 15 2021 Leontiy Volodin <lvol@altlinux.org> 2.15-alt1
- New version (2.15).

* Thu Oct 07 2021 Leontiy Volodin <lvol@altlinux.org> 2.14-alt1
- New version (2.14).

* Wed Jul 28 2021 Leontiy Volodin <lvol@altlinux.org> 2.13-alt1
- New version (2.13).

* Thu Nov 05 2020 Leontiy Volodin <lvol@altlinux.org> 2.12-alt1
- New version (2.12) with rpmgs script.

* Tue Jul 14 2020 Leontiy Volodin <lvol@altlinux.org> 2.11-alt1
- New version (2.11) with rpmgs script.
- Updated license tag.

* Mon Dec 09 2019 Leontiy Volodin <lvol@altlinux.org> 2.10-alt1
- New version (2.10) with rpmgs script.

* Thu Aug 22 2019 Leontiy Volodin <lvol@altlinux.org> 2.9-alt1
- Initial build for ALT Sisyphus (thanks fedora for this spec).
