Name: perl-Plack
Version: 0.9989
Release: alt1
Summary: Plack - Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)

Packager: Vladimir Lettiev <crux@altlinux.ru>

Group: Development/Perl
License: Perl
Url: http://search.cpan.org/~miyagawa/Plack/

BuildArch: noarch
Source: %name-%version.tar
BuildRequires: perl-unicore perl-devel perl-Hash-MultiValue perl-Devel-StackTrace-AsHTML perl-Try-Tiny perl-libwww perl-Devel-StackTrace perl-Test-TCP perl-HTTP-Body perl-Test-Requires perl-URI perl-Filesys-Notify-Simple perl-File-ShareDir perl-parent perl-CGI-Emulate-PSGI perl-CGI-Compile perl-FCGI-Client perl-CGI perl-libapreq apache2-mod_perl perl-FCGI perl-HTTP-Server-Simple-PSGI perl-Moose perl-Net-FastCGI perl-Module-Refresh perl-Module-Install perl-podlators

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

%package Apache1
Summary: Apache 1.3.x handlers to run PSGI application
Group: Development/Perl
Requires: %name = %version-%release

%description Apache1
This is a handler module to run any PSGI application with mod_perl
on Apache 1.3.x.

%package Apache2
Summary: Apache 2.0 handlers to run PSGI application
Group: Development/Perl
Requires: %name = %version-%release

%description Apache2
This is a handler module to run any PSGI application with mod_perl
on Apache 2.x.

%package FCGI
Summary: FastCGI handler for Plack
Group: Development/Perl
Requires: %name = %version-%release

%description FCGI
This is a handler module to run any PSGI application as a standalone
FastCGI daemon or a .fcgi script.

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/plackup
%_man1dir/plackup.1*
%perl_vendor_privlib/HTTP/Message/PSGI.pm
%perl_vendor_privlib/HTTP/Server/PSGI.pm
%perl_vendor_privlib/auto/share/dist/Plack/baybridge.jpg
%perl_vendor_privlib/auto/share/dist/Plack/face.jpg
%perl_vendor_privlib/Plack*
%doc Changes README 
%exclude %perl_vendor_privlib/Plack/Handler/Apache1.pm
%exclude %perl_vendor_privlib/Plack/Server/Apache1.pm
%exclude %perl_vendor_privlib/Plack/Handler/Apache2.pm
%exclude %perl_vendor_privlib/Plack/Handler/Apache2/Registry.pm
%exclude %perl_vendor_privlib/Plack/Server/Apache2.pm
%exclude %perl_vendor_privlib/Plack/Server/FCGI.pm
%exclude %perl_vendor_privlib/Plack/Handler/FCGI.pm

%files Apache1
%perl_vendor_privlib/Plack/Handler/Apache1.pm
%perl_vendor_privlib/Plack/Server/Apache1.pm

%files Apache2
%perl_vendor_privlib/Plack/Handler/Apache2.pm
%perl_vendor_privlib/Plack/Handler/Apache2/Registry.pm
%perl_vendor_privlib/Plack/Server/Apache2.pm

%files FCGI
%perl_vendor_privlib/Plack/Server/FCGI.pm
%perl_vendor_privlib/Plack/Handler/FCGI.pm

%changelog
* Sat Jul 07 2012 Eugene Prokopiev <enp@altlinux.ru> 0.9989-alt1
- New version 0.9989

* Thu Feb 16 2012 Eugene Prokopiev <enp@altlinux.ru> 0.9985-alt1
- New version 0.9985

* Tue Jul 26 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9982-alt1
- New version 0.9982 

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9974-alt1
- New version 0.9974

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9973-alt1
- New version 0.9973
- Plack::Handler::Net::FastCGI removed from core

* Mon Feb 07 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9967-alt1
- New version 0.9967
- Separated subpackages for handlers: Apache1, Apache2 and FCGI

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 0.9962-alt1
- New version 0.9962

* Mon Dec 13 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9956-alt1
- New version 0.9956

* Fri Nov 19 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9951-alt1
- New version 0.9951
- Fixed generation of man1 pages

* Fri Oct 01 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9950-alt1
- New version 0.9950

* Mon Sep 20 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9949-alt1
- New version 0.9949

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9948-alt1
- New version 0.9948

* Sun Aug 29 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9946-alt1
- initial build
