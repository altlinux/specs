%define dist CGI-Session-SQLite
Name: perl-%dist
Version: 1.0
Release: alt4

Summary: Simple Common Gateway Interface class for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: perl-CGI-Session-SQLite.patch

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-CGI-Session perl-DBD-SQLite perl-devel

%description
This perl library uses perl5 objects to make it easy to create
Web fill-out forms and parse their contents.  This package
defines CGI objects, entities that contain the values of the
current query string and other state variables.  Using a CGI
object's methods, you can examine keywords and parameters
passed to your script, and create forms whose initial values
are taken from the current query (thereby preserving state
information).

%prep
%setup -q -n %dist-%version
%patch -p2

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CGI

%changelog
* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.0-alt4
- rebuilt as plain src.rpm

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Feb 06 2009 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt3
- update for build with new CGI::Session

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt2
- cleanup spec

* Thu Jun 16 2005 Denis Smirnov <mithraen@altlinux.ru> 1.0-alt1
- build

