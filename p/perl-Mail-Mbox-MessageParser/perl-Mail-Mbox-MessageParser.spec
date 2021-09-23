# BEGIN SourceDeps(oneline):
BuildRequires: perl(UNIVERSAL/require.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
%define dist Mail-Mbox-MessageParser
Name: perl-%dist
Version: 1.5111
Release: alt2

Summary: A fast and simple mbox folder reader
License: GPL
Group: Development/Perl
URL: %CPAN %dist
BuildArch: noarch
# http://git.altlinux.org/gears/p/%name.git
Source0: http://www.cpan.org/authors/id/D/DC/DCOPPIT/%{dist}-%{version}.tar.gz
Patch: Mail-Mbox-MessageParser-1.5105-alt.patch

# Automatically added by buildreq on Tue Feb 27 2007
BuildRequires: perl-FileHandle-Unget perl-Module-Install perl-Storable perl-Text-Diff perl(File/Slurp.pm) perl(Test/Compile.pm)

%description
Mail::Mbox::MessageParser is a feature-poor but very fast mbox parser.
It uses the best of three strategies for parsing a mailbox: either using
cached folder information, GNU grep, or highly optimized Perl.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%dir %perl_vendor_privlib/Mail
%dir %perl_vendor_privlib/Mail/Mbox
%perl_vendor_privlib/Mail/Mbox/MessageParser.pm
%dir %perl_vendor_privlib/Mail/Mbox/MessageParser
%perl_vendor_privlib/Mail/Mbox/MessageParser/*.pm

%changelog
* Thu Sep 23 2021 Igor Vlasenko <viy@altlinux.org> 1.5111-alt2
- fixed build

* Thu Jul 12 2018 Igor Vlasenko <viy@altlinux.ru> 1.5111-alt1
- automated CPAN update

* Sun Jul 08 2018 Igor Vlasenko <viy@altlinux.ru> 1.5108-alt1
- automated CPAN update

* Mon Jul 02 2018 Igor Vlasenko <viy@altlinux.ru> 1.5106-alt1
- automated CPAN update

* Wed Oct 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.5105-alt1
- new version
- rediffed changes to Mail-Mbox-MessageParser-1.5105-alt.patch
- uploaded as srpm (due to broken design of gear repository)

* Tue Nov 16 2010 Dmitry V. Levin <ldv@altlinux.org> 1.5002-alt1
- Updated to 1.5002.
- Applied fix for CPAN#58053, fixes grepmail with perl 5.12.
- Build with bundled perl-Module-Install, system one is too old.

* Tue Feb 27 2007 Alexey Tourbin <at@altlinux.ru> 1.5000-alt1
- 1.4005 -> 1.5000
- imported into git and adapted for gear
- removed Module::Install bundled stuff
- changed Makefile.PL to avoid extra build dependencies

* Sat Aug 26 2006 Alexey Tourbin <at@altlinux.ru> 1.4005-alt1
- 1.4004 -> 1.4005

* Thu Aug 10 2006 Alexey Tourbin <at@altlinux.ru> 1.4004-alt1
- 1.30 -> 1.4004

* Tue May 03 2005 Alexey Tourbin <at@altlinux.ru> 1.30-alt1
- 1.20 -> 1.3000
- use system modules for building (remove some modules under inc/)
- manual pages not packaged (use perldoc)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.20-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Aug 09 2004 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.14 -> 1.20

* Tue May 18 2004 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- initial revision (required by recent grepmail)
- License: GPL
