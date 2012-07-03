%define Name iSCSI
%define bname iscsi
Name: open-%bname
%define module_name %name
Version: 2.0.871
License: %gpl2plus
Release: alt5
Summary: Utils to operate with %Name
Group: System/Kernel and hardware
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
URL: http://%name.org
Source: http://www.%name.org/bits/%name-%version.tar
Source1: iscsi-gen-initiatorname.sh
Patch: %name-%version-%release.patch
Conflicts: linux-iscsi

# Automatically added by buildreq on Fri Jun 08 2007 (-bi)
BuildRequires: glibc-devel-static
BuildRequires: rpm-build-licenses

%description
%Name is an internet storage protocol, originally developed by CISCO
systems.
This is a Linux implementation of user-space utils to access %bname
storages.


%package -n kernel-source-%module_name
Summary: Linux %module_name modules sources
Group: Development/Kernel

%description -n kernel-source-%module_name
This package contains sources for %module_name kernel modules.

%prep
%setup -n %name-%version
%patch -p1

%build
for d in utils/fwparam_ibft utils usr; do
    %make_build -C $d
done

install -d -m 0755 kernel-source-%module_name-%version/include
install -m 0644 include/* kernel-source-%module_name-%version/include/
install -m 0644 kernel/* kernel-source-%module_name-%version/

%install
%make_install DESTDIR=%buildroot initddir=%_initdir \
    install_programs install_initd_alt install_etc install_doc

install -m 0755 %SOURCE1 %buildroot/sbin/iscsi-gen-initiatorname

install -d -m 0755 %buildroot%_usrsrc/kernel/sources
tar -c kernel-source-%module_name-%version | bzip2 --best --stdout > \
    %buildroot%_usrsrc/kernel/sources/kernel-source-%module_name-%version.tar.bz2

%post
if [ ! -f /etc/iscsi/initiatorname.iscsi ] ; then
    /sbin/iscsi-gen-initiatorname
fi
%post_service %name

%preun
%preun_service %name


%files
%doc README THANKS etc/iface.example
%dir %_sysconfdir/%bname
%config(noreplace) %_sysconfdir/%bname/%{bname}d.conf
%_initdir/*
/sbin/*
%_man8dir/*

%files -n kernel-source-%module_name
%_usrsrc/kernel/sources/*.tar.bz2

%changelog
* Wed Jan  4 2012 Terechkov Evgenii <evg@altlinux.org> 2.0.871-alt5
- Fixes fot ALT#23676 (thanks to naf@) and ALT#26775

* Thu Apr 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.871-alt4
- reapir build

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.871-alt3
- Fix path to LOCKFILE

* Wed Aug 26 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.871-alt2
- Add "mount -a -O _netdev" during start
- Add {pre,post}_service %name
- Add patch from ubuntu (https://launchpad/bugs/408915)

* Thu Aug 06 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.871-alt1
- 2.0-871

* Tue May 05 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0.870.3-alt3
- Add %_sysconfdir/%bname to spec

* Sun May 03 2009 Slava Dubrovskiy <dubrsl@altlinux.ru> 2.0.870.3-alt2
- Add iscsi-gen-initiatorname.sh
- Update init script

* Sat Feb 28 2009 Led <led@altlinux.ru> 2.0.870.3-alt1
- 2.0-870.3

* Sun Feb 15 2009 Led <led@altlinux.ru> 2.0.870.2-alt1
- 2.0-870.2

* Wed May 14 2008 Led <led@altlinux.ru> 2.0.869.2-alt0.1
- 2.0-869-2
- fixed License

* Tue May 06 2008 Led <led@altlinux.ru> 2.0.869-alt0.1
- 2.0-869
- added kernel-source-%module_name subpackage

* Tue Nov 20 2007 Led <led@altlinux.ru> 2.0.865.15-alt0.1
- 2.0-865.15
- added URL
- added ChangeLog to docs

* Tue Oct 02 2007 Led <led@altlinux.ru> 2.0.865.12-alt0.1
- 2.0-865.12

* Thu Aug 16 2007 Led <led@altlinux.ru> 2.0.865.10-alt0.1
- 2.0-865.10:
  + fixes some security issues, which can be exploited by malicious,
    local users to cause a DoS (Denial of Service) (CVE-2007-3099,
    CVE-2007-3099).
  + added utils: iscsi-iname, fwparam_ibft
- fixed License

* Fri Jun 08 2007 Led <led@altlinux.ru> 2.0.754-alt0.1
- 2.0-754
- cleaned up spec
- fixed License
- cleaned up %name-alt-init.patch
- cleaned up BuildRequires
- added docs

* Wed Dec 20 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 2.0.730-alt2
- Some fixes

* Wed Dec 20 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 2.0.730-alt1
- Some minor fixes

* Mon Nov 27 2006 Yury A. Romanov (damned) <damned@altlinux.ru> 2.0.730-alt0
- Initial build for ALTLinux
