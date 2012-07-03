Summary: NFS server configuration tool
Name: system-config-nfs
Version: 1.3.51
Release: alt2.1
Url: http://fedorahosted.org/%name
License: GPLv2+
Group: System/Configuration/Networking

BuildArch: noarch
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar
BuildRequires: desktop-file-utils intltool python-dev

Requires: nfs-utils consolehelper

%py_requires libglade


%description
system-config-nfs is a graphical user interface for creating,
modifying, and deleting nfs shares.

%prep
%setup -q

%build
%make

%install
%makeinstall_std

desktop-file-install --vendor system --delete-original       \
  --dir %buildroot%_desktopdir             \
  --add-category X-Red-Hat-Base        \
  --add-category X-Red-Hat-ServerConfig        \
%buildroot%_desktopdir/system-config-nfs.desktop

%find_lang %name

mkdir -p %buildroot/%_sbindir/
mv %buildroot/%_bindir/%name %buildroot/%_sbindir/

ln -s %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
rm -f %buildroot%_sbindir/%name
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
PROGRAM=/usr/share/system-config-nfs/system-config-nfs.py
SESSION=true
FALLBACK=true
EOF

%files -f %name.lang
%doc COPYING
%_bindir/system-config-nfs
%_datadir/system-config-nfs
%_desktopdir/system-config-nfs.desktop
%_iconsdir/hicolor/48x48/apps/system-config-nfs.png
%config(noreplace) %_sysconfdir/security/console.apps/system-config-nfs
%config(noreplace) %_sysconfdir/pam.d/system-config-nfs

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.51-alt2.1
- Rebuild with Python-2.7

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.51-alt2
- add alterator category

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.51-alt1
- initial from Fedora
