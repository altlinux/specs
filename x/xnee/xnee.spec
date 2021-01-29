Summary: X11 environment recorder
Name: xnee
Version: 3.19
Release: alt3
Group: System/X11

License: GPLv3+
Url: http://www.gnu.org/software/xnee/
Source0: http://ftp.gnu.org/gnu/xnee/xnee-%version.tar.gz
Patch: xnee-3.19-alt-cnee-info.patch
Patch1: xnee-gcc10.patch

# Automatically added by buildreq on Thu Jan 28 2021
# optimized out: fontconfig fontconfig-devel ghostscript-classic glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gnu-config libImageMagick6-common libX11-devel libX11-locales libXext-devel libXfixes-devel libXi-devel libatk-devel libcairo-devel libfreetype-devel libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libgpg-error libharfbuzz-devel libpango-devel libsasl2-3 perl perl-Encode perl-Text-Unidecode perl-Unicode-EastAsianWidth perl-Unicode-Normalize perl-libintl perl-parent pkg-config python2-base sh4 tex-common texlive texlive-collection-basic texlive-dist xorg-proto-devel
BuildRequires: ImageMagick-tools dia fonts-ttf-dejavu ghostscript-common ghostscript-utils glibc-devel-static imake libICE-devel libXtst-devel libgtk+2-devel makeinfo texi2dvi texi2html xorg-cf-files

BuildRequires: xvfb-run xdpyinfo texlive-dist

%description
A suite of programs that can record, replay and distribute
user actions under the X11 environment. Think of it as a
robot that can imitate the job you just did.

%package libs
Summary: The shared libraries required for Xnee clients
Group: System/Libraries

%description libs
The xnee-lib package provides the essential shared libraries for any
Xnee client program or interface.

%package devel
Summary: Files needed for building applications with libxnee
Group: Development/C

%description devel
The xnee-devel package includes header files and libraries
necessary for developing programs which use the xnee-lib library.

%package -n cnee
Summary: Command-line interface of Xnee
Group: System/X11

%description -n cnee
Command-line interface of a suite of programs that can record,
replay and distribute user actions under the X11 environment. Think
of it as a robot that can imitate the job you just did.

%prep
%setup
%patch -p1
%patch1 -p1
cat > %name.desktop <<@@@
[Desktop Entry]
Name=Xnee
GenericName=X11 Recorder
Comment=Replay action under X11 environment
Exec=gnee
Icon=xnee
Terminal=false
Type=Application
Categories=Utility;
@@@

%build
%autoreconf
%configure --disable-gnome-applet      	\
	   --enable-man                	\
           --enable-doc                	\
           --enable-gui                	\
  	   --enable-xinput2		\
	   --enable-cli      		\
           --enable-lib                \
	   --disable-static \
	   --disable-static-programs
#           --enable-static=no          \
#           --enable-static-programs=no
%make_build LIBS="-lX11 -lXi -lXtst"

%install
%make DESTDIR=%buildroot install install-info install-html install-pdf
mkdir -p %buildroot%_includedir/libxnee
install -pm 644 libxnee/include/libxnee/*.h %buildroot%_includedir/libxnee/
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%check
xvfb-run make check

%files
%_bindir/gnee
%_datadir/pixmaps/xnee.png
%_datadir/pixmaps/xnee.xpm
%_datadir/applications/xnee.desktop
%_datadir/xnee/
%_mandir/man1/[^c]*
%_infodir/[^c]*

%files libs
%doc AUTHORS BUGS COPYING EXAMPLES FAQ NEWS TODO ChangeLog
%_libdir/libxnee.so.*
%_libdir/libtestcb.so.*

%files devel
%_libdir/libxnee.so
%_libdir/libtestcb.so
%_includedir/libxnee/

%files -n cnee
%_bindir/cnee
%_mandir/man1/cnee.1*
%_infodir/cnee*

%changelog
* Thu Jan 28 2021 Fr. Br. George <george@altlinux.ru> 3.19-alt3
- Resurrect from orphaned
- Fix gcc10 build

* Tue Dec 29 2015 Fr. Br. George <george@altlinux.ru> 3.19-alt2
- Build documentation

* Mon Dec 28 2015 Fr. Br. George <george@altlinux.ru> 3.19-alt1
- Autobuild version bump to 3.19
- Do some tests

* Mon May 12 2014 Fr. Br. George <george@altlinux.ru> 3.18-alt1
- Initial build from FC

* Mon Apr 28 2014 Matthieu Saulnier <fantom@fedoraproject.org> - 3.18-1
- Update to 3.18
- Fix spelling-error in summary and description

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 26 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 3.16-1
- Update to 3.16
- Fix bogus date in %%changelog section in spec file

* Tue Feb 12 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 3.15-2
- Add test suite in %%check section
- Undo previous fix devel subpackage requires

* Mon Feb 04 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 3.15-1
- Update to 3.15
- Fix devel subpackage requires
- Cleanup in %%install section

* Tue Jan 08 2013 Matthieu Saulnier <fantom@fedoraproject.org> - 3.14-1
- Update to 3.14

* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 3.13-3
- Add French translation in spec file

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 21 2012 Matthieu Saulnier <fantom@fedoraproject.org> 3.13-1
- update to 3.13 version
- remove "Group" tag in spec file

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.11-1
- update to 3.11
- URL for download sources has been changed

* Mon Dec 12 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10.93-1
- update to 3.10.93

* Thu Dec 01 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10.91-1
- update to 3.10.91

* Thu Nov 24 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10.90-1.1
- remove name macro in removing bash_bash.sh line

* Thu Nov 24 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10.90-1
- update to 3.10.90 version
- remove "defattr" lines in spec file

* Tue Nov 22 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-8
- fix AutoQA

* Tue Nov 22 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-7
- rename "xnee" to "Xnee"

* Fri Nov 04 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-6
- move doc files in libs package

* Thu Nov 03 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-5
- minor cleanup spec file

* Sat Oct 22 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-4
- delete simple_bash.sh file

* Thu Oct 20 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-3
- add libtestcb in xnee-libs package
- clean up spec file

* Sun Oct 16 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-2
- add COPYING in libs package

* Tue Aug 23 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.10-1
- update to 3.10 version

* Sat Aug 06 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- clean up spec file

* Fri Aug 05 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- add header in libxnee-devel

* Wed Aug 03 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- add cnee subpackage

* Sun Jul 31 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- add libxnee and libxnee-devel subpackages

* Thu Jul 28 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- minor specfile cleanup

* Wed Jul 27 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- clean up spec file

* Thu Jun 23 2011 Matthieu Saulnier <casper.le.fantom@gmail.com> 3.09-1
- initial RPM
