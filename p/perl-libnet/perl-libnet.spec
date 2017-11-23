%define _unpackaged_files_terminate_build 1
%define dist libnet
Name: perl-%dist
Version: 3.11
Release: alt1
Epoch: 1

Summary: Collection of Network protocol modules for Perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SH/SHAY/%{dist}-%{version}.tar.gz
Patch: %name-3.04-alt.patch

BuildArch: noarch
Requires: /etc/perl5

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-devel

%description
libnet is a collection of Perl modules which provides a simple
and consistent programming interface (API) to the client side
of various protocols used in the internet community.

The RFC implemented in this distribution are

Net::FTP 	RFC959		File Transfer Protocol
Net::SMTP	RFC821		Simple Mail Transfer Protocol
Net::Time	RFC867		Daytime Protocol
Net::Time	RFC868		Time Protocol
Net::NNTP	RFC977		Network News Transfer Protocol
Net::POP3	RFC1939		Post Office Protocol 3
Net::SNPP	RFC1861		Simple Network Pager Protocol

%prep
%setup -q -n %{dist}-%{version}
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot/etc/perl5/Net
mv %buildroot{%perl_vendor_privlib,/etc/perl5}/Net/libnet.cfg

%files
%doc	Changes README Artistic Copying
%dir	/etc/perl5/Net
%config(noreplace) /etc/perl5/Net/libnet.cfg
%dir	%perl_vendor_privlib/Net
	%perl_vendor_privlib/Net/*.pm
%doc	%perl_vendor_privlib/Net/*.pod
%dir	%perl_vendor_privlib/Net/FTP
	%perl_vendor_privlib/Net/FTP/*.pm

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.11-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.10-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.09-alt1
- automated CPAN update

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.08-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.07-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.05-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.04-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.27-alt1
- new version 1.27

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 1:1.23-alt1
- 1.22 -> 1.23

* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 1:1.22-alt2
- rebuilt

* Thu Mar 06 2008 Alexey Tourbin <at@altlinux.ru> 1:1.22-alt1
- 1.21 -> 1.22
- Net/Config.pm: fixed /etc/perl5/Net/libnet.cfg loading

* Tue Aug 21 2007 Alexey Tourbin <at@altlinux.ru> 1:1.21-alt1
- 1.20 -> 1.21
- reviewed and updated my previous changes
- changed src.rpm packaging to keep upstream tarball intact

* Sat Apr 07 2007 Alexey Tourbin <at@altlinux.ru> 1:1.20-alt2
- applied change #30576 from perl-5.9 tree, which reverts unconditional
  utf8::encode() call in Net::Cmd (#10976, rt.cpan.org #24835)
- also applied patch from rt.cpan.org #25019, with which Net::FTP
  no longer "Removes Last Character of Each Line"

* Mon Feb 26 2007 Alexey Tourbin <at@altlinux.ru> 1:1.20-alt1
- 1.19 -> 1.20

* Sat Jun 11 2005 Alexey Tourbin <at@altlinux.ru> 1:1.19-alt3
- Net/Domain.pm: use Sys::Hostname to find out hostname (cpan #13208)
- Net/NNTP.pm: fix precedence error in article routine (deb #275142)

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1:1.19-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Thu Jul 01 2004 Alexey Tourbin <at@altlinux.ru> 1:1.19-alt1
- 1.17 -> 1.19

* Fri Sep 26 2003 Alexey Tourbin <at@altlinux.ru> 1:1.17-alt1
- 1.17

* Fri Jun 20 2003 Alexey Tourbin <at@altlinux.ru> 1:1.16-alt1
- 1.16
- don't look for any previous installation/the existing libnet.cfg
- Net/libnet.cfg moved to /etc/perl5 (requires perl-5.8.1)
- triggerun added to move old configuration file on upgrade

* Sat Apr 26 2003 Alexey Tourbin <at@altlinux.ru> 1:1.13-alt3
- ignore Authen::SASL dependency

* Fri Mar 20 2003 Alexey Tourbin <at@altlinux.ru> 1:1.13-alt2
- nointeractive.patch removed; alt-ftp-passive.patch added
- specfile cleanup; docs added

* Wed Mar 19 2003 Stanislav Ievlev <inger@altlinux.ru> 1:1.13-alt1
- 1.13

* Sat Oct 26 2002 Alexey Tourbin <at@altlinux.ru> 1:1.12-alt2
- rebuilt for perl-5.8 with new rpm macros

* Thu Jun 13 2002 Stanislav Ievlev <inger@altlinux.ru> 1.12-alt1
- 1.12

* Wed Mar 27 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0901-alt1
- 1.0901

* Mon Jun 25 2001 Stanislav Ievlev <inger@altlinux.ru> 1.0703-ipl3mdk
- Rebuilt with perl-5.6.1

* Mon Jan 29 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.0703-ipl2mdk
- Changed:
  + skipping 'make test' due to its dependancy on network environment

* Sun Jan 28 2001 Mikhail Zabaluev <zabaluev@parascript.com> 1.0703-ipl1mdk
- Changed:
  + adapted spec for Sisyphus

* Tue Jun 27 2000 Mikhail Zabaluev <mookid@sigent.ru> 1.0703-3mdk_mhz
- fixed .packlist and RPM filelist
- ExclusiveArch: noarch

* Wed May 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0703-2mdk
- Don't ask interactive questions.

* Mon Apr  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0703-1mdk
- 1.0703
- fixed group
- rebuild with new perl
- fixed location

* Tue Feb 29 2000 Jean-Michel Dault <jmdault@netrevolution.com> 1.0607-1mdk
- upgraded to 1.0607

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- rebuilt for Mandrake 7

* Sun Aug 29 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- bzip2'd sources

* Tue May 11 1999 root <root@alien.devel.redhat.com>
- Spec file was autogenerated.
