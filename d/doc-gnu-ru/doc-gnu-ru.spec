%define LANG	ru
%define longLANG Russian
%define formathtml	HTML
%define formatpdf PDF

Name: doc-gnu-%LANG
Version: 1.0
Release: alt2.qa4

Packager: Repocop Q. A. Robot <repocop@altlinux.org>

Summary: Manuals and other non-technical ducuments in %longLANG from GNU Project
Group: Books/Computer books

Source0: %name-philosophy.tar.bz2
Source1: %name-manuals.tar.bz2
Source2: %name-extra.tar.bz2

Url: http://www.gnu.org.ru/
License: GPL

BuildArch: noarch
BuildRequires: texi2html sed, grep, perl-base

AutoReq: no

%package -n %name-html
Summary: Manuals and other non-technical ducuments (html format, in %longLANG) from GNU Project
Group: Books/Howtos

%description
GNU manuals are documents which describe tools from GNU Project.
The latest versions of these documents are located
at http://www.gnu.org.ru/

In this package, you can find GNU documents written in %longLANG. This is probably
not the most full collection of them (as comapred to other languages) and
some of them may be outdated, so you may wish to visit GNU site
http://www.gnu.org/doc/doc.html

%description -n %name-html
GNU manuals are documents which describe tools from GNU Project.
The latest versions of these documents are located
at http://www.gnu.org.ru/

In this package, you can find GNU documents written in %longLANG. This is probably
not the most full collection of them (as comapred to other languages) and
some of them may be outdated, so you may wish to visit GNU site
http://www.gnu.org/doc/doc.html

%prep
%install
#config
srcenc=koi8-r
dstenc=koi8-r
insertmeta_koi8=1 # 1-true 0-false
insertmeta_1251=0

#process
rootdir=$RPM_BUILD_ROOT
mkdir -p $rootdir
pushd $rootdir
bzcat %SOURCE0 | tar xv
bzcat %SOURCE1 | tar xv
bzcat %SOURCE2 | tar xv

  htmlbase=$rootdir%_docdir/%name/%formathtml
  pdfbase=$rootdir%_docdir/%name/%formatpdf
  mkdir -p $htmlbase
#process manuals
	#process texi
	for srcdir in `find doc-gnu-ru-manuals/* -type d` ; do
		docname=`basename $srcdir`
		texifile=$srcdir/$docname.texi
		[ -f $texifile ] || texifile=$texifile"nfo";
		mkdir -p $htmlbase/$docname
		pushd $htmlbase/$docname
		echo ----------------------------------- $texifile _________________________
		texi2html $rootdir/$texifile
		ln -s $docname.html index.html
		popd
	done
	#convert texinfo*.html's to koi8-r
	for htmlfile in `find $htmlbase/texinfo -type f -name \*.htm*`; do
		iconv -f iso-8859-5 -t koi8-r $htmlfile > $htmlfile.new
		mv -f $htmlfile.new $htmlfile
	done
	#process tarred htmls
	for srcfile in `find doc-gnu-ru-manuals -name \*.tar`; do
		subdir=`echo $srcfile| sed -e "s/doc-gnu-ru-manuals//"|sed -e "s/\/[^\/]*$//"`
    	pushd $htmlbase$subdir
		tar xf  $rootdir/$srcfile
		popd
	done
	#insert meta
	for htmlfile in `find $htmlbase -type f -name \*.htm*`; do
    	if [ $insertmeta_koi8 == 1 ]; then
			perl -p -i -e '$/=">"; s/<HEAD(\n)*>/<HEAD><meta content="text\/html; charset=KOI8-R" http-equiv="Content-Type">/i'  $htmlfile
		fi
		if [ $insertmeta_1251 == 1 ]; then
			perl -p -i -e '$/=">"; s/<HEAD(\n)*>/<HEAD><meta content="text\/html; charset=Windows-1251" http-equiv="Content-Type">/i'  $htmlfile
		fi
		if [ $srcenc != $dstenc ]; then
		 iconv -f $srcenc -t $dstenc $htmlfile > $htmlfile.new
		 mv -f $htmlfile.new $htmlfile
		fi
	done

#process philosophy
	#process tarred htmls
	for srcfile in `find doc-gnu-ru-philosophy -name \*.tar`; do
		subdir=`echo $srcfile| sed -e "s/doc-gnu-ru-philosophy//"|sed -e "s/\/[^\/]*$//"`
    	pushd $htmlbase$subdir
		tar xf  $rootdir/$srcfile
		popd
	done
#make index
  ./makedirindex 'GNU-Документация' '<meta http-equiv="Content-Type" content="text/html; charset=koi8-r">' 'doc-gnu-ru-philosophy' 'Философия' 'doc-gnu-ru-manuals' 'Руководства'
  mv -f index.html $htmlbase
  install -m 644 gnu-head-sm.jpg $htmlbase/gnu-head-sm.jpg
popd;

unset rootdir

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=GNU Documentation
Comment=Manuals and other non-technical ducuments (html format, in Russian) from GNU Project
Icon=howto
Exec=url_handler.sh /usr/share/doc/doc-gnu-ru/HTML/index.html
Categories=Development;Documentation;
EOF


%files -n %name-html
%_docdir/%name/%formathtml
%_desktopdir/%{name}.desktop

%changelog
* Sun Apr 10 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa4
- NMU: second cleanup of .desktop files

* Tue Mar 29 2011 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa3
- NMU: converted debian menu to freedesktop

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa2
- NMU (by repocop): the following fixes applied:
  * update_menus for doc-gnu-ru-html

* Thu Apr 10 2008 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa1
- NMU (by repocop): the following fixes applied:
 * update_menus for doc-gnu-ru-html

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt2
- rebuild

* Fri Mar 29 2002 Maxim Dzumanenko <mvd@altlinux.ru> 1.0-alt1
- first version
