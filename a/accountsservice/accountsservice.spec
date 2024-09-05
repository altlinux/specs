%def_enable check
%define _localstatedir %_var
%define _libexecdir %_prefix/libexec

Name: accountsservice
Version: 23.13.9
Release: alt5
Summary: D-Bus interfaces for querying and manipulating user account information

Group: System/Base
License: GPLv3+
Url: https://www.freedesktop.org/wiki/Software/AccountsService/
Vcs: https://gitlab.freedesktop.org/accountsservice/accountsservice.git

Source: %name-%version.tar
Patch1: %name-%version.patch

BuildRequires: meson >= 0.63.0
BuildRequires: gtk-doc
BuildRequires: pkgconfig(gio-2.0) >= 2.63.5
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(glib-2.0) >= 2.63.5
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: gobject-introspection-devel
BuildRequires: vala-tools
BuildRequires: libsystemd-devel >= 186 systemd-devel
# for test
%if_enabled check
BuildRequires: python3-module-pygobject3 python3-module-dbusmock
BuildRequires: /proc
%endif

Requires: polkit
Requires: shadow-utils
Requires: lib%name = %version-%release

%package -n lib%name
Summary: Client-side library to talk to accountservice
Group: System/Libraries

%description -n lib%name
The libaccountsservice package contains a library that can
be used by applications that want to interact with the accountsservice
daemon.

%package -n lib%name-devel
Summary: Development files for accountsservice
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
The libaccountsservice-devel package contains headers and other
files needed to build applications that use accountsservice.

%description
The accountsservice project provides a set of D-Bus interfaces for
querying and manipulating user account information and an implementation
of these interfaces, based on the useradd, usermod and userdel commands.

%package -n lib%name-gir
Summary: GObject introspection data for the accountsservice library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the accountsservice library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the accountsservice library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %version-%release lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the accountsservice library

%prep
%setup
%patch1 -p1

%build
%meson \
    -Dadmin_group=wheel \
    -Dextra_admin_groups="adm,netadmin" \
    -Ddefault_user_groups="audio,video,camera,scanner,cdrom,cdwriter,fuse,users,usershares,uucp,xgrp" \
    -Dsystemdsystemunitdir=%_unitdir
%meson_build

%install
%meson_install
# Install empty directory for interfaces
mkdir -p %buildroot%_datadir/%name/interfaces
%find_lang accounts-service

%check
%meson_test

%files -f accounts-service.lang
%doc COPYING README.md AUTHORS
%_libexecdir/accounts-daemon
%_datadir/dbus-1/system.d/org.freedesktop.Accounts.conf
%_datadir/dbus-1/system-services/org.freedesktop.Accounts.service
%_datadir/polkit-1/actions/org.freedesktop.accounts.policy
%dir %_localstatedir/lib/AccountsService/
%attr(700,root,root) %dir %_localstatedir/lib/AccountsService/users
%attr(775,root,root) %dir %_localstatedir/lib/AccountsService/icons
%_datadir/%name
%_unitdir/accounts-daemon.service

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/dbus-1/interfaces/*.xml
%_datadir/vala/vapi/%name.deps
%_datadir/vala/vapi/%name.vapi

%files -n lib%name-gir-devel
%_girdir/*.gir

%changelog
* Wed Sep 04 2024 Evgeny Sinelnikov <sin@altlinux.org> 23.13.9-alt5
- Fixed problem with local users definition (difference with previous
  release - fixed path to /etc/tcb/ is removed, which allows to work
  with nsswitch.conf) (thx Maria Alexeeva) (ALT#47499).

* Wed Aug 07 2024 Maria Alexeeva <alxvmr@altlinux.org> 23.13.9-alt4
- Fixed a problem with defining local users in Gnome.
- Reading /etc/shadow changed to reading /etc/tcb/
- Fixed tests for working with /etc/tcb/

* Mon Jun 24 2024 Alexey Shabalin <shaba@altlinux.org> 23.13.9-alt3
- Sync with upstream main branch.
- Add reuires dbus.service to accounts-daemon.service (ALT#50663).

* Wed Feb 21 2024 Alexey Shabalin <shaba@altlinux.org> 23.13.9-alt2
- Sync with upstream main branch
- Fixed show users list (ALT#48825).
- Fix Url tag (ALT#49452)

* Wed Jul 05 2023 Alexey Shabalin <shaba@altlinux.org> 23.13.9-alt1
- 23.13.9
- set minimum_uid=1000
- add extra_admin_groups="adm,netadmin"
- add patch for default_user_groups="audio,video,camera,scanner,cdrom,cdwriter,fuse,users,usershares,uucp,xgrp"

* Thu Mar 23 2023 Alexey Shabalin <shaba@altlinux.org> 23.11.69-alt1
- 23.11.69

* Mon Apr 04 2022 Alexey Shabalin <shaba@altlinux.org> 22.08.8-alt1
- 22.08.8

* Sat Jul 20 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.55-alt1
- 0.6.55

* Fri Mar 22 2019 Alexey Shabalin <shaba@altlinux.org> 0.6.54-alt2
- upstream snapshot 3179baffbb6b521c97b470156d7deb364890bad6

* Mon Oct 01 2018 Alexey Shabalin <shaba@altlinux.org> 0.6.54-alt1
- 0.6.54

* Tue Aug 14 2018 Fr. Br. George <george@altlinux.ru> 0.6.50-alt2
- Ignore ALT-specific empty /etc/shadow (closes: #35210)

* Fri Jul 27 2018 Alexey Shabalin <shaba@altlinux.org> 0.6.50-alt1
- 0.6.50

* Fri May 18 2018 Alexey Shabalin <shaba@altlinux.ru> 0.6.49-alt1
- 0.6.49

* Sat Aug 05 2017 Alexey Shabalin <shaba@altlinux.ru> 0.6.45-alt1
- 0.6.45

* Mon Dec 26 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.43-alt1
- 0.6.43

* Tue Jun 14 2016 Alexey Shabalin <shaba@altlinux.ru> 0.6.42-alt1
- 0.6.42

* Tue Jan 27 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.40-alt1
- 0.6.40

* Thu Oct 30 2014 Alexey Shabalin <shaba@altlinux.ru> 0.6.39-alt1
- 0.6.39

* Fri Oct 03 2014 Alexey Shabalin <shaba@altlinux.ru> 0.6.38-alt1
- 0.6.38

* Fri Apr 25 2014 Alexey Shabalin <shaba@altlinux.ru> 0.6.37-alt1
- 0.6.37

* Wed Jul 10 2013 Alexey Shabalin <shaba@altlinux.ru> 0.6.34-alt1
- 0.6.34
- drop patches from github.com/mmonaco/accountsservice

* Thu Jan 31 2013 Alexey Shabalin <shaba@altlinux.ru> 0.6.30-alt2
- merge with github.com/mmonaco/accountsservice/exclude-v3 for
  add config with excluded users

* Mon Jan 28 2013 Alexey Shabalin <shaba@altlinux.ru> 0.6.30-alt1
- 0.6.30

* Wed Nov 28 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.29-alt2
- upstream snapshot 4d5166d1833e42d81b854374aa6e73f83a67a70e
- fixed a crash on 32bit systems

* Thu Nov 22 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.29-alt1
- 0.6.29

* Tue Nov 13 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.26-alt1
- 0.6.26

* Wed Sep 26 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.25-alt1
- 0.6.25

* Fri Jul 20 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.22-alt1
- 0.6.22
- Correct CVE-2012-2737, local file disclosure.

* Mon May 21 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.21-alt1
- 0.6.21

* Fri Apr 06 2012 Alexey Shabalin <shaba@altlinux.ru> 0.6.17-alt1
- 0.6.17
- build with libsystemd-login and libsystemd-daemon

* Fri Oct 21 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.15-alt1
- 0.6.15

* Wed Sep 14 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.14-alt1
- 0.6.14

* Wed Aug 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.13-alt1
- 0.6.13

* Tue May 24 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.12-alt1
- pre 0.6.13

* Wed May 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.10-alt1
- 0.6.10

* Fri Apr 08 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.8-alt1
- 0.6.8
- use global %%systemd_unitdir macros

* Thu Mar 10 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.5-alt1
- 0.6.5

* Fri Feb 04 2011 Alexey Shabalin <shaba@altlinux.ru> 0.6.3-alt1
- initial build for ALT Linux Sisyphus
