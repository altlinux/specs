Name: pear-core
Version: 1.9.4
Release: alt1

Summary: PHP Extension and Application Repository
Summary(ru_RU.UTF-8): Пакет с рaсширениями для PHP

License: PHP
Group: Development/Other
Url: http://pear.php.net

Packager: Denis Klimov <zver@altlinux.ru>
Source: %name-%version.tar

BuildArch: noarch
Requires: php5

BuildPreReq: php5
BuildRequires: rpm-build-pear >= 0.3
BuildRequires: rpm-build-php5

Obsoletes: php-pear
Provides: php-pear

Obsoletes: pear < 1.3.4-alt1.1
Provides: pear

Provides: pear-PEAR = %version
Provides: pear-Console_Getopt = 1.3.1
Provides: pear-Structures_Graph = 1.0.4
Provides: pear-Archive_Tar = 1.3.10

%description
PEAR is a code repository for PHP extensions and PHP library code
similar to TeX's CTAN and Perl's CPAN.

This package contains also
Console_Getopt, Structures_Graph, Archive_Tar modules.

%prep
%setup
%build

%install
INCPATH="."
XMLLIST=""
for i in PEAR Archive_Tar Structures_Graph Console_Getopt ; do
    INCPATH="$INCPATH:$i"
    XMLLIST="$XMLLIST $i/package.xml"
done
INCARG="-d include_path='$INCPATH'"

php -C -q $INCARG -d output_buffering=1 -d variables_order=EGPCS -d open_basedir="" \
    -d safe_mode=0 -d register_argc_argv="On" -d auto_prepend_file="" -d auto_append_file="" \
    PEAR/scripts/pearcmd.php install --offline --packagingroot=%buildroot $XMLLIST

# FIXME: pear/pecl/peardev can be our scripts

%files
%pear_dir/
%_bindir/pear
%_bindir/pecl
%_bindir/peardev

%changelog
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

