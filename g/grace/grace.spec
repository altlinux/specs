%def_with netcdf
%def_without pdflib
%def_with lpr

Name: grace
Version: 5.1.25
Release: alt4

Summary: WYSIWYG tool to make two-dimensional plots of scientific data
License: GPL
Group: Sciences/Mathematics

Url: http://plasma-gate.weizmann.ac.il/Grace/
Source: ftp://plasma-gate.weizmann.ac.il/pub/grace/src/grace5/%name-%version.tar.gz
Source4: grace.desktop
Source5: grace.xpm
Source6: grace-32.xpm
Source7: grace-set_default_enc
Patch1: grace-5.1.9-alt1-alt-makefile-bindir.patch
Patch2: grace-5.1.9-alt1-alt-makefile-install_GRACECLI.patch
Patch3: grace-5.1.9-alt1-alt-makefile-install_man.patch
Patch4: grace-5.1.9-alt1-alt-makefile-install_grace_np.patch
Patch5: grace-5.1.11-alt1-alt-makefile-font_links.patch
Patch6: grace-5.1.9-alt1-alt-config-gracerc.patch
Patch7: grace-5.1.22-alt-libpng15.patch
Packager: Michael Shigorin <mike@altlinux.org>

Requires: fonts-type1-urw >= 1.0.7
Requires: url_handler >= 0.2.1

BuildPreReq: libXext-devel

# Automatically added by buildreq on Sun Aug 31 2014
# optimized out: fontconfig gnu-config groff-base libICE-devel libSM-devel libX11-devel libXau-devel libXt-devel libcloog-isl4 libhdf5-8-seq libnetcdf7-seq libopenmotif-devel sgml-common t1lib tex-common texlive-base texlive-base-bin texlive-common texlive-generic-recommended texlive-latex-base texlive-latex-recommended texlive-xetex xorg-printproto-devel xorg-xproto-devel zlib-devel
BuildRequires: OpenSP imake libXbae-devel libXext-devel libXmu-devel libXp-devel libXpm-devel libfftw3-devel libjpeg-devel libnetcdf-devel libpng-devel linuxdoc-tools t1lib-devel xorg-cf-files

BuildRequires: sgml-tools texlive-latex-recommended

%{?_with_pdflib:BuildRequires: libpdflib-lite-devel}
%{?_with_lpr:BuildRequires: /usr/bin/lpr}
# argh
%{?_with_netcdf:BuildRequires: libnetcdf-devel}
%{?_with_netcdf:Requires: libnetcdf libhdf5}
# no need this conflict now
#{?_with_netcdf:Conflicts: libnetcdf-mpi libhdf5-mpi mpi-selector openmpi}

Summary(ru_RU.UTF-8): WYSIWYG-средство для подготовки двумерных графиков

%description
Grace is a tool to make two-dimensional plots of numerical data. It runs
under various (if not all) flavours of UNIX with X11 and M*tif. Its
capabilities are roughly similar to GUI-based programs like Sigmaplot or
Microcal Origin plus script-based tools like gnuplot or Genplot. Its
strength lies in the fact that it combines the convenience of a
graphical user interface with the power of a scripting language which
enables it to do sophisticated calculations or perform automated tasks.

%description -l ru_RU.UTF-8
Grace -- это программа для подготовки двумерных графиков по численным
данным. Она работает на множестве (если не на всех) разновидностей UNIX,
где есть X11 и M*tif. Возможности этой программы аналогичны таким
программам, как Sigmaplot или Microcal Origin, однако, сочетают в себе и
возможности таких программ, как gnuplot или Genplot.  Мощь этой
программы состоит в том, что она сочетает в себе удобство графического
интерфейса с большими возможностями языка сценариев, что позволяет
проводить сложные вычисления или делать автоматическую обработку.

%package devel
Summary: A library for interfacing with Grace using pipes
Summary(ru_RU.UTF-8): Библиотека для взаимодействия с Grace через каналы (pipes)
Group: Development/C
Requires: %name = %version-%release

%description devel
A library for interfacing with Grace using pipes

%description -l ru_RU.UTF-8 devel
Библиотека для взаимодействия с Grace через каналы (pipes)

%prep
%setup -n %name-%version
%patch1 -p1
%patch2 -p1
#patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
#patch7 -p2
cp -a %SOURCE7 set_default_enc

%build
%add_optflags -I%_includedir/netcdf-3
%configure \
	--prefix=%_datadir \
        --with-bundled-xbae=no \
	%{subst_enable netcdf} \
	--enable-xmhtml=no \
	--with-helpviewer="url_handler.sh %%s" \
	--with-printcmd="lpr" \
	--enable-grace-home=%_datadir/grace
%make_build

%install
# NB: it's _not_ %%makeinstall_std unfortunately
%makeinstall DESTDIR=%buildroot

mkdir -p %buildroot%_man1dir
install -pm644 doc/*.1 %buildroot%_man1dir

install -pm755 set_default_enc %buildroot%_datadir/grace/auxiliary/
ln -s ../../doc/%name-%version/doc %buildroot%_datadir/grace/doc
# UTF-8.enc missing by 5.1.23
#ln -s UTF-8.enc %buildroot%_datadir/grace/fonts/enc/Default.enc

install -pDm644 %SOURCE4 %buildroot%_desktopdir/%name.desktop
install -pDm644 %SOURCE5 %buildroot%_miconsdir/%name.xpm
install -pDm644 %SOURCE6 %buildroot%_niconsdir/%name.xpm
install -pDm644 %SOURCE6 %buildroot%_liconsdir/%name.xpm

%post
GRACE_HOME=%_datadir/grace %_datadir/grace/auxiliary/set_default_enc

%triggerpostun -- grace < 5.1.9-alt2
GRACE_HOME=%_datadir/grace %_datadir/grace/auxiliary/set_default_enc

%files
%_bindir/*
%dir %_datadir/grace
%_datadir/grace/*
%_man1dir/*
%_desktopdir/*
%_niconsdir/*.xpm
%_miconsdir/*.xpm
%_liconsdir/*.xpm
%doc doc CHANGES COPYRIGHT LICENSE src/XMgrace.ad

%files devel
%dir %_libdir/grace
%dir %_includedir/grace
%_libdir/grace/*
%_includedir/grace/*

# TODO:
# - build with XmHTML, PDFlib (which are currently orphaned)
# - look into printing support

%changelog
* Mon Dec 25 2017 Michael Shigorin <mike@altlinux.org> 5.1.25-alt4
- build against fftw3 instead of fftw

* Tue Aug 29 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.1.25-alt3
- Rebuilt with libnetcdf11.

* Mon Jan 09 2017 Michael Shigorin <mike@altlinux.org> 5.1.25-alt2
- fixed FTBFS (by dropping BR: lprng; default to "lpr")

* Mon Feb 16 2015 Michael Shigorin <mike@altlinux.org> 5.1.25-alt1
- new version 5.1.25

* Sun Aug 31 2014 Michael Shigorin <mike@altlinux.org> 5.1.24-alt1
- new version 5.1.24
- disabled patch3
- fixed doc symlink
- buildreq

* Fri Jun 20 2014 Michael Shigorin <mike@altlinux.org> 5.1.23-alt1
- new version 5.1.23
  + dropped patch7
- enable printing support by default
- minor spec fixups

* Thu Jul 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt9.5
- Requires: libhdf5-8

* Tue Jul 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt9.4
- Rebuilt with new libhdf5

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt9.3
- Rebuilt with libpng15

* Tue Sep 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt9.2
- Rebuilt with libhdf5-7

* Sun Apr 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt9.1
- Rebuilt with libnetcdf7

* Wed Mar 30 2011 Michael Shigorin <mike@altlinux.org> 5.1.22-alt9
- re-disabled pdflib support by default as it's still non-free

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt8
- Rebuilt for debuginfo
- Enabled PDFlib support

* Fri Nov 26 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.1.22-alt7
- Rebuilt for soname set-versions

* Tue Jun 23 2009 Terechkov Evgenii <evg@altlinux.ru> 5.1.22-alt6
- Rebuilt against new libpng

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 5.1.22-alt5
- argh, apt selects libnetcdf6-mpi from multiple providers;
  resorting to conditional Conflicts:, better ideas are welcome
  (libnetcdf*/libhdf* side probably)

* Sat Jun 06 2009 Michael Shigorin <mike@altlinux.org> 5.1.22-alt4
- fixed Group:
- build with netcdf by default (thanks real@ for openmpi fixups)
- optional pdflib support (disabled by default: non-free library)

* Wed Jun 03 2009 Michael Shigorin <mike@altlinux.org> 5.1.22-alt3
- optional netcdf support (disabled by default: pulls openmpi in)
- use system provided Xbae instead of a bundled copy

* Thu May 21 2009 Michael Shigorin <mike@altlinux.org> 5.1.22-alt2
- rebuilt against libXm.so.4

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 5.1.22-alt1
- 5.1.22
- adopted an orphan
  + need to deorphan libnetcdf, XmHTML; maybe PDFlib [non-free]
    for more features
- dropped debian menufile
- added desktop file from PLD
- dubbed 32x32 icon as 64x64 (ouch!)
- spec cleanup
- buildreq

* Sun Oct 29 2006 Yury A. Zotov <yz@altlinux.ru> 5.1.20-alt3
- use libfftw again

* Sat Oct 14 2006 Yury A. Zotov <yz@altlinux.ru> 5.1.20-alt2
- do not use libfftw and libnetcdf

* Thu Jun 08 2006 Yury A. Zotov <yz@altlinux.ru> 5.1.20-alt1
- new version
- symlinks to fonts are updated
- Requires: fonts-type1-urw

* Sun Feb 26 2006 Yury A. Zotov <yz@altlinux.ru> 5.1.19-alt1
- new version
- BuildRequires is updates
- grace-5.1.9-alt1-alt-configure-helpviewer.patch is removed

* Mon Feb 21 2005 Yury A. Zotov <yz@altlinux.ru> 5.1.18-alt1
- new version

* Sat Aug 28 2004 Yury A. Zotov <yz@altlinux.ru> 5.1.17-alt1
- new version

* Sat Jun 19 2004 Yury A. Zotov <yz@altlinux.ru> 5.1.15-alt1
- new version

* Wed Oct 29 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.13-alt3
- build with openmotif

* Sat Oct 18 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.13-alt2
- rebuild with t1lib-5.0.0

* Fri Oct 17 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.13-alt1
- 5.1.13

* Fri Apr 11 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.12-alt3
- now set_default_encoding script handles multiple entries
  of locales in LANGUAGE variable from %_sysconfdir/sysconfig/i18n

* Thu Apr 10 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.12-alt2
- default encoding is deduced from value of LANGUAGE variable
  from %_sysconfdir/sysconfig/i18n
- added Requires: urw-fonts >= 2.0

* Mon Feb 24 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.12-alt1
- new version
- Source6: grace-set_default_enc is Source7 now
- workaround for IsoLatin7.enc removed

* Sun Jan 26 2003 Yury A. Zotov <yz@altlinux.ru> 5.1.11-alt1
- new version
- russian and ukrainian encoding files are removed from
  sources because they are in main grace source now
- all symbolic links are relative

* Sun Oct 13 2002 Yury A. Zotov <yz@altlinux.ru> 5.1.10-alt1
- new version
- build with gcc3.2

* Fri Aug 30 2002 Yury A. Zotov <yz@altlinux.ru> 5.1.9-alt2
- build with FFTW library (libfftw)

* Wed Aug 14 2002 Yury A. Zotov <yz@altlinux.ru> 5.1.9-alt1
- new version

* Thu Jun 13 2002 Yury A. Zotov <yz@altlinux.ru> 5.1.8-alt2
- Default.enc removed if exists before creating
- needs=x11 rather than needs=text in grace.menu

* Thu Jun 13 2002 Yury A. Zotov <yz@altlinux.ru> 5.1.8-alt1
- initial version
