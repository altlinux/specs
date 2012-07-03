Name: gocr
Version: 0.49
Release: alt2

Summary: GOCR/JOCR is an optical character recognition program
Summary(ru_RU.KOI8-R): GOCR/JOCR - программа распознавания символов (OCR)

License: GPL
Group: Graphics
Url: http://jocr.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://www-e.uni-magdeburg.de/jschulen/ocr/%name-%version.tar.bz2
Patch: %name.as-needed.patch

BuildRequires: hostinfo, libnetpbm-devel, transfig, 

%description
GOCR/JOCR is an optical character recognition program, released under the GNU
General Public License. It reads images in many formats (pnm, pbm, pgm, ppm,
some pcx and tga image files (or PNM from stdin) and outputs a text file; if
pnm-tools are installed and running on a linux-like system you can also use
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp and others.

You can use XSane or Kooka as a graphical frontends for GOCR.

%description -l ru_RU.KOI8-R
GOCR/JOCR - это программа оптического распознавания символов,
выпущенная под лицензией GNU General Public License.
Она читает изображения во многих форматах (pnm, pbm, pgm, ppm,
некоторые файлы pcx и tga (или PNM со стандартного ввода)
и выводит текстовый файл;
если уставлены pnm-tools, и программа запускается на Linux-системе,
вы также можете использовать форматы 
pnm.gz, pnm.bz2, png, jpg, tiff, gif, bmp и другие.

Вы можете использовать программы XSane или Kooka как графические
оболочки для GOCR.

%prep
%setup -q
#patch

%build
%configure
%make_build

%install
%makeinstall_std
rm -f %buildroot%_bindir/%name.tcl

%files
%doc AUTHORS BUGS CREDITS HISTORY README READMEde.txt REMARK.txt REVIEW TODO
%doc doc/examples.txt doc/gocr.html doc/unicode.txt
#%doc api/doc/api.tex api/doc/api.txt api/doc/developers.txt
%_bindir/gocr
%_man1dir/gocr.1*

%changelog
* Wed Apr 27 2011 Andrey Cherepanov <cas@altlinux.org> 0.49-alt2
- Merge with vitty@

* Tue Apr 26 2011 Andrey Cherepanov <cas@altlinux.org> 0.49-alt1
- New version 0.49
- Fix building

* Tue Apr 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.45-alt2
- fix build

* Tue May 20 2008 Vitaly Lipatov <lav@altlinux.ru> 0.45-alt1
- new version 0.45 (with rpmrb script)
- rename gocr-devel to libgocr-devel

* Tue Jul 24 2007 Vitaly Lipatov <lav@altlinux.ru> 0.44-alt1
- new version 0.44 (with rpmrb script)

* Tue Dec 12 2006 Vitaly Lipatov <lav@altlinux.ru> 0.43-alt0.1
- new version 0.43
- update as-needed fix

* Sat Apr 01 2006 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt2
- fix for ld --as-needed

* Sun Mar 20 2005 Vitaly Lipatov <lav@altlinux.ru> 0.40-alt1
- new version

* Wed Sep 01 2004 Vitaly Lipatov <lav@altlinux.ru> 0.39-alt2
- fixed summary encoding (bug #5059)
- add russian description

* Mon Apr 26 2004 Vitaly Lipatov <lav@altlinux.ru> 0.39-alt1
- new version

* Mon Dec 08 2003 Vitaly Lipatov <lav@altlinux.ru> 0.37-alt1
- first build for Sisyphus

* Sun Feb  9 2003 Andreas Hirczy <ahi@itp.tu-graz.ac.at>
- Update to gocr 0.37

* Mon Jul 16 2001 Andreas Hirczy <ahi@itp.tu-graz.ac.at>
- Update to gocr 0.3.2

* Tue Apr 10 2001 Andreas Hirczy <ahi@itp.tu-graz.ac.at>
- Update to gocr 0.3.1
- add documentation to package
- add library and header to package

* Mon Aug 14 2000 Tim Waugh <twaugh@redhat.com>
- Created
