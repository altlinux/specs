Name: perl-Plack
Version: 1.0047
Release: alt1

Summary: Plack - Perl Superglue for Web frameworks and Web Servers (PSGI toolkit)
License: Perl
Group: Development/Perl

Url: %CPAN Plack
Source: %name-%version.tar

BuildRequires: perl-Apache-LogFormat-Compiler perl-HTTP-Tiny perl-File-ShareDir-Install perl-File-ShareDir perl-unicore perl-devel
BuildRequires: perl-Hash-MultiValue perl-Devel-StackTrace-AsHTML perl-Try-Tiny perl-libwww perl-Devel-StackTrace
BuildRequires: perl-Test-TCP perl-HTTP-Body perl-Test-Requires perl-URI perl-Filesys-Notify-Simple perl-parent
BuildRequires: perl-CGI-Emulate-PSGI perl-CGI-Compile perl-FCGI-Client perl-CGI apache2-mod_perl perl-FCGI perl-HTTP-Server-Simple-PSGI perl-Moose
BuildRequires: perl-Net-FastCGI perl-Module-Refresh perl-podlators perl-Stream-Buffered
BuildRequires: perl(Cookie/Baker.pm) perl(HTTP/Headers/Fast.pm) perl(HTTP/Entity/Parser.pm) perl(HTTP/Entity/Parser/JSON.pm) perl(JSON/PP.pm)
BuildArch: noarch

%description
Plack is a set of tools for using the PSGI stack. It contains middleware
components, a reference server and utilities for Web application
frameworks. Plack is like Ruby's Rack or Python's Paste for WSGI.

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
# don't need this for build
sed -i "/authority/d" Makefile.PL
sed -i "/author_tests/d" Makefile.PL

# remove apache1 support
find . -iname 'apache1*' -delete

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README* LICENSE
%_bindir/plackup
%_man1dir/plackup.1*
%perl_vendor_privlib/HTTP/Message/PSGI.pm
%perl_vendor_privlib/HTTP/Server/PSGI.pm
%perl_vendor_privlib/auto/share/dist/Plack/baybridge.jpg
%perl_vendor_privlib/auto/share/dist/Plack/face.jpg
%perl_vendor_privlib/Plack*
%doc Changes
%exclude %perl_vendor_privlib/Plack/Handler/Apache2.pm
%exclude %perl_vendor_privlib/Plack/Handler/Apache2/Registry.pm
%exclude %perl_vendor_privlib/Plack/Handler/FCGI.pm

%files Apache2
%perl_vendor_privlib/Plack/Handler/Apache2.pm
%perl_vendor_privlib/Plack/Handler/Apache2/Registry.pm

%files FCGI
%perl_vendor_privlib/Plack/Handler/FCGI.pm

%changelog
* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.0047-alt1
- automated CPAN update

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0044-alt2
- Updated build dependencies.
- Removed apache1 support.

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 1.0044-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.0042-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.0039-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.0037-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.0033-alt1
- automated CPAN update

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 1.0030-alt1
- new version 1.0030

* Fri Sep 20 2013 Vladimir Lettiev <crux@altlinux.ru> 1.0029-alt1
- 1.0014 -> 1.0029
- updated build deps

* Fri Dec 14 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0014-alt1
- 1.0004 -> 1.0014
- updated build deps

* Sun Sep 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.0004-alt1
- 0.9989 -> 1.0004

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
