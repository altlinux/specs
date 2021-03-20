Name: nightfall
Version: 1.92
Release: alt1
Summary: Nightfall is an astronomy application for emulation of eclipsing stars

License: GPLv2+
Group: Education
Url: http://www.hs.uni-hamburg.de/DE/Ins/Per/Wichmann/Nightfall.html
Source0: http://www.la-samhna.de/%name/%name-%version.tar.gz
Source1: nightfall.desktop
#Patch0: nightfall-1.62-fixmakefile.patch
#need to get debug symbols
Patch0:         nightfall-1.82-optflags.patch
Patch1:         nightfall-1.82-makefile.patch
#fix buffer overflow
Patch2:         nightfall-1.82-buffoverflow.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildRequires: libgtk+2-devel desktop-file-utils libfreeglut-devel libgomp-devel libjpeg-devel
Requires: gnuplot a2ps

%description
Nightfall is an astronomy application for fun, education, and science.
It can produce animated views of eclipsing binary stars,
calculate synthetic lightcurves and radial velocity curves,
and eventually determine the best-fit model for a given set of
observational data of an eclipsing binary star system.
It is, however, not able to fry your breakfast egg on your harddisk.

%prep
%setup -q
#patch0 -p2 -b .makefile
%patch0 -p1
%patch1 -p1
%patch2 -p1

# fix build on aarch64
#cp -af config.{guess,sub} .

%build
export CFLAGS='%{optflags} -fcommon'
export CXXFLAGS='%{optflags} -fcommon'
export FFLAGS='%{optflags} -fcommon'


#configure --with-gnuplot --enable-gnome
#make %_smp_mflags


%configure \
   --with-gnuplot \
   --enable-opengl \
   --enable-openmp \
   --disable-rpath \
   --disable-gnome \
   --with-locale-prefix=%{_datadir}/locale
%make_build


%install
make DESTDIR=$RPM_BUILD_ROOT install
%find_lang %name
desktop-file-install --vendor fedora --dir $RPM_BUILD_ROOT%_datadir/applications %SOURCE1

%files -f %name.lang
%doc UserManual.pdf UserManual.html README AUTHORS ChangeLog
%attr(755,root,root) %_bindir/nightfall
%attr(644,root,root) %_mandir/man1/nightfall.*
%_datadir/nightfall/*
%_datadir/applications/fedora-nightfall.desktop

%changelog
* Sat Mar 20 2021 Ilya Mashkin <oddity@altlinux.ru> 1.92-alt1
- 1.92

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.70-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Dec 20 2009 Ilya Mashkin <oddity@altlinux.ru> 1.70-alt1
- 1.70

* Mon Jan 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.68-alt1
- 1.68

* Fri Jan 09 2009 Ilya Mashkin <oddity@altlinux.ru> 1.62-alt1
- Initial build for ALT

* Sat Mar 1  2008 Marek Mahut <mmahut@fedoraproject.org> - 1.62-4
- Rebuild for GCC 4.3

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.62-3
- Autorebuild for GCC 4.3

* Sun Nov 25 2007 Marek Mahut <mmahut@fedoraproject.org> - 1.62-2
- Initial build.
