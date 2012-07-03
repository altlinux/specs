%define dist CPAN
Name: perl-%dist
Version: 1.9800
Release: alt1

Summary: Download and build Perl modules from CPAN sites
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# avoid extra dependencies
%filter_from_requires /^perl.CPAN.Meta/d
%filter_from_requires /^perl.CPAN.SQLite/d
%filter_from_requires /^perl.Devel.Size/d

# Automatically added by buildreq on Thu Nov 10 2011
BuildRequires: gnupg perl-Archive-Tar perl-Archive-Zip perl-CPAN-Checksums perl-Expect perl-File-HomeDir perl-HTTP-Tiny perl-IO-Stty perl-Module-Build perl-Module-CoreList perl-Module-Pluggable perl-Module-Signature perl-Net-Ping perl-Parse-CPAN-Meta perl-Sort-Versions perl-Term-ReadKey perl-Test-Perl-Critic perl-Test-Pod perl-Test-Pod-Coverage perl-Text-Diff perl-Text-Glob perl-YAML perl-YAML-Syck perl-libwww

%description
The CPAN (Comprehensive Perl Archive Network) module is designed
to automate the make and install of perl modules and extensions.
It includes some searching capabilities and knows how to fetch
the raw data from the net.

%prep
%setup -q -n %dist-%version
rm -rv inc/

# XXX tests fail
rm t/30shell.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
	%_bindir/cpan
#dir	/etc/perl5/CPAN
#config(noreplace) %ghost /etc/perl5/CPAN/Config.pm
	%perl_vendor_privlib/App
	%perl_vendor_privlib/CPAN*

%changelog
* Thu Nov 10 2011 Alexey Tourbin <at@altlinux.ru> 1.9800-alt1
- 1.9301 -> 1.9800

* Sat Dec 20 2008 Alexey Tourbin <at@altlinux.ru> 1.93.01-alt1
- restored /etc/perl5/CPAN/Config.pm

* Sat Dec 20 2008 Alexey Tourbin <at@altlinux.ru> 1.93.01-alt0
- 1.92_58 -> 1.9301

* Wed Mar 12 2008 Alexey Tourbin <at@altlinux.ru> 1.92_58-alt0
- 1.76 -> 1.92_58

* Wed Dec 15 2004 Alexey Tourbin <at@altlinux.ru> 1.76-alt2
- rebuild in new environment
- build against system Test::More (removed BUNDLE/Test)
- manual pages not packaged (use perldoc)

* Sun Aug 03 2003 Alexey Tourbin <at@altlinux.ru> 1.76-alt1
- 1.76

* Sat Jul 05 2003 Alexey Tourbin <at@altlinux.ru> 1.71-alt1
- 1.71
- fixed triggerpostun script

* Sat Jun 14 2003 Alexey Tourbin <at@altlinux.ru> 1.70-alt2
- CPAN/Config.pm will now be created in /etc/perl5
- triggerpostun added to move old configuration file on upgrade

* Fri Mar 14 2003 Alexey Tourbin <at@altlinux.ru> 1.70-alt1
- 1.70
- perl(Term/ReadLine/Gnu.pm) dependency added
- README excluded (=man CPAN)

* Wed Oct 23 2002 Alexey Tourbin <at@altlinux.ru> 1.63-alt1
- initial build for %distribution
