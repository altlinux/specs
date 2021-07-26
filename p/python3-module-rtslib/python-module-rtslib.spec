Name:           python3-module-rtslib
Version:        2.1.fb69
Release:        alt3

Summary:        API for Linux kernel LIO SCSI target

License:        Apache-2.0
Group:          Development/Python3
URL:            https://github.com/open-iscsi/rtslib-fb

Source:         %name-%version.tar

BuildArch:      noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-six
BuildRequires: python3-module-pyudev
BuildRequires: python3-module-kmod

Requires: python3-module-kmod

%description
API for generic Linux SCSI kernel target. Includes the 'target'
service and targetctl tool for restoring configuration.

%package -n target-restore
Summary:        Systemd service for targetcli/rtslib
Group:          System/Servers

%description -n target-restore
Systemd service to restore the LIO kernel target settings
on system restart.

%prep
%setup

sed 's|/var/target|/var/lib/target|' -i rtslib/root.py


sed -i "s/__version__ = .*/__version__ = '%version'/g" \
	rtslib/__init__.py

%build
gzip --stdout doc/targetctl.8 > doc/targetctl.8.gz
gzip --stdout doc/saveconfig.json.5 > doc/saveconfig.json.5.gz

%python3_build_debug

%install
%python3_install
mkdir -p %buildroot{%_man8dir,%_man5dir,%_unitdir,%_sysconfdir/target/backup,%_localstatedir/target/{pr,alua}}

install -m 644 systemd/target.service %buildroot%_unitdir/target.service
install -m 644 doc/targetctl.8.gz %buildroot%_man8dir/
install -m 644 doc/saveconfig.json.5.gz %buildroot%_man5dir/

%post -n target-restore
%post_service target

%preun -n target-restore
%preun_service target

%files
%doc COPYING README.md doc/getting_started.md
%python3_sitelibdir/*

%files -n target-restore
%_bindir/targetctl
%_unitdir/target.service
%dir %_sysconfdir/target
%dir %_sysconfdir/target/backup
%dir %_localstatedir/target
%dir %_localstatedir/target/pr
%dir %_localstatedir/target/alua
%_man8dir/targetctl.8.*
%_man5dir/saveconfig.json.5.*

%changelog
* Mon Jul 26 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.fb69-alt3
- Rename package, spec cleanup.

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.fb69-alt2
- build python3 only
- add def_without doc to disable epydoc

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 2.1.fb69-alt1
- 2.1.fb69
- add target-restore package

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 2.1.fb48-alt2.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.fb48-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 31 2016 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb48-alt2
- Man pages packaging fixed

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb48-alt1
- First build for ALT (based on Fedora 2.1.fb48-1.fc21.src)

