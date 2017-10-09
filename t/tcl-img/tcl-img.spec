%define teaname img
%define major 1.4

Name: tcl-img
Version: 1.4.2
Release: alt1

Summary: Tcl Image Formats (Img)
License: BSD
Group: Development/Tcl
Url: http://tkimg.sf.net

Provides: %teaname = %version-%release
Obsoletes: %teaname
Conflicts: tcl < 8.6.7-alt2

# git://git.altlinux.org/gears/t/tcl-img.git
Source0: %name-%version-%release.tar

BuildRequires: rpm-build-tcl >= 0.5-alt1
BuildRequires: libjpeg-devel libpng12-devel tk-devel zlib-devel
BuildRequires: tcllib

%description
%name is a Tk enhancement, adding support for many other Image formats:
BMP, XBM, XPM, GIF, PNG, JPEG, postscript and others.

%prep
%setup
find . -name config.cache -delete

%build
export TCL_SRC_DIR=%_includedir/tcl
export TK_SRC_DIR=%_includedir/tk
%autoreconf
%configure --with-tcl=%_libdir --with-tk=%_libdir
%make_build

gzip -9 ChangeLog

%install
%make_install DESTDIR=%buildroot install

%files
%doc ANNOUNCE ChangeLog.gz README doc/*.css doc/*.htm
%_tcllibdir/Img%version/*.so
%_tcllibdir/Img%version/pkgIndex.tcl
%_mandir/mann/*

%changelog
* Tue Sep 12 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.2-alt1
- 1.4.2 released

* Sun Apr 07 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt2
- use png12 from now

* Tue Jun 23 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.2-alt1
- 1.3.2 release

* Sun Nov 26 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt5
- pngtcl: removed png_{read,write}_destroy from stub table

* Fri Jul 21 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt4
- fixed build on x86_64

* Sun Apr 16 2006 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt3
- CVS snapshot @ 20060125
- tiff support dropped

* Wed Nov  3 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt2
- rebuilt against new shiny tcl reqprov finder

* Sun Sep 26 2004 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.3.0-alt1
- new major release
- built with system libjpeg, libpng, libtiff

* Tue Oct  1 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 1.2.4-alt1
- name changed
- rebuilt with tcl 8.4
