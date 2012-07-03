Summary: Samba server configuration tool
Name: system-config-samba
Version: 1.2.96
Release: alt1
Url: http://fedorahosted.org/%name
License: GPLv2+
Group: System/Configuration/Networking

BuildArch: noarch
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar
BuildRequires: python-devel intltool desktop-file-utils

Requires: samba consolehelper

%py_requires libglade

%description
system-config-samba is a graphical user interface for creating,
modifying, and deleting samba shares.

%prep
%setup -q

%build
%make_build

%install

make DESTDIR=%buildroot \
%if_with polkit1
    POLKIT0_SUPPORTED=0 \
%else
    POLKIT1_SUPPORTED=0 \
%endif
    install

desktop-file-install --vendor system --delete-original       \
  --dir %buildroot%_desktopdir %buildroot%_desktopdir/system-config-samba.desktop

mkdir -p %buildroot/%_sbindir/
mv %buildroot/%_bindir/%name %buildroot/%_sbindir/

ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
install -d %buildroot%_sysconfdir/pam.d/

cat>%buildroot%_sysconfdir/pam.d/%name<<EOF
#%PAM-1.0
auth    sufficient      pam_rootok.so
auth    required        pam_stack.so service=system-auth
account required        pam_permit.so
password        required        pam_deny.so
session optional        pam_xauth.so
EOF

install -d %buildroot%_sysconfdir/security/console.apps/
cat>%buildroot%_sysconfdir/security/console.apps/%name<<EOF
USER=root
PROGRAM=%_sbindir/%name
SESSION=true
FALLBACK=true
EOF


%find_lang %name

%files -f %name.lang
%doc COPYING
%config(noreplace) %_sysconfdir/pam.d/*
%config(noreplace) %_sysconfdir/security/console.apps/*
%_bindir/system-config-samba
%_sbindir/system-config-samba
%_datadir/system-config-samba
%_desktopdir/system-config-samba.desktop
%_iconsdir/hicolor/*/apps/system-config-samba.png
%_sysconfdir/dbus-1/system.d/*.conf
%_datadir/dbus-1/system-services/*.service
%if_with polkit1
%_datadir/polkit-1/actions/org.fedoraproject.config.samba.policy
%else
%_datadir/PolicyKit/policy/org.fedoraproject.config.samba.policy
%endif
%python_sitelibdir/scsamba
%python_sitelibdir/scsamba-%version-py%__python_version.egg-info
%python_sitelibdir/scsamba.dbus-%version-py%__python_version.egg-info

%changelog
* Tue Feb 07 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.96-alt1
- 1.2.96

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.93-alt1.1
- Rebuild with Python-2.7

* Fri Sep 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.93-alt1
- 1.2.93

* Fri Aug 19 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.92-alt1
- 1.2.92

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.91-alt3
- add alterator category (ALT #25419)

* Fri Apr 08 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.91-alt2
- use consolehelper

* Sun Apr 03 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.91-alt1
- Initial from Fedora
