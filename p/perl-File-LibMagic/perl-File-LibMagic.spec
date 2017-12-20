%define _unpackaged_files_terminate_build 1
%define dist File-LibMagic
Name: perl-File-LibMagic
Version: 1.16
Release: alt1

Summary: Perl wrapper for libmagic
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/D/DR/DROLSKY/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: libmagic-devel perl-devel zlib-devel perl(ExtUtils/CBuilder.pm) perl(Test/Fatal.pm)

%description
The "File::LibMagic" is a simple perl interface to libmagic from
the file-4.x package from Christos Zoulas (ftp://ftp.astron.com/pub/file/).

%prep
%setup -q -n %{dist}-%{version}

#if [ %version == 1.16 ];then
sed -i -e s,us-ascii,7bit, t/oo-api.t
#fi

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.md CONTRIBUTING.md INSTALL.md
%perl_vendor_archlib/File
%perl_vendor_autolib/File

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1
- rebuild with new perl 5.22.0

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- rebuild with new perl 5.20.1

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.99-alt1
- 0.97 -> 0.99

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.97-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 0.96-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.96-alt2
- rebuilt for perl-5.14

* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.96-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.90-alt1.1
- rebuilt with perl 5.12

* Wed Feb 18 2009 Alexey Tourbin <at@altlinux.ru> 0.90-alt1
- 0.89 -> 0.90

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.89-alt1
- removed perl dir ownership
- new version

* Fri Jun 01 2007 Igor Vlasenko <viy@altlinux.ru> 0.84-alt1
- first build for ALT Linux Sisyphus

