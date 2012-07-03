Name: iptables
Version: 1.4.14
Release: alt2

Summary: Tools for managing Linux kernel packet filtering capabilities
License: GPLv2+
Group: System/Kernel and hardware
Url: http://www.netfilter.org/projects/iptables/

# git://git.netfilter.org/iptables
# http://git.altlinux.org/people/ldv/packages/?p=iptables.git
Source: %name-%version-%release.tar

Requires: lib%name = %version-%release
# Backwards compatibility for libipq.
%define lib_suffix %nil
%{expand:%%define lib_suffix %(test %_lib != lib64 && echo %%nil || echo '()(64bit)')}
Provides: libipq.so.0.0%lib_suffix

%def_disable static

%description
Iptables is used to set up, maintain, and inspect the tables of IP
packet filter rules in the Linux kernel.  Several different tables may
be defined.  Each table contains a number of built-in chains and may
also contain user-defined chains.

Each chain is a list of rules which can match a set of packets.
Each rule specifies what to do with a packet that matches.  This is
called a `target', which may be a jump to a user-defined chain in
the same table.

%package ipv6
Summary: IPv6 support for iptables
Group: System/Kernel and hardware
Requires: %name = %version-%release
BuildArch: noarch

%description ipv6
Ip6tables is used to set up, maintain, and inspect the tables of IPv6
packet filter rules in the Linux kernel.  Several different tables may
be defined.  Each table contains a number of built-in chains and may
also contain user-defined chains.

Each chain is a list of rules which can match a set of packets.
Each rule specifies what to do with a packet that matches.  This is
called a `target', which may be a jump to a user-defined chain in
the same table.

%package -n lib%name
Summary: iptables dhared libraries
Group: Development/C
# lib%name was introduced since 1.4.13.
Conflicts: %name < 1.4.13

%description -n lib%name
Iptables is used to set up, maintain, and inspect the tables of IP
packet filter rules in the Linux kernel.

This package contains libip4tc, libip6tc, libxtables, libipq and libiptc
shared libraries.

%package -n lib%name-devel
Summary: iptables development files
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %name-devel < %version-%release

%description -n lib%name-devel
Iptables is used to set up, maintain, and inspect the tables of IP
packet filter rules in the Linux kernel.

This package contains development files required to build software that
operates with netfilter.

%package -n lib%name-devel-static
Summary: iptables static development files
Group: Development/C
Requires: lib%name-devel = %version-%release
Provides: %name-devel-static = %version-%release
Obsoletes: %name-devel-static < %version-%release

%description -n lib%name-devel-static
Iptables is used to set up, maintain, and inspect the tables of IP
packet filter rules in the Linux kernel.

This package contains static library required to build software that
operates with netfilter.

%prep
%setup -n %name-%version-%release

%build
%add_optflags -fno-strict-aliasing
%autoreconf
%configure \
	%{subst_enable static} \
	--enable-libipq \
	--sbindir=/sbin \
	--with-xtlibdir=/%_lib/iptables \
	#

%make_build V=1

%install
%makeinstall_std

# convert an absolute symlink into relative
ln -snf ../../sbin/xtables-multi %buildroot%_bindir/iptables-xml

mkdir -p %buildroot/%_lib
# Relocate some shared libraries from %_libdir/ to /%_lib/.
for f in %buildroot%_libdir/lib{ip?tc,xtables}*.so; do
	t=`objdump -p "$f" |awk '/SONAME/ {print $2}'`
	[ -n "$t" ]
	ln -snf ../../%_lib/"$t" "$f"
done
mv %buildroot%_libdir/lib{ip?tc,xtables}*.so.* %buildroot/%_lib/
ln -s libipq.so.0.0.0 %buildroot%_libdir/libipq.so.0.0

output_format=$(%__cc $CFLAGS $LDFLAGS -shared -xc /dev/null -o/dev/null -Wl,--verbose -v 2>&1 |
		sed -n -f output-format.sed)
cat >%buildroot%_libdir/libiptc.so <<EOF
/* GNU ld script */

/* Ensure this .so library will not be used by a link
   for a different format on a multi-architecture system.  */
   $output_format

   GROUP ( AS_NEEDED ( -lip4tc -lip6tc ) )
EOF

install -pDm644 iptables/iptables.xslt %buildroot%_datadir/%name/iptables.xslt

# Install ip*tables.h header files.
mkdir -p %buildroot%_includedir/iptables
install -pm644 include/ip*tables.h %buildroot%_includedir/
install -pm644 include/iptables/internal.h %buildroot%_includedir/iptables/

# Install startup scripts and associated config files.
install -pDm755 iptables.init %buildroot%_initdir/iptables
cp -p %buildroot%_initdir/ip{,6}tables
sed -i s/iptables/ip6tables/g %buildroot%_initdir/ip6tables

install -pDm600 iptables_params %buildroot%_sysconfdir/sysconfig/iptables_params
cp -p %buildroot%_sysconfdir/sysconfig/ip{,6}tables_params
sed -i s/iptables/ip6tables/g %buildroot%_sysconfdir/sysconfig/ip6tables_params

install -pDm600 iptables_data %buildroot%_sysconfdir/sysconfig/iptables
cp -p %buildroot%_sysconfdir/sysconfig/ip{,6}tables
sed -i s/iptables/ip6tables/g %buildroot%_sysconfdir/sysconfig/ip6tables

install -pDm600 iptables_modules %buildroot%_sysconfdir/sysconfig/iptables_modules
cp -p %buildroot%_sysconfdir/sysconfig/ip{,6}tables_modules
sed -i s/iptables/ip6tables/g %buildroot%_sysconfdir/sysconfig/ip6tables_modules

%set_verify_elf_method strict

%post
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add iptables
fi

%preun
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del iptables
fi

%post ipv6
if [ $1 -eq 1 ]; then
	/sbin/chkconfig --add ip6tables
fi

%preun ipv6
if [ $1 -eq 0 ]; then
	/sbin/chkconfig --del ip6tables
fi

%files
%config(noreplace) %_sysconfdir/sysconfig/iptables*
%doc INCOMPATIBILITIES
%config %_initdir/iptables
/sbin/*
%_bindir/*
%_man1dir/*
%_man8dir/*
/%_lib/iptables/
%_datadir/%name/
# hack around arepo: we have to package something harmless just to trigger
# arepoizer, to generate i586-iptables package required by several other
# i586-* packages.
%ifarch i586
/usr/lib/libiptc.so
%endif

%files ipv6
%config(noreplace) %_sysconfdir/sysconfig/ip6tables*
%config %_initdir/ip6tables

%files -n lib%name
/%_lib/lib*.so.*
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_pkgconfigdir/*.pc
%_man3dir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib*.a
%endif

%changelog
* Mon May 28 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.14-alt2
- libiptc.so: fix on %%_lib != lib64.

* Sun May 27 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.14-alt1
- Updated to v1.4.14.

* Fri May 25 2012 Dmitry V. Levin <ldv@altlinux.org> 1.4.13-alt1
- Updated to v1.4.13-6-gc022454 (closes: #26540, #27208).
- Moved shared libraries to libiptables subpackage.
- Renamed iptables-devel subpackage to libiptables-devel.
- Merged most of IPv6 support files to the main subpackage.
- Dropped libiptc.so.0, turned libiptc.so into a linker script.

* Fri Oct 29 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.10-alt1
- Updated to v1.4.10.

* Tue Aug 03 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.9-alt1
- Updated to v1.4.9.

* Fri May 21 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.8-alt1
- Updated to v1.4.8.

* Tue Mar 02 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.7-alt1
- Updated to v1.4.7.

* Wed Feb 17 2010 Dmitry V. Levin <ldv@altlinux.org> 1.4.6-alt1
- Updated to v1.4.6.
- Added NETFLOW target.

* Wed Sep 23 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.5-alt1
- Updated to v1.4.5.

* Wed Jul 01 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.4-alt1
- Updated to v1.4.4.

* Tue Jun 02 2009 Dmitry V. Levin <ldv@altlinux.org> 1.4.3.2-alt1
- Updated to v1.4.3.2-9-gc304d77.
- Fixed build for enabling "%%set_verify_elf_method strict".
- Imported manpage fixes from Debian 1.4.3.2-2 package.
- Disabled devel-static packaging by default.
- Packaged %_datadir/%name/iptables.xslt.

* Thu Nov 27 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt4
- Removed obsolete %%post_ldconfig/%%postun_ldconfig calls.
- Fixed build with glibc-2.9.

* Tue Aug 05 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt3
- Backported ipset support (by Igor Zubkov.  Closes: #16326).

* Tue May 13 2008 Dmitry V. Levin <ldv@altlinux.org> 1.4.0-alt2
- Fixed build to use glibc-kernheaders again.
- Fixed compilation warnings.

* Sun May 11 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- Updated to 1.4.0

* Fri Sep 21 2007 Dmitry V. Levin <ldv@altlinux.org> 1.3.7-alt2
- iptables.init: Unload iptables modules on stop (#12869).

* Sat Dec 09 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.7-alt1
- Updated to 1.3.7.
- Fixed IPT_LIB_DIR and IP6T_LIB_DIR.

* Sat Jul 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt4
- Build libipt_recent.so (closes #9622).

* Fri Mar 03 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt3
- Updated modprobe patch.

* Wed Mar 01 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt2
- Updated to svn snapshot 6466.

* Mon Feb 27 2006 Dmitry V. Levin <ldv@altlinux.org> 1.3.5-alt1
- Updated to 1.3.5.
- Reviewed patches, removed obsolete ones, reworked all the rest.
- Rewritten startup script and related stuff.

* Tue May 24 2005 Dmitry V. Levin <ldv@altlinux.org> 1.3.1-alt2
- Added multilib support (mouse, closes #6745).

* Fri Apr 29 2005 Anton D. Kachalov <mouse@altlinux.org> 1.3.1-alt1.1
- multilib support

* Tue Mar 16 2005 Alexey Voinov <voins@altlinux.ru> 1.3.1-alt1
- new version (1.3.1)
- makefile patch updated
- freebug patch is no longer needed
- modprobe patch updated
- iptcdefs patch added (they're idiots!!!)

* Fri Oct 29 2004 Alexey Voinov <voins@altlinux.ru> 1.2.11-alt3
- modprobe patch added (fixes CAN-2004-0986, alternative to upstream)
- zerocounters patch added

* Wed Sep 08 2004 Alexey Voinov <voins@altlinux.ru> 1.2.11-alt2
- freebug patch added (fix for #5055)

* Tue Aug 03 2004 Alexey Voinov <voins@altlinux.ru> 1.2.11-alt1
- new version (1.2.11)
- numeric patch removed
- ccld patch updated
- -n added to service iptables status.

* Thu May 13 2004 Alexey Voinov <voins@altlinux.ru> 1.2.9-alt6
- fixed requirements between subpackages

* Wed May 05 2004 Alexey Voinov <voins@altlinux.ru> 1.2.9-alt5
- replace all references to ld with gcc to prevent problems with
  new glibc. (s/$(LD)/$(CC)/g) [ccld patch]
- replace obsolete _init with __...__((constructor))s

* Tue Mar 23 2004 Alexey Voinov <voins@altlinux.ru> 1.2.9-alt4
- servname patch added. it allows service names as port numbers in
 --to-ports option [#1264]

* Mon Mar 22 2004 Alexey Voinov <voins@altlinux.ru> 1.2.9-alt3
- fixed done message when starting
- libip?tables.so is now explicitly linked with libdl and libiptc

* Fri Jan 30 2004 Alexey Voinov <voins@altlinux.ru> 1.2.9-alt2
- fixed initscript a little (it reports proper status on failure)
- possibiblity to filter iptables config added

* Tue Nov 11 2003 Alexey Voinov <voins@altlinux.ru> 1.2.9-alt1
- new version (1.2.9)

* Thu Aug 28 2003 Alexey Voinov <voins@altlinux.ru> 1.2.8-alt3
- logging patch disabled [it caused sigsegv]
- libiptables and libip6tables was made shared
- post/postun scripts added
- more spec clean up

* Mon Aug 25 2003 Alexey Voinov <voins@altlinux.ru> 1.2.8-alt2
- spec clean up
- devel and devel-static packages added
- deps on kernel removed
- all extenstion modules moved from /usr/lib to /lib

* Thu Aug 14 2003 Peter Novodvorsky <nidd@altlinux.com> 1.2.8-alt1
- added logging patch.
- 1.2.8

* Tue Nov 26 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.7a-alt1
- 1.2.7a
- Rebuilt in new environment
- Added package iptables-ipv6
- Some spec cleanup
- Completely upgraded initscript's
- Fixed provides

* Tue Apr 16 2002 Konstantin Volckov <goldhead@linux.ru.net> 1.2.6a-alt1
- 1.2.6a
- Applied patch-o-matic userspace patches
- Fixed numeric bug
- Rebuilt with new kernel

* Mon Mar 11 2002 Konstantin Volckov <goldhead@linux.ru.net> 1.2.5-alt2
- Rebuilt with new kernel
- Added missed modules
- Fixed detection of NETLINK module

* Thu Jan 24 2002 Konstantin Volckov <goldhead@linux.ru.net> 1.2.5-alt1
- 1.2.5

* Fri Nov 23 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.2.4-alt1
- 1.2.4
- Fixed iptables-restore

* Thu Oct 11 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.2.3-alt2
- Fixed iptables.init scripts

* Tue Sep 4 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.2.3-alt1
- New version 1.2.3

* Thu Jun 7 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.2.2 alt1
- New version 1.2.2

* Sun Mar 18 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.2.1 ipl1
- New version 1.2.1
- init script
- tools iptables-save | iptables-restore

* Fri Feb 23 2001 Konstantin Volckov <goldhead@linux.ru.net> 1.2-ipl1mdk
- First Build for RE

* Tue Jan 09 2001 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.2-1mdk
- new and shiny source.

* Sat Dec 16 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.1.2-2mdk
- really build it on the alpha with egcs.

* Sat Dec 16 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 1.1.2-1mdk
- shamelessly rip a rpm from Red Hat.
- update to 1.1.2.
- build on alpha as well.

* Thu Aug 17 2000 Bill Nottingham <notting@redhat.com>
- build everywhere

* Tue Jul 25 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 1.1.1

* Thu Jul 13 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Tue Jun 27 2000 Preston Brown <pbrown@redhat.com>
- move iptables to /sbin.
- excludearch alpha for now, not building there because of compiler bug(?)

* Fri Jun  9 2000 Bill Nottingham <notting@redhat.com>
- don't obsolete ipchains either
- update to 1.1.0

* Mon Jun  4 2000 Bill Nottingham <notting@redhat.com>
- remove explicit kernel requirement

* Tue May  2 2000 Bernhard Rosenkränzer <bero@redhat.com>
- initial package
