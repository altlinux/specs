%def_without tcl
%def_with python

Name: pilot-link
Version: 0.12.5
Release: alt1.1.1

Summary: File transfer utilities between Linux and PalmPilots
License: GPL
Group: Communications

URL: http://www.pilot-link.org/
Source: http://downloads.pilot-link.org/pilot-link-%version.tar.bz2

# from Fedora
Patch1: pilot-link-0.12.1-var.patch
Patch2: pilot-link-0.12.2-open.patch
Patch3: pilot-link-0.12.3-clio.patch
Patch4: pilot-link-0.12.5-mp.patch
Patch5: pilot-link-0.12.5-redefinePerlsymbols.patch

Requires: lib%name = %version-%release

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: libbluez-devel libpng-devel libpopt-devel libreadline-devel libusb-compat-devel perl-devel

%if_with tcl
BuildRequires: tcl-devel tk
%endif

%if_with python
BuildRequires: python-devel
%endif

%description
This suite of tools allows you to upload and download programs and
data files between a Linux/UNIX machine and the PalmPilot.  It has a
few extra utils that will allow for things like syncing the
PalmPilot's calendar app with Ical.  Note that you might still need to
consult the sources for pilot-link if you would like the Python, Tcl,
or Perl bindings.

Install pilot-link if you want to synchronize your Palm with your Operating System.

%package -n lib%name
Summary: Shared libraries to use pilot-link
Group: System/Libraries
License: LGPL
PreReq: %_sysconfdir/udev/rules.d

%description -n lib%name
Shared libraries needed to use pilot-link.

%package -n lib%name-devel
Summary: PalmPilot development files
Group: Development/C
License: LGPL
Requires: lib%name = %version-%release
Provides: %name-devel = %version
Obsoletes: %name-devel < %version

%description -n lib%name-devel
This package contains the header and other files that are necessary to build
applications that use pilot-link suite.

You'll need to install libpilot-link-devel if you want to develop
PalmPilot synchronizing applications.

%package -n pilot-debug
Summary: Programs to interact with Palm debug monitor.
Group: Development/Other
Requires: lib%name = %version-%release

%description -n pilot-debug
This package contains utilities that provide command line and
graphical interfaces to the Palm debug monitor.

%package -n perl-%name
Summary: Pilot-link perl bindings
Group: Development/Other
Requires: lib%name = %version-%release

%description -n perl-%name
This package contains pilot-link perl bindings.

%if_with python
%package -n python-module-%name
Summary: Pilot-link python bindings
Group: Development/Other
Requires: lib%name = %version-%release

%description -n python-module-%name
This package contains pilot-link python bindings.
%endif

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%autoreconf
%configure \
	--disable-static \
	--enable-conduits \
	--enable-threads \
	--enable-libusb \
%if_with python
	--with-python \
%endif
	--with-perl \
%if_with tcl
	--with-tcl=%_libdir \
%endif
	--with-libpng

%make_build

%install
%make_install DESTDIR=%buildroot install
# mandir1='$(mandir)/man1' mandir7='$(mandir)/man7' INSTALL="./libtool /usr/bin/install -p"

mkdir -p %buildroot%_sysconfdir/udev/rules.d
install -p -m644 doc/60-libpisock.rules %buildroot%_sysconfdir/udev/rules.d/75-lib%name.rules

%files
%_bindir/pilot-*
%exclude %_bindir/pilot-debugsh
%if_with tcl
%_bindir/pitclsh
%endif
%_datadir/%name
%doc AUTHORS NEWS doc/*

%files -n lib%name
%_sysconfdir/udev/rules.d/*
%_libdir/libpisock.so.*
%_libdir/libpisync.so.*
%if_with tcl
%_libdir/libpitcl*.so.*
%endif

%files -n lib%name-devel
%_datadir/aclocal/*
%_libdir/libpisock.so
%_libdir/libpisync.so
#_libdir/libpisock++.so
%if_with tcl
%_libdir/libpitcl*.so
%endif
%_includedir/*
%_pkgconfigdir/pilot-link.pc

%files -n pilot-debug
%_bindir/pilot-debugsh

%files -n perl-%name
%perl_vendor_archlib/PDA
%perl_vendor_autolib/PDA

%if_with python
%files -n python-module-%name
%python_sitelibdir/*pisock*
%endif

%changelog
* Mon Apr 16 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.5-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 27 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.12.5-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.12.5-alt1
- 0.12.3 -> 0.12.5
- added patches from Fedora
- built for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12.3-alt2.2
- rebuilt with perl 5.12

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.12.3-alt2.1.1
- Rebuilt with python 2.6

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 0.12.3-alt2.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libpilot-link
  * postun_ldconfig for libpilot-link

* Sun Oct 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 0.12.3-alt2
- Fix FTBFS in current Sisyphus (O_CREAT needs mode set).

* Tue Dec 04 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.12.3-alt1
- 0.12.3 release.

* Thu Apr 12 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.12.2-alt2
- Backport fix for .m4 files from CVS HEAD.

* Tue Feb 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.12.2-alt1
- 0.12.2 release.

* Fri Oct 20 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.12.1-alt2
- Merged fixes by raorn@:
  + Fix udev rules.
  + Changed group "dialout" to "uucp". Rule file prioroty raized to
	75 (70-permissions.rules will drop it ,suggested by vsu@).
  + Moved rule file to libpilot-link package and made it "%%config".
  + Changed BUS && ACTION condition to SUBSYSTEM || ACTION
	(suggested by vsu@). 
  + PreReq on %_sysconfdir/udev/rules.d/, do not provide it.

* Sun Oct 01 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.12.1-alt1
- New version: 0.12.1 "Fresh Air". 

* Mon Jun 05 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.12.0-alt0.pre4.1
- New version: 0.12.0-pre4 "Anoxia".
- Some spec cleanup.
- Removed examples subpackage.
- Added perl and python bindings subpackages.
- Building without tcl as it's borken for now.
- Added libusb-devel to BuildRequires, enabling libusb support.
- Added libpopt-devel to BuildRequires, using system popt for now.
- %%files changes compared to previous build in pilot-link package:
  - %%_bindir/addresses
  - %%_bindir/money2qif
  - %%_bindir/pilot-archive
  - %%_bindir/pilot-datebook
  - %%_bindir/pilot-prc
  - %%_libdir/libpisock++*
  + %%_bindir/ietf2datebook
  + %%_bindir/pilot-treofoto
  + %%_bindir/pilot-undelete
  + %%_bindir/pilot-wav
  + %%_bindir/sync-plan

* Fri Dec 30 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.11.8-alt1.1.1
- Rebuilt with libreadline.so.5.

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.11.8-alt1.1
- Rebuilt with libstdc++.so.6.

* Sun Jan 25 2004 Anatoly Yakushin <jaa@altlinux.ru> 0.11.8-alt1
- new version, delete static lib

* Thu Oct 24 2002 AEN <aen@altlinux.ru> 0.11.5-alt3
- added missing libpisock++.so.*

* Thu Oct 24 2002 AEN <aen@altlinux.ru> 0.11.5-alt2
- added missing libpisync.so.*

* Tue Oct 15 2002 Alexander Bokovoy <ab@altlinux.ru> 0.11.5-alt1
- 0.11.5
- new maintainer
- Removed:
    + Tcl, Perl, Python bindings removed due their unmaintained state

* Sat Oct  5 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.9.5-ipl12mdk
- rebuilt with tcl 8.4

* Thu Jul 18 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.5-ipl11mdk
- Rebuild with terminfo
- Fixed buildrequires

* Fri Jun 14 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.9.5-ipl10mdk
- rebuilt in new env

* Tue Mar 05 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.9.5-ipl9mdk
- Fixed .libs tcl patch
- Added some MDK patches

* Wed Aug 15 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.5-ipl8mdk
- Fixed file lists - moved some perl programs from pilot-link to perl-PDA-pilot

* Sat Aug 11 2001 Mikhail Zabaluev <mhz@altlinux.ru> 0.9.5-ipl7mdk
- Removed the most ugly Perl hacks
- Moved scripts from perl-PDA-Pilot to the main package
- Segregated pilot-debug and examples
- Corrected pixdir patch
- LGPL license for libraries and bindings
- Explicitly disable python bindings to slash off build dependencies
- Excluded libpitcl development files since no external package would care

* Fri Jun 27 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.9.5-ipl6mdk
- Release 0.9.5 version
- Added perl patch
- Added perl-PDA-Pilot & pilot-link-tcl packages
- Some spec cleanup
- Fixed buildrequires

* Thu May 17 2001 AEN <aen@logic.ru> 0.9.5-ipl5mdk
- new prerelease

* Sat Jan 27 2001 Dmitry V. Levin <ldv@fandra.org> 0.9.5-ipl2mdk
- Specfile cleanup.
- Relibification.

* Wed Jan 24 2001 Konstantin Volckov <goldhead@linux.ru.net> 0.9.5-ipl1mdk
- Fixed broken build

* Sat Dec 16 2000 AEN <aen@logic.ru>
- adopted for RE

* Wed Nov 15 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.5-0.3.2mdk
- Rebuild with last stdlibc++
- Split lib package

* Fri Oct 27 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.5-0.3.1mdk
- Release 0.9.5-pre3

* Tue Oct  3 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.3-15mdk
- Remove pilot-bug since it is unusefull and bring tcltk dependences.

* Fri Sep 22 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.3-14mdk
- Move perl part to its own package (which was preventing bootstrapping of package)

* Tue Aug 29 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.3-13mdk
- merge Alpha diff from Stefan van der Eijk

* Mon Aug 28 2000 Frederic Crozat <fcrozat@mandrakesoft.com> 0.9.3-12mdk
- BM + macroszification

* Wed May 17 2000 David BAUENS <baudens@mandrakesoft.com> 0.9.3-11mdk
- Fix build for i486

* Thu Apr 13 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.9.3-10mdk
- fix group

* Tue Mar 28 2000 Pixel <pixel@mandrakesoft.com> 0.9.3-9mdk
- cleanup
- patch for perl 5.6
- rebuild for new readline

* Tue Mar 21 2000 Yoann Vandoorselaere <yoann@mandrakesoft.com> 0.9.3-8mdk
- Fix group.

* Thu Jan 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.3-7mdk
- libtoolize --force.

* Sat Dec 18 1999 John Buswell <johnb@mandrakesoft.com>
- Fixes sync-plan
- Fixed spec to build and install perl modules

* Sat Nov  6 1999 John Buswell <johnb@mandrakesoft.com>
- Build Release

* Tue Nov  2 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 0.9.3.
- Fix building as user.
- Rewrote spec.

* Wed May 05 1999 Bernhard Rosenkränzer <bero@mandrakesoft.com>
- Mandrake adaptions
- handle RPM_OPT_FLAGS
- %post / %postun: make -p

* Tue Apr 06 1999 Preston Brown <pbrown@redhat.com>
- strip binaries

* Tue Mar 30 1999 Preston Brown <pbrown@redhat.com>
- added missing files from devel subpackage

* Fri Mar 26 1999 Preston Brown <pbrown@redhat.com>
- move /usr/lib/pix to /usr/lib/pilot-link (dumb, BAD name)

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 5)

* Wed Feb 24 1999 Preston Brown <pbrown@redhat.com>
- Injected new description and group.

* Thu Jan 21 1999 Bill Nottingham <notting@redhat.com>
- arm fix

* Fri Sep 24 1998 Michael Maher <mike@redhat.com>
- cleaned up spec file, updated package

* Tue May 19 1998 Michael Maher <mike@redhat.com>
- updated rpm

* Thu Jan 29 1998 Otto Hammersmith <otto@redhat.com>
- added changelog
- updated to 0.8.9
- removed explicit requires for /usr/bin/perl
