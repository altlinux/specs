# do not use rpmrb (multiple Version entries here)

%define LIBPLOT_VERSION 4.3
%define LIBXMI_VERSION 1.3
%define fname tek

Name: plotutils
Version: 2.5.1
Release: alt3.qa2

Summary: GNU Plotutils -- plotting utilities

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPLv3
Group: Graphics
Url: http://www.gnu.org/software/plotutils/plotutils.html

Source: ftp://ftp.gnu.org/gnu/plotutils/plotutils-%version.tar.gz
Patch: %name-info.patch
Patch1: %name-c++.patch

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: flex gcc-c++ imake libXaw-devel libXext-devel libpng-devel rpm-build-java rpm-build-mono rpm-build-seamonkey xorg-cf-files xorg-sdk

BuildPreReq: rpm-build-fonts

%description
The GNU plotting utilities include:
(1) GNU libplot, a shared library for exporting 2-D vector graphics
files and for performing vector graphics animation under the X
Window System. Its output file formats include pseudo-GIF, PNM, Adobe
Illustrator, Postscript (editable with the free 'idraw' drawing editor),
Fig (editable with the free g' drawing editor), PCL 5, HP-GL and HP-GL/2,
Tektronix, and GNU metafile format. Many Postscript, PCL, and Hershey
fonts are supported. A separate class library, 'libplotter', provides
a C++ binding to libplot's functionality.
(2) Sample command-line applications 'graph', 'plot', 'tek2plot',
'pic2plot', and 'plotfont', which are built on top of GNU libplot. 'graph'
is a powerful utility for XY plotting, 'plot' translates GNU metafiles to
other formats, 'tek2plot' translates legacy Tektronix data, 'pic2plot'
translates box-and-arrow diagrams in the pic language, and 'plotfont'
plots character maps.
(3) Command-line applications 'spline', 'double', and 'ode', which are
useful in scientific plotting. 'spline' does spline interpolation of input
data of arbitrary dimensionality. It uses cubic splines, splines under
tension, or cubic Bessel interpolation. 'ode' is an interactive program
that can integrate a user-specified system of ordinary differential
equations.

%package -n libplot
Summary: libplot plotting library - from plotutils package
Group: Development/C
Version: %LIBPLOT_VERSION

%description -n libplot
GNU libplot: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%package -n libplot-devel
Summary: libplot header files
Group: Development/C
Version: %LIBPLOT_VERSION
Requires: libplot = %LIBPLOT_VERSION-%release

%description -n libplot-devel
libplot header files.

%package -n libplotter
Summary: libplotter plotting library - from plotutils package
Group: Development/C
Version: %LIBPLOT_VERSION

%description -n libplotter
GNU libplotter: a function library for exporting two-dimensional
vector graphics files, and for displaying animated vector.

%package -n libplotter-devel
Summary: libplotter header files
Group: Development/C
Requires: libplotter = %LIBPLOT_VERSION-%release
Version: %LIBPLOT_VERSION

%description -n libplotter-devel
libplotter header files.

%package -n libxmi
Summary: libxmi library - from plotutils package
Summary(pl):	libxmi - biblioteka z pakietu plotutils
Group: Development/C
Version: %LIBXMI_VERSION

%description -n libxmi
GNU libxmi: a function library for exporting two-dimensional vector
graphics files, and for displaying animated vector.

%package -n libxmi-devel
Summary: libxmi header files
Group: Development/C
Requires: libxmi = %LIBXMI_VERSION-%release
Version: %LIBXMI_VERSION

%description -n libxmi-devel
libxmi header files.

%prep
%setup -q

%build
CXXFLAGS="-fno-rtti -fno-exceptions"
%configure \
	--disable-static \
	--enable-libplotter \
	--enable-libxmi
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

cd fonts/pcf
gzip -9nf *.pcf || :
%bitmap_fonts_install %fname

%post -n libplot
%post_fonts

%postun -n libplot
%postun_fonts

%files
%doc AUTHORS COMPAT KNOWN_BUGS NEWS ONEWS PROBLEMS README THANKS TODO
%_bindir/*
%_infodir/plotutils.info*
%_man1dir/*
%_datadir/ode
%_datadir/pic2plot
%_datadir/tek2plot

%files -n libplot -f fonts/pcf/%fname.files
%doc doc/{demo-page,*.doc,*.txt,*.bib}
%doc libplot/{DEDICATION,HUMOR,README*,VERSION}
%_libdir/libplot.so.*
%_datadir/libplot/

%files -n libplot-devel
%_libdir/libplot.so
#_examplesdir/libplot-%LIBPLOT_VERSION
%_includedir/plot.h
%_includedir/plotcompat.h

%files -n libplotter
%_libdir/libplotter.so.*

%files -n libplotter-devel
%_libdir/libplotter.so
%_includedir/plotter.h

%files -n libxmi
%doc libxmi/{AUTHORS,NEWS,README*,TODO,VERSION}
%_libdir/libxmi.so.*

%files -n libxmi-devel
%_infodir/libxmi.info*
%_libdir/libxmi.so
%_includedir/xmi.h

%changelog
* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt3.qa2
- Removed RPATH

* Thu Nov 25 2010 Igor Vlasenko <viy@altlinux.ru> 2.5.1-alt3.qa1
- rebuild using girar-nmu to require/provide setversion 
  by request of mithraen@

* Tue Dec 02 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt3
- update buildreqs, remove post install_info sections

* Tue Nov 18 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt2
- rename font dir to tek (fix bug #17924)

* Sat Nov 15 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5.1-alt1
- new version 2.5.1 (with rpmrb script)
- change license to GPLv3
- drop post/postin_ldconfig
- use rpm-build-fonts
- update buildreqs

* Sat Feb 19 2005 Vitaly Lipatov <lav@altlinux.ru> 2.4.1-alt1
 - first build for ALT Linux Sisyphus
 - spec from PLD Team <feedback@pld.org.pl>
