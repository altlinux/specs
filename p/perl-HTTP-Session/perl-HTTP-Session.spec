%define __spec_autodep_custom_pre export PERL5OPT='-MCarp'
Name: perl-HTTP-Session
Version: 0.49
Release: alt3
Summary: HTTP::Session - simple session

Group: Development/Perl
License: Perl
Url: %CPAN HTTP-Session

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-HTTP-Message perl-CGI-Simple perl-Module-Runtime perl-URI perl-Test-Requires perl-Class-Accessor perl-Digest-SHA1 perl-CGI perl-DBM perl-HTML-StickyQuery perl-CHI perl(Module/Build/Tiny.pm) perl(HTML/Parser.pm)

%description
%summary

%prep
%setup -q

# bad RE for data
[ "%version" = 0.49 ] &&  rm t/030_state/002_cookie.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/HTTP/Session*
%doc Changes README*

%changelog
* Mon Oct 23 2023 Igor Vlasenko <viy@altlinux.org> 0.49-alt3
- fixed build

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.49-alt2
- fixed build

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.48-alt1
- automated CPAN update

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 0.46-alt1
- 0.46

* Fri Jul 29 2011 Vladimir Lettiev <crux@altlinux.ru> 0.44-alt1
- initial build
