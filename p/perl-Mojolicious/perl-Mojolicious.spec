%define _unpackaged_files_terminate_build 1
Epoch: 1
Name: perl-Mojolicious
Version: 9.30
Release: alt1
Summary: Real-time web framework

Group: Development/Perl
License: Perl
Url: %CPAN Mojolicious

Source0: %name-%version.tar
Source1: hypnotoad.init
Source2: hypnotoad.sysconfig

BuildArch: noarch
BuildRequires: perl-devel perl-EV perl-Digest-SHA perl-Encode perl-I18N-LangTags perl-Locale-Maketext perl-unicore perl-Encode-JP perl-Pod-Simple perl-IO-Socket-SSL perl-podlators perl-Compress-Raw-Zlib perl-IO-Compress perl(JSON/PP.pm) perl(experimental.pm) perl(CPAN/Meta/YAML.pm)

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
%doc Changes README.md examples
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
%doc Changes

%changelog
* Mon Nov 28 2022 Igor Vlasenko <viy@altlinux.org> 1:9.30-alt1
- new version

* Sun Oct 16 2022 Igor Vlasenko <viy@altlinux.org> 1:9.28-alt1
- new version

* Tue Sep 13 2022 Igor Vlasenko <viy@altlinux.org> 1:9.27-alt1
- new version

* Tue May 24 2022 Igor Vlasenko <viy@altlinux.org> 1:9.26-alt1
- new version

* Sun May 01 2022 Igor Vlasenko <viy@altlinux.org> 1:9.25-alt1
- new version

* Tue Apr 19 2022 Igor Vlasenko <viy@altlinux.org> 1:9.24-alt1
- new version

* Thu Apr 07 2022 Igor Vlasenko <viy@altlinux.org> 1:9.23-alt1
- new version

* Sun Oct 24 2021 Igor Vlasenko <viy@altlinux.org> 1:9.22-alt1
- new version

* Tue Aug 17 2021 Igor Vlasenko <viy@altlinux.org> 1:9.21-alt1
- new version

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 1:9.19-alt1
- new version

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 1:9.18-alt1
- new version

* Wed Apr 14 2021 Igor Vlasenko <viy@altlinux.org> 1:9.17-alt1
- new version

* Tue Apr 13 2021 Igor Vlasenko <viy@altlinux.org> 1:9.16-alt1
- new version

* Wed Mar 24 2021 Igor Vlasenko <viy@altlinux.org> 1:9.14-alt1
- new version

* Mon Mar 15 2021 Igor Vlasenko <viy@altlinux.org> 1:9.10-alt1
- new version

* Wed Mar 03 2021 Igor Vlasenko <viy@altlinux.org> 1:9.02-alt1
- new version

* Wed Feb 17 2021 Igor Vlasenko <viy@altlinux.ru> 1:9.01-alt1
- new version

* Tue Feb 16 2021 Igor Vlasenko <viy@altlinux.ru> 1:9.0-alt1
- new version

* Wed Feb 10 2021 Igor Vlasenko <viy@altlinux.ru> 1:8.73-alt1
- new version

* Mon Feb 01 2021 Igor Vlasenko <viy@altlinux.ru> 1:8.72-alt1
- new version

* Thu Jan 21 2021 Igor Vlasenko <viy@altlinux.ru> 1:8.71-alt1
- new version

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 1:8.70-alt1
- new version

* Wed Dec 30 2020 Igor Vlasenko <viy@altlinux.ru> 1:8.69-alt1
- new version

* Fri Dec 25 2020 Igor Vlasenko <viy@altlinux.ru> 1:8.67-alt1.1
- new version

* Mon Dec 14 2020 Igor Vlasenko <viy@altlinux.ru> 8.67.1-alt1
- unofficial 8.68 pre release for aas@

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 8.67-alt1
- new version

* Tue Dec 01 2020 Igor Vlasenko <viy@altlinux.ru> 8.66-alt1
- new version

* Wed Nov 18 2020 Igor Vlasenko <viy@altlinux.ru> 8.65-alt1
- new version

* Sun Nov 08 2020 Igor Vlasenko <viy@altlinux.ru> 8.64-alt1
- new version

* Sat Oct 24 2020 Igor Vlasenko <viy@altlinux.ru> 8.63-alt1
- new version

* Tue Oct 06 2020 Igor Vlasenko <viy@altlinux.ru> 8.61-alt1
- new version

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 8.60-alt1
- new version

* Tue Sep 01 2020 Igor Vlasenko <viy@altlinux.ru> 8.58-alt1
- new version

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 8.55-alt1
- new version

* Sat Jun 06 2020 Igor Vlasenko <viy@altlinux.ru> 8.52-alt1
- new version

* Mon Apr 27 2020 Igor Vlasenko <viy@altlinux.ru> 8.40-alt1
- new version

* Wed Apr 22 2020 Igor Vlasenko <viy@altlinux.ru> 8.38-alt1
- new version

* Sat Apr 04 2020 Igor Vlasenko <viy@altlinux.ru> 8.36-alt1
- new version

* Wed Mar 25 2020 Igor Vlasenko <viy@altlinux.ru> 8.35-alt1
- new version

* Mon Feb 17 2020 Igor Vlasenko <viy@altlinux.ru> 8.33-alt1
- new version

* Sat Jan 25 2020 Igor Vlasenko <viy@altlinux.ru> 8.32-alt1
- new version

* Wed Jan 08 2020 Igor Vlasenko <viy@altlinux.ru> 8.29-alt1
- new version

* Wed Dec 11 2019 Igor Vlasenko <viy@altlinux.ru> 8.27-alt1
- new version

* Thu Nov 07 2019 Igor Vlasenko <viy@altlinux.ru> 8.26-alt1
- new version

* Mon Sep 30 2019 Igor Vlasenko <viy@altlinux.ru> 8.25-alt1
- new version

* Fri Sep 20 2019 Igor Vlasenko <viy@altlinux.ru> 8.24-alt1
- new version

* Thu Aug 15 2019 Igor Vlasenko <viy@altlinux.ru> 8.23-alt1
- new version

* Mon Jul 22 2019 Igor Vlasenko <viy@altlinux.ru> 8.22-alt1
- new version

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 8.21-alt1
- new version

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 8.18-alt1
- new version

* Fri May 24 2019 Igor Vlasenko <viy@altlinux.ru> 8.17-alt1
- new version

* Tue May 21 2019 Igor Vlasenko <viy@altlinux.ru> 8.16-alt1
- new version

* Sat Apr 27 2019 Igor Vlasenko <viy@altlinux.ru> 8.15-alt1
- new version

* Mon Apr 22 2019 Igor Vlasenko <viy@altlinux.ru> 8.14-alt1
- new version

* Wed Mar 27 2019 Igor Vlasenko <viy@altlinux.ru> 8.13-alt1
- new version

* Sat Feb 02 2019 Igor Vlasenko <viy@altlinux.ru> 8.12-alt1
- automated CPAN update

* Thu Jan 03 2019 Igor Vlasenko <viy@altlinux.ru> 8.11-alt1
- automated CPAN update

* Sat Dec 22 2018 Igor Vlasenko <viy@altlinux.ru> 8.10-alt1
- automated CPAN update

* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 8.09-alt1
- automated CPAN update

* Fri Nov 09 2018 Igor Vlasenko <viy@altlinux.ru> 8.06-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 8.04-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 8.02-alt1
- automated CPAN update

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 7.88-alt1
- automated CPAN update

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 7.87-alt1
- automated CPAN update

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 7.85-alt1
- automated CPAN update

* Wed Jun 13 2018 Igor Vlasenko <viy@altlinux.ru> 7.84-alt1
- automated CPAN update

* Wed Jun 06 2018 Igor Vlasenko <viy@altlinux.ru> 7.83-alt1
- automated CPAN update

* Mon May 28 2018 Igor Vlasenko <viy@altlinux.ru> 7.82-alt1
- automated CPAN update

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 7.81-alt1
- automated CPAN update

* Thu May 17 2018 Igor Vlasenko <viy@altlinux.ru> 7.79-alt1
- automated CPAN update

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 7.77-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 7.76-alt1
- automated CPAN update

* Fri Apr 13 2018 Igor Vlasenko <viy@altlinux.ru> 7.75-alt1.1
- automated CPAN update

* Thu Apr 12 2018 Igor Vlasenko <viy@altlinux.ru> 7.75-alt1
- automated CPAN update

* Mon Apr 09 2018 Igor Vlasenko <viy@altlinux.ru> 7.74-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 7.72-alt1
- automated CPAN update

* Sat Mar 17 2018 Igor Vlasenko <viy@altlinux.ru> 7.71-alt1
- automated CPAN update

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 7.70-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 7.67-alt1
- automated CPAN update

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
