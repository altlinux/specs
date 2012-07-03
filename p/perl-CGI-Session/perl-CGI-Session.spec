%define dist CGI-Session
Name: perl-%dist
Version: 4.48
Release: alt2

Summary: Persistent session data in CGI applications
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# avoid dependency on perl-devel
%add_findreq_skiplist */CGI/Session/Test*

# Automatically added by buildreq on Mon Nov 14 2011 (-bi)
BuildRequires: perl-CGI perl-CGI-Simple perl-DBD-Pg perl-DBD-SQLite perl-DBD-mysql perl-DBM perl-FreezeThaw perl-Module-Build

%description
CGI-Session is a Perl5 library that provides an easy, reliable and modular
session management system across HTTP requests. Persistency is a key feature
for such applications as shopping carts, login/authentication routines, and
application that need to carry data across HTTP requests. CGI::Session does
that and many more.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CGI

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 4.48-alt2
- rebuilt as plain src.rpm
- disabled dependency on perl-devel

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 4.48-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 4.42-alt1
- automated CPAN update

* Fri Feb 06 2009 Denis Smirnov <mithraen@altlinux.ru> 4.40-alt5
- some more fixes in build requires

* Fri Feb 06 2009 Denis Smirnov <mithraen@altlinux.ru> 4.40-alt4
- fix build requires

* Fri Feb 06 2009 Denis Smirnov <mithraen@altlinux.ru> 4.40-alt3
- version update

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 3.95-alt3
- cleanup spec

* Thu Jun 16 2005 Denis Smirnov <mithraen@altlinux.ru> 3.95-alt2
- rebuild

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.95-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Feb 16 2004 Denis Smirnov <mithraen@altlinux.ru> 3.95-alt1
- package created
