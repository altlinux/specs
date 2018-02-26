Name: system-config-audit
Epoch: 1
Version: 0.4.20
Release: alt1

Summary: Utility for editing audit configuration
License: %gpl2only
Group: Monitoring

URL: https://fedorahosted.org/system-config-audit/
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: python-devel python-module-audit desktop-file-utils libaudit-devel intltool

Requires: python-module-pygtk-libglade

%description
This package provides a GUI that allows the user to configure the Linux
audit subsystem.

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build 

%install
%make_install  DESTDIR=%buildroot install-fedora

%find_lang %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%name.desktop
%_datadir/%name
%python_sitelibdir_noarch/%name
%_libexecdir/%name-server
%_datadir/applications/%name.desktop
%_libexecdir/%name-server-real
%config(noreplace) %_sysconfdir/pam.d/%name-server
%config(noreplace) %_sysconfdir/security/console.apps/%name-server

%changelog
* Thu Apr 12 2012 Mikhail Efremov <sem@altlinux.org> 1:0.4.20-alt1
- server.c: Include missing header.
- Fix for automake 1.11.2.
- Updated to 0.4.20.

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:0.4.19-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Mikhail Efremov <sem@altlinux.org> 1:0.4.19-alt1
- Updated to 0.4.19.
- fix summary.

* Thu Jul 01 2010 Mikhail Efremov <sem@altlinux.org> 1:0.4.15-alt1
- Separate from audit
