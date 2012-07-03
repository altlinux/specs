%define teaname img
%define major 1.3

Name: tcl-img
Version: 1.3.2
Release: alt1

Summary: Tcl Image Formats (Img)
License: BSD
Group: Development/Tcl
Url: http://tkimg.sf.net

Provides: %teaname = %version-%release
Obsoletes: %teaname

Source0: %name-%version-%release.tar

BuildRequires: rpm-build-tcl >= 0.4-alt1
BuildRequires: libjpeg-devel libpng-devel tk-devel zlib-devel

%description
%name is a Tk enhancement, adding support for many other Image formats:
BMP, XBM, XPM, GIF, PNG, JPEG, postscript and others.

%prep
%setup
find . -name pkgIndex.tcl.in| while read; do
%teapatch -C ${REPLY%%/*}
sed -i 's/@lib@/%_lib/' ${REPLY}
done

%build
find . -name configure.in |while read; do
    (cd ${REPLY%%/*} && autoconf)
done
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install
find %buildroot%_tcldatadir -name pkgIndex.tcl|\
grep -v tkimg%major |while read; do
grep -v '^\#' $REPLY
rm -rf ${REPLY%%/*}
done >> %buildroot%_tcldatadir/tkimg%major/pkgIndex.tcl
find %buildroot '(' -path \*%_includedir/\* -o -path \*%_libdir/\*.sh \
	-o -path \*%_libdir/\*.a ')' -delete

%files
%doc doc/*
%_tcllibdir/*.so
%_tcldatadir/*

%changelog
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
