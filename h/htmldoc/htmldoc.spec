%define subversion r1629
%define sourceversion 1.9.x

Name: htmldoc
Version: 1.9.0
Release: alt1.%subversion.5
Serial: 1

License: GPL with exceptions (see COPYING.txt)
Group: Text tools
Url: http://www.easysw.com/htmldoc/
Summary: htmldoc creates pdf and ps from html
Summary(ru_RU.UTF8): htmldoc - программа преобразования html в pdf и ps

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source: %name-%sourceversion-%subversion.tar.bz2
Source2: htmldoc.png

Patch1: htmldoc-1.9.x-%subversion-fix.overflow.patch
Patch2: htmldoc-1.9.0-alt-libpng15.patch
Patch3: htmldoc-1.9.0-alt-compat.patch

PreReq: fontconfig >= 2.4.2
Requires: fonts-type1-htmldoc

BuildPreReq: rpm-build-fonts

# Automatically added by buildreq on Tue Mar 29 2011
BuildRequires: gcc-c++ libfltk-devel libjpeg-devel libpng-devel libssl-devel

%description
Htmldoc is a HTML processing program that generates HTML, PostScript, and PDF
files with a table of contents.

%description -l ru_RU.UTF8
Htmldoc - программа обработки HTML, которая позволяет создавать PDF, PostScript
и HTML с оглавлением.

%package -n fonts-type1-htmldoc
Summary: Font used by htmldoc function
Group: System/Fonts/Type1

%description -n fonts-type1-htmldoc
This Package provides a htmldoc Type1 fonts
from Irmologion project.

%prep
%setup -n %name-%sourceversion-%subversion
%patch1 -p1
%patch2 -p2
%patch3 -p2
autoconf

%build
export LDFLAGS="-Wl,-rpath-link -Wl,%_x11libdir"
%configure \
  --disable-localjpeg  \
  --disable-localzlib  \
  --disable-localpng

%make_build

%install
%makeinstall

mkdir -p rpmdoc/html
install -m 644 doc/*.html rpmdoc/html
install -m 644 doc/*.png rpmdoc/html

rm -fr %buildroot%_datadir/%name/fonts
rm -fr %buildroot%_docdir/%name

mkdir -p rpmdoc/html
install -m 644 doc/*.html rpmdoc/html
install -m 644 doc/*.png rpmdoc/html

mkdir -p %buildroot%_datadir/%name/data/

install -d -m 755 %buildroot%_sysconfdir/X11/fs/config
install -d -m 755 %buildroot%_fontsdir/%name

install -d -m755 %buildroot%_fontpathdir/

mkdir -p %buildroot%_fontsdir/%name
find -name \*.pfa -print -exec cp -t %buildroot%_fontsdir/%name {} \;
find -name \*.pfb -print -exec cp -t %buildroot%_fontsdir/%name {} \;
find -name \*.afm -print -exec cp -t %buildroot%_fontsdir/%name {} \;
mkfontscale %buildroot%_fontsdir/%name
ln -s fonts.scale %buildroot%_fontsdir/%name/fonts.dir

ln -s  %_fontsdir/%name %buildroot%_datadir/%name/fonts

mkdir -p %buildroot%_fontpathdir
ln -s ../../..%_fontsdir/%name %buildroot%_fontpathdir/%name-%name:pri=40

install -D -m 644 %SOURCE2 %buildroot%_niconsdir/%name.png
install -D -m 644 %SOURCE2 %buildroot%_liconsdir/%name.png

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Htmldoc
Comment=HTML to PDF/PS/Indexed HTML converter
Icon=%name
Exec=%name
Terminal=false
Categories=Office;Publishing;
MimeType=text/html;
EOF

%triggerun -- %name <= 7.0.0-alt1
if [ -x %_sbindir/chkfontpath -a -f %_sysconfdir/X11/fs/config ]; then
	%_sbindir/chkfontpath -q -r %_fontsdir/%name ||:
fi

%pre -n fonts-type1-htmldoc
if [ -L "%_datadir/%name/fonts" ]; then
  d=$(realpath "%_datadir/%name/fonts")
  rm -f -- "%_datadir/%name/fonts"
  if [ "$d"  != "%_datadir/fonts/htmldoc" ]; then
    echo  " mv -f -- $d %_datadir/fonts/htmldoc"
    mv -f -- "$d" "%_datadir/fonts/htmldoc"
  fi
fi

%post
%_bindir/fc-cache %_fontsdir/Type1 ||:

%postun
%files
%doc COPYING.txt README.txt doc/htmldoc.pdf
%doc rpmdoc/html/
%_bindir/%name
%_man1dir/*
%dir %_datadir/%name
%_datadir/%name/*
%exclude %_datadir/%name/fonts
%_desktopdir/%{name}.desktop
%_liconsdir/%{name}.*
%_niconsdir/%{name}.*

%files -n fonts-type1-htmldoc
%_fontpathdir/
%_fontsdir/*
%_datadir/%name/fonts

%changelog
* Thu Feb 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:1.9.0-alt1.r1629.5
- Fixed build with new toolchain.

* Fri Sep 28 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.9.0-alt1.r1629.4
- Rebuilt with libpng15

* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.9.0-alt1.r1629.3
- NMU: converted menu to desktop file

* Tue Mar 29 2011 Hihin Ruslan <ruslandh@altlinux.ru> 1:1.9.0-alt1.r1629.2
- fix BuildRequires

* Fri Dec 04 2009 Hihin Ruslan <ruslandh@altlinux.ru> 1:1.9.0-alt1.r1629.1
- new version

* Mon Nov 30 2009 Hihin Ruslan <ruslandh@altlinux.ru> 1:1.9.0-alt1.r1563.3
- add htmldoc-1.9.x-r1663.fix-overflow.patch

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1:1.9.0-alt1.r1563.2.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue Jun 17 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1:1.9.0-alt1.r1563.2
- correct spec

* Mon Jun 16 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1:1.9.0-alt1.r1563.1
- new version

* Fri Mar 14 2008 Hihin Ruslan <ruslandh@altlinux.ru> 1.9.x-alt1
- new version

* Fri Sep 17 2004 Andrei Bulava <abulava@altlinux.ru> 1.8.23-alt5
- Fixed non-ISO-8859-1 charset support by way of replacing built-in fonts
  with ones generated from urw-fonts, which had cyrillic glyphs (#5183).
- Minor fixes:
  + fixed building with XFree86-libs' %_sysconfdir/ld.so.conf.d/X11R6.conf
  + updated BuildRequires.

* Mon Jun 21 2004 Andrei Bulava <abulava@altlinux.ru> 1.8.23-alt4
- Spec fixes:
  + typos;
  + cleanup;
  + got rid of obsolete RPM_BUILD_ROOT;
  + macros were used where possible.

* Mon May 10 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.8.23-alt3.1
- Rebuilt with openssl-0.9.7d.

* Sat Feb 08 2003 Ott Alex <ott@altlinux.ru> 1.8.23-alt3
- Fixing spec and add menu

* Sun Nov 03 2002 Ott Alex <ott@altlinux.ru> 1.8.23-alt1
- New version. Now builded with GUI

* Sat Oct 19 2002 Ott Alex <ott@altlinux.ru> 1.8.22-alt1
- Initial build

