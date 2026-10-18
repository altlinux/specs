Name: pear-core
Version: 1.10.18
Release: alt1

Summary: PHP Extension and Application Repository

License: PHP
Group: Development/Other
Url: https://pear.php.net

Packager: Denis Klimov <zver@altlinux.ru>
%define getopt_ver 1.4.3
%define graph_ver 1.2.0
%define arctar_ver 1.6.1
%define xmlutil_ver 1.4.5

# Sources are the same release tarballs as in Fedora php-pear (pear.php.net, rpmgs repacks them)
# Source-url: http://download.pear.php.net/package/PEAR-%version.tgz
Source: PEAR-%version.tar
# Source1-url: http://download.pear.php.net/package/Console_Getopt-%getopt_ver.tgz
Source1: Console_Getopt-%getopt_ver.tar
# Source2-url: http://download.pear.php.net/package/Structures_Graph-%graph_ver.tgz
Source2: Structures_Graph-%graph_ver.tar
# Source3-url: http://download.pear.php.net/package/XML_Util-%xmlutil_ver.tgz
Source3: XML_Util-%xmlutil_ver.tar
# Archive_Tar 1.6.1 is released on GitHub only (installable without --force on PEAR >= 1.10.10)
# Source4-url: https://github.com/pear/Archive_Tar/archive/refs/tags/%arctar_ver.tar.gz
Source4: Archive_Tar-%arctar_ver.tar
Source10: pear.sh
Source11: pecl.sh
Source12: peardev.sh

BuildArch: noarch
Requires: /usr/bin/php

BuildRequires: /usr/bin/php
BuildRequires: rpm-build-pear >= 0.5

Obsoletes: php-pear
Provides: php-pear

Obsoletes: pear < 1.3.4-alt1.1
Provides: pear

Provides: pear-PEAR = %version
Provides: pear-Console_Getopt = %getopt_ver
Provides: pear-Structures_Graph = %graph_ver
Provides: pear-Archive_Tar = %arctar_ver
Provides: pear-XML_Util = %xmlutil_ver
Obsoletes: pear-XML_Util < 1.3

%description
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN.

This package contains also
Console_Getopt, Structures_Graph, Archive_Tar modules.

%prep
%setup -cT
# unpack every module to its own dir with package.xml
unpack_module()
{
    tar xf "$2"
    test -f "$1/package.xml"
}
unpack_module PEAR %SOURCE0
unpack_module Console_Getopt %SOURCE1
unpack_module Structures_Graph %SOURCE2
unpack_module XML_Util %SOURCE3
unpack_module Archive_Tar %SOURCE4

%build

%install
INCPATH="."
XMLLIST=""
for i in PEAR Archive_Tar Structures_Graph Console_Getopt XML_Util ; do
    INCPATH="$INCPATH:$i"
    XMLLIST="$XMLLIST $i/package.xml"
done
INCARG="-d include_path='$INCPATH'"

php -C -q $INCARG -d output_buffering=1 -d variables_order=EGPCS -d open_basedir="" \
    -d safe_mode=0 -d register_argc_argv="On" -d auto_prepend_file="" -d auto_append_file="" \
    PEAR/scripts/pearcmd.php install --force --offline --packagingroot=%buildroot $XMLLIST

# Replace /usr/bin/* with simple scripts:
install -m 755 %SOURCE10 %buildroot%_bindir/pear
install -m 755 %SOURCE11 %buildroot%_bindir/pecl
install -m 755 %SOURCE12 %buildroot%_bindir/peardev

%files
%pear_dir/
%_bindir/pear
%_bindir/pecl
%_bindir/peardev

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 1.10.18-alt1
- new version 1.10.18
- new versions of modules:
  + Archive_Tar 1.6.1
  + Console_Getopt 1.4.3
  + Structures_Graph 1.2.0
  + XML_Util 1.4.5
- download all module tarballs from pear.php.net and GitHub with rpmgs
  (SourceN-url), like Fedora php-pear does

* Thu Sep 09 2021 Vitaly Lipatov <lav@altlinux.ru> 1.10.13-alt1
- use /usr/bin/php
- new versions:
  + PEAR 1.10.13
  + Archive_Tar 1.4.14
  + Console_Getopt 1.4.3
  + XML_Util 1.4.5

* Wed Feb 13 2019 Vitaly Lipatov <lav@altlinux.ru> 1.10.1-alt2
- switch to php7 only
- Obsoletes pear-XML_Util (ALT bug 34669)

* Thu Feb 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.1-alt1
- New versions: 
  + PEAR-1.10.1
  + Console_Getopt-1.4.1
  + Structures_Graph-1.1.1
  + Archive_Tar-1.4.2
  + XML_Util-1.4.1
- drop requires php5, allow install with php7
- replace /usr/bin/* with simple scripts

* Wed Jan 07 2015 Pavel Isopenko <pauli@altlinux.org> 1.9.4-alt2
- New version Archive_Tar 1.3.13

* Thu May 31 2012 Nikolay A. Fetisov <naf@altlinux.ru> 1.9.4-alt1
- New version pear 1.9.4 and other modules (closes:#27387)

* Sun Oct 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.9.1-alt1
- new version pear 1.9.1 and other modules
- rearrange repo and rewrite build procedure

* Fri Nov 06 2009 Sergey Alembekov <rt@altlinux.ru> 1.7.1-alt2.2
- updated modules: Archive_Tar

* Wed Jul 01 2009 Boris Savelev <boris@altlinux.org> 1.7.1-alt2.1
- NMU
- remove memory limit for pecl (closes:#14050)

* Tue Jun 30 2009 Boris Savelev <boris@altlinux.org> 1.7.1-alt2
- NMU
- remove memory limit for pear (closes:#14050)

* Mon Apr 07 2008 Denis Klimov <zver@altlinux.ru> 1.7.1-alt1
- fix non canonical path in files section

* Mon Jan 21 2008 Denis Klimov <zver@altlinux.ru> 1.6.2-alt6
- add versions for provides

* Fri Jan 18 2008 Denis Klimov <zver@altlinux.ru> 1.6.2-alt5
- up memory limit to 15M in pear.sh

* Fri Jan 18 2008 Denis Klimov <zver@altlinux.ru> 1.6.2-alt4
- install with pear.sh

* Thu Jan 17 2008 Denis Klimov <zver@altlinux.ru> 1.6.2-alt3
- up memory limit in pear.sh
- add testdir and dot files from pear dir

* Mon Jan 14 2008 Denis Klimov <zver@altlinux.ru> 1.6.2-alt2
- add xml file for install Structures_Graph
- new install method
- add provides for pear-Archive_Tar, pear-Console_Getopt and pear-Structures_Graph
- add BuildRequires rpm-build-pear with version

* Wed Jan 09 2008 Denis Klimov <zver@altlinux.ru> 1.6.2-alt1
- add obsoletes and provides for pear, add provides for pear-PEAR - fix #13852 bug
- use macroses from rpm-build-pear
- change source filename format to %%name-%%version.tar

* Tue Oct 02 2007 Denis Klimov <zver@altlinux.ru> 1.6.1-alt3
- add docs and tutorials for Structures_Graph

* Mon Oct 01 2007 Denis Klimov <zver@altlinux.ru> 1.6.1-alt2
- remove wrong php5-base require

* Tue Aug 21 2007 Denis Klimov <zver@altlinux.ru> 1.6.1-alt1
- rewrite spec file
- divide to subpackages

* Mon Aug 08 2005 Alexey Gladkov <legion@altlinux.ru> 1.3.4-alt1.1
- rebuild with new PHP.
- Requires at php-base added.
- BuildRequires at php-devel added.
- Install directory changed to %%php_peardir.
- Macro phpcli changed to %%_bindir/php.

* Mon Jan 17 2005 Vladimir Lettiev <crux@altlinux.ru> 1.3.4-alt1
- updated modules: PEAR, XML_RPC, XML_Parser, DB, HTTP, Mail, Net_Socket, Log

* Mon May 17 2004 Vladimir Lettiev <crux@altlinux.ru> 1.3.1-alt2
- new modules: Date, HTML_Common, HTML_Select
- updated modules: Archive_Tar, DB, Mail, Net_SMTP, Net_Socket, XML_Parser
- added tag Provides
- corrected tag Summary (PEAR is not only for PHP v.4)

* Thu Apr 08 2004 Vladimir Lettiev <crux@altlinux.ru> 1.3.1-alt1
- first release of PEAR separated from php

