Name: docbook2X
Version: 0.8.7
Release: alt0.1.qa1
Summary: Convert docbook into man and Texinfo

Group: Text tools
License: BSD
Url: http://docbook2x.sourceforge.net/
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/docbook2x/%name-%version.tar.bz2

# Automatically added by buildreq on Mon Nov 20 2006
BuildRequires: OpenSP perl-XML-SAX tidy xml-commons-resolver xml-utils xsltproc

BuildRequires: libxslt openjade
Requires: libxslt openjade texinfo

%description
docbook2X converts DocBook documents into man pages and Texinfo
documents.

%prep
%setup -q

%build
# to avoid clashing with docbook2* from docbook-utils
%configure --program-transform-name='s/docbook2/db2x_docbook2/'
%make_build
mkdir html
cp doc/*.html html

%install
%make_install install DESTDIR=%buildroot
rm -rf %buildroot%_docdir/
rm -f %buildroot%_infodir/dir
find %buildroot -type f -name .packlist -exec rm -f {} ';'
find %buildroot -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %buildroot -type f -name 'perllocal.pod' -exec rm -f {} ';'
find %buildroot -type d -depth -exec rmdir {} 2>/dev/null ';'

%files
%doc README THANKS AUTHORS html/
%_bindir/db2x_manxml
%_bindir/db2x_texixml
%_bindir/db2x_xsltproc
%_bindir/db2x_docbook2man
%_bindir/db2x_docbook2texi
%_bindir/sgml2xml-isoent
%_bindir/utf8trans
#_docdirbook2X/
%_datadir/docbook2X/
%_man1dir/*
%_infodir/docbook2*

%changelog
* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.7-alt0.1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for docbook2X
  * postclean-05-filetriggers for spec file

* Mon Nov 20 2006 Vitaly Lipatov <lav@altlinux.ru> 0.8.7-alt0.1
- initial build for ALT Linux Sisyphus (thanks FC)

* Mon Sep 11 2006 Patrice Dumas <pertusus@free.fr> 0.8.7-2
- correct the perl-XML-SAX to be perl(XML::SAX::ParserFactory)

* Thu May 18 2006 Patrice Dumas <pertusus@free.fr> - 0.8.7-1
- update to 0.8.7

* Fri Feb 17 2006 Patrice Dumas <pertusus@free.fr> - 0.8.6-1
- update to 0.8.6
- drop patch as SGMLSpl.pm is included in the scripts, not distributed
- BR perl-XML-SAX (close 188481)

* Fri Feb 17 2006 Patrice Dumas <pertusus@free.fr> - 0.8.5-2
- rebuild for fc5

* Fri Feb  3 2006 Patrice Dumas <pertusus@free.fr> - 0.8.5-1
- FE submission
