%define _unpackaged_files_terminate_build 1

Name: mailman3
Version: 3.2.2
Release: alt3

Summary: Managing electronic mail discussion and e-newsletter lists.
License: GPLv3
Group: Development/Python3
Url: http://www.list.org/
BuildArch: noarch

Source0: %name-%version.tar
Source1: %name.cfg
Source2: %name-tmpfiles.conf
Source3: %name.service
Source4: %name.logrotate
Source5: %name-digests.service
Source6: %name-digests.timer

Patch0: %name-fix-import.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
BuildPreReq: python3-module-setuptools
BuildRequires: python3-module-aiosmtpd
BuildRequires: python3-module-alembic
BuildRequires: python3-module-atpublic
BuildRequires: python3-module-click
BuildRequires: python3-module-dns >= 1.14.0
BuildRequires: python3-module-flufl.bounce
BuildRequires: python3-module-flufl.i18n
BuildRequires: python3-module-flufl.lock
BuildRequires: python3-module-lazr.config
BuildRequires: python3-module-passlib
BuildRequires: python3-module-requests
BuildRequires: python3-module-SQLAlchemy
BuildRequires: python3-module-zope.component
BuildRequires: python3-module-zope.configuration
BuildRequires: python3-module-zope.event
BuildRequires: python3-module-zope.interface

Requires: python3-module-%name = %EVR


%description
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later. The name of
this software is spelled 'Mailman' with a leading capital 'M' but with a lower
case second 'm'. Any other spelling is incorrect.

%package -n python3-module-%name
Summary: Managing electronic mail discussion and e-newsletter lists.
Group: Development/Python3
BuildArch: noarch
%add_python3_req_skip flufl lazr

Requires: python3-module-alembic
Requires: python3-module-atpublic
Requires: python3-module-editor
Requires: python3-module-aiosmtpd
Requires: python3-module-alembic
Requires: python3-module-atpublic
Requires: python3-module-click
Requires: python3-module-dns >= 1.14.0
Requires: python3-module-falcon >= 1.0.0
Requires: python3-module-flufl.bounce
Requires: python3-module-flufl.i18n >= 2.0.1
Requires: python3-module-flufl.lock >= 3.1
Requires: python3-module-passlib >= 1.6.0
Requires: python3-module-SQLAlchemy >= 1.0.9
Requires: python3-module-requests

%py3_requires lazr.config zope.interface requests zope.hookable
%py3_requires zope.component zope.configuration zope.event
%py3_requires zope.deprecation zope.deferredimport

%description -n python3-module-%name
This is GNU Mailman, a mailing list management system distributed under the
terms of the GNU General Public License (GPL) version 3 or later. The name of
this software is spelled 'Mailman' with a leading capital 'M' but with a lower
case second 'm'. Any other spelling is incorrect.

This package contain python modules for %name.

%prep
%setup

%patch0 -p1

%build
%python3_build

%install
%python3_install

mkdir -p %buildroot%_libexecdir/%name
mv %buildroot%_bindir/* %buildroot%_libexecdir/%name/

cat > %buildroot%_bindir/%name << EOF
#!/bin/sh
if [ "\$(whoami)" != "mailman" ]; then
    echo "This command must be run under mailman user."
    exit 1
fi
%_libexecdir/%name/mailman \$@
EOF
chmod +x %buildroot%_bindir/%name

install -D -m 0640 %SOURCE1 %buildroot%_sysconfdir/mailman.cfg
install -D -m 0644 %SOURCE2 %buildroot%_tmpfilesdir/%name.conf
install -D -m 0644 %SOURCE3 %buildroot%_unitdir/%name.service

mkdir -p %buildroot%_sysconfdir/logrotate.d/
cat %name.logrotate > %buildroot%_sysconfdir/logrotate.d/%name

install -D -m 0644 %SOURCE5 %buildroot%_unitdir/%name-digests.service
install -D -m 0644 %SOURCE6 %buildroot%_unitdir/%name-digests.timer

mkdir -p %buildroot%_logdir/%name
mkdir -p %buildroot%_localstatedir/%name
mkdir -p %buildroot%_spooldir/%name
mkdir -p %buildroot%_runtimedir/%name %buildroot%_lockdir/%name
mkdir -p %buildroot%_sysconfdir/%name.d
mkdir -p %buildroot%_localstatedir/%name/data

%pre
getent group mailman >/dev/null || groupadd -r mailman ||:
getent passwd mailman >/dev/null || \
    useradd -r -u mailman -g mailman -d %_localstatedir/%name -s /sbin/nologin \
        -c "Mailman, the mailing-list manager" mailman >/dev/null

%post
%post_service %name
/bin/systemctl reload-or-try-restart %name-digests.timer ||:

%preun
%preun_service %name
/bin/systemctl disable %name-digests.timer ||:
/bin/systemctl stop %name-digests.timer ||:

%files
%doc README.* COPYING
%_bindir/%name
%_libexecdir/%name
%config(noreplace) %attr(640,mailman,mailman) %_sysconfdir/mailman.cfg
%config(noreplace) %_sysconfdir/logrotate.d/%name
%_unitdir/*.service
%_unitdir/*.timer
%_tmpfilesdir/%name.conf
%dir %_sysconfdir/%name.d
%dir %attr(0755,mailman,mailman) %_localstatedir/%name
%dir %attr(2775,mailman,mail)   %_localstatedir/%name/data
%dir %attr(0755,mailman,mailman) %_spooldir/%name
%dir %attr(0755,mailman,mailman) %_logdir/%name
%dir %attr(0755,mailman,mailman) %_runtimedir/%name
%dir %attr(0755,mailman,mailman) %_lockdir/%name

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Thu Apr 20 2023 Anton Vyatkin <toni@altlinux.org> 3.2.2-alt3
- Fix Requires

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.2-alt2
- fix import module 'importlib_resources'

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.2-alt1
- Version updated to 3.2.2

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.0-alt5
- fix path to mailman3.conf

* Tue Mar 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.0-alt4
- Lockdir path fixed

* Tue Mar 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.0-alt3
- Requires fixed

* Fri Feb 22 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.0-alt2
- Broken reqs for p8 branch fixed

* Thu Feb 07 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.2.0-alt1
- Initial build for Sisyphus
