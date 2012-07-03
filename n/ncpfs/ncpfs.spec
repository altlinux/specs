Name: ncpfs
Version: 2.2.6
Release: alt9

Summary: Utilities for the %name filesystem, a NetWare client for Linux
License: GPL
Group: Networking/Other
Packager: Dmitry Lebkov <dlebkov@altlinux.ru>

# ftp://platan.vc.cvut.cz/pub/linux/%name/%name-%version/%name-%version.tar.gz
Source: %name-%version.tar
Source1: mount.ncp
Source2: ncpfs.control

Patch0: ncpfs-2.2.6-alt-makefile.patch
Patch1: ncpfs-2.2.6-alt-compile.patch
Patch2: ncpfs-2.2.6-alt-gcc41-compile.patch
Patch3: ncpfs-2.2.6-alt-warnings.patch

Patch10: ncpfs-2.2.3-fix.patch
Patch11: ncpfs-2.2.3-array.patch
Patch12: ncpfs-2.2.4-pie.patch
Patch13: ncpfs-2.2.6-getuid.patch
Patch15: ncpfs-2.2.6-align.patch
Patch16: ncpfs-2.2.6-rh-mount-issue.patch

Requires: libncp = %version-%release

# Automatically added by buildreq on Mon Jan 15 2007
BuildRequires: libpam-devel control

%define controlled_binaries ncpmount ncpumount slist

#uildPreReq: gcc3.4

%package -n libncp
Summary: Shared library for access the %name filesystem
Group: System/Libraries

%package -n libncp-devel
Summary: Development environmnt for the %name filesystem
Group: Development/C
Requires: libncp = %version-%release

%package -n ipxutils
Summary: Tools for configuring and debugging IPX interfaces and networks
Group: System/Configuration/Networking

%description
Ncpfs is a filesystem which understands the Novell NetWare(TM)
NCP protocol.  Functionally, NCP is used for NetWare the way NFS
is used in the TCP/IP world.  For a Linux system to mount a NetWare
filesystem, it needs a special mount program.  The %name package
contains such a mount program plus other tools for configuring and
using the %name filesystem.

Install the %name package if you need to use the %name filesystem
to use Novell NetWare files or services.

%description -n libncp
Ncpfs is a filesystem which understands the Novell NetWare(TM)
NCP protocol.  Functionally, NCP is used for NetWare the way NFS
is used in the TCP/IP world.  For a Linux system to mount a NetWare
filesystem, it needs a special mount program.  The %name package
contains such a mount program plus other tools for configuring and
using the %name filesystem.

This package contains shared library required to run NCP-based software.

%description -n libncp-devel
Ncpfs is a filesystem which understands the Novell NetWare(TM)
NCP protocol.  Functionally, NCP is used for NetWare the way NFS
is used in the TCP/IP world.  For a Linux system to mount a NetWare
filesystem, it needs a special mount program.  The %name package
contains such a mount program plus other tools for configuring and
using the %name filesystem.

This package contains static library and headers required to develop
NCP-based software.

%description -n ipxutils
The ipxutils package includes utilities (ipx_configure, ipx_internal_net,
ipx_interface, ipx_route) necessary for configuring and debugging IPX
interfaces and networks under Linux. IPX is the low-level protocol used
by Novell's NetWare file server system to transfer data.

Install ipxutils if you need to configure IPX networking on your network.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch15 -p1
%patch16 -p1

%build
%configure \
	--enable-pam \
	--disable-function-sections \
	--disable-mount-v2

%make_build
%make_build -C ipxdump
cp -p ipxdump/README README.ipxdump
cp -p contrib/pam/README README.pam_ncp

%install
mkdir -p %buildroot{/sbin,%_sbindir,/lib/security}
%makeinstall install-dev \
	libsodir=%buildroot/%_libdir \
	libadir=%buildroot/%_libdir \
	LIB_PAM_SECURITY=%buildroot/lib/security

# Move these to permit /usr from NFS
for f in ipx_{configure,internal_net,interface}; do
	mv "%buildroot/%_bindir/$f" "%buildroot/sbin/$f"
done

install -p -m755 ipxdump/ipx{dump,parse} %buildroot/%_bindir

ln -s ..%_bindir/ncpmount %buildroot/sbin/mount.ncp
ln -s mount.ncp %buildroot/sbin/mount.ncpfs

# These could be SUID root, but it's a security hole.
# PS: we'll let local sysadmin control that
chmod a-s %buildroot/%_bindir/*

for n in %controlled_binaries; do
	install -pD -m755 %SOURCE2 "%buildroot%_controldir/$n"
	subst -p "s/@NAME@/$n/" "%buildroot%_controldir/$n"
done

%find_lang %name

%pre
/usr/sbin/groupadd -r -f netadmin &>/dev/null
for n in %controlled_binaries; do
	%pre_control $n
done

%post
for n in %controlled_binaries; do
	%post_control -s restricted $n
done

%files -n libncp
%_libdir/*.so.*

%files -n libncp-devel
%_libdir/*.so
%_libdir/*.*a
%_includedir/*
%_man3dir/*

%files -f %name.lang
/sbin/m*
%_sbindir/*
%_bindir/[nps]*
/lib/security/*
%config %_controldir/*
%_man1dir/*
%_man5dir/*
%_man8dir/n*
%_man8dir/mount.ncp.8*
%doc BUGS Changes ConfigFile INSTALL FAQ README README.pam_ncp

%files -n ipxutils
/sbin/ipx*
%_bindir/ipx*
%_man8dir/ipx*
%doc ipx-1.0/COPYING ipx-1.0/README README.ipxdump

%changelog
* Wed Mar 09 2011 Dmitry V. Levin <ldv@altlinux.org> 2.2.6-alt9
- Imported fix of race conditions in ncpmount/ncpumount operations
  from Fedora (fixes CVE-2009-3297).

* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.6-alt8
- Rebuilt for soname set-versions

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 2.2.6-alt7.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libncp
  * postun_ldconfig for libncp
  * postclean-05-filetriggers for spec file

* Sun Apr 06 2008 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt7
- control(8) support (fixes #2275, partially #2289) by mike@

* Mon Jan 15 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt6
- fix x86_64 build

* Mon Jan 15 2007 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt5
- spec-file fix: apply patches, missed in alt4

* Tue Nov 07 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt4
- rebuild with latest ALT Sisyphus

* Mon Jul 03 2006 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt3
- compilation with gcc4.1 fixed

* Wed Oct 05 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt2
- compilation fixed

* Fri Jan 28 2005 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.6-alt1
- new version 2.2.6
  + CAN-2005-001{3,4} security fix in upstream

* Wed Oct 08 2003 Dmitry Lebkov <dlebkov@altlinux.ru> 2.2.3-alt1
- new version 2.2.3

* Thu Oct 17 2002 Rider <rider@altlinux.ru> 2.2.0.18.a-ipl5mdk
- rebuild (gcc 3.2)

* Mon Apr 15 2002 Rider <rider@altlinux.ru> 2.2.0.18.a-ipl4mdk
- rebuild

* Sat Jan 20 2001 Dmitry V. Levin <ldv@fandra.org> 2.2.0.18.a-ipl3mdk
- RE adaptions.
- Fixed compilation.
- Split out libncp and libncp-devel subpackages.
- Updated code to new modutils.

* Sun Nov 05 2000 David BAUDENS <baudens@mandrakesoft.com> 2.2.0.18.a-3mdk
- Use optimizations

* Tue Aug 30 2000 Florin Grad <florin@mandrakesoft.com> 2.2.0.18.a-2mdk
- changing some macros

* Tue Aug 29 2000 Florin Grad <florin@mandrakesoft.com> 2.2.0.18.a-1mdk
- new version
- adding some macros

* Tue May 23 2000 Vincent Saugey <vince@mandrakesoft.com> 2.2.0.17.a-4mdk
- new version
- adding new macros

* Tue May 23 2000 Vincent Saugey <vince@mandrakesoft.com> 2.2.0.17.a-4mdk
- Add ldconfig to ncp package

* Mon May 22 2000 Vicnent Saugey <chmouel@mandrakesoft.com> 2.2.0.17.a-3mdk
- Fix file list

* Thu May 18 2000 Vincent Saugey <vince@mandrakesoft.com> 2.2.0.17.a-2mdk
- Many fix in build process
- Add build pam-devel require
- Change all %install process don't use the buggy Makefile of source for install

* Wed May 10 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 2.2.0.17.a-1mdk
- 2.2.0.17
- Add large key patch
- Add net-pf-4 to /etc/conf.modules in %post.

* Fri Apr 14 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 2.2.0.16.a-3mdk
- Fix groups.
- s/.gz/.bz2/ in rpm.files
- do not issue 2 sed call , just use the sed -e option.

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 2.2.0.16.a
- left ipx_interface out of %files.
- fix mount.ncp USER arg.
- move ipxdump docs to the package that it's in...
- fix bug in slist/nwsfind

* Mon May 17 1999 Axalon Bloodstone <axalon@relic.net>
- More Mandake adaptions, bzip2 manpages
- broken manpage symlinks

* Sat May 15 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add patch from Axalon Bloodstone <axalon@Jumpstart.netpirate.org>

* Wed May 05 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
- fix compilation

* Tue Apr  6 1999 Bill Nottingham <notting@redhat.com>
- turn off setuid on nwsfind
- move ipxutils to using ncpfs versioning for sanity reasons

* Fri Mar 26 1999 Bill Nottingham <notting@redhat.com>
- doesn't work on alpha, apparently
- add a mount.ncp mount helper

* Mon Mar 22 1999 Bill Nottingham <notting@redhat.com>
- remove dangling symlink

* Tue Feb 23 1999 Bill Nottingham <notting@redhat.com>
- update to 2.2.0.12

* Fri Jan 22 1999 Bill Nottingham <notting@redhat.com>
- build for arm. Yuk.

* Wed Dec  9 1998 Bill Nottingham <notting@redhat.com>
- update to 2.2.0.11

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.2.0.

* Fri Jul 10 1998 Jeff Johnson <jbj@redhat.com>
- exclusively i386 for now.

* Tue Jul  7 1998 Jeff Johnson <jbj@redhat.com>
- move ipx_configure/ipx_internal_net to /sbin to permit /usr from NFS.

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Apr 13 1998 Cristian Gafton <gafton@redhat.com>
- manhattan rebuild
- there is a new version out, 2.0.12, but it contains RSA crypto code, so
  it's of no use for us. :-(
- buildroot and spec file cleanup

* Thu Dec 18 1997 Erik Troan <ewt@redhat.com>
- uid_t, gid_t, mode_t fixes for glibc 2.0.5 and linux 2.0.x

* Wed Oct 23 1997 Michael Fulbright <msf@redhat.com>
- added a few file which were missing from the file list

* Sun Oct 19 1997 Erik Troan <ewt@redhat.com>
- updated to 2.0.11
- massive hacking for glibc

* Thu Mar 06 1997 Michael K. Johnson <johnsonm@redhat.com>
- nwrights program now included in package.
