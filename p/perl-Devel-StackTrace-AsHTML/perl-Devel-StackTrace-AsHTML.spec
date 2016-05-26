%define m_distro Devel-StackTrace-AsHTML
Name: perl-Devel-StackTrace-AsHTML
Version: 0.15
Release: alt1
Summary: Devel::StackTrace::AsHTML - Displays stack trace in HTML

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~miyagawa/Devel-StackTrace-AsHTML/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-devel perl-Devel-StackTrace perl-Module-Install perl-Test-Base perl-Module-Install-AuthorTests perl-Module-Install-ReadmeFromPod

%description
Devel::StackTrace::AsHTML adds "as_html" method to Devel::StackTrace
which displays the stack trace in beautiful HTML, with code snippet
context and function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical
variables of each stack frame.

%prep
%setup -q -n %m_distro-%version
sed -i -e '/auto_set_repository/d;/use_test_base/d' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Devel/StackTrace/AsHTML*
%doc Changes README 

%changelog
* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Tue Jun 24 2014 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt1
- New version 0.11

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- initial build
