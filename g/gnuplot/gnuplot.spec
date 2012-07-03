Name: gnuplot
Version: 4.4.0
Release: alt2
Epoch: 1

Summary: A program for plotting mathematical expressions and data
Summary (ru_RU.UTF-8): Программа для построения графиков математических выражений и данных
License: Freeware-like
Group: Sciences/Other
URL: http://gnuplot.sourceforge.net/
Packager: Alexey Morsov <swi@altlinux.ru>

Source0: %name-%version.tar
Source2: http://www.gnuplot.info/faq/%name-faq.html.bz2
Source3: %name.desktop
Source4: %name.menu

Source10: %name.16.png
Source11: %name.32.png
Source12: %name.48.png

Source14: gnuplot-emacs.el

Patch1: gnuplot-4.2.4-build.alt.patch

BuildRequires(pre): rpm-build-texmf 
BuildPreReq: desktop-file-utils
BuildRequires: gcc-c++ ghostscript-module-X groff-base imake libXt-devel libncurses-devel libreadline-devel tetex-latex xorg-cf-files zlib-devel libgd2-devel libpng-devel libjpeg-devel
BuildRequires: tetex-core tetex-dvips
# for wxt terminal
BuildRequires: libwxGTK-devel libcairo-devel libpango-devel
# for lua/TikZ
BuildRequires: liblua5-devel texmf-pgf

Requires(post,postun): desktop-file-utils 


%package -n emacs-mode-%name
Summary: A GNU Emacs major mode for %name
Summary(ru_RU.UTF-8): Основной режим GNU Emacs для %name
BuildArch: noarch
BuildPreReq: emacs-devel >= 0.0.1-alt2
BuildRequires: emacs-common texinfo
Group: Editors
Requires: %name = %version-%release emacs-base
Obsoletes: emacs-gnuplot <= 0.6.0-alt1
Provides: emacs-gnuplot

%package -n emacs-mode-%name-el
Summary:  The Emacs Lisp sources for bytecode included in emacs-mode-%name
Summary(ru_RU.UTF-8): Исходный код Emacs Lisp для emacs-mode-%name
BuildArch: noarch
Group: Development/Other
Requires: emacs-mode-%name = %version-%release
Obsoletes: emacs-gnuplot <= 0.6.0-alt1
Provides: emacs-gnuplot-el

%description
Gnuplot is a command-line driven, interactive function plotting program
especially suited for scientific data representation. Gnuplot can be used to
plot functions and data points in both two and three dimensions and in many
different formats.

Install gnuplot if you need a graphics package for scientific data
representation.

%description -l ru_RU.UTF-8
Gnuplot это интерактивная программа, предназначенная для построения
графиков.  Она особенно хорошо подходит для представления научных 
данных.  Gnuplot может строить 2-х и 3-х мерные графики функций 
и числовых данных во множестве различных графических форматов.

%description -n emacs-mode-%name
A GNU Emacs major mode for %name

%description -n emacs-mode-%name -l ru_RU.UTF-8
Основной режим GNU Emacs для %name

%description -n emacs-mode-%name-el
The Emacs Lisp sources for bytecode included in %name

%description -n emacs-mode-%name-el -l ru_RU.UTF-8
Исходный код Emacs Lisp для emacs-mode-%name


%prep
%setup -q 
%patch1 -p1


%build
#export CFLAGS="$RPM_OPT_FLAGS -fno-fast-math"
%configure --prefix=%{_prefix} --with-readline=gnu --with-png --with-gif=png --without-linux-vga \
	--with-cdrwc --without-row-help --enable-thin-splines \
	--with-texdir=%buildroot%{_texmfmain}/%{name} \
	--with-lua \
	--with-gihdir=%{name}/4.4/
#find -type f -print0 |
#	xargs -r0 fgrep -l gdImageGif |
#	xargs perl -pi -e 's/gdImageGif/gdImagePng/g'

# due to some problems with building on i586 in SMP mode turn it off to noSMP
%make_build

pushd lisp
	#./configure --prefix=%{_prefix} --datadir=%{_datadir} --with-emacs=emacs --infodir=%{_infodir} \
	./configure --prefix=%{_prefix} --with-emacs=emacs --infodir=%{_infodir} \
	%make_build
popd

install -p -m644 %SOURCE2 .
bunzip *.html.bz2

pushd tutorial
    make pdf
#    pdflatex tutorial
popd

pushd docs
    make pdf
    pdftex gpcard
popd


%install
%makeinstall

pushd lisp
    mkdir -p %buildroot%{_emacslispdir}/%name
    install -m 644 *.el* $RPM_BUILD_ROOT%{_emacslispdir}/%name
    mkdir -p %buildroot/etc/emacs/site-start.d
    install -m 644 %SOURCE14 %buildroot/etc/emacs/site-start.d/gnuplot.el
    %add_lisp_loadpath %buildroot%_emacslispdir/%name
    %byte_recompile_lispdir
    make pdf
    make ps
    mkdir -p %buildroot%_defaultdocdir/emacs-%{name}-%{version}
    install -m 644 COPYING ChangeLog README README.1st gpelcard.pdf gpelcard.ps %buildroot%_defaultdocdir/emacs-%{name}-%{version}/
popd

# menus
install -D -pm644 %SOURCE3  %buildroot%_desktopdir/%name.desktop

# icon
install -D -pm644 %SOURCE10  %buildroot/%_miconsdir/%name.png
install -D -pm644 %SOURCE11  %buildroot/%_niconsdir/%name.png
install -D -pm644 %SOURCE12  %buildroot/%_liconsdir/%name.png


%files
%doc README ChangeLog BUGS Copyright NEWS
%doc demo tutorial/tutorial.pdf gnuplot-faq.html
%doc docs/psdoc docs/gpcard.pdf docs/gnuplot.pdf
%_bindir/*
%_mandir/man?/*
%_libexecdir/%name
%_datadir/%name
%_desktopdir/*
%_infodir/%{name}*
%_niconsdir/*.png
%_miconsdir/*.png
%_liconsdir/*.png
%_texmfmain/%name

%files -n emacs-mode-%name
%dir %_defaultdocdir/emacs-%{name}-%{version}/
%_defaultdocdir/emacs-%{name}-%{version}/*
%dir %_emacslispdir/*.elc
%_emacslispdir/%name/*.elc
%config(noreplace) /etc/emacs/site-start.d/gnuplot.el

%files -n emacs-mode-%name-el
%_emacslispdir/*.el
%_emacslispdir/%name/*.el

%changelog
* Fri Mar 26 2010 Alexey Morsov <swi@altlinux.ru> 1:4.4.0-alt2
- add wxt terminal support
- fix .gih file location

* Thu Mar 18 2010 Alexey Morsov <swi@altlinux.ru> 1:4.4.0-alt1
- new version

* Wed Sep 09 2009 Alexey Morsov <swi@altlinux.ru> 1:4.2.6-alt1
- new version
- fix desktop file

* Thu Aug 20 2009 Alexey Morsov <swi@altlinux.ru> 1:4.2.5-alt2
- fix #21142

* Thu Apr 23 2009 Alexey Morsov <swi@altlinux.ru> 1:4.2.5-alt1
- new version

* Thu Dec 11 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.4-alt1
- new version
- remove deprecated macro from post/postun

* Fri Aug 29 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt4.1
- fix build
  + remove _target_cpu macro
  + put make_build macro back

* Tue Aug 19 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt4
- fix build on i586
  + use make instead make_build macro (no smp)

* Wed Aug 13 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt3
- fix build
  + get support for png/jpeg terminal back

* Tue Jun 24 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt2
- build emacs-mode-gnuplot (obsolute emacs-gnuplot)

* Fri May 16 2008 Alexey Morsov <swi@altlinux.ru> 1:4.2.3-alt1
- new version
- clean build requires
- fix iconsdir to correspond with policy
- patch desktop file to correspond with policy

* Fri Sep 14 2007 Alexey Morsov <swi@altlinux.ru> 1:4.2.2-alt1
- version 4.2.2
- bug fixes

* Thu May 03 2007 Alexey Morsov <swi@altlinux.ru> 1:4.2.0-alt2
- add some configure keys for better ploting and
fixing work with help and CLI (by const@)
- create .desktop 

* Mon Mar 05 2007 Alexey Morsov <swi@altlinux.ru> 1:4.2.0-alt1
- new release (4.2)
- disable lisp part totaly

* Fri Dec 15 2006 Alexey Morsov <swi@altlinux.ru> 4.2.rc2-alt1
- new version
- fix spec for tutorial
- fix patch0 for new version

* Wed Nov 02 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 4.0.0-alt3
- [Bug 8361] x86_64 support request

* Wed Jun 22 2005 Constantin (Const) Mikhaylenko <const@altlinux.ru> 4.0.0-alt2
- bugfix; removed emax-mode-* packages

* Tue May 18 2004 Constantin (Const) Mikhaylenko <const@altlinux.ru> 4.0.0-alt1
- new version

* Mon Mar 17 2003 Stanislav Ievlev <inger@altlinux.ru> 3.7.3-alt1
- new version

* Wed Sep 25 2002 Stanislav Ievlev <inger@altlinux.ru> 3.7.2-alt1
- 3.7.2
- added subpackages for emacs modes
- added packager tag

* Thu Oct 11 2001 Dmitry V. Levin <ldv@altlinux.ru> 3.7.1-ipl16mdk
- Rebuilt with libpng.so.3

* Sun Sep 16 2001 Rider <rider@altlinux.ru> 3.7.1-ipl14mdk
- BuildRequires fix

* Sun Aug 27 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-13mdk
- now should also compile on non x86 arch, /me sucks

* Fri Aug 25 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-12mdk
- removed -ffast-math option to improve reliability

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-11mdk
- automatically added packager tag

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 3.7.1-10mdk
- automatically added BuildRequires

* Thu Jul 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-9mdk
- BM
- macroweruivieruweiovjzations

* Fri Apr 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-8mdk
- fixed menu entry adding 32x32 icon

* Fri Apr 28 2000 Giuseppe GhibР <ghibo@mandrakesoft.com> 3.7.1-7mdk
- added XFree86-devel in BuildPreReq for X11.
- removed bzip2 man pages (done by spec_helper).
- removed gnu-readline and put back minimal-readline otherwise the
  Boer's patch doesn't work.

* Mon Apr 17 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-6mdk
- fix directory owns.
- now uses gnu readline library instead of minimal built-in readline.

* Mon Apr 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-5mdk
- added icon.

* Thu Mar 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.7.1-4mdk
- new groups.
- menu entry.

* Thu Nov 11 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- added Pieter de Boer's patch <ptdeboer@cs.utwent.nl> for splot X11
  interactive rotations.
- added gnuplot-mode documentation.

* Tue Nov  9 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- updated to 3.7.1.
- added gnuplot-faq.html.
- added PDF documentation.

* Mon Nov  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- 3.7.0.2.
- fix license.
- add emacs-mode.
- add some documentation.

* Fri Oct 1 1999 Giuseppe GhibР <ghibo@linux-mandrake.com>
- Changed the 3.7.0->3.7.0.1 patch to a more recent version because
the previous version has broken the postscript terminal.

* Tue Jul 20 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Rebuild without svgalib.

* Wed Jun 30 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Update to 3.7.0.1.

* Tue May 11 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Tue Feb  2 1999 Jeff Johnson <jbj@redhat.com>
- update to 3.7.

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Fri Sep 11 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.6beta347

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Oct 20 1997 Donnie Barnes <djb@redhat.com>
- spec file cleanups

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
