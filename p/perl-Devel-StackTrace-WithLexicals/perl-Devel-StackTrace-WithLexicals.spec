%define m_distro Devel-StackTrace-WithLexicals
Name: perl-Devel-StackTrace-WithLexicals
Version: 0.10
Release: alt1
Summary: Devel::StackTrace + PadWalker

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~sartak/Devel-StackTrace-WithLexicals/

BuildArch: noarch
Source: %m_distro-%version.tar
BuildRequires: perl-PadWalker perl-Devel-StackTrace perl-devel

%description
Devel::StackTrace is pretty good at generating stack traces.
PadWalker is pretty good at the inspection and modification of your
callers' lexical variables.
Devel::StackTrace::WithLexicals is pretty good at generating stack
traces with all your callers' lexical variables.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Devel/StackTrace/WithLexicals*
%doc Changes 

%changelog
* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- New version 0.08

* Mon Aug 30 2010 Vladimir Lettiev <crux@altlinux.ru> 0.04-alt1
- initial build
