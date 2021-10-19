Summary: geomview -- interactive geometry viewing program

%define pre %nil
%def_without xforms

Name: geomview
Version: 1.9.5
Release: alt2

License: LGPLv2+
Group: Sciences/Mathematics
Url: http://www.geomview.org
Packager: Ilya Mashkin <oddity@altlinux.ru>
Source: http://ftp1.sourceforge.net/geomview/%name-%version.tar.xz
Source1: %{name}_16.xpm
Source2: %{name}_32.xpm
Source3: %{name}_48.xpm
#Patch0: http://ftp.debian.org/debian/pool/main/g/geomview/%{name}_%version-8.diff.bz2
Patch: geomview-1.8.2-rc9-alt-xforms-path.patch
Patch1: geomview-1.9.4-alt-DSO.patch

# Automatically added by buildreq on Sun Jan 13 2008 (-bi)
BuildRequires: flex gcc-c++ imake tcsh xorg-cf-files zlib-devel libXt-devel libXext-devel lesstif-devel

BuildPreReq: libGL-devel libGLU-devel

#B uildRequires: flex gcc-c++ libstdc++-devel openmotif-devel tcl-devel tcsh tk-devel

%if_with xforms
BuildPreReq: libxforms-devel
%endif

%define DIRSETTINGS moduledir=%_libdir/%{name} geomdatadir=%_datadir/%{name}/data
# explicitly added texinfo for info files
BuildRequires: texinfo

#BuildRequires: rpm-build-compat >= 0.4

%description
 Geomview is interactive geometry software which is
 particularly appropriate for mathematics research and education.
 Geomview can display 3-D graphics output from Mathematica and Maple.
 In particular, geomview can display things in hyperbolic and
 spherical space as well as Euclidean space.
 .
 Geomview allows multiple independently controllable objects and
 cameras.  It provides interactive control for motion, appearances
 (including lighting, shading, and materials), picking on an
 object, edge or vertex level, snapshots in SGI image file or
 Renderman RIB format, and adding or deleting objects is provided
 through direct mouse manipulation, control panels, and keyboard
 shortcuts.  External programs can drive desired aspects of the
 viewer (such as continually loading changing geometry or
 controlling the motion of certain objects) while allowing
 interactive control of everything else.
 Homepage: http://www.geomview.org.


%prep
%setup -n %name-%version
#%patch0 -p0
%patch1 -p2

%build
autoreconf -fisv
CONFFLAGS='--enable-shared' # --disable-static'

%configure $CONFFLAGS

%make_build %DIRSETTINGS \
	ACLOCAL="`pwd`/missing aclocal" \
	AUTOCONF="`pwd`/missing autoconf" \
	AUTOMAKE="`pwd`/missing automake" \
	AUTOHEADER="`pwd`/missing autoheader"

%set_verify_info_method relaxed

%install
%makeinstall_std %DIRSETTINGS
install -m644 -D %SOURCE1 $RPM_BUILD_ROOT%_miconsdir/%{name}.xpm
install -m644 -D %SOURCE2 $RPM_BUILD_ROOT%_niconsdir/%{name}.xpm
install -m644 -D %SOURCE3 $RPM_BUILD_ROOT%_liconsdir/%{name}.xpm

mv doc/geomview.html doc/html

# due to ImageMagic conflict
# $RPM_BUILD_ROOT%_man1dir/animate.* 
# another conflict
for i in \
$RPM_BUILD_ROOT%_man1dir/animate.* \
; do
	fname=`basename $i`
	dname=`dirname $i`
	mv $i $dname/%name-$fname
done

# xforms 
#$RPM_BUILD_ROOT%_man1dir/sweep.* \
#$RPM_BUILD_ROOT%_man3dir/sweep.* \

rm -fv %buildroot%_libdir/*.a

%__install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Geomview
Comment=geomview -- interactive geometry viewing program
Icon=%{name}
Exec=%{name}
Terminal=false
Categories=Science;Math;
EOF

%files
%doc doc/html
%doc AUTHORS NEWS README INSTALL.Geomview
#doc doc/gvplot.txt 
%doc doc/OOGL.m.txt doc/motion.tex doc/oogltour doc/example*
#doc src/bin/sweep/sweep.1* src/bin/sweep/sweep.3*
%doc src/bin/animate/animate.1* src/lib/geomutil/bdy/bdy.3* src/lib/geomutil/geomutil.3* 
#exclude doc/%name.pdf
#find src -name *.[1-9] --- lots of old stuff
%_bindir/*
%_man1dir/*
%if_with xforms
#%_man3dir/*
%endif
%_infodir/%{name}*
%_infodir/figs/*
%_libdir/%name
%_docdir/geomview/
%_man1dir/*
%_man3dir/*
%_man5dir/*
#%_libdir/lib%{name}.so.*
%_libdir/lib%{name}*.so
%dir %_datadir/%name
%_datadir/%name/data
%dir %_datadir/%name/Maple
%dir %_datadir/%name/Mathematica
%_datadir/%name/Ma*/*
%_miconsdir/%{name}.xpm
%_niconsdir/%{name}.xpm
%_liconsdir/%{name}.xpm
%_desktopdir/%{name}.desktop
# todo: geomview-devel
%exclude /usr/include/%{name}
%exclude %_libdir/lib%name.so

%changelog
* Tue Oct 19 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.5-alt2
- Fixed FTBFS.

* Thu May 27 2021 Ilya Mashkin <oddity@altlinux.ru> 1.9.5-alt1
- 1.9.5
- Update License to LGPLv2+
- Add mans and docs

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt4.qa3.1
- NMU: added BR: texinfo

* Thu Jun 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt4.qa3
- Fixed build

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt4.qa2
- NMU: converted menu to desktop file

* Sat Apr 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.4-alt4.1
- Fixed build

* Fri Jul 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.9.4-alt4
- fix build

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.9.4-alt3
- remove deprecated post/postun from spec
- update requires (build with lesstif)

* Thu Apr 03 2008 Vlasenko Igor <viy@altlinux.ru> 1.9.4-alt2
- autoreconf'ed

* Sat Jan 12 2008 Igor Vlasenko <viy@altlinux.ru> 1.9.4-alt1
- new version
- note: 
   xforms modules and Tcl/Tk modules moved to the separate packages
	gvemod-ndview
	gvemodules-xforms
	gvemodules-tcltk
- TODO: to be built.

* Sun Dec 24 2006 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt5.rc9
- rc9
- fixed #10501 (added /usr/share/geomview)

* Mon Sep 11 2006 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt4
- removed man 1,3 sweep due to conflct (#9976)
* Fri Sep 01 2006 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt2
- built with xforms

* Sun Aug 27 2006 Igor Vlasenko <viy@altlinux.ru> 1.8.2-alt1
- new version

* Mon Oct 10 2005 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt3
- xforms are now optional

* Thu Jul 28 2005 Igor Vlasenko <viy@altlinux.org> 1.8.1-alt2
- built with xforms

* Tue Mar 29 2005 Igor Vlasenko <viy@altlinux.ru> 1.8.1-alt1
- first build for AltLinux
