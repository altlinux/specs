Name: netatalk
Version: 3.1.13
Release: alt1

Summary: Open Source Apple Filing Protocol(AFP) File Server

License: GPLv2+
Group: Networking/Other
Url: http://netatalk.sourceforge.net

Source0: http://download.sourceforge.net/netatalk/netatalk-%version.tar.bz2
Source1: netatalk.pam-system-auth
Patch0: netatalk-3.0.1-basedir.patch
Patch1: netatalk-3.1.12-alt-mysql8-transition.patch
Patch2: netatalk-3.1.12-afpstats-python3-compat.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: cracklib-devel flex libacl-devel libattr-devel libavahi-devel
BuildRequires: libdb4-devel libdbus-glib-devel libevent-devel libgcrypt-devel
BuildRequires: libkrb5-devel libldap-devel libmysqlclient-devel libpam-devel
BuildRequires: libssl-devel libtdb-devel perl-bignum perl-IO-Socket-INET6

%description
Netatalk is a freely-available Open Source AFP file server. A *NIX/*BSD
system running Netatalk is capable of serving many Macintosh clients
simultaneously as an AppleShare file server (AFP).

%package devel
Summary: Development files for %name
Requires: %name = %EVR
Group: Development/C

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup

# use system libevent instead
rm -frv libevent/

%patch0 -p1
%patch1 -p0
%patch2 -p1

# Avoid re-running the autotools
touch -r aclocal.m4 configure configure.ac macros/gssapi-check.m4

# fix permissions
find include \( -name '*.h' -a -executable \) -exec chmod -x {} \;

# py2 -> py3
sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ \( -name '*.py' -o -name 'afpstats' \))

%build
%add_optflags -fcommon
%configure \
        --localstatedir=%_localstatedir             \
        --with-acl                                  \
        --with-cracklib                             \
        --with-docbook                              \
        --with-kerberos                             \
        --with-libgcrypt                            \
        --with-pam                                  \
        --with-pkgconfdir=%_sysconfdir/netatalk/    \
        --with-shadow                               \
        --with-tbd=no                               \
        --with-uams-path=%_libdir/netatalk          \
        --enable-pgp-uam                            \
        --enable-shared                             \
        --enable-krbV-uam                           \
        --enable-overwrite                          \
        --with-init-style=redhat-systemd            \
        --with-spotlight                            \
        --with-dbus-daemon=/usr/bin/dbus-daemon     \
        --without-libevent                          \
        --with-libevent-header=%_includedir         \
        --with-libevent-lib=%_libdir                \
        --without-tdb                               \
        --with-bdb                                  \
        --disable-silent-rules                      \
        --disable-static

%make_build

# Build the local docs.
make -C doc/manual html-local

%install
%makeinstall_std
# Ghost lock dir.
mkdir -p %buildroot/var/lock/netatalk

# Use specific pam conf.
install -pm644 %SOURCE1 %buildroot%_sysconfdir/pam.d/netatalk

find %buildroot -name '*.la' -delete -print

%check
sh test/afpd/test.sh

%files
%doc AUTHORS CONTRIBUTORS NEWS COPYING COPYRIGHT doc/manual/*.html
%config(noreplace) %_sysconfdir/dbus-1/system.d/netatalk-dbus.conf
%dir %_sysconfdir/netatalk
%config(noreplace) %_sysconfdir/netatalk/afp.conf
%config(noreplace) %_sysconfdir/netatalk/dbus-session.conf
%config(noreplace) %_sysconfdir/netatalk/extmap.conf
%config(noreplace) %_sysconfdir/pam.d/netatalk
%_bindir/*
%exclude %_bindir/netatalk-config
%_libdir/netatalk/
%_libdir/libatalk.so.*
%_mandir/man*/*
%exclude %_mandir/man*/netatalk-config*
%_sbindir/*
%ghost %dir /var/lock/netatalk
/usr/lib/systemd/system/netatalk.service
%exclude %_localstatedir/netatalk/CNID/README
%exclude %_localstatedir/netatalk/README

%files devel
%_bindir/netatalk-config
%_datadir/aclocal/netatalk.m4
%_includedir/atalk/
%_libdir/libatalk.so
%_mandir/man*/netatalk-config.1*

%changelog
* Thu Nov 17 2022 Yuri N. Sedunov <aris@altlinux.org> 3.1.13-alt1
- 3.1.13 (fixed CVE-2021-31439, CVE-2022-23121, CVE-2022-23122,
  CVE-2022-23123, CVE-2022-23124, CVE-2022-23125 and CVE-2022-0194)

* Wed May 12 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.12-alt5
- Fixed FTBFS.

* Fri Mar 26 2021 Grigory Ustinov <grenka@altlinux.org> 3.1.12-alt4
- Fixed FTBFS with -fcommon

* Mon Oct 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 3.1.12-alt3
- python2 -> python3

* Tue Feb 05 2019 Nikolai Kostrigin <nickel@altlinux.org> 3.1.12-alt2
- Fix FTBFS against libmysqlclient21

* Wed Dec 26 2018 Grigory Ustinov <grenka@altlinux.org> 3.1.12-alt1
- Build new version.

* Fri Oct 12 2018 Grigory Ustinov <grenka@altlinux.org> 3.1.11-alt1
- Build new version.

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
