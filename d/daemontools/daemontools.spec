Name: daemontools
Version: 0.76
Release: alt12
Summary: Daemontools by DJB
License: Public domain
Group: System/Servers
Url: http://cr.yp.to/

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar
Source1: %name.rpm.macro

Patch: %name-%version.command.patch
Patch1: %name.errno.patch
Patch2: %name.check.setgroup.patch
Patch3: %name.warnings.patch

Requires(pre): startup
Requires(post): daemontools-common = %version-%release

%description
Daemontools by DJB

%package common
Group: System/Base
Summary: Daemontools and other packages shared files
Conflicts: %name < %version-%release
Requires: rpm-macros-%name = %version-%release
BuildArch: noarch

%description common
Daemontools and other packages shared files

%package -n rpm-macros-%name
Summary: Set of RPM macros for packaging %name-based applications
Group: Development/Other
# helps old apt to resolve file conflict at dist-upgrade (thanks to Stanislav Ievlev)
Conflicts: daemontools-common <= 0.76-alt7
BuildArch: noarch

%description -n rpm-macros-%name
Set of RPM macros for packaging %name-based applications for ALT Linux.
Install this package if you want to create RPM packages that use %name.

%prep
%setup -c
%patch -p1
%patch1 -p1
%patch2 -p0
%patch3 -p1

%build
pushd admin/%name-%version
package/compile
popd

%install
mkdir -p %buildroot/bin %buildroot%_sysconfdir/daemontools.d

cp -a admin/%name-%version/command/* %buildroot/bin/
install -D -m644 %SOURCE1 %buildroot%_rpmmacrosdir/%name

%post
if grep svscanboot %_sysconfdir/inittab >/dev/null
then
  echo 'inittab contains an svscanboot line. I assume that svscan is already running.'
else
  echo 'Adding svscanboot to inittab...'
  rm -f %_sysconfdir/inittab'{new}'

  cat %_sysconfdir/inittab > %_sysconfdir/inittab'{new}'
  echo >>  %_sysconfdir/inittab'{new}'
  echo 'SV:123456:respawn:/bin/svscanboot' >> %_sysconfdir/inittab'{new}'
  mv -f %_sysconfdir/inittab'{new}' %_sysconfdir/inittab
  kill -HUP 1
  echo 'init should start svscan now.'
fi
if [ ! -f %_sysconfdir/daemontools.d/.gitignore ]; then
	echo supervise > %_sysconfdir/daemontools.d/.gitignore
fi

%files
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
/bin/tai64n
/bin/tai64nlocal

%files common
%dir %_sysconfdir/daemontools.d

%files -n rpm-macros-%name
%_rpmmacrosdir/%name

%changelog
* Mon Jan 31 2011 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt12
- add daemontools_log_install macro

* Wed Nov 17 2010 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt11
- make daemontools-common and rpm-macros-daemontools noarch

* Tue Oct 19 2010 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt10
- auto rebuild

* Fri Dec 12 2008 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt9
- fix build

* Tue Nov 18 2008 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt8
- Add .gitignore to %_sysconfdir/daemontools.d for etckeeper
- create rpm-macro-daemontools (patch from repocop)

* Fri Nov 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt7
- Add daemontools-common subpackage

* Fri Nov 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt6
- rebuild for Sisyphus (DJB change license to public domain)
- change path for spool from /service to %_sysconfdir/daemontools.d

* Fri Aug 25 2006 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt5
- add requires(pre) to startup for %_sysconfdir/inittab

* Fri Aug 18 2006 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt4
- spec cleanup

* Tue Sep 28 2004 Denis Smirnov <mithraen@altlinux.ru> 0.76-alt3
- first build for Sisyphus
