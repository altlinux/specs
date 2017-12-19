Name: perl-Mojolicious
Version: 7.59
Release: alt1
Summary: Real-time web framework

Group: Development/Perl
License: Perl
Url: %CPAN Mojolicious

Source0: %name-%version.tar
Source1: hypnotoad.init
Source2: hypnotoad.sysconfig

BuildArch: noarch
BuildRequires: perl-devel perl-EV perl-Digest-SHA perl-Encode perl-I18N-LangTags perl-Locale-Maketext perl-unicore perl-Encode-JP perl-Pod-Simple perl-IO-Socket-SSL perl-podlators perl-Compress-Raw-Zlib perl-IO-Compress perl(JSON/PP.pm) perl(experimental.pm)

%description
Mojolicious is a next generation web framework for the Perl programming
language.
Features:
* An amazing MVC web framework supporting a simplified single file mode
  through Mojolicious::Lite.
  Powerful out of the box with RESTful routes, plugins, Perl-ish
  templates, session management, signed cookies, testing framework,
  static file server, I18N, first class unicode support and much more
  for you to discover.
* Very clean, portable and Object Oriented pure Perl API without any
  hidden magic and no requirements besides Perl 5.8.7.
* Full stack HTTP 1.1 and WebSocket client/server implementation with
  TLS, Bonjour, IDNA, Comet (long polling), chunking and multipart
  support.
* Builtin async IO web server supporting epoll, kqueue, UNIX domain
  sockets and hot deployment, perfect for embedding.
* Automatic CGI, FastCGI and PSGI detection.
* JSON and XML/HTML5 parser with CSS3 selector support.
* Fresh code based upon years of experience developing Catalyst.

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
mkdir -p %buildroot/%_initdir
cp %SOURCE1 %buildroot/%_initdir/hypnotoad
mkdir -p %buildroot/%_sysconfdir/sysconfig
cp %SOURCE2 %buildroot/%_sysconfdir/sysconfig/hypnotoad

%files
%doc LICENSE Changes README.md examples
%_bindir/hypnotoad
%_bindir/mojo
%_bindir/morbo
%_initdir/hypnotoad
%_sysconfdir/sysconfig/hypnotoad
%_man1dir/hypnotoad.1*
%_man1dir/mojo.1*
%_man1dir/morbo.1*
%perl_vendor_privlib/Mojo*
%perl_vendor_privlib/Test/Mojo.pm
%perl_vendor_privlib/ojo.pm
%doc LICENSE Changes

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 7.59-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 7.46-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 7.31-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 7.26-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 7.18-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 7.12-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 7.10-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 7.08-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 7.0-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 6.63-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 6.62-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 6.57-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 6.52-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 6.35-alt1
- automated CPAN update

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 6.30-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 6.29-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 6.24-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 5.71-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 5.70-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 5.69-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 5.17-alt1
- automated CPAN update

* Fri Jul 04 2014 Igor Vlasenko <viy@altlinux.ru> 5.12-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 5.10-alt1
- new version 5.10

* Fri Dec 13 2013 Vladimir Lettiev <crux@altlinux.ru> 4.60-alt1
- 4.16 -> 4.60

* Wed Jun 26 2013 Eugene Prokopiev <enp@altlinux.ru> 4.16-alt1
- 3.57 -> 4.16
- Add simple initscript for hypnotoad

* Mon Nov 19 2012 Eugene Prokopiev <enp@altlinux.ru> 3.57-alt1
- 3.44 -> 3.57

* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 3.44-alt1
- 3.05 -> 3.44

* Sun Jul 08 2012 Eugene Prokopiev <enp@altlinux.ru> 3.05-alt1
- New version 3.05

* Sat Jul 07 2012 Eugene Prokopiev <enp@altlinux.ru> 3.03-alt1
- New version 3.03

* Thu Apr 12 2012 Vladimir Lettiev <crux@altlinux.ru> 2.80-alt1
- New version 2.80

* Tue Feb 28 2012 Eugene Prokopiev <enp@altlinux.ru> 2.55-alt1
- New version 2.55

* Sat May 28 2011 Vladimir Lettiev <crux@altlinux.ru> 1.34-alt1
- New version 1.34

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt1
- New version 1.11

* Fri Feb 18 2011 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1
- initial build
