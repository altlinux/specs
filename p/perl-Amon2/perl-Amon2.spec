%define _unpackaged_files_terminate_build 1
Name: perl-Amon2
Version: 6.16
Release: alt1
Summary: Amon2 - lightweight web application framework

Group: Development/Perl
License: Perl
Url: %CPAN Amon2
VCS: https://github.com/tokuhirom/Amon.git

BuildArch: noarch
Source: %name-%version.tar

BuildRequires: perl-Module-Build-Tiny perl-Module-CPANfile perl-Router-Boom perl-Test-Requires perl-Plack perl-Data-OptList perl-Text-Xslate perl-JSON perl-Module-Find perl-Mouse perl-Router-Simple perl-Router-Simple-Sinatraish perl-Class-Accessor perl-Text-Xslate-Bridge-TT2Like perl-Data-Section-Simple perl-Plack-Middleware-ReverseProxy perl-HTTP-Session perl-HTML-FillInForm-Lite perl-CGI perl-Encode-JP perl-Plack-Middleware-Session perl-AnyEvent perl-Protocol-WebSocket

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README.mkdn README.md
%_bindir/amon2-setup.pl
%_man1dir/amon2-setup.*
%perl_vendor_privlib/Amon2*
%perl_vendor_privlib/auto/share/dist/Amon2
%doc Changes

%changelog
* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 6.16-alt1
- new version 6.16

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 6.15-alt1
- new version

* Sat Nov 07 2020 Igor Vlasenko <viy@altlinux.ru> 6.14-alt2
- dropped MRO::Compat dep
- upstream: https://github.com/tokuhirom/Amon/issues/128

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 6.14-alt1
- new version

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 6.13-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 6.12-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 6.11-alt1
- automated CPAN update

* Wed Apr 23 2014 Vladimir Lettiev <crux@altlinux.ru> 6.02-alt1
- 6.00 -> 6.02

* Mon Dec 09 2013 Vladimir Lettiev <crux@altlinux.ru> 6.00-alt1
- 4.01 -> 6.00

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 4.01-alt1
- 3.53 -> 4.01

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 3.53-alt1
- 3.35 -> 3.53
- new builddeps: perl-AnyEvent perl-Protocol-WebSocket

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 3.35-alt1
- New version 3.35

* Thu Dec 15 2011 Vladimir Lettiev <crux@altlinux.ru> 3.32-alt1
- New version 3.32

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 3.31-alt1
- New version 3.31

* Thu Jul 28 2011 Vladimir Lettiev <crux@altlinux.ru> 2.49-alt1
- initial build
