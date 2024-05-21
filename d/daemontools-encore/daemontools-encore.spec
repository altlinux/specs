#============================================================================
# Please do not edit!
# Created by specgen utility from files in specs/ subdir
#============================================================================
Name: daemontools-encore
Summary: Daemontools by DJB
Version: 1.10
Release: alt2
License: Public domain
Group: System/Servers
Url: http://untroubled.org/daemontools-encore/
Packager: Denis Smirnov <mithraen@altlinux.ru>
Source: %name-%version.tar
Source1: %name.rpm.macro
Source2: daemontools.service
Source3: %name.watch
Patch: %name-%version-%release.patch

%package -n daemontools
Summary: Daemontools and other packages shared files
Group: System/Base
Requires(pre): startup
Requires(post): daemontools-common = %version-%release
Requires(post): daemontools-utils = %version-%release

%description -n daemontools
Daemontools and other packages shared files

%package -n daemontools-common
Summary: Daemontools and other packages shared files
Group: System/Base
BuildArch: noarch

%description -n daemontools-common
Daemontools and other packages shared files


%package -n daemontools-utils
Summary: Daemontools programs and utilities
Group: System/Base

%description -n daemontools-utils
Daemontools programs and utilities


%package -n rpm-macros-daemontools
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
BuildArch: noarch
Conflicts: daemontools-common <= 0.76-alt7

%description -n rpm-macros-daemontools
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.


%description
daemontools-encore is a collection of tools for managing UNIX services.
It is derived from the public-domain release of daemontools by D. J.
Bernstein, which can be found at http://cr.yp.to/daemontools.html
daemontools-encore adds numerous enhancements above what daemontools
could do while maintaining backwards compatibility with daemontools.
See the CHANGES file for more details on what features have been added.


%prep
%setup
%patch -p1
sed -i -e '1s!^!%buildroot!' -e '1s!usr/local/!/!' conf-bin
sed -i -e '1s!^!%buildroot!' -e '1s!local!share!' conf-man
sed -i 's!env - /bin/sh rts.sh!#env - /bin/sh rts.sh!' Makefile
sed -i 's!diff -u rts.exp rts!#diff -u rts.exp rts!' Makefile
sed -i 's!PATH=/command:!PATH=!' svscanboot.sh
sed -i 's!/command/svc!/bin/svc!' svscanboot.sh
sed -i 's!/service!/etc/daemontools.d!g' svscanboot.sh

%build
%make_build

%install
mkdir -p %buildroot%_man8dir/
mkdir -p %buildroot/bin
make install DESTDIR=%buildroot
mkdir -p %buildroot/bin %buildroot%_sysconfdir/daemontools.d
install -D -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name
install -D -m644 %SOURCE2 %buildroot%_unitdir/daemontools.service

%post -n daemontools
if [ ! -f %_sysconfdir/inittab ]; then
  echo '/etc/inittab not exists. I assume that used systemd-based configuration'
elif grep svscanboot %_sysconfdir/inittab >/dev/null; then
  echo 'inittab contains an svscanboot line. I assume that svscan is already running.'
else
  echo 'Adding svscanboot to inittab...'
  rm -f %_sysconfdir/inittab'{new}'
  cat %_sysconfdir/inittab > %_sysconfdir/inittab'{new}'
  echo >> %_sysconfdir/inittab'{new}'
  echo 'SV:123456:respawn:/bin/svscanboot' >> %_sysconfdir/inittab'{new}'
  mv -f %_sysconfdir/inittab'{new}' %_sysconfdir/inittab
  kill -HUP 1
  echo 'init should start svscan now.'
fi
if [ ! -f %_sysconfdir/daemontools.d/.gitignore ]; then
	echo supervise > %_sysconfdir/daemontools.d/.gitignore
fi
systemctl=/bin/systemctl
if [ -f "$systemctl" ]; then
    $systemctl enable daemontools.service ||:
    $systemctl start daemontools.service ||:
fi

%files -n daemontools
%doc CHANGES* ChangeLog LICENSE README TODO
%_unitdir/daemontools.service

%files -n daemontools-common
%dir %_sysconfdir/daemontools.d

%files -n daemontools-utils
/bin/envdir
/bin/envuidgid
/bin/fghack
/bin/multilog
/bin/pgrphack
/bin/readproctitle
/bin/setlock
/bin/setuidgid
/bin/softlimit
/bin/supervise
/bin/svc
/bin/svok
/bin/svscan
/bin/svscanboot
/bin/svstat
/bin/svup
/bin/tai64n
/bin/tai64nlocal
%_man8dir/*

%files -n rpm-macros-daemontools
%_rpmmacrosdir/%name

%changelog
* Tue May 21 2024 Paul Wolneykien <manowar@altlinux.org> 1.10-alt2
- Move all programs and manual pages to the separate
  'daemontools-utils' package.
- Use %%_unitdir macro to install and package unit files.

* Tue Mar 14 2017 Denis Smirnov <mithraen@altlinux.ru> 1.10-alt1
- first build for Sisyphus

