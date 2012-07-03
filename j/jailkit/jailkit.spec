Name: jailkit
Version: 2.5
Release: alt1.1.1

Summary: utilities for jailing a user or process
License: GPL
Group: File tools
URL: http://olivier.sessink.nl/jailkit/ 
Packager: George Litvinov <litvinovg@altlinux.org>

Source: %name-%version.tar

BuildRequires: glibc libtool-common pkgconfig python

%description 
Jailkit is a set of utilities to limit user accounts to a specific directory and to specific commands. Setting up a jail is a lot easier using these utilities. A jail is a directory in your system, and the user cannot see/do anything outside that directory. The user is jailed in the directory. The chroot(2) system call is used to put the user inside the jail..

%prep
%setup -v

%build
%configure
%make_build

%install
%make install DESTDIR=%buildroot install

%files 
%_sysconfdir/jailkit
%_sbindir/jk_addjailuser
%_bindir/jk_uchroot
%_sbindir/jk_check
%_sbindir/jk_chrootlaunch
%_sbindir/jk_chrootsh
%_sbindir/jk_cp
%_sbindir/jk_init
%_sbindir/jk_jailuser
%_sbindir/jk_list
%_sbindir/jk_lsh
%_sbindir/jk_socketd
%_sbindir/jk_update
%_datadir/jailkit
%_man8dir/jailkit.8.gz
%_man8dir/jk_addjailuser.8.gz
%_man8dir/jk_check.8.gz
%_man8dir/jk_chrootlaunch.8.gz
%_man8dir/jk_chrootsh.8.gz
%_man8dir/jk_cp.8.gz
%_man8dir/jk_init.8.gz
%_man8dir/jk_jailuser.8.gz
%_man8dir/jk_list.8.gz
%_man8dir/jk_lsh.8.gz
%_man8dir/jk_socketd.8.gz
%_man8dir/jk_uchroot.8.gz
%_man8dir/jk_update.8.gz

%changelog
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.5-alt1.1.1
- Rebuild with Python-2.7

* Wed Dec 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Sun Jan 20 2009 Litvinov George <litvinovg@altlinux.org> 2.5-alt1
- initial build for altlinux
