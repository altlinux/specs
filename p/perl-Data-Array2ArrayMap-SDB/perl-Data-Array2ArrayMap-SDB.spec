#################### WARNING! ######################
# this spec file is for ALT Linux distro only.     #
# other distro may have problems with rpm macro!!! #
####################################################

%define module Data-Array2ArrayMap-SDB

Name: perl-%module
Version: 0.15
Release: alt1.1.1

Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: Perl && C++/XS module to access static db (SDB) files.
License: GPL or Artistic
Group: Development/Perl
Source: %module-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: gcc-c++ perl-devel

%description
%{summary}

%package -n libmapsdb-devel
Group: Development/C
Summary: header files for mapsdb library (access to static db (SDB) files).

%description -n libmapsdb-devel
header files for mapsdb library (access to static db (SDB) files).

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot%_includedir
cp -a sdblib %buildroot%_includedir/mapsdb

%files
#doc README Changes README.ru FAQ
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%files -n libmapsdb-devel
%_includedir/mapsdb

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- rebuild with new perl 5.24.1

* Thu Jan 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- new version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- rebuild with new perl 5.20.1

* Sun Dec 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- new version

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt3
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt2.1
- rebuilt with perl 5.12

* Tue Sep 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- perl packaging fix

* Tue Oct 23 2007 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- new version

* Tue Oct 02 2007 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- new version

* Tue Sep 25 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- fixed bug in writing deep trees

* Fri Aug 24 2007 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- new version

* Sun Aug 05 2007 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- First build for Sisyphus.
