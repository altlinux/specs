%define _unpackaged_files_terminate_build 1
Name: perl-Net-OpenSSH
Version: 0.83
Release: alt1

Summary: Net::OpenSSH - Perl SSH client package implemented on top of OpenSSH
Group: Development/Perl
License: Perl

# Cloned from https://github.com/salva/p5-Net-OpenSSH.git
Source: %name-%version.tar
Url: %CPAN Net-OpenSSH

BuildArch: noarch
BuildRequires: openssh-clients perl-devel perl(Moo.pm)

%add_findreq_skiplist */OpenSSH/More.pm

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes examples
%perl_vendor_privlib/Net/OpenSSH*
%doc Changes README

%changelog
* Tue Jan 31 2023 Igor Vlasenko <viy@altlinux.org> 0.83-alt1
- new version

* Fri Mar 25 2022 Igor Vlasenko <viy@altlinux.org> 0.82-alt1
- new version

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- new version

* Sat Jun 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.79-alt1
- new version

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.78-alt1
- automated CPAN update

* Fri Mar 09 2018 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 0.74-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.73-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.70-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.65-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Mon Apr 16 2012 Vladimir Lettiev <crux@altlinux.ru> 0.57-alt1
- 0.57

* Wed Aug 24 2011 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- initial build
