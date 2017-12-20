Name: cpan2rpm
Version: 2.028
Release: alt5

Summary: cpan2rpm - A Perl module packager

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL
Group: Development/Other
Url: http://perl.arix.com/cpan2rpm/

BuildArch: noarch
Source: %name-%version.tar.bz2
Patch: %name-%version-alt.patch
Patch1: cpan2rpm-2.028-untar.patch
Patch2: cpan2rpm-2.028-alt-viy-perl-version-check.patch
Patch3: cpan2rpm-2.028-alt-viy-fix-for-named-sourcedir.patch
# included in patch3
Patch4: cpan2rpm-2.028-alt-viy-perl526.patch

Requires: perl-Compress-Zlib perl-URI perl-devel perl-libwww sisyphus
# Automatically added by buildreq on Sun Feb 27 2005
BuildRequires: perl-Compress-Zlib perl-URI perl-devel perl-libwww perl(Pod/PlainText.pm)
BuildRequires: perl-podlators

%description
This script generates an RPM package from a Perl module.  It uses the
standard RPM file structure and creates a spec file, a source RPM,
and a binary, leaving these in their respective directories.

The script can operate on local files, directories, urls and CPAN
module names.  Install this package if you want to create RPMs out of
Perl modules.

The syntax for cpan2rpm supports multiple *distribution* names, which
can take one of four different forms:

1. a CPAN module name (e.g. XML::Simple) - When a module name is passed,
   the script will "walk" search.cpan.org to determine the latest distribution.
   If an exact match is not found, the CPAN module is used to make
   this determination.  If you have not yet configured this module,
   please refer to the REQUIREMENTS section below for further instructions.

2. a URL (both http:// and ftp:// style locators will work) - 
   In this and the above case, an automatic download of the needed tarball
   is performed (see notes for how).  The tarball is deposited in the SOURCES
   directory.

3. a path to a tarball (e.g. /tmp/XML-Simple-1.05.tar.gz) - 
   In this case, the tarball indicated gets copied to the SOURCES directory.

4. a directory path - The directory specified must contain a Makefile.PL.
   If the user intends to build a package from a directory
   (i.e. user does NOT specify --spec-only), the commands:

    perl Makefile.PL
    make
    make dist

will be performed in that directory in order to create the tarball
necessary for package creation.

%prep
%setup -q
%patch -b .orig -p2
%patch1 -p2
%patch2 -p2
%patch3 -p0
#patch4 -p1
sed -i "s|.*system.*||g" Makefile.PL
sed -i 's/Pod::Text/Pod::PlainText/' cpan2rpm

%build
# Do not build spec, it is unneeded and requests download action
echo Skipping >cpan2rpm.spec.PL
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%_man1dir/*
%doc README Changes

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 2.028-alt5
- bugix: fixed build with perl 5.26

* Tue Nov 05 2013 Igor Vlasenko <viy@altlinux.ru> 2.028-alt4
- NMU: added missing Pod dependencies

* Fri Nov 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.028-alt3
- bugfix: proper macro expansion in %_sourcedir

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.028-alt2
- bugfix: proper prefix in files 

* Mon Aug 29 2011 Igor Vlasenko <viy@altlinux.ru> 2.028-alt1
- updated to 2.028 upstream release
- disabled patch1 (fixed upstream)

* Sat Nov 27 2010 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt5
- use Pod::PlainText instead Pod::Text (ALT bug #24592)
- do not use perl_vendor_man3dir macro

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.027-alt4.1
- rebuilt with perl 5.12

* Sun Sep 20 2009 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt4
- disable run cpan2rpm during build

* Fri Oct 10 2008 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt3
- hack for directory ownership violation (bug #17453)
- do not pack man in generated specs (bug #17468)

* Sun Jun 03 2007 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt2
- fix some tarball unpacking (bug #11937), thanks viy@

* Thu Mar 01 2007 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt1
- add sisyphus to requires (fix bug #10955)

* Sat Nov 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt0.6
- fix requires

* Sun Sep 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt0.5
- use add_changelog from system
- set --no-upgrade-chk --spec-only by default
- disable internet checking during build
- fix summary generating (remove module name from it)

* Thu Aug 18 2005 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt0.4
- add --rpm/--rpm-args options (patch from Sir Raorn (#7636))

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt0.3
- add more compatibility (patch updated)

* Mon Jun 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt0.2
- add patch for ALT Perl policy compatible spec generating

* Sun Feb 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.027-alt0.1
- first build for ALT Linux Sisyphus (not supports ALT spec yet)

