%define _unpackaged_files_terminate_build 1

%add_python3_req_skip libsvsync.rsync
%add_python3_req_skip libsvsync.samdb

Name: svsync
Version: 1.2
Release: alt2

Summary: Sysvol rSync python script
License: GPLv3+
Group: Other
Url: https://altlinux.space/alt-domain/svsync
BuildArch: noarch

Provides: /usr/bin/%name
Provides: /usr/bin/%{name}d

BuildRequires: rpm-build-python3
Requires: python3-module-paramiko+gssapi
Requires: python3-module-%name

Source0: %name-%version.tar

%description
%name is the service for automatization sysvol rsync with systemd-timer.

%package -n python3-module-%name
Summary: The python3-module-%name package contains Python3 libraries with function for sysvol rsync.
Group: Development/Other
Requires: rsync

%description -n python3-module-%name
python3-module-%name contains all necessary functions for identify
upstream(PDC emulator or ISTG) and rsync sysvol from it.

%prep
%setup -q

%install
mkdir -p \
	%buildroot%python3_sitelibdir
cp -r %name \
	%buildroot%python3_sitelibdir

mkdir -p \
	%buildroot%_bindir/ \
	%buildroot%_sbindir/ \
	%buildroot%_cachedir/%name/creds

ln -s %python3_sitelibdir/%name/%name \
	%buildroot%_sbindir/%name

ln -s %python3_sitelibdir/%name/%{name}d \
	%buildroot%_sbindir/%{name}d

install -Dm0644 dist/%{name}d.service %buildroot%_unitdir/%{name}d.service
install -Dm0644 dist/%{name}d.timer %buildroot%_unitdir/%{name}d.timer
install -Dm0644 dist/environment %buildroot%_sysconfdir/sysconfig/%{name}d
install -Dm0644 completion/%name.sh %buildroot/%_datadir/bash-completion/completions/%name

%post
%post_systemd %{name}d.service %{name}d.timer

%preun
%preun_systemd %{name}d.service %{name}d.timer

%files
%_sbindir/%name
%_sbindir/%{name}d
%_datadir/bash-completion/completions/%name
%_unitdir/%{name}d.service
%_unitdir/%{name}d.timer
%python3_sitelibdir/%name/%{name}d
%python3_sitelibdir/%name/%name

%files -n python3-module-%name
%python3_sitelibdir/%name
%exclude %python3_sitelibdir/%name/%{name}*
%config(noreplace) %_sysconfdir/sysconfig/%{name}d
%dir %attr(0700, root, root) %_cachedir/%name/creds
%dir %attr(0700, root, root) %_cachedir/%name/

%changelog
* Fri Aug 08 2025 Korney Gedert <kiper@altlinux.org> 1.2-alt2
- chore: update url in .spec
- docs: fix inaccuracy in README.MD

* Tue Jul 29 2025 Korney Gedert <kiper@altlinux.org> 1.2-alt1
- docs: update README.MD
- chore: add upstream name to log
- fix: sysvol folder different names

* Wed Jul 23 2025 Korney Gedert <kiper@altlinux.org> 1.1-alt1
- fix: disable some checks due to Samba 4.21
- fix: samba uses global object for LoadParm
- fix: add paramiko with gssapi into requires
- fix: add creds folder to files
- fix: move cache and config to python3-module-svsync
- fix: add %post and %preun for service and timer
- fix: sbin path of svsyncd for service

* Mon Jun 30 2025 Korney Gedert <kiper@altlinux.org> 1.0-alt1
- Initial release.
