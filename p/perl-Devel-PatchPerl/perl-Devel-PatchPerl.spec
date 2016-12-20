Name: perl-Devel-PatchPerl
Version: 1.46
Release: alt1

Summary: Patch perl source a la Devel::PPPort's buildperl.pl
Group: Development/Perl
License: perl

Url: %CPAN Devel-PatchPerl
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-Module-Pluggable perl-File-pushd perl-devel perl-IPC-Cmd

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%_bindir/patchperl
%_man1dir/patchperl*
%perl_vendor_privlib/Devel/PatchPerl*
%doc Changes LICENSE README

%changelog
* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.40-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 1.10-alt1
- 0.94 -> 1.10

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 0.94-alt1
- 0.76 -> 0.94

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt2
- packaged patchperl

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.76-alt1
- initial build for ALTLinux

