Name: manpages-xsl
Version: 0.2
Release: alt2

%define my_summary XSL-stylesheets for compiling DocBook to manual pages
%define smbxsl_url ftp://ftp.samba.org/pub/unpacked/samba-docs/xslt

Summary: %my_summary
License: GPL
Group: Publishing
Url: http://ilya-evseev.narod.ru/posix/%name
BuildArch: noarch
Packager: Ilya G. Evseev <evseev@altlinux.ru>
Source0: %smbxsl_url/man.xsl
Source1: %smbxsl_url/manpage-summary.xsl
Source2: getfiles.lftp
Patch0: remove_smbdeps.patch
Requires: alt-docs-xsl-common docbook-style-xsl

%define pkgname     alt-docs-xsl-manpages
%define xsl_topdir  %_datadir/xml/alt-docs-xsl
%define xsl_mandir  %xsl_topdir/manpages
%define mydocdir    %_docdir/%name-%version

%define my_summary_ru     XSL-стили для компиляции XML-документов формата DocBook в man-страницы
%define my_description    This package contain XSL styles developed by Samba Team for compiling documentation from DocBook to manual pages.
%define my_description_ru Данный пакет содержит XSL-стили, созданные в рамках проекта Samba и предназначенные для компиляции XML-документов, использующих разметку DocBook, в man-страницы.

Summary(ru_RU.KOI8-R): %my_summary_ru

%description
%my_description
%description -l ru_RU.KOI8-R
%my_description_ru

%package -n %pkgname
Summary: %my_summary
Summary(ru_RU.KOI8-R): %my_summary_ru
Group: Publishing
%description -n %pkgname
%my_description
%description -n %pkgname -l ru_RU.KOI8-R
%my_description_ru

%prep
# %setup -c -q

%build

%install
mkdir -p %buildroot%xsl_mandir
%__cp -af %SOURCE0 %SOURCE1 %buildroot%xsl_mandir
cd %buildroot%xsl_mandir
%__patch < %PATCH0

mkdir -p %buildroot%mydocdir
cat << __EOF__ > %buildroot%mydocdir/docbook2man
#!/bin/sh

if [ \$# = 0 ]; then
    echo Usage: docbook2man file.xml...
else
    xsltproc --xinclude --stringparam chunker.output.encoding "KOI8-R" \\
	"%xsl_mandir/man.xsl" "\$@"
fi

## EOF ##
__EOF__

%files -n %pkgname
%doc %mydocdir
%xsl_mandir

%changelog
* Wed May 06 2009 Slava Semushin <php-coder@altlinux.ru> 0.2-alt2
- NMU
- docbook2man: make it work (Closes: #19933)

* Sat Jan  1 2005 Ilya G. Evseev <evseev@altlinux.ru> 0.2-alt1
- source stylesheets are taken directly from Samba site, then patched locally,
  see getfiles.lftp script for details.

* Fri Dec 24 2004 Ilya G. Evseev <evseev@altlinux.ru> 0.1-alt1
- Initial build

## EOF ##
