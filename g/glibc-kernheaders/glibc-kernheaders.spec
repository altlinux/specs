%define kernel_base_version 3.3
%define kernel_source kernel-source-%kernel_base_version

Name: glibc-kernheaders
Version: %kernel_base_version.8
Release: alt1

Summary: Linux kernel C header files for use by glibc and other userspace software
License: GPLv2
Group: Development/Kernel
Url: http://www.kernel.org/

# git://git.altlinux.org/gears/g/%name.git
Patch: %name-%version-%release.patch

BuildRequires: rpm-build-kernel
BuildRequires: %kernel_source = 1.0.0

Provides: kernel-headers = %version-%release
Provides: linux-libc-headers = %version-%release
Obsoletes: linux-libc-headers

%define base_arch %_target_cpu
%ifarch %ix86 x86_32 x86_64
%define base_arch x86
%endif
%ifarch %arm
%define base_arch arm
%endif
%ifarch ppc ppc64
%define base_arch powerpc
%endif

%description
This package includes the C header files that specify the interface
between the Linux kernel and userspace libraries and programs.
The header files define structures and constants that are needed for
building most standard programs and are also needed to build glibc.

%prep
%setup -cT
tar -xf %kernel_src/%kernel_source.tar.*
cd %kernel_source
%patch -p1

%install
%define hdr_dir %_includedir/linux-default
make -C %kernel_source headers_install_all \
	INSTALL_HDR_PATH=%buildroot%hdr_dir \
	HDR_ARCH_LIST="%base_arch"
find %buildroot%_includedir -name "*.install*" -delete
ln -snf asm-%base_arch %buildroot%hdr_dir/include/asm
[ "%base_arch" = "%_target_cpu" ] ||
	ln -snf asm-%base_arch %buildroot%hdr_dir/include/asm-%_target_cpu

%check
set +x
d="$PWD"
cd %buildroot%hdr_dir/include
for f in {linux,asm}/*.h; do
	printf '#include <%%s>\n' "$f" |
		%__cc %optflags -S -I"$PWD" -o/dev/null -xc - ||
			echo "$f"
done > "$d"/fail.list
cd - > /dev/null

%pre
for d in %hdr_dir/include/asm-%_target_cpu; do
	[ -d "$d" -a ! -L "$d" ] || continue
	rmdir "$d" 2> /dev/null ||:
done

%files
%hdr_dir

%changelog
* Fri Jun 08 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.8-alt1
- Updated to v3.3.8.

* Mon May 14 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.6-alt1
- Updated to v3.3.6.

* Sat May 12 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.5-alt2
- Added %%check.
- Added a workaround for
  https://bugzilla.altlinux.org/show_bug.cgi?id=27320#c3

* Fri May 11 2012 Dmitry V. Levin <ldv@altlinux.org> 3.3.5-alt1
- Updated to v3.3.5.
- Dropped upgrade trigger.
- Packaged /usr/include/linux-default/include/asm-%%_target_cpu symlink
  to make packages always different on different architectures.

* Fri Dec 03 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.36-alt5
- linux/netlink.h: fixed gcc -Wconversion compilation warning.

* Fri Oct 29 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.36-alt4
- Restore kvm.h, kvm_para.h an a.out (regression after 2.6.36-alt2).

* Fri Oct 22 2010 Dmitry V. Levin <ldv@altlinux.org> 2.6.36-alt3
- Fixed upgrade from earlier releases where %%asmdir
  was a directory.
- Dropped unsupported architectures.

* Fri Oct 22 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.36-alt2
- Make package noarch:
  + package headers for all architectures
  + setup asm symlink on %%post

* Fri Oct 15 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.36-alt1
- Updated to v2.6.36
- Drop useless fail.log

* Fri Mar 26 2010 Kirill A. Shutemov <kas@altlinux.org> 2.6.33-alt1
- Updated to v2.6.33

* Tue Oct 27 2009 Kirill A. Shutemov <kas@altlinux.org> 2.6.32-alt1
- Updated to v2.6.32-rc5

* Tue May 12 2009 Kirill A. Shutemov <kas@altlinux.ru> 2.6.29-alt3
- Updated to v2.6.29.3
- Use "powerpc" base arch on ppc and ppc64
- Delete .install and ..install.cmd files

* Tue Feb 24 2009 Kirill A. Shutemov <kas@altlinux.ru> 2.6.29-alt2
- Updated to v2.6.29-rc6

* Sun Feb 22 2009 Kirill A. Shutemov <kas@altlinux.ru> 2.6.29-alt1
- Updated to v2.6.29-rc5
- Reexport <linux/ext2_fs.h> and <linux/inotify.h> since changes
  is not approved by upstream

* Wed Sep 17 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.27-alt3
- Unexport <linux/ext2_fs.h> and <linux/inotify.h>

* Tue Sep 16 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.27-alt2
- linux/inotify.h: do not include <linux/fcntl.h> in userspace
- linux/smb.h: do not include <linux/time.h> in userspace

* Wed Sep 10 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.27-alt1
- Update to v2.6.27-rc6
- There is no kernel-source-2.6.27 in Sisyphus, so pack whole tree

* Wed Sep 03 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt5
- Use rpm-build-kernel instead kernel-build-tools in Buildrequires

* Sat Mar 29 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt4
- Export aligned_u64, aligned_be64 and aligned_le64 to userspece

* Tue Mar 25 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt3
- Sync with kernel-image-std-def-2.6.24-alt5
- Include <linux/fs.h> into linux/ext2_fs.h for FS_IOC* defines

* Fri Mar 21 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt2
- Make linux/wireless.h be able to compile
- Include <linux/types.h> into linux/if_arp.h for __u* typedef
- Include <linux/types.h> into linux/atmmpc.h for __be32 typedef
- Wrap 'struct termios' into ifdef __KERNEL_ to avoid conflict with glibc

* Tue Mar 04 2008 Kirill A. Shutemov <kas@altlinux.ru> 2.6.24-alt1
- Based on kernel-image-std-def-2.6.24-alt5
- Dropped _syscallX macros

* Sat Feb 09 2008 Dmitry V. Levin <ldv@altlinux.org> 2.6.18-alt4
- Merged with kernel-image-std-smp-2.6.18-alt11.
- asm-powerpc/unistd.h: Fixed a leftover from a merge (Wartan Hachaturow).
- Unexported asm/page.h, asm/elf.h, asm/user.h and linux/user.h (Kirill A. Shutemov).

* Thu Nov 29 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.18-alt3
- Reenabled AutoReqProv.

* Sun Nov 04 2007 Sergey Vlasov <vsu@altlinux.ru> 2.6.18-alt2
- Fix package upgrade (%_includedir/linux-default/include/asm was a symlink
  before moving to "make headers_install", but now it is a real directory).

* Tue Oct 30 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.18-alt1
- Specfile cleanup.

* Tue Oct 23 2007 Kirill A. Shutemov <kas@altlinux.ru> 2.6.18-alt0.9
- Use kernel's "make headers_install" to generate userspace headers
- Based on kernel-image-std-smp-2.6.18-alt8
- Headers fixes:
  + Fix noise in futex.h
  + V4L/DVB (5867): videodev2.h: add missing <sys/time.h> for userspace
  + Restore macros _syscallX
  + linux/types.h related fixes:
    + use __u8/__u32 in userspace ioctl defines for I2O
    + linux/audit.h needs linux/types.h
    + replace u8 and u32 with __u8 and __u32 in scsi.h for user space
    + include <linux/types.h> into linux/if_fddi.h for __be16 typedef
    + include <linux/types.h> into linux/nbd.h for __be32 and __be64 typedefs
    + include <linux/types.h> into linux/ethtool.h for __u32 typedef
- Export linux/serial_reg.h and asm/unaligned.h to userspace

* Sun Sep 23 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt7
- Made linux/sem.h and linux/videodev2.h compilable in userspace.
- Provides/Obsoletes linux-libc-headers.

* Thu Apr 12 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt6
- Updated linux/futex.h (Kirill A. Shutemov):
  + Backported FUTEX_* constants.
  + Fixed linux/futex.h compilation.

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt5
- Disabled sanitization of compiler*.h.

* Thu Jan 25 2007 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt4
- Sanitize headers (#10634).

* Sun Oct 08 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt3
- linux/joystick.h: Include <linux/types.h> instead of <asm/types.h>.
- asm-i386/system.h: Replace u(8|16|32) types with __u(8|16|32).

* Fri Oct 06 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt2
- Removed improper kernheaders-2.6.9-alt-byteorder.patch, see
  https://bugzilla.altlinux.org/show_bug.cgi?id=5409#c5 for details.
- linux/types.h:
  + Include <sys/types.h>;
  + Hide "struct ustat" definition from userspace.
- linux/cciss_ioctl.h: Include <linux/compiler.h>.

* Mon Oct 02 2006 Dmitry V. Levin <ldv@altlinux.org> 2.6.17-alt1
- Updated to linux-2.6.17.
- Applied patch from SuSE to make headers more ready for userspace.
- Backported byteorder and MAX_NESTED_LINKS fixes from std26 headers.

* Tue Oct 04 2005 Dmitry V. Levin <ldv@altlinux.org> 2.4.29-alt2
- Fixed linux/if_fddi.h (see #8122).

* Tue Aug 09 2005 Anton D. Kachalov <mouse@altlinux.org> 2.4.29-alt1
- Updated headers to 2.4.29.
- Updated asm/unistd.h to linux-2.6.12.
- Added headers for x86_64 architecture.
- Added URL.

* Tue May 10 2005 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt2
- Updated asm/termbits.h to linux-2.6.11.
- Updated asm/unistd.h to linux-2.6.11.
- Updated linux/prctl.h to linux-2.6.11.

* Sat Apr 10 2004 Dmitry V. Levin <ldv@altlinux.org> 2.4.25-alt1
- Updated to linux-2.4.25.
- Updated linux/prctl.h to linux-2.6.5.
- Updated asm/unistd.h to linux-2.6.5.

* Fri Jun 20 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4.21-alt1
- Updated to linux-2.4.21.

* Mon Jun 09 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt4
- Relocated to proper place, %_includedir/linux-default/include/.

* Tue Jun 03 2003 Dmitry V. Levin <ldv@altlinux.org> 2.4-alt3
- Tarball and specfile cleanup.

* Wed May 28 2003 Peter Novodvorsky <nidd@altlinux.com> 2.4-alt2
- Removed all requires.

* Tue May 27 2003 Peter Novodvorsky <nidd@altlinux.com> 2.4-alt1
- Rebuilt with ALTLinux adaptations for new kernel policy.

* Sun Apr 13 2003 Ajran van de Ven <arjanv@redhat.com> 2.4-8.13
- remove more kernel private files

* Fri Apr 11 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.12
- update <linux/prctl.h> header
- remove i386 <asm/io.h>, replace it with a warning and <sys/io.h> include
  (Arjan van de Ven)

* Mon Feb 10 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.11
- update syscall numbers for all arches from 2.5.64 headers

* Fri Feb  7 2003 Bill Nottingham <notting@redhat.com> 2.4-8.10
- update more wireless headers

* Wed Feb  5 2003 Bill Nottingham <notting@redhat.com> 2.4-8.9
- update wireless headers

* Thu Jan 30 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.7
- make /usr/include/asm during build if it doesn't exist

* Thu Jan 30 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.6
- remove unpackaged file

* Thu Jan 30 2003 Bill Nottingham <notting@redhat.com>
- update netfilter headers

* Thu Jan 30 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.5
- don't include <linux/types.h> etc. in <asm-s390*/ptrace.h>

* Thu Jan 16 2003 Jakub Jelinek <jakub@redhat.com> 2.4-8.4
- updated s390 headers, added s390x headers
- HTB in <linux/pkt_sched.h>
- no -debuginfo subpackage

* Thu Dec 12 2002 Jakub Jelinek <jakub@redhat.com> 2.4-8.3
- update version.h from kernel-2.4.20-0.pp.6

* Tue Nov 26 2002 Jakub Jelinek <jakub@redhat.com> 2.4-8.2
- update unistd.h from kernel-2.4.19-0.pp.19

* Thu Oct 10 2002 Jakub Jelinek <jakub@redhat.com>
- generate stubs automatically
- remove /usr/include/scsi from file list

* Thu Oct 10 2002 Arjan van de Ven <arjanv@redhat.com
- added support for mixed 32/64 headers

* Tue Mar 21 2002 Arjan van de Ven <arjanv@redhat.com
- update ethtool and other network ioctls

* Tue Feb 10 2002 Arjan van de Ven <arjanv@redhat.com
- removed autoconf.h content

* Sun Feb 10 2002 Arjan van de Ven <arjanv@redhat.com
- fix missing include that broke quota.h

* Mon Jan 07 2002 Arjan van de Ven <arjanv@redhat.com
- fix rhconfig.h include file to not care about /boot/kernel.h

* Wed Jan 02 2002 Florian La Roche <Florian.LaRoche@redhat.de>
- fix #warning in <asm-i386/rwlock.h> and <asm-i386/spinlock.h>

* Thu Dec 6 2001 Arjan van de Ven <arjanv@redhat.com>
- fix misplaced #endif

* Tue Dec 4 2001 Arjan van de Ven <arjanv@redhat.com>
- fix version.h to not include /boot/kernel.h

* Wed Oct 31 2001 Arjan van de Ven <arjanv@redhat.com>
- Initial packaging
