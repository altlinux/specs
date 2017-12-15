Name: perl-B-Flags
Version: 0.17
Release: alt1.1

Summary: B::Flags - Friendlier flags for B
License: Perl
Group: Development/Perl

URL: %CPAN B-Flags
# Cloned from git git://github.com/rurban/b-flags.git
Source: %name-%version.tar

BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/B/Flags.pm
%perl_vendor_autolib/B/Flags

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- rebuild with new perl 5.26.1

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.24.1

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1.1
- rebuild with new perl 5.20.1

* Tue Oct 15 2013 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1
- 0.06 -> 0.10

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt3
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt2
- rebuilt for perl-5.16

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 0.06-alt1
- Initial release for ALTLinux Sisyphus

