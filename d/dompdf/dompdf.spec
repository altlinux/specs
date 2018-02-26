Name: dompdf
Version: 0.5.1
Release: alt2
BuildArch: noarch

Group: Networking/WWW
Summary: The PHP5 HTML to PDF converter 
Summary(ru_RU.UTF-8): Конвертер страниц HTML в PDF
Url: http://www.digitaljunkies.ca/dompdf/
License: LGPL
Packager: Michael A. Kangin <prividen@altlinux.org>

Requires: php-engine >= 5 php5-dom php5-gd2 php5-mbstring fonts-type1-urw ttf2pt1 
PreReq:	webserver-common

BuildPreReq: rpm-macros-webserver-common 

Source0: %name-%version.tgz
Source1: encodetable.koi8-r.php
Source2: apache2_dompdf.conf
Source3: encodetable.cp1251.php

%description
dompdf is an HTML to PDF converter. At its heart, dompdf is (mostly)
CSS2.1 compliant HTML layout and rendering engine written in PHP. It
is a style-driven renderer: it will download and read external
stylesheets, inline style tags, and the style attributes of individual
HTML elements. It also supports most presentational HTML attributes.

%prep
%setup -q

%build

%install

sed -i -e "s|dompdf_config.inc.php|%_datadir/%name/dompdf_config.inc.php|" \
	%name.php load_font.php
sed -i -e "s|../dompdf_config.inc.php|%_datadir/%name/dompdf_config.inc.php|" \
	www/examples.php
sed -i -e '/DOMPDF_FONT_DIR/c define("DOMPDF_FONT_DIR", "%webserver_webappsdir/%name/fonts/");' \
	dompdf_config.inc.php
sed -i -e 's|__WEBAPPDIR/|%webserver_webappsdir/|' %SOURCE2

mkdir -p %buildroot%_datadir/%name
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%webserver_webappsdir/%name

install -m 755  %name.php load_font.php %buildroot%_bindir/
cp -r dompdf_config.inc.php include lib %buildroot%_datadir/%name/
cp -r www %buildroot%webserver_webappsdir/%name/
mv %buildroot%_datadir/%name/lib/fonts %buildroot%webserver_webappsdir/%name/
ln -s %webserver_webappsdir/%name/www %buildroot%_datadir/%name/
install -m 644 %SOURCE1 %buildroot%_datadir/%name/lib/
install -m 644 %SOURCE3 %buildroot%_datadir/%name/lib/
install -m 644 %SOURCE2 ./

# make links for use URW fonts
link_font() {
ln -sf "%_datadir/fonts/type1/urw/$1.afm" "%buildroot%webserver_webappsdir/%name/fonts/$2.afm"
ln -sf "%_datadir/fonts/type1/urw/$1.pfb" "%buildroot%webserver_webappsdir/%name/fonts/$2.pfb"
}

link_font n021003l Times-Roman
link_font n021004l Times-Bold
link_font n021023l Times-Italic
link_font n021024l Times-BoldItalic
link_font n019003l Helvetica
link_font n019004l Helvetica-Bold 
link_font n019023l Helvetica-Oblique
link_font n019024l Helvetica-BoldOblique
link_font n022003l Courier
link_font n022004l Courier-Bold
link_font n022023l Courier-Oblique
link_font n022024l Courier-BoldOblique

%files

%add_findreq_skiplist %webserver_webappsdir/%name/www
%add_findreq_skiplist %webserver_webappsdir/%name/fonts/*
%add_findreq_skiplist %_bindir/*

%_bindir/*
%dir %_datadir/%name
%_datadir/%name/*
%dir %attr(0755,root,_webserver) %webserver_webappsdir/%name
%dir %attr(2775,root,%webserver_group) %webserver_webappsdir/%name/fonts
%webserver_webappsdir/%name/fonts/*
%attr(0664,root,%webserver_group) %config(noreplace) %webserver_webappsdir/%name/fonts/dompdf_font_family_cache
%webserver_webappsdir/%name/www
%doc ChangeLog HACKING INSTALL LICENSE.LGPL README TODO apache2_dompdf.conf

%changelog
* Tue Sep 08 2009 Michael A. Kangin <prividen@altlinux.org> 0.5.1-alt2
- Cyrillic support improved;
- Fix some buggy markup processings

* Mon Aug 24 2009 Michael A. Kangin <prividen@altlinux.org> 0.5.1-alt1
- Initial build for Sisyphus


