%define m_distro HTML-Widget

Name: perl-%m_distro
Version: 1.11
Release: alt2

Summary: HTML Widget And Validation Framework

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz
# Patch from debian #605809
# Fixed tests with perl-HTML-Tree >= 4
Patch: html-tree-4.patch

# Automatically added by buildreq on Fri Jun 13 2008
BuildRequires: perl-Class-Accessor-Chained perl-Class-Data-Accessor perl-Date-Calc perl-Devel-StackTrace perl-Email-Valid perl-HTML-Scrubber perl-HTML-Tree perl-Log-Agent perl-Module-Install perl-Module-Pluggable-Fast perl-NEXT perl-Test-NoWarnings perl-Test-Pod perl-Test-Pod-Coverage

%description
Create easy to maintain HTML widgets!

Everything is optional, use validation only or just generate
forms, you can embed and merge them later.

The API was designed similar to other popular modules like
Data::FormValidator and FormValidator::Simple, HTML::FillInForm
is also built in (and much faster).

This Module is very powerful, don't misuse it as a template system!

%prep
%setup -q -n %m_distro-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTML/Widget*
%exclude %perl_vendor_archlib

%changelog
* Wed Mar 09 2011 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt2
- Applied patch from debian to make tests compatible
  with perl-HTML-Tree >= 4
- Updated buildrequires
- Spec cleanup

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.11-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Fri Jun 13 2008 Michael Bochkaryov <misha@altlinux.ru> 1.11-alt1
- first build for ALT Linux Sisyphus

