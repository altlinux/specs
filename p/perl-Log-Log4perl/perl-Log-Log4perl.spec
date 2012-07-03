%define dist Log-Log4perl
Name: perl-%dist
Version: 1.33
Release: alt1

Summary: Log4j implementation for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MS/MSCHILLI/Log-Log4perl-1.33.tar.gz
Patch: perl-Log-Log4perl-1.09-alt-disable-tobedone-LDAP.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011 (-bi)
BuildRequires: perl-DBD-CSV perl-Data-Dump perl-Filter perl-IPC-SysV perl-Log-Dispatch perl-RRD perl-XML-DOM perl-devel

%description
Log::Log4perl lets you remote-control and fine-tune the logging
behaviour of your system from the outside. It implements the widely
popular (Java-based) Log4j logging package in pure Perl.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

# FIXME: Log::Log4perl::JavaMap::RollingFileAppender depends
# on Log::Dispatch::FileRotate, which requires Log::Log4perl.
%add_findreq_skiplist */Log/Log4perl/JavaMap/RollingFileAppender.pm

# XXX Can't locate object method "new" via package "Log::Log4perl::Layout::PatternLayout"
%add_findreq_skiplist */Log/Log4perl/Layout.pm
%add_findreq_skiplist */Log/Log4perl/Layout/PatternLayout/Multiline.pm
%add_findreq_skiplist */Log/Log4perl/Layout/SimpleLayout.pm

%files
%doc Changes README
%perl_vendor_privlib/Log
%_bindir/l4p-tmpl

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Wed Apr 27 2011 Alexey Tourbin <at@altlinux.ru> 1.32-alt1
- 1.21 -> 1.32

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 21 2009 Michael Bochkaryov <misha@altlinux.ru> 1.21-alt1
- 1.21 version

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Apr 23 2008 Michael Bochkaryov <misha@altlinux.ru> 1.15-alt1
- updated to 1.15 version

* Thu Mar 22 2007 Sir Raorn <raorn@altlinux.ru> 1.09-alt1
- first build for ALT Linux Sisyphus
