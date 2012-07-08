Name: perl-Mojolicious
Version: 3.05
Release: alt1
Summary: Real-time web framework

Group: Development/Perl
License: Perl
Url: %CPAN Mojolicious

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-devel perl-EV perl-Digest-SHA perl-Encode perl-I18N-LangTags perl-Locale-Maketext perl-unicore perl-Encode-JP perl-Pod-Simple perl-IO-Socket-SSL perl-podlators

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

%files
%_bindir/hypnotoad
%_bindir/mojo
%_bindir/morbo
%_man1dir/hypnotoad.1*
%_man1dir/mojo.1*
%_man1dir/morbo.1*
%perl_vendor_privlib/Mojo*
%perl_vendor_privlib/Test/Mojo.pm
%perl_vendor_privlib/ojo.pm
%doc LICENSE Changes README.pod

%changelog
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
