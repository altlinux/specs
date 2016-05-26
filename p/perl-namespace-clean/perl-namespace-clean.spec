%define _unpackaged_files_terminate_build 1
%define dist namespace-clean

Name: perl-namespace-clean
Version: 0.27
Release: alt1

Summary: Keep imports and functions out of your namespace

License: Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source: http://www.cpan.org/authors/id/R/RI/RIBASUSHI/namespace-clean-%{version}.tar.gz

BuildRequires: perl-B-Hooks-EndOfScope perl-Package-Stash perl-devel

%description
None.

%prep
%setup -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/namespace/clean.pm
%perl_vendor_privlib/namespace/clean/_Util.pm

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.24-alt1
- 0.024
- spec cleanup

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- initial revision, for MooseX::Types


