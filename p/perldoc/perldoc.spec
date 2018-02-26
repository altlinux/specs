%define dist Pod-Perldoc
Name: perldoc
Version: 3.15
Release: alt1

Summary: perldoc is program for reading Pod documentation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Pod::Perldoc frontends require additional modules
%add_findreq_skiplist */Pod/Perldoc/ToTk.pm */Pod/Perldoc/ToRtf.pm */Pod/Perldoc/ToXml.pm

BuildArch: noarch
Requires: groff-base less

# Added by buildreq2 on Thu Apr 21 2005
BuildRequires: less perl-Pod-Simple perl-devel
BuildRequires: perl-Pod-Parser

%description
perldoc is program for reading Pod documentation.  Pod (the Plain
Old Documentation format) is a simple-to-use markup language used
for writing documentation for Perl, Perl programs, and Perl modules.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	ChangeLog README
	%_bindir/perldoc
%dir	%perl_vendor_privlib/Pod
	%perl_vendor_privlib/Pod/Perldoc*
	%perl_vendor_privlib/perldoc.pod

%changelog
* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 3.15-alt1
- new version 3.15
- dropped patches (Closes: #9043)
- rebuilt with perl 5.12

* Fri Apr 22 2005 Alexey Tourbin <at@altlinux.ru> 3.14-alt2
- implemented cache for nroff formatted output (mkdir ~/.perldoc)

* Thu Dec 09 2004 Alexey Tourbin <at@altlinux.ru> 3.14-alt1
- initial revision (split off from perl-base)
