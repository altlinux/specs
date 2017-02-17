BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
Name: perl-CGI-Compile
Version: 0.22
Release: alt1
Summary: CGI::Compile - Compile .cgi scripts to a code reference like ModPerl::Registry

Group: Development/Perl
License: Perl
Url: %CPAN CGI-Compile

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-File-pushd perl-Test-Requires perl-Test-NoWarnings perl-CGI

%description
CGI::Compile is an utility to compile CGI scripts into a code reference
that can run many times on its own namespace, as long as the script is
ready to run on a persistent environment.

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CGI/Compile.pm
%doc Changes README

%changelog
* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- automated CPAN update

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt1
- New version 0.15

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- New version 0.14

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.12-alt1
- initial build
