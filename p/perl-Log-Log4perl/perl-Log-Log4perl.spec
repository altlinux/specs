%define _unpackaged_files_terminate_build 1
%add_findreq_skiplist %perl_vendor_privlib/Log/Log4perl/Filter/MDC.pm
%define dist Log-Log4perl
Name: perl-%dist
Version: 1.49
Release: alt1

Summary: Log4j implementation for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/MS/MSCHILLI/%{dist}-%{version}.tar.gz
Patch: perl-Log-Log4perl-1.37-alt-disable-tobedone-LDAP.patch

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 27 2011 (-bi)
BuildRequires: perl-DBD-CSV perl-Data-Dump perl-Filter perl-IPC-SysV perl-Log-Dispatch perl-RRD perl-XML-DOM perl-devel

%description
Log::Log4perl lets you remote-control and fine-tune the logging
behaviour of your system from the outside. It implements the widely
popular (Java-based) Log4j logging package in pure Perl.

%package Appender-RRDs
Summary: %dist backend - Log to a RRDtool Archive
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release

%description Appender-RRDs
Log::Log4perl::Appender::RRDs appenders facilitate writing data
to RRDtool round-robin archives via Log4perl. For documentation
on RRD and its Perl interface RRDs (which comes with the distribution),
check out http://rrdtool.org.

Messages sent to Log4perl's RRDs appender are expected to be numerical values
(ints or floats), which then are used to run a rrdtool update command
on an existing round-robin database. The name of this database needs to
be set in the appender's dbname configuration parameter.

If there's more parameters you wish to pass to the update method,
use the rrdupd_params configuration parameter:

    log4perl.appender.RRDapp.rrdupd_params = --template=in:out

To read out the round robin database later on, use rrdtool fetch
or rrdtool graph for graphic displays.


%prep
%setup -q -n %{dist}-%{version}
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
%exclude %perl_vendor_privlib/Log/Log4perl/Appender/RRDs.pm

%files Appender-RRDs
%perl_vendor_privlib/Log/Log4perl/Appender/RRDs.pm

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.49-alt1
- automated CPAN update

* Tue Dec 06 2016 Igor Vlasenko <viy@altlinux.ru> 1.48-alt2
- Appender-RRDs moved to subpackage (closes: #32850)

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.48-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.47-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.46-alt1
- automated CPAN update

* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Tue Mar 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Wed Sep 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.42-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.37-alt1
- 1.33 -> 1.37
- fixed build with perl-5.16
- updated alt-disable-tobedone-LDAP patch

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
