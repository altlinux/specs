%define build_static 0

Name: netatalk
Version: 2.2.4
Release: alt2

Summary: AppleTalk networking programs
License: GPL, BSD
Group: Networking/Other

Url: http://netatalk.sourceforge.net
Source0: %name-%version.tar
Source1: atalk.init
Source2: netatalk.pamd

BuildRequires: libdb4-devel libpam-devel libwrap-devel zlib-devel
BuildRequires: libgcrypt-devel
BuildRequires: libssl-devel
BuildRequires: perl-bignum

%description
This package enables Linux to talk to Macintosh computers via the
AppleTalk networking protocol. It allows Linux to act as a file server
over AppleTalk or IP for Macs.

Netatalk is available under the GPL and BSD licenses.

%package devel
Summary: Headers and shared libraries for AppleTalk development
Group: Development/C
Requires: %name = %version-%release
Requires: libpam-devel libssl-devel libwrap-devel libacl-devel libattr-devel automake-common
BuildArch: noarch

%description devel
This package contains the header files and shared libraries for building
AppleTalk networking programs

%if %build_static
%package devel-static
Summary: Static libraries for AppleTalk development
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains static libraries for building
AppleTalk networking programs
%endif

%prep
%setup -n %name-%version

# rename uniconv -> uniconv_netatalk
# to prevent filename conflict with uniconvertor
sed -i "s|uniconv|uniconv_netatalk|" man/man1/uniconv.1.tmpl

#remove lp2pap
#sed -i "s| lp2pap|#lp2pap|" contrib/shell_utils/Makefile.am

%build
%autoreconf
%configure \
	--with-pam=yes \
	--enable-ddp \
	--enable-redhat-sysv \
	--with-shadow \
	--enable-fhs \
	--with-cnid-cdb-backend \
	--with-cnid-dbd-backend \
	--with-cnid-last-backend \
	--enable-acl \
	--libexecdir=%_bindir \
	--localstatedir=%_var \
%if %build_static
	--enable-static
%else
	--disable-static
%endif
%make_build

%install
mkdir -p %buildroot{%_sysconfdir/{netatalk,pam.d},%_initdir,%_libdir/netatalk}
mkdir -p %buildroot{%_man1dir,%_man3dir,%_man4dir,%_man8dir}
%make_install install DESTDIR=%buildroot
rm -f %buildroot%_bindir/acleandir.rc
rm -f %buildroot%_includedir/netatalk/at.h
# override RH-style initscript
install -pD -m755 %SOURCE1 %buildroot%_initdir/atalk
# ...and PAM configuration as well
install -pD -m644 %SOURCE2 %buildroot%_sysconfdir/pam.d/%name
# rename uniconv -> uniconv_netatalk
# to prevent filename conflict with uniconvertor
mv %buildroot%_bindir/uniconv %buildroot%_bindir/uniconv_netatalk
mv %buildroot%_man1dir/uniconv.1 %buildroot%_man1dir/uniconv_netatalk.1

%post
%post_service atalk

%preun
%preun_service atalk

%files
%dir %_sysconfdir/%name
%dir %_libdir/%name
%config(noreplace) %_sysconfdir/%name/*
%config %_initdir/atalk
%exclude %_initdir/netatalk
%config %_sysconfdir/pam.d/%name
%_bindir/*
%_sbindir/*
%_mandir/man?/*
%_libdir/%name/*.so
%_datadir/%name/
%doc CONTRIBUTORS COPYING COPYRIGHT NEWS
%doc doc/DEVELOPER doc/README.*
%exclude %_libdir/libatalk.a
%exclude %_libdir/%name/*.la

%files devel
%dir %_includedir/atalk
%dir %_includedir/netatalk
%_includedir/atalk/*
%_includedir/netatalk/*
%_datadir/aclocal/*

%if %build_static
%files devel-static
%_libdir/libatalk.a
%_libdir/%name/*.a
%endif


%changelog
* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.4-alt2
- Fixed localstatedir location.

* Sat Apr 16 2016 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.2.4-alt1.qa1
- NMU: rebuilt with libgcrypt.so.11 -> libgcrypt.so.20.

* Sat Dec  8 2012 Sergey Kurakin <kurakin@altlinux.org> 2.2.4-alt1
- 2.2.4
- cups support removed
- legacy AppleTalk support presents, but disabled
  in default configuration. PAP too

* Sun Apr  3 2011 Sergey Kurakin <kurakin@altlinux.org> 2.0.5-alt2
- lsb-header added
- SysVinit header corrected: don't start atalk by default
- fix DHCAST128 UAM build (buildreq)

* Mon Mar 28 2011 Michael Shigorin <mike@altlinux.org> 2.0.5-alt1.3
- devel subpackage made noarch

* Sun Mar 27 2011 Michael Shigorin <mike@altlinux.org> 2.0.5-alt1.2
- re-added lost BR:

* Mon Oct  4 2010 Sergey Kurakin <kurakin@altlinux.org> 2.0.5-alt1.1
- rebuild with new openssl (libcrypto soname change)

* Tue Dec 22 2009 Sergey Kurakin <kurakin@altlinux.org> 2.0.5-alt1
- 2.0.5:
  + fix CVE-2008-5718
  + more bugfixes

* Tue Nov 10 2009 Sergey Kurakin <kurakin@altlinux.org> 2.0.4-alt3
- rebuild with current libdb version

* Mon Jun  8 2009 Sergey Kurakin <kurakin@altlinux.org> 2.0.4-alt2
- 2.0.4 release
  + bug fixes, new configuration options, new encodings
  + timeout program removed (now is part of coreutils)
- minor fixes in initscript

* Sat Jan 31 2009 Sergey Kurakin <kurakin@altlinux.org> 2.0.4-alt1.beta2
- 2.0.4beta2 features new configuration options
  working around with MacOS 10.5 Leopard permission issues

* Fri Mar 21 2008 Sergey Kurakin <kurakin@altlinux.org> 2.0.3-alt8
- build fixed: libgnutls-devel added to BuildRequires
- libatalk.a moved from -devel to -devel-static subpackage

* Tue Jan  8 2008 Sergey Kurakin <kurakin@altlinux.org> 2.0.3-alt7
- resolved filename conflict with uniconvertor package:
  uniconv (netatalk volume encoding convertor) renamed
  to uniconv_netatalk

* Sun Dec  2 2007 Sergey Kurakin <kurakin@altlinux.org> 2.0.3-alt6
- fix initscripts to run cnid_metad daemon,
  needed for "dbd" CNID scheme to work
- replaced obsolete configure parameter "--with-did"

* Tue May 15 2007 Michael Shigorin <mike@altlinux.org> 2.0.3-alt5
- accepted spec fixes and improvements (see #11772):
  + Tue May 14 2007 Sergey Kurakin <kurakin@quittance.ru> 2.0.3-alt5
  - fixed x86_64 build
  - the same time, figured out, what's up with %_libdir stuff
  - CUPS support enabled
  - added BuildRequires: zlib-devel, needed for CUPS support
- removed what got commented out
- buildreq (added libcups-devel too)

* Fri Mar 30 2007 Michael Shigorin <mike@altlinux.org> 2.0.3-alt4
- investigated licensing question:
  + source tarball contains both GPL (COPYING) and BSD (COPYRIGHT)
  + Fedora ships as GPL
  + Mandriva ships as BSD
  + http://sourceforge.net/projects/netatalk/ mentions both
  * changed License: to "GPL, BSD" so users can choose themselves

* Tue Mar 27 2007 Sergey Kurakin <kurakin@quittance.ru> 2.0.3-alt3
- proper libdb4.3+ patch instead of invalid in 2.0.1-alt2
- license is GNU GPL in fact

* Mon Mar 26 2007 Michael Shigorin <mike@altlinux.org> 2.0.3-alt2
- built for ALT Linux Sisyphus; based on spec+patch by Sergey Kurakin
  (in its turn based on ApplianceWare 1.5.x package)
- introduced devel-static subpackage (not built by default)
- added devel subpackages Requires: (based on 1.5.3-alt13)
- replaced RH-style initscript and PAM configuration by conforming
  ones (from 1.5.3-alt13; courtesy of Alexander Bokovoy and
  Ihar Viarheichyk)
- fixed mandir directory intersections with filesystem
- minor spec cleanup
- buildreq

* Thu Mar 22 2007 Sergey Kurakin <kurakin@quittance.ru> 2.0.3-alt1.3
- just rebuild
* Sun Apr  2 2006 Sergey Kurakin <kurakin@actdesign.com> 2.0.3-alt1.2
- rebuild
* Mon Jun 13 2005 Sergey Kurakin <kurakin@actdesign.com> 2.0.3-alt1
- new version
* Sat Jun 11 2005 Sergey Kurakin <kurakin@actdesign.com> 2.0.1-alt3
- rebuild
* Sat Feb 26 2005 Sergey Kurakin <kurakin@actdesign.com> 2.0.1-alt2
- rebuild with libdb4.3
* Sun Oct 31 2004 Sergey Kurakin <kurakin@actdesign.com> 2.0.1-alt1
- new version
- added documentation
* Mon Jul 26 2004 Sergey Kurakin <kurakin@actdesign.com> 2.0-beta2
- new version

* Thu Mar 25 2004 Alexander Bokovoy <ab@altlinux.ru> 1.5.3-alt13
- Fixed:
    + Build against GCC 3.3
    + License is GNU GPL in fact
    + PAM service conforms to ALT PAM Policy now

* Fri Oct 31 2003 Alexander Bokovoy <ab@altlinux.ru> 1.5.3-alt4
- Build for ALT Linux Sisyphus

