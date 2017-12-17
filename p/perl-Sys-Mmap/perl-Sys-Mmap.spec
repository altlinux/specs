%define m_distro Sys-Mmap
Name: perl-%m_distro
Version: 0.19
Release: alt1.1
Summary: Perl module to use mmap to map in a file as a Perl variable
Group: Development/Perl
License: Artistic/GPL
Url: http://search.cpan.org/CPAN/authors/id/T/TO/TODDR/Sys-Mmap-0.16.tar.gz
Source: %m_distro-%version.tar.gz
Packager: Alex Negulescu <alecs@altlinux.org>
BuildRequires: libnss-role perl-devel

%description
perl-Sys-Mmap is a Perl module to use mmap to map in a file as a Perl variable.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/Sys/*
%dir %perl_vendor_autolib/Sys/Mmap/*
%doc Artistic Changes Copying MANIFEST META.yml README

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- rebuild with new perl 5.26.1

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1.1
- rebuild with new perl 5.22.0

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt5.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt5
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.16-alt4
- rebuilt for perl-5.16

* Thu Nov 10 2011 Alex Negulescu <alecs@altlinux.org> 0.16-alt3
- added libnss-role, fix build issue

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 0.16-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Thu Jan 13 2011 Alex Negulescu <alecs@altlinux.org> 0.14-alt1
- initial build

