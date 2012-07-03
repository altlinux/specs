Name: powersave
Summary: General Powermanagement daemon supporting APM and ACPI and CPU frequency scaling
Version: 0.15.20
Release: alt3
License: GPL
Group: System/Kernel and hardware
Url: http://sourceforge.net/projects/powersave
Summary: General Powermanagement daemon supporting APM and ACPI and CPU frequency scaling
ExclusiveArch: %ix86 x86_64 ia64
Source0: %name-%version.tar.bz2
Source1: %name.init
Source2: cpufreq-detect.sh

Packager: Damir Shayhutdinov <damir@altlinux.ru>

Patch0: powersave-0.10.22-disable-videobios.patch
Patch1: powersave-0.10.15-disable-suspend.patch
Patch2: powersave-0.15.11-alt-fix-linkage.patch
Patch3: powersave-0.15.20-alt-fix-script-message.patch

# Automatically added by buildreq on Mon Apr 24 2006
BuildRequires: doxygen gcc-c++ libcpufreq-devel libdbus-glib-devel libhal-devel libsysfs-devel glibc-kernheaders pkg-config lynx

BuildPreReq:  fillup >= 1.42-alt4 liblazy-devel
PreReq:  fillup >= 1.42-alt4 hal >= 0.5.4-alt6 acpid
Requires: lib%name = %version-%release
Requires: pm-utils
Provides: %_libexecdir/powersave/scripts

%description
Powersave gives you control over the ACPI power buttons, three user
defined battery states (warning, low, critical) and supports proper
standby/suspend handling.

Additionally it could control the frequency of your processor if it
supports SpeedStep(Intel) or PowerNow(AMD) technology. This will
greatly reduce power consumption and heat production in your system.

Together with the kpowersave it should be the preferred power 
managing application.

%package -n lib%name
Summary: Shared library for controlling various ACPI parameters.
Group: System/Libraries

%description -n lib%name
C shared library which provides interface to control various ACPI parameters, 
such as CPU frequency, ACPI power buttons, standby/suspend etc.

%package -n lib%name-devel
Summary: Headers for developing programs that will use lib%name
License: GPL
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < 0.14.0-alt3
%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use lib%name.


%prep
%setup -q -n %name-%version
#patch0 -p1
#patch1 -p1
%patch2 -p1
%patch3 -p2

%__subst "s/\/var\/run\/hal\/haldaemon.pid/\/var\/run\/hal\.pid/" daemon/*.cpp

%build
sed -i -e 's/CVS-HEAD/%version/' configure.ac
subst 's,/var/adm/fillup-templates,%_fillupdir,' config_files/Makefile.am
autoreconf -fi
%configure CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions" \
             --enable-buildenv --libdir=%_libdir --mandir=%_mandir --enable-docs \
	     --with-kde-bindir=%_bindir --with-gnome-bindir=%_bindir

%make_build -e 'VERSION_NO="\"%version\""'

%install
# Version will be used for link to library: .so.%version, see below in %files
%make install -e DESTDIR=%buildroot POWERSAVE_LIB_VERSION=%version TRANSLATION_DIR="%_datadir/locale/"
# rc script
mkdir -p $RPM_BUILD_ROOT%_initdir
install -pm755 %SOURCE1 $RPM_BUILD_ROOT%_initdir/powersaved
install -pm755 %SOURCE2 $RPM_BUILD_ROOT%_sbindir/cpufreq-detect.sh

rm -f $RPM_BUILD_ROOT%_sbindir/rcpowersaved
sed -i 's@/bin/dbus-send@%_bindir/dbus-send@g' %buildroot%_libexecdir/powersave/{powersave-notify,scripts/helper_functions}

# Generate shell functions provides list.
(
	echo '# shell functions provides list'
	for f in $RPM_BUILD_ROOT%_libexecdir/powersave/scripts/{helper_functions,x_helper_functions}; do
		[ -x "$f" ] || continue
		sed -ne 's/^\([A-Za-z][A-Za-z_0-9]*\)[[:space:]]*()[[:space:]]*{$/\1/pg' "$f"
	done |LC_COLLATE=C sort -u
) >$RPM_BUILD_ROOT%_libexecdir/powersave/scripts/.provides.sh

mkdir -p $RPM_BUILD_ROOT%_rpmlibdir/
cat <<EOF >$RPM_BUILD_ROOT%_rpmlibdir/powersave-files.req.list
%_libexecdir/powersave/scripts	powersave
EOF

mkdir -p $RPM_BUILD_ROOT%_sysconfdir/powersave
touch $RPM_BUILD_ROOT%_sysconfdir/powersave/{battery,common,cpufreq,events,scheme_performance,scheme_powersave,thermal}

%find_lang power-management

%files -f power-management.lang
%doc docs/README* docs/powersave.html docs/powersave_manual.txt contrib
%_sbindir/*
%_bindir/*
%_libexecdir/powersave
%_mandir/*/*
%_initdir/powersaved
%_fillupdir/*
%_sysconfdir/dbus-1/system.d/powersave.conf
%_sysconfdir/acpi/*
%exclude %_defaultdocdir/powersave/scripts/restore_default_config
%exclude %_libexecdir/powersave/rcpowersaved
%_rpmlibdir/powersave-files.req.list
%dir %_sysconfdir/powersave
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/battery
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/common
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/cpufreq
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/events
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/scheme_performance
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/scheme_powersave
%verify(not md5 size mtime) %ghost %config(missingok,noreplace) %_sysconfdir/powersave/thermal

%files -n lib%name
%_libdir/libpowersave*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/libpowersave*.so
%_libdir/pkgconfig/*

%post
%fillup_config scheme_performance powersave
%fillup_config scheme_powersave powersave
%fillup_config events powersave
%fillup_config thermal powersave
%fillup_config battery powersave
%fillup_config cpufreq powersave
%fillup_config common powersave
%post_service powersaved

%preun
%preun_service powersaved

%changelog
* Sat Nov 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.15.20-alt3
- added some fixes by raorn@:
  + drop obsolete ldconfig calls
  + don't fillup non-existant configs (closes: ALT#17770)
  + package powersave-files.eq.list for third-party packaged scripts
  + Generate shell function provides list for scripts/*helper_functions.
  + Requires: pm-utils (closes: ALT#17855).
  + Mark configuration files created by fillup as %%ghost (closes: ALT#12901)
  + Fix segfault in script reply handler (closes: ALT#17861)

* Fri Oct 10 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.15.20-alt2
- add cpufreq-detect.sh script (silicium@)

* Sun Apr 06 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.15.20-alt1
- New upstream version

* Sat Oct 20 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.15.11-alt3
- New upstream version

* Fri Jan 19 2007 Damir Shayhutdinov <damir@altlinux.ru> 0.14.0-alt3
- Move libraries into separate subpackage (#10686)
- Fix initscript (raorn@, #10776)

* Thu Dec 28 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.14.0-alt2
- Rebuilt with new dbus

* Mon Dec 11 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.14.0-alt1
- NMU
- New version 

* Tue Jul 04 2006 Anton Farygin <rider@altlinux.ru> 0.12.20-alt1
- new version

* Fri Apr 21 2006 Anton Farygin <rider@altlinux.ru> 0.12.11-alt2
- pkg-config added

* Fri Apr 21 2006 Anton Farygin <rider@altlinux.ru> 0.12.11-alt1
- new version

* Thu Apr 06 2006 Anton Farygin <rider@altlinux.ru> 0.12.2-alt2
- fixed powersave configs location (#9372)

* Wed Mar 22 2006 Anton Farygin <rider@altlinux.ru> 0.12.2-alt1
- new version

* Tue Feb 21 2006 Anton Farygin <rider@altlinux.ru> 0.10.22-alt2
- new version

* Sun Oct 30 2005 Anton Farygin <rider@altlinux.ru> 0.10.15.1-alt2
- post-scripts fixed

* Wed Oct 26 2005 Anton Farygin <rider@altlinux.ru> 0.10.15.1-alt1
- new version
- fixed powersaved initscript

* Mon Oct 17 2005 Anton Farygin <rider@altlinux.ru> 0.10.15-alt1
- updated to new version
- disabled suspend2disk by default (swsuspend don't work with std-* kernels)

* Tue Jul 05 2005 Anton Farygin <rider@altlinux.ru> 0.9.25-alt2
- fixed negative values into polling select interval

* Tue Jul 05 2005 Anton Farygin <rider@altlinux.ru> 0.9.25-alt1
- first build for ALT Linux
