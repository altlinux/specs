Summary: Tools for managing the Oracle Cluster Filesystem 2
Name: ocfs2-tools
Version: 1.6.4
Release: alt1.2
License: GPL
Group: System/Kernel and hardware
Source: %name-%version.tar.bz2
Source1: cluster.conf
Patch0: %name-initscript.patch
Patch1: %name-gcc43-alt.patch
Patch2: %name-1.6.4-alt-umode_t.patch
Url: http://oss.oracle.com/projects/ocfs2-tools/
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>
BuildRequires: e2fsprogs-devel, glib2-devel, python-module-pygtk , python-devel, readline-devel, ncurses-devel, libe2fs-devel, libuuid-devel

%description
Tools to manage Oracle Cluster Filesystem 2 volumes.

%package -n ocfs2console
Summary: GUI frontend for OCFS2 management
Group: System/Kernel and hardware
Requires: ocfs2-tools = %version
%py_provides o2cb ocfs2 plist

%description -n ocfs2console
GUI frontend for management and debugging of Oracle Cluster Filesystem 2
volumes.

%package -n ocfs2-tools-devel
Summary: Headers and static archives for ocfs2-tools
Group: Development/Other
Requires: ocfs2-tools = %version

%description -n ocfs2-tools-devel
ocfs2-tools-devel contains the libraries and header files needed to
develop ocfs2 filesystem-specific programs.

%prep
%setup -n ocfs2-tools-%version
%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
%configure --enable-dynamic-ctl=yes --enable-dynamic-fsck=yes --disable-debug --prefix=/usr --mandir=%_datadir/man --libdir=%_libdir
make

%install
mkdir -p %buildroot%_sysconfdir/sysconfig %buildroot%_initdir
install -m755 vendor/common/o2cb.init %buildroot%_initdir/o2cb
install -m755 vendor/common/ocfs2.init %buildroot%_initdir/ocfs2
install -m644 vendor/common/o2cb.sysconfig %buildroot%_sysconfdir/sysconfig/o2cb
mkdir -p %buildroot/var/run/o2cb

mkdir -p %buildroot/%_sysconfdir/ocfs2/
install -m600 %SOURCE1 %buildroot/%_sysconfdir/ocfs2/

make DESTDIR="%buildroot" install

%__python -c "import compileall; compileall.compile_dir('%buildroot/%python_sitelibdir/ocfs2interface', ddir='%_libdir/%python_sitelibdir/ocfs2interface')"

%post
%post_service o2cb
%post_service ocfs2

%preun
%preun_service ocfs2
%preun_service o2cb

%files
%doc README.O2CB COPYING CREDITS MAINTAINERS
%doc documentation/users_guide.txt
/sbin/*
%_initdir/*
%config(noreplace) %_sysconfdir/sysconfig/o2cb
%config(noreplace) %_sysconfdir/ocfs2/cluster.conf
%_sbindir/o2hbmonitor
%_bindir/o2info
%_man7dir/o2cb.7.gz
%_man8dir/debugfs.ocfs2.8.gz
%_man8dir/fsck.ocfs2.8.gz
%_man8dir/fsck.ocfs2.checks.8.bz2
%_man8dir/mkfs.ocfs2.8.gz
%_man8dir/tunefs.ocfs2.8.gz
%_man8dir/mount.ocfs2.8.gz
%_man8dir/mounted.ocfs2.8.gz
%_man8dir/o2cb_ctl.8.gz
%_man8dir/o2image.8.gz
%_man8dir/ocfs2_hb_ctl.8.gz
%_man1dir/o2info.1.gz
%dir /var/run/o2cb

%files -n ocfs2console
%_libdir/python%__python_version/site-packages/ocfs2interface
%_sbindir/ocfs2console
%_man8dir/ocfs2console.8.gz

%files -n ocfs2-tools-devel
%_libdir/*.a
%_libdir/pkgconfig/*.pc
%dir %_includedir/o2cb
%_includedir/o2cb/*.h
%dir %_includedir/o2dlm
%_includedir/o2dlm/*.h
%dir %_includedir/ocfs2
%_includedir/ocfs2/*.h
%dir %_includedir/ocfs2-kernel
%_includedir/ocfs2-kernel/*.h

%changelog
* Tue Jun 19 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.4-alt1.2
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.4-alt1.1
- Rebuild with Python-2.7

* Mon Feb 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.4-alt1
- 1.6.4

* Thu Sep 30 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Mon Jun 07 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.4-alt1
- 1.4.4
- pack sample config

* Tue Nov 24 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt5
- add libuuid-devel to buildrequires (due to libe2fs-devel requires change)

* Thu Jul 23 2009 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt4
- minor specfile changes

* Mon Nov 10 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt3
- dropped old requires

* Tue Oct 28 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt2
- new toolchain build

* Tue Sep 23 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Fri Aug 08 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt3
- add condrestart&condstop to initscripts

* Sun Feb 17 2008 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt2
- Rebuild with python2.5

* Thu Nov 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.7-alt1
- 1.2.7
- Changes to tunefs.ocfs2 include allowing users to remove the slots, shrink the journal size and 
- query the superblock parameters. The other change relates to the hueristically determined cluster
- size value by mkfs.ocfs2. For more efficient disk usage, it now picks the smallest value that
- will allow it to address the full device.

* Mon Oct 08 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue May 22 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt1.3
- Changed to alt1.3

* Tue May 22 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt1.2
- Added console package

* Tue May 22 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt1.1
- Changes to initscripts

* Mon May 21 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt1
- Changes to initscripts

* Fri May 18 2007 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.4-alt0
- Initial build for ALT

* Thu Jan 27 2005 Manish Singh <manish.singh@oracle.com>
- Add ocfs2console

* Fri Jan 21 2005 Manish Singh <manish.singh@oracle.com>
- Initial rpm spec
