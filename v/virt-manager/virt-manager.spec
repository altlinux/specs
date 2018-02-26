%add_python_req_skip guestfs
%define _libexecdir /usr/libexec
%define qemu_user  _libvirt
%define preferred_distros "altlinux,fedora,rhel"
%define kvm_packages "qemu-kvm,qemu-system"
%define libvirt_packages "libvirt"
%define default_graphics "vnc"
%def_without tui

Name: virt-manager
Version: 0.9.1
Release: alt1
Summary: Virtual Machine Manager

Group: System/Configuration/Other
License: GPLv2+
Url: http://virt-manager.org/
BuildArch: noarch

# git://git.fedorahosted.org/python-virtinst.git
Source: %name-%version.tar

%add_python_req_skip sparkline virtManager
%add_python_compile_include %_datadir/%name

# ALT#15494
Requires: python-module-pygtk-libglade
Requires: python-module-virtinst >= 0.600.0
PreReq: GConf2

# Automatically added by buildreq on Thu Jul 02 2009
BuildRequires: libgtk+2-devel librarian python-module-pygtk-devel libGConf-devel
BuildPreReq: intltool gettext perl-Pod-Parser

%description
Virtual Machine Manager provides a graphical tool for administering
virtual machines for KVM, Xen, and QEmu. Start, stop, add or remove
virtual devices, connect to a graphical or serial console, and see
resource usage statistics for existing VMs on local or remote machines.
Uses libvirt as the backend management API.

%prep
%setup

%build
./autogen.sh
%configure \
	%{subst_with tui} \
	--with-qemu-user=%qemu_user \
	--with-libvirt-package-names=%libvirt_packages \
	--with-kvm-packages=%kvm_packages \
	--with-preferred-distros=%preferred_distros \
	--with-default-graphics=%default_graphics

%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%post
%gconf2_install %name

%preun
if [ $1 = 0 ]; then
%gconf2_uninstall %name
fi

%files -f %name.lang
%_sysconfdir/gconf/schemas/%name.schemas
%_bindir/*
%_libexecdir/%name-launch
%_datadir/%name
#%%_datadir/omf/%name
#%%_datadir/gnome/help/%name
%_desktopdir/%name.desktop
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/dbus-1/services/%name.service
%_man1dir/*
%doc AUTHORS ChangeLog NEWS README

%changelog
* Mon Apr 09 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Wed Nov 16 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt2.git.9d2119
- git snapshot

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.0-alt1.1
- Rebuild with Python-2.7

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Tue Mar 29 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.7-alt1
- 0.8.7

* Mon Feb 28 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt3.hg20110224
- snapshot 20110224

* Thu Feb 17 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt3.hg20110215
- snapshot 20110215

* Fri Feb 11 2011 Anton Protopopov <aspsk@altlinux.org> 0.8.6-alt2
- Don't always launch consoles for running domains (ALT #25073)

* Tue Jan 18 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.6-alt1
- 0.8.6

* Tue Jan 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1.hg20110107
- snapshot 20110107
- build as noarch

* Thu Dec 30 2010 Alexey Shabalin <shaba@altlinux.ru> 0.8.5-alt1.hg20101220
- snapshot 20101220 (with spice support)
- define _libexecdir as /usr/libexec (fix dbus service)

* Tue Dec 07 2010 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt3
- Add perl-Pod-Parser to build requires

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt2
- Merge with gears/

* Tue Dec 15 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.2-alt1
- Updated to 0.8.2.

* Wed Dec 09 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.1-alt1
- Updated to 0.8.1.

* Tue Dec 01 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt2
- Add Packager field

* Thu Oct 08 2009 Anton Protopopov <aspsk@altlinux.org> 0.8.0-alt1
- Updated to 0.8.0.

* Thu Jul 02 2009 Dmitry V. Levin <ldv@altlinux.org> 0.7.0-alt1
- Updated to 0.7.0.

* Mon Dec 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.6.0-alt1
- new version
- remove post scripts

* Tue Apr 29 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt2
- fix #15493, #15494

* Sun Apr 13 2008 Eugene Ostapets <eostapets@altlinux.ru> 0.5.4-alt1
- First build for ALTLinux

