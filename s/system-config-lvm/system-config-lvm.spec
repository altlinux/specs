Summary: A utility for graphically configuring Logical Volumes
Name: system-config-lvm
Version: 1.1.16
Release: alt1.1
Url: http://fedorahosted.org
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar
License: GPLv2
Group: System/Configuration/Other
BuildArch: noarch

BuildRequires: intltool desktop-file-utils glib2-devel 
%py_requires libglade

%description
system-config-lvm is a utility for graphically configuring Logical Volumes

%prep
%setup -q
%autoreconf

%build
%configure
%make_build

%install

%makeinstall_std

desktop-file-install --vendor system --delete-original		\
  --dir %buildroot%_desktopdir			\
  --remove-category Application					\
 --remove-category SystemSetup					\
  --remove-category X-Red-Hat-Base				\
  --add-category Settings					\
  --add-category System						\
%buildroot%_desktopdir/system-config-lvm.desktop

%find_lang %name

mkdir -p %buildroot/%_sbindir/

ln -sf %_libexecdir/consolehelper/helper %buildroot%_bindir/%name
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
PROGRAM=/usr/share/system-config-lvm/system-config-lvm.py
SESSION=true
FALLBACK=true
EOF

%files -f %name.lang

%doc COPYING
#%doc docs/ReleaseNotes
#%doc docs/html/*
%_sbindir/*
%_bindir/*
%_desktopdir/system-config-lvm.desktop
%_datadir/system-config-lvm
%config(noreplace) %_sysconfdir/pam.d/system-config-lvm
%config(noreplace) %_sysconfdir/security/console.apps/system-config-lvm

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.16-alt1.1
- Rebuild with Python-2.7

* Thu Aug 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.16-alt1
- 1.1.16

* Mon Apr 11 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.15-alt2
- add alterator category

* Mon Apr 04 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.15-alt1
- Initial from Fedora
