%define dist Log-Report
Name: perl-%dist
Version: 0.94
Release: alt1

Summary: Report a problem, pluggable handlers and language support
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MARKOV/Log-Report-0.94.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011
BuildRequires: perl-Log-Log4perl perl-PPI perl-Test-Pod

%description
Handling messages to users can be a hassle, certainly when the same
module is used for command-line and in a graphical interfaces, and
has to cope with internationalization at the same time; this set of
modules tries to simplify this.  Log::Report combines gettext features
with Log::Dispatch-like features.  However, you can also use this
module to do only translations or only message dispatching.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

# XXX Can't locate object method "new" via package "Log::Report::Dispatcher"
%add_findreq_skiplist */Log/Report/Dispatcher/*

# XXX Can't locate object method "new" via package "Log::Report::Translator::POT"
%add_findreq_skiplist */Log/Report/Translator/*

%files
%doc ChangeLog README
%perl_vendor_privlib/Log
%_bindir/xgettext-perl

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.94-alt1
- automated CPAN update

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 0.92-alt1
- 0.28 -> 0.92

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Thu Jan 08 2009 Vitaly Lipatov <lav@altlinux.ru> 0.20-alt1
- new version 0.20 (with rpmrb script)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.19-alt1
- new version 0.19 (with rpmrb script)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 0.18-alt1
- initial build for ALT Linux Sisyphus
