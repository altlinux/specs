%define _unpackaged_files_terminate_build 1
%define dist Pod-Perldoc
Name: perl-%dist
Version: 3.27
Release: alt1

Summary: perldoc is program for reading Pod documentation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MA/MALLEN/Pod-Perldoc-%{version}.tar.gz

# Pod::Perldoc frontends require additional modules
%add_findreq_skiplist */Pod/Perldoc/ToTk.pm
%add_findreq_skiplist */Pod/Perldoc/ToRtf.pm
%add_findreq_skiplist */Pod/Perldoc/ToXml.pm

BuildArch: noarch

Provides: perldoc = %version
Obsoletes: perldoc < %version

Requires: groff-base less

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: less perl-devel perl-parent perl-podlators

%description
perldoc is program for reading Pod documentation.  Pod (the Plain
Old Documentation format) is a simple-to-use markup language used
for writing documentation for Perl, Perl programs, and Perl modules.

%prep
%setup -q -n %dist-%version

# disable build dependency on Tk::Pod
%ifdef __buildreqs
sed -i- 's/require Tk;/die;/' t/load.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
	%_bindir/perldoc
	%_man1dir/perldoc.*
	%perl_vendor_privlib/Pod
# XXX perl-pod has pod/perldoc.pod
#%doc	%perl_vendor_privlib/perldoc.pod
%exclude %perl_vendor_privlib/perldoc.pod

%changelog
* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.27-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 3.26-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 3.25-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 3.24-alt1
- automated CPAN update

* Mon Feb 24 2014 Igor Vlasenko <viy@altlinux.ru> 3.23-alt1
- automated CPAN update

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 3.21-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 3.20-alt1
- automated CPAN update

* Tue Sep 25 2012 Alexey Tourbin <at@altlinux.ru> 3.17-alt1
- 3.15 -> 3.17
- renamed perldoc packages to perl-Pod-Perldoc

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.15-alt1
- new version 3.15
- dropped patches (Closes: #9043)
- rebuilt with perl 5.12

* Fri Apr 22 2005 Alexey Tourbin <at@altlinux.ru> 3.14-alt2
- implemented cache for nroff formatted output (mkdir ~/.perldoc)

* Thu Dec 09 2004 Alexey Tourbin <at@altlinux.ru> 3.14-alt1
- initial revision (split off from perl-base)
