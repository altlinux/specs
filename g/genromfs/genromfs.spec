Name: genromfs
Version: 0.5.2
Release: alt0.2

Summary: Utility for creating romfs filesystems
License: GPL
Group: System/Kernel and hardware
Url: http://romfs.sourceforge.net
Packager: Dmitry V. Levin <ldv@altlinux.org>

Source: http://prdownloads.sourceforge.net/romfs/genromfs-%version.tar

Provides: /bin/genromfs

%description
Genromfs is a tool for creating romfs filesystems, which are lightweight,
read-only filesystems supported by the Linux kernel.  Romfs filesystems
are mainly used for the initial RAM disks used during installation.

%prep
%setup -q

%build
%def_enable Werror
make CFLAGS="%optflags -DVERSION=\\\"%version\\\"" LDFLAGS="%optflags"

%install
install -pDm755 genromfs %buildroot/bin/genromfs
install -pDm644 genromfs.8 %buildroot%_man8dir/genromfs.8
mkdir -p %buildroot%_bindir
ln -s ../../bin/genromfs %buildroot%_bindir/

%files
/bin/*
%_bindir/*
%_man8dir/*
%doc NEWS *.txt genrommkdev

%changelog
* Mon Oct 16 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt0.2
- Fixed build with -D_FORTIFY_SOURCE=2 -Werror.

* Mon Oct 16 2006 Dmitry V. Levin <ldv@altlinux.org> 0.5.2-alt0.1
- Updated to cvs snapshot 20050818.

* Thu Sep 22 2005 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt5
- Converted absolute symlink into relative.

* Mon Oct 25 2004 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt4
- Specfile cleanup.

* Thu Oct 24 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.1-alt3
- Rebuilt in new environment

* Mon Aug 19 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.1-alt2
- Moved genromfs to /bin
- Added Provides: /bin/genromfs (Required by new mkinitrd)

* Thu Mar 07 2002 Dmitry V. Levin <ldv@altlinux.org> 0.5.1-alt1
- 0.5.1
- Added more docs.
- Fixed Url and Source tags.

* Sun Feb 10 2002 Rider <rider@altlinux.ru> 0.5-alt1
- Russian summary
- URL tag
- 0.5

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 0.3-ipl10mdk
- RE adaptions.

* Thu Jul 20 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.3-10mdk
- BM, macros

* Sat Jun 10 2000 Etienne Faure <etienne@mandrakesoft.com> 0.3-9mdk
-rebuild on kenobi

* Wed Apr 05 2000 John Buswell <johnb@mandrakesoft.com> 0.3-8mdk
- fixed vendor tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 0.3-7mdk
- fixed groups
- spec helper

* Wed Dec 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Add a defattr.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 4)

* Thu Nov  5 1998 Jeff Johnson <jbj@redhat.com>
- import from ultrapenguin 1.1.

* Thu Oct 30 1998 Jakub Jelinek <jj@ultra.linux.cz>
- new package
