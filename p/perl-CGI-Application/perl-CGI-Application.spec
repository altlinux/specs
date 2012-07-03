%define dist CGI-Application
Name: perl-%dist
Version: 4.50
Release: alt1

Summary: Framework for building reusable web-applications
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# support for PSGI is optional
%filter_from_requires /PSGI/d

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-CGI perl-Class-ISA perl-HTML-Template perl-Module-Build perl-libnet

%description
CGI::Application is intended to make it easier to create sophisticated,
reusable web-based applications.  This module implements a methodology which,
if followed, will make your web software easier to design, easier to document,
easier to write, and easier to evolve.

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
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 4.50-alt1
- 4.31 -> 4.50
- disabled dependency on CGI::PSGI

* Sat Feb 26 2011 Alexey Tourbin <at@altlinux.ru> 4.31-alt1
- 4.06 -> 4.31

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 4.06-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Dec 01 2008 Denis Smirnov <mithraen@altlinux.ru> 4.06-alt2
- cleanup spec

* Mon Jun 26 2006 Denis Smirnov <mithraen@altlinux.ru> 4.06-alt1
- version update

* Thu Jun 16 2005 Denis Smirnov <mithraen@altlinux.ru> 4.01-alt1
- build
