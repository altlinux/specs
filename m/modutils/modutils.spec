%define mitver 3.1
%def_enable mit

Name: modutils
Version: 2.4.27
Release: alt11

Summary: Obsolete version of the kernel module utilities
License: GPL
Group: System/Kernel and hardware
Url: ftp://ftp.kernel.org/pub/linux/utils/kernel/modutils/v2.4
ExclusiveOS: Linux
Packager: Sergey Vlasov <vsu@altlinux.ru>

Source0: %url/modutils-%version.tar.bz2
Source1: modutils.macros
Source2: 00kernel.modutils
Source4: modules.conf

%if_enabled mit
Source5: http://www.kernel.org/pub/linux/utils/kernel/module-init-tools/module-init-tools-%mitver.tar.bz2
%endif

Patch1: modutils-2.4.2-rh-prepost.patch
Patch2: modutils-2.4.27-rh-owl-syms.patch
Patch3: modutils-2.4.27-rh-versions.patch
Patch4: modutils-2.4.27-rh-showconfig.patch

Patch11: modutils-2.4.27-alt-aliases.patch
Patch12: modutils-2.4.27-alt-insmod-GPL.patch
Patch13: modutils-2.4.27-alt-modprobe-bL.patch
Patch14: modutils-2.4.27-alt-depmod-prtdepend-cut_prefix.patch
Patch15: modutils-2.4.27-alt-allowable-licenses.patch
Patch16: modutils-2.4.26-alt-kernelversion.patch
Patch18: modutils-2.4.25-alt-include.patch
Patch19: modutils-2.4.27-alt-insmod-force_load.patch
Patch21: modutils-2.4.25-alt-glob-sort.patch
Patch22: modutils-2.4.27-deb-alt-fixes.patch
Patch23: modutils-2.4.27-alt-warning-stderr.patch
Patch24: modutils-2.4.27-owl-warnings.patch

Patch101: module-init-tools-3.1-alt-release-memory.patch
Patch102: module-init-tools-3.1-alt-depmod-check-aliases.patch
Patch103: module-init-tools-3.1-alt-modinfo-legacy.patch
Patch120: modutils-2.4.27-alt-mit-combined.patch
Patch121: modutils-2.4.27-alt-doc.patch
Patch122: modutils-2.4.27-alt-no-builtin.patch

PreReq: module-init-tools >= 3.3
Requires(post): module-init-tools-compat >= 3.3
Requires(post): chkconfig, coreutils, mktemp, grep
Obsoletes: modules
# due to statically linked utilities
Conflicts: mkinitrd < 1:2.8.0-alt1
# due to %_sysconfdir/modutils.d/pcmcia
Conflicts: pcmcia-cs < 0:3.2.4-alt1

# Automatically added by buildreq on Thu Jan 06 2005
BuildRequires: docbook-utils flex zlib-devel

%description
The modutils packages includes the module management programs.  Examples
of loaded and unloaded modules are device drivers and filesystems,
as well as some other things.

THIS PACKAGE IS OBSOLETE.
It is needed only during conversion of the old configuration syntax to the
new format used by the module-init-tools package.  After performing the
conversion and upgrading old packages with dependencies on modutils
this package can be removed from the system together with the
module-init-tools-compat package.

%prep
%if_enabled mit
%setup -q -a5
%else
%setup -q
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch18 -p1
%patch19 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1

%if_enabled mit
mv module-init-tools-%mitver module-init-tools
pushd module-init-tools
%patch101 -p1
%patch102 -p1
%patch103 -p1
popd
%patch120 -p1
%patch121 -p1
%patch122 -p1
%endif

find -type f -name \*.orig -delete
bzip2 -9k ChangeLog
chmod 755 insmod/kernelversion_*

%build
# gcc4.1 -fstrict-aliasing miscompiles obj/obj_reloc.c (#10768)
%add_optflags -fno-strict-aliasing
autoconf
%if_enabled mit
pushd module-init-tools
%configure --enable-zlib CPPFLAGS="-D_COMBINED_MODUTILS_=1"
%make_build combined 
pushd doc
docbook2man modinfo.sgml
popd
popd
%endif

%configure \
	--enable-zlib \
	--with-dynamic-zlib \
	--exec_prefix=/

%make_build dep all

%install
mkdir -p %buildroot/sbin
%makeinstall sbindir=%buildroot/sbin

install -pD -m644 %_sourcedir/modutils.macros %buildroot/lib/modutils/macros
install -pD -m644 %_sourcedir/modules.conf %buildroot%_sysconfdir/modules.conf
for f in %_sourcedir/00kernel.modutils; do
	n="${f%%.modutils}"
	install -pD -m644 "$f" "%buildroot%_sysconfdir/modutils.d/${n##*/}"
done

%if_enabled mit
install -pD -m644 module-init-tools/doc/modinfo.8 \
	%buildroot%_man8dir/modinfo.8
%endif

ln -snf modules.conf.5 %buildroot%_man5dir/conf.modules.5

# Obsoleted by man-pages-2.25.
rm -rf %buildroot%_man2dir

# Rename utilities and man pages to *.old for use with module-init-tools.
for f in depmod insmod lsmod modinfo modprobe rmmod; do
	mv %buildroot/sbin/$f %buildroot/sbin/$f.old
	mv %buildroot%_man8dir/$f.8 %buildroot%_man8dir/$f.old.8
done
for f in kallsyms ksyms lsmod.old modprobe.old rmmod.old; do
	ln -sf insmod.old %buildroot/sbin/$f
done

%post
[ $1 -ge 2 ] || exit 0

# Get rid of the old installations on upgrade.
if [ -x %_initdir/kerneld ]; then
	/sbin/chkconfig --del kerneld
fi
if [ -e %_sysconfdir/conf.modules -a ! -e %_sysconfdir/modules.conf ]; then
	%__mv -f %_sysconfdir/conf.modules %_sysconfdir/modules.conf
fi

/sbin/depmod -a ||:

# Convert modutils configuration to module-init-tools
new_config=%_sysconfdir/modprobe.d/local-autoconverted
[ -f $new_config ] || {
	echo "Converting modutils configuration to module-init-tools..."
	modules_conf=`mktemp -t modutils.XXXXXXXXXXX`
	/sbin/modprobe.old -c >"$modules_conf"
	for f in %_sysconfdir/modules.conf %_sysconfdir/modutils.d/*; do
		[ "${f%%.rpm*}" = "$f" -a "${f%%\~}" = "$f" ] || continue
		[ -r "$f" ] || continue
		[ "$f" = %_sysconfdir/modutils.d/00kernel ] && continue ||:
		name="${f#%_sysconfdir/modutils.d/}"
		if [ "$name" = "$f" ]; then
			out="$new_config"
		else
			out=%_sysconfdir/modprobe.d/"$name"
		fi
		if [ -f "$out" ]; then
			fgrep -qs "# Auto-converted-from: $f" "$out" || {
				cat >&2 <<EOF
warning: $out exists and is not autoconverted
warning: creating $out.rpmconv instead
EOF
				out="$out.rpmconv"
			}
		fi
		rm -f "$out"
		cat >"$out" <<EOF
# This configuration file was automatically converted from the old syntax
# used by the modutils package.
#
# Auto-converted-from: $f
# If you want to edit this file manually, remove the line above to prevent
# the conversion script from overwriting the file if you redo the conversion.

EOF
		/sbin/modprobe.old -c -C "$f" --no-builtin |
			/sbin/generate-modprobe.conf --stdin \
				--full-config="$modules_conf" >>"$out"
	done
	rm -f "$modules_conf"
	echo "... done"
}

# Convert hotplug blacklist to module-init-tools
old_blacklist=%_sysconfdir/hotplug/blacklist
new_blacklist=%_sysconfdir/modprobe.d/blacklist-autoconverted
if [ ! -f $new_blacklist ] && [ -n "$(ls -1 $old_blacklist $old_blacklist.d/* 2>/dev/null)" ]; then
	echo "Converting hotplug blacklist ($old_blacklist)..."

	cat >$new_blacklist <<EOF
# This configuration was automatically converted from the old syntax used
# by the hotplug package ($old_blacklist).

EOF
	for f in $old_blacklist $old_blacklist.d/*; do
		[ "${f%%.rpm*}" = "$f" -a "${f%%\~}" = "$f" ] || continue
		[ -r "$f" ] || continue
		egrep -sh -v '^(#|$|.*[^-0-9A-Za-z_])' "$f"
	done |
	tr '-' '_' |
	egrep -v '^(usb_uhci|usbcore|irusb|audio|usb_midi|dmfe)$' |
	sort -u |
	while read m; do
		/sbin/modprobe --set-version=2.6.0 -c |
			egrep -qs "^blacklist[[:space:]]+$m\$" && continue ||:
		echo "blacklist $m" >>$new_blacklist
	done

	echo "... done, created $new_blacklist"
fi

%files
%config(noreplace) %_sysconfdir/modules.conf
%config %_sysconfdir/modutils.d
/lib/modutils
/sbin/*
%_mandir/man?/*
%doc README CREDITS TODO ChangeLog.bz2 example/kallsyms.c include/kallsyms.h

%changelog
* Wed Apr 30 2008 Dmitry V. Levin <ldv@altlinux.org> 2.4.27-alt11
- Fixed %%setup invocation.

* Sun Apr 15 2007 Dmitry V. Levin <ldv@altlinux.org> 2.4.27-alt10
- Compiled with gcc 4.1 but disable optimization based on strict aliasing rules.
- Reduced macro abuse in specfile.

* Sun Feb 04 2007 Sergey Vlasov <vsu@altlinux.ru> 2.4.27-alt9
- Compile with gcc 3.4 (gcc 4.1 miscompiles obj/obj_reloc.c (#10768), which
  leads to depmod segfault when removing old kernel module packages).

* Tue Jan 30 2007 Sergey Vlasov <vsu@altlinux.ru> 2.4.27-alt8
- Note: This package is OBSOLETE now (2.4.x kernels are no longer supported,
  and modutils is replaced by module-init-tools for 2.6.x kernels).  It
  should be installed only to convert old configuration files to the new
  syntax used by module-init-tools.  After performing this conversion and
  upgrading other packages which had dependencies on modutils this package
  can and should be removed from the system together with the
  module-init-tools-compat package.

- Repackaged as a compatibility package for module-init-tools (renamed most
  programs to *.old to be called by module-init-tools implementation on old
  kernels; renamed man pages accordingly).
- Removed modules(5) manpage (moved to module-init-tools).
- Added alt-no-builtin patch:
  + modprobe: add --no-builtin option to disable all builtin rules (both
    compiled-in rules and /lib/modutils/macros)
- Always update module dependencies in %%post during upgrade.
- Added %%post script to convert modutils configuration to module-init-tools.
  This is handled here because module-init-tools should not depend on
  modutils, and old modutils is needed to do the conversion.

* Tue Oct 31 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4.27-alt7
- Fixed check for verbose flag in insmod, patch from Alexander Kanevskiy.
- Fixed two compiler warnings in deb-alt-fixes patch.

* Fri Mar 10 2006 Dmitry V. Levin <ldv@altlinux.org> 2.4.27-alt6
- Remove manual pages from 2nd section.

* Mon Nov 07 2005 Dmitry V. Levin <ldv@altlinux.org> 2.4.27-alt5
- Rediffed few patches (synced with Owl).
- Added modules(5) manpage from Debian.
- Applied fixes from Debian modutils-2.4.27.0-3 package.

* Tue Jun 21 2005 Sergey Vlasov <vsu@altlinux.ru> 2.4.27-alt4
- 00kernel.modutils: added "prune .versions" for new kernel-modules-nvidia.

* Sat Jan 15 2005 Sergey Vlasov <vsu@altlinux.ru> 2.4.27-alt3
- module-init-tools 3.1 release.
- Dropped module-init-tools-3.0-pre9-alt-format patch (fixed upstream).
- Updated alt-mit-combined patch:
  + modprobe (2.6.x): do not try to save nonexistent /proc/ksyms in
    /var/log/ksymoops (#4860).
  + modprobe, insmod (2.6.x): when insmod is invoked from modprobe, treat
    EEXIST error from init_module syscall as success (fixes failure when
    several modprobe processes are running in parallel - often happens with
    hotplug).
- Added alt-release-memory patch:
  + depmod (2.6.x): instead of trying to load all modules into memory, keep
    only some required tables from modules (decreases "depmod -a" memory
    consumption on 2.6.10 module tree from 68M to about 7.5M).
- Updated alt-depmod-check-aliases, alt-modinfo-legacy patches for new
  module-init-tools.

* Sun Jun 27 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.27-alt2
- Added 2.6 support to insmod from modutils instead of invoking a dumb version
  from module-init-tools; this adds the module path search capability and
  --force option for 2.6 (#3914).
- Fixed depmod -A bugs:
  + 2.6: check mtime of all included config files, not just /etc/modules.conf
    (#3960);
  + 2.4, 2.6: check only generated files which are really generated for the
    used kernel version (previously depmod -A updated dependencies for 2.4.x
    every time because of nonexistent modules.alias).
- Added alt-modinfo-legacy patch: add support for 2.4.x-style module parameters
  to the new modinfo.
- Now using new modinfo from module-init-tools for all modules (no more
  inconsistent output format and missing information depending on which kernel
  is booted).
- Fixed module path search bug in insmod and modprobe ('-' and '_' should be
  equivalent, but were not).
- Updated documentation to reflect recent changes.
- Updated BuildRequires.

* Thu Mar 11 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.27-alt1
- modutils 2.4.27 release.
- module-init-tools 3.0 release.
- Dropped alt-alias-loop patch (merged upstream).
- Updated alt-aliases patch (bugfix part merged upstream).
- Added alt-warning-stderr patch: output warning messages to stderr (fixes
  problem with the "Note: /etc/modules.conf is more recent than..." message
  corrupting modprobe -c and --list-module-files output).

* Sun Feb 29 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.26-alt2
- Removed builtin above and below commands from modprobe and placed them into
  00kernel.modutils only for kernels < 2.5.x; fixes problems with hid module
  loading in 2.6.x.

* Thu Feb 19 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.26-alt1
- 2.4.26 release.
- Updated alt-aliases patch; removed broken alias for apm, fixed alias for pg.
- Dropped remove-aliases patch (builtin aliases for older kernels do not seem
  to break 2.6.x).
- Replaced kernel24.modutils and kernel26.modutils with common 00kernel.modutils.
- Dropped parport.modutils (none of the lines there were really needed, and
  "options parport_pc irq=7" did not work at all - #2784).
- Dropped configure-zlib patch (now --with-dynamic-zlib is available).
- Updated kernelversion patch from Dmitry V. Levin <ldv@>.
- Split glob-sort and list-module-files patches.
- Updated mit-combined patch for 2.4.26 (Makefile changes).

* Tue Feb 17 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.25-alt22
- modprobe: added "--list-module-files" and "--kernel-release=REL"
  support for mkinitrd.
- Sort files during glob expansion (fixes problems with undefined
  order of /etc/modutils.d/* inclusion).

* Mon Feb 16 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.25-alt21
- Added alias checking to depmod for 2.6 (some buggy modules specify
  invalid aliases).
- Updated 2.6 support patch:
  - fixed problem with "depmod -A" not updating dependencies after
    modules.conf modifications.

* Fri Feb 13 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.25-alt20
- modprobe: fixed alias loop detection.
- modutils.macros: reverted alt19 change (including modules.alias is
  too slow).
- Fixed format string bugs in module-init-tools.
- Updated 2.6 support patch:
  - always ignore '-'/'_' differences when comparing module names
  - read modules.alias and modules.symbols only if regular alias and
    probe/probeall lookup failed (reading these files is slow)
  - with -L, take the printed module name from the file name
    (workaround for mkinitrd which does not know about '-'/'_'
    handling in 2.6)
  - ignore more old options in insmod for 2.6

* Tue Feb 10 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.25-alt19
- Merged with modutils-2.4.26-3 from Fedora.
- Updated module-init-tools to 3.0-pre9.
- modutils.macros: include modules.alias and modules.symbols for the current
  kernel if they exist (for 2.6).
- Rewritten 2.6 support patch (now only modprobe is common for 2.4 and 2.6,
  other utilities call versions from module-init-tools).
- kernel26.modutils: added back lost vlan_module alias.

* Wed Feb 04 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.25-alt18
- updated 2.6 support patch from Gleb Stiblo <ulfr@altlinux.ru>:
  + fixed bug in /proc/modules parsing
- added Patch22: write modules.alias and modules.symbols only if they are
  really needed (these files break old versions of modutils).

* Fri Jan 16 2004 Sergey Vlasov <vsu@altlinux.ru> 2.4.25-alt17
- fixed "builtin" aliases in kernel24.modutils, kernel26.modutils

* Wed Jan 14 2004 Gleb Stiblo <ulfr@altlinux.ru> 2.4.25-alt16
- command line printed in error log is some errors were occured

* Mon Jan 09 2004 Gleb Stiblo <ulfr@altlinux.ru> 2.4.25-alt15
- -] removed from modprobe. 

* Mon Jan 06 2004 Gleb Stiblo <ulfr@altlinux.ru> 2.4.25-alt14
- insmod: --force-vermagic, --force-modversion and -o added
- modprobe: --force-vermagic, --force-modversion and --force added

* Mon Jan 05 2004 Gleb Stiblo <ulfr@altlinux.ru> 2.4.25-alt13
- merged with alias-remove patch
- include impruvments

* Mon Jan 05 2004 Gleb Stiblo <ulfr@altlinux.ru> 2.4.25-alt12
- depmod: mit is not used now.
- depmod: ccwmap is absent; some diffs in isapnpmap: 0x0 vendor is not
  supported by mu but supported by mit.
- modprobe: command line in /var/log/messages.
- modprobe: -] will be removed in next time. Now it is present only for
  backward cap.
- rmmod: -a not supported. May cause errors (i.e. network modules
  usecount is 0 but modules is used by eth*).
- rmmod: persistent info is not supported.
- autoclean is not supported.

* Thu Dec 25 2003 Rider <rider@altlinux.ru> 2.4.25-alt11
- above, alias and options default configs moved to %_sysconfdir/modutils.d and
  fixed for kernel 2.6.

* Thu Dec 23 2003 Gleb Stiblo <ulfr@altlinux.org> 2.4.25-alt10
- now only depmod used from mit. Support for 2.6 integrated in insmod,
  lsmod, modinfo, modprobe, rmmod.

* Thu Dec 19 2003 Gleb Stiblo <ulfr@altlinux.org> 2.4.25-alt9
- _ and - checking fixed

* Thu Dec 19 2003 Gleb Stiblo <ulfr@altlinux.org> 2.4.25-alt8
- kernel module autoload must work

* Thu Dec 18 2003 Gleb Stiblo <ulfr@altlinux.org> 2.4.25-alt7
- -] is not needed now. Will be removed
- module-init-tools/modprobe.c and lsmod.c are not used now

* Thu Dec  4 2003 Ed V. Bartosh <ed@altlinux.ru> 2.4.25-alt6
- module-init-tools integrated (for using with 2.6 kernel)
- options for 2.4 and 2.6 modprobe are the same, only -h and -d are missed.
- modprobe -L *** for 2.6 generate modulename now
- -] allow to use modprobe for 2.6.0 on 2.4.x system

* Fri Oct 17 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt5
- modprobe: fixed --showconfig exit status when there is no
  dependency file available.
- insmod: set TAINT_FORCED_MODULE flag only when load is really forced.

* Sat Sep 27 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt4
- Resurrected rh-systemmap patch (compatibility issues).
- %%post: do not run "depmod -A" after first install.
- Added comment to default %_sysconfdir/modules.conf (mike).

* Tue Aug 12 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt3
- Relocated %_sysconfdir/modutils.d/pcmcia to pcmcia-cs subpackage.

* Sat Aug 02 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt2
- Removed obsolete patches.
- config parser: extended include directive support.
- Added %_sysconfdir/modutils.d/ support (#0001998).
- Changed plip/parport defaults (#0002784).
- Moved stuff from /lib/modutils/macros to %_sysconfdir/modutils.d/.

* Mon Apr 28 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt1
- Updated to 2.4.25

* Mon Mar 24 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.24-alt1
- Updated to 2.4.24

* Mon Jan 20 2003 Konstantin Volckov <goldhead@altlinux.ru> 2.4.22-alt1
- Updated to 2.4.22
- Changed NVdriver to nvidia
- Added alias char-major-134 apm
- Added alias char-major-212 slamrmo

* Fri Oct 18 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.21-alt1
- Updated to 2.4.21

* Mon Aug 05 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.19-alt1
- 2.4.19; Owl warning fixes and new rh aliases were merged upstream.

* Fri Aug 02 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.18-alt1
- 2.4.18
- Added some more default aliases (rh).
- Fixed checking of kernel version (rh).

* Fri Jun 14 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.16-alt1
- 2.4.16
- Fixed -Wall warnings (Owl).

* Sat Jun 01 2002 Dmitry V. Levin <ldv@altlinux.org> 2.4.15-alt1
- 2.4.15, updated patches.
- Added more licenses to gpl compatibility list.
- Added kernelversion_{major,minor} internally defined commands.
- Load hid then usbmouse is loaded (mdk).
- Disabled build of statically linked utilities
  (unneeded since mkinitrd >= 1:2.8.0-alt1 uses busybox).

* Fri Jan 11 2002 Dmitry V. Levin <ldv@alt-linux.org> 2.4.12-alt4
- macros: added kernel-dependent vlan_module alias (#0000363).

* Mon Dec 24 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.12-alt3
- depmod: fixed cutting prefix algorithm in prtdepend.

* Fri Dec 06 2001 Konstantin Volckov <goldhead@altlinux.ru> 2.4.12-alt2
- load kbdev and mousedev when hid is loaded and not the opposite (mdk).

* Thu Nov 22 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.12-alt1
- 2.4.12
- Added modprobe --basedir option.
- Added modprobe --listonly option (goldhead).

* Tue Nov 20 2001 Dmitry V. Levin <ldv@alt-linux.org> 2.4.11-alt1
- 2.4.11

* Mon Oct 08 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.10-alt1
- 2.4.10

* Tue Aug 21 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.7-alt1
- 2.4.7
- Dropped %_sysconfdir/cron.d/kmod (rh).

* Tue May 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.6-alt1
- 2.4.6
- Updates aliases.
- Built with "--enable-zlib".
- Read macros file /lib/modutils/macros (mdk).
- Added default post/preun for binfmt_misc (rh).

* Thu Mar 29 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.5-alt1
- 2.4.5

* Tue Mar 27 2001 Dmitry V. Levin <ldv@altlinux.ru> 2.4.4-alt1
- 2.4.4

* Wed Feb 28 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.3-ipl1mdk
- 2.4.3

* Tue Feb 20 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.2-ipl2mdk
- Updated aliases.

* Wed Jan 24 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.2-ipl1mdk
- 2.4.2

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.1-ipl2mdk
- modules.conf: added aliases for irda and wacom (MDK).

* Tue Jan 09 2001 Dmitry V. Levin <ldv@fandra.org> 2.4.1-ipl1mdk
- 2.4.1

* Tue Jan 02 2001 Dmitry V. Levin <ldv@fandra.org> 2.3.24-ipl1mdk
- 2.3.24

* Thu Dec 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.23-ipl1mdk
- 2.3.23
- Fix bug with empty MODULE_GENERIC_STRING entries depmod loops (MDK).
- Added aliases for LVM.

* Sun Dec 10 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.22-ipl1mdk
- 2.3.22

* Wed Nov 22 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.21-ipl1mdk
- 2.3.21

* Tue Nov 21 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.20-ipl1mdk
- 2.3.20

* Tue Nov 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.19-ipl2mdk
- Security fix (from Keith Owens <kaos@OCS.COM.AU>).

* Mon Oct 23 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.19-ipl1mdk
- 2.3.19

* Thu Oct 12 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.18-ipl1mdk
- 2.3.18

* Fri Sep 29 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.17-ipl2mdk
- Exclude .rhkvtmag when trying to depmod -a (Chmouel).

* Tue Sep 26 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.17-ipl1mdk
- 2.3.17
- Automatically added BuildRequires.

* Thu Sep 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.16-ipl2mdk
- Requires: vixie-cron >= 3.0.1-ipl45mdk.

* Mon Sep 11 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.16-ipl1mdk
- 2.3.16

* Thu Aug 17 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.15-ipl1mdk
- 2.3.15

* Mon Aug 14 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.14-ipl1mdk
- 2.3.14

* Wed Aug  2 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.13-ipl1mdk
- 2.3.13
- move /etc/conf.modules --> /etc/modules.conf

* Wed May 31 2000 Dmitry V. Levin <ldv@fandra.org> 2.3.11-ipl1mdk
- 2.3.11
- Crypto aliases added.
- RE and Fandra adaptions.

* Mon Apr 10 2000 Adam Lebsack <adam@mandrakesoft.com> 2.3.10-2mdk
- Removed the installing of /etc/rc.d/init.d/kerneld

* Tue Mar 21 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.10-1mdk
- Remove static files.
- Move depmod_is_necessary  to initscripts package.
- 2.3.10.

* Mon Mar 13 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.9-2mdk
- Don't cry when a conf.modules is much recent than modules.dep.
- Adjust groups.

* Mon Mar  6 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.3.9-1mdk
- 2.3.9.
- Patch upgrade disabling warning about conf.modules.
- getmod() also in alsa/ directory.

* Mon Nov 29 1999 Pixel <pixel@linux-mandrake.com>
- added prog is_depmod_necessary
- depmod -a now done only if is_depmod_necessary

* Mon Oct 25 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Merge with rh changes.

* Tue May 18 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Fixing typo.

* Fri Apr 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Removing kerneld.
- Adptations patch.
- Cleaning .spec.

* Tue Apr 13 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Add patchs from Redhat6.0.

* Sat Apr 10 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- Mandrake adaptions
- bzip2 man/info pages
- restore de,fr,tr locales from RH 5.2 version
- Don't load kerneld if we have kmod.

* Mon Mar 15 1999 Bill Nottingham <notting@redhat.com>
- added support for /lib/modules/foo/pcmcia
- make kerneld initscript not start by default

* Tue Feb 23 1999 Matt Wilson <msw@redhat.com>
- added sparc64 support from UltraPenguin

* Tue Jan 12 1999 Cristian Gafton <gafton@redhat.com>
- call libtoolize to allow it to compile on the arm

* Wed Dec 23 1998 Jeff Johnson <jbj@redhat.com>
- search /lib/modules/preferred before defaults but after specified paths.

* Tue Nov 17 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 2.1.121

* Thu Nov 05 1998 Erik Troan <ewt@redhat.com>
- added -m, -i options

* Thu Oct 01 1998 Michael K. Johnson <johnsonm@redhat.com>
- fix syntax error I introduced when enhancing initscript

* Wed Sep 30 1998 Michael K. Johnson <johnsonm@redhat.com>
- enhance initscript

* Fri Aug 28 1998 Jeff Johnson <jbj@redhat.com>
- recompile statically linked binary for 5.2/sparc

* Tue Jul 28 1998 Jeff Johnson <jbj@redhat.com>
- pick up ultrapenguin patches (not applied for now).
- pre-generate keyword.c so gperf doesn't have to be present (not applied).
- util/sys_cm.c: fix create_module syscall (signed return on sparc too)

* Wed Jul 15 1998 Jeff Johnson <jbj@redhat.com>
- correct %postun typos

* Fri May 01 1998 Erik Troan <ewt@redhat.com>
- added /lib/modules/preferred to search path

* Fri Apr 24 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Tue Apr 07 1998 Cristian Gafton <gafton@redhat.com>
- updated to 2.1.85
- actually make use of the BuildRoot

* Fri Apr  3 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Fix sparc64, add modinfo64 on sparc.

* Wed Mar 23 1998 Jakub Jelinek <jj@ultra.linux.cz>
- Handle EM_SPARCV9, kludge to support both 32bit and 64bit kernels
  from the same package on sparc/sparc64.

* Fri Nov  7 1997 Michael Fulbright
- removed warning message when conf.modules exists and is a empty

* Tue Oct 28 1997 Erik Troan <ewt@redhat.com>
- patched to honor -k in options
- added modprobe.1
- added init script

* Thu Oct 23 1997 Erik Troan <ewt@redhat.com>
- removed bogus strip of lsmod (which is a script)

* Mon Oct 20 1997 Erik Troan <ewt@redhat.com>
- updated to 2.1.55
- builds in a buildroot

* Mon Aug 25 1997 Erik Troan <ewt@redhat.com>
- added insmod.static

* Sun Aug 24 1997 Erik Troan <ewt@redhat.com>
- built on Intel
- combined rmmod and insmod
