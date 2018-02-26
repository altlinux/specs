%define dist libwww-perl
Name: perl-libwww
Version: 6.04
Release: alt1

Summary: WWW client/server library for Perl (aka LWP)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Patch: libwww-perl-6.03-alt-ftp-req.patch

BuildArch: noarch

Provides: %name-perl = %version
Obsoletes: %name-perl < %version

# requires Authen::NTLM; not required by any package
%add_findreq_skiplist */LWP/Authen/Ntlm.pm
# requires HTTP::GHTTP; not required by any package
%add_findreq_skiplist */LWP/Protocol/GHTTP.pm

# disable HTML::Format dependencies in lwp-request
%filter_from_requires /^perl.HTML.Format/d

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-Encode-Locale perl-File-Listing perl-HTTP-Cookies perl-HTTP-Daemon perl-HTTP-Negotiate perl-Net-HTTP perl-WWW-RobotRules perl-devel perl-podlators

%description
The libwww-perl collection is a set of Perl modules which provides a
simple and consistent application programming interface to the
World-Wide Web.  The main focus of the library is to provide classes
and functions that allow you to write WWW clients.  The library also
contain modules that are of more general use and even classes that
help you implement simple HTTP servers.

%prep
%setup -q -n %dist-%version
%patch -p1
bzip2 -k Changes

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

ln -snf lwp-request %buildroot%_bindir/GET
ln -snf lwp-request %buildroot%_bindir/HEAD
ln -snf lwp-request %buildroot%_bindir/POST

ln -snf lwp-request.1 %buildroot%_man1dir/GET.1
ln -snf lwp-request.1 %buildroot%_man1dir/HEAD.1
ln -snf lwp-request.1 %buildroot%_man1dir/POST.1

%files
%doc	Changes.bz2 README README.SSL
	%_bindir/lwp-*
	%_bindir/GET
	%_bindir/HEAD
	%_bindir/POST
	%_man1dir/lwp-*.*
	%_man1dir/GET.*
	%_man1dir/HEAD.*
	%_man1dir/POST.*
%dir	%perl_vendor_privlib/LWP
	%perl_vendor_privlib/LWP.pm
	%perl_vendor_privlib/LWP/*
%doc	%perl_vendor_privlib/lwp*.pod

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.04-alt1
- 6.03 -> 6.04

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.02 -> 6.03

* Mon Apr 04 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- 6.01 -> 6.02
- HTTPS support unbundled into separate CPAN distribution
- no dependency on perl-LWP-Protocol-https, install explicitly

* Tue Mar 22 2011 Alexey Tourbin <at@altlinux.ru> 6.01-alt1
- 5.837 -> 6.01
- packaged as separate CPAN distributions: File-Listing, HTML-Form,
  HTTP-Cookies, HTTP-Daemon, HTTP-Date, HTTP-Message, HTTP-Negotiate,
  Net-HTTP, and WWW-RobotRules
- default SSL base class changed from from Net::SSL to IO::Socket::SSL

* Wed Jan 19 2011 Alexey Tourbin <at@altlinux.ru> 5.837-alt1
- 5.833 -> 5.837
- disabled dependency on AnyDBM_File

* Mon Nov 29 2010 Igor Vlasenko <viy@altlinux.ru> 5.833-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Oct 23 2009 Alexey Tourbin <at@altlinux.ru> 5.833-alt1
- 5.831 -> 5.833

* Wed Sep 16 2009 Alexey Tourbin <at@altlinux.ru> 5.831-alt1
- 5.830 -> 5.831

* Tue Jul 28 2009 Alexey Tourbin <at@altlinux.ru> 5.830-alt1
- 5.829 -> 5.830

* Fri Jul 10 2009 Alexey Tourbin <at@altlinux.ru> 5.829-alt1
- 5.826 -> 5.829
- depends on Encode
- packaged /usr/bin/lwp-dump

* Tue Apr 28 2009 Alexey Tourbin <at@altlinux.ru> 5.826-alt1
- 5.824 -> 5.826

* Sat Feb 14 2009 Alexey Tourbin <at@altlinux.ru> 5.824-alt1
- 5.821 -> 5.824

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 5.821-alt2
- backported bugfixes from 5.822

* Tue Nov 25 2008 Alexey Tourbin <at@altlinux.ru> 5.821-alt1
- 5.820 -> 5.821

* Thu Nov 06 2008 Alexey Tourbin <at@altlinux.ru> 5.820-alt1
- 5.817 -> 5.820
- HTTP/Headers.pm (clone) now requires Storable.pm

* Sat Oct 11 2008 Alexey Tourbin <at@altlinux.ru> 5.817-alt1
- 5.815 -> 5.817

* Thu Sep 25 2008 Alexey Tourbin <at@altlinux.ru> 5.815-alt1
- 5.814 -> 5.815

* Sat Aug 09 2008 Alexey Tourbin <at@altlinux.ru> 5.814-alt1
- 5.813 -> 5.814

* Thu Jun 19 2008 Alexey Tourbin <at@altlinux.ru> 5.813-alt1
- 5.812 -> 5.813

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 5.812-alt1
- 5.810 -> 5.812

* Sat Apr 12 2008 Alexey Tourbin <at@altlinux.ru> 5.810-alt1
- 5.808 -> 5.810

* Tue Aug 07 2007 Alexey Tourbin <at@altlinux.ru> 5.808-alt1
- 5.805 -> 5.808

* Sun Apr 08 2007 Alexey Tourbin <at@altlinux.ru> 5.805-alt3
- LWP/Protocol/nntp.pm (request): do not clobber $_ (rt.cpan.org #25132)
- lwp-request (POST): relaxed content-type check (#6792, cpan #26151)

* Sun Jan 14 2007 Alexey Tourbin <at@altlinux.ru> 5.805-alt2
- imported sources into git and adapted for gear
- lwp-request: relaxed dependencies on perl-HTML-Format
- lwp-request: debian patch for -b option (deb #294595)

* Mon May 22 2006 Alexey Tourbin <at@altlinux.ru> 5.805-alt1
- 5.803 -> 5.805
- restored manual pages for GET, HEAD, etc.

* Wed Jun 22 2005 Alexey Tourbin <at@altlinux.ru> 5.803-alt3
- fixed alt-deps-ftp.patch (breakage reported by Ivan Adzhubey)

* Fri Apr 15 2005 Alexey Tourbin <at@altlinux.ru> 5.803-alt2
- patched to clarify dependencies on Compress::Zlib, Net::FTP, and Net::SSL

* Wed Dec 22 2004 Alexey Tourbin <at@altlinux.ru> 5.803-alt1
- 5.79 -> 5.803
- renamed: %name-perl -> %name
- manual pages not packaged (use perldoc)

* Thu Apr 15 2004 Alexey Tourbin <at@altlinux.ru> 5.79-alt1
- 5.76 -> 5.79

* Sat Dec 06 2003 Alexey Tourbin <at@altlinux.ru> 5.76-alt1
- 5.76

* Thu Nov 13 2003 Alexey Tourbin <at@altlinux.ru> 5.75-alt1
- 5.75
- mdk-empty_header.patch merged upstream, alt-syntax.patch needed no more
- alt-makefile.patch updated (not to read media.types of already installed
  package when running tests)

* Fri Oct 17 2003 Alexey Tourbin <at@altlinux.ru> 5.72-alt1
- 5.72
- syntax.patch: fix syntax error
- makefile.patch:
  + don't run "live" tests
  + don't look for the existing installation

* Sat Apr 26 2003 Alexey Tourbin <at@altlinux.ru> 5.69-alt2
- skip dependencies in:
  + LWP/Authen/Ntlm.pm (requires Authen/Ntlm.pm)
  + HTTP/Cookies/Microsoft.pm (requires Win32.pm)
  + LWP/Protocol/GHTTP.pm
- specfile cleanup

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 5.69-alt1
- 5.69

* Tue Oct 29 2002 Alexey Tourbin <at@altlinux.ru> 5.65-alt2
- rebuilt for perl-5.8 with new rpm macros

* Thu Jun 13 2002 Stanislav Ievlev <inger@altlinux.ru> 5.65-alt1
- 5.65

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 5.64-alt1
- 5.64

* Thu Dec 20 2001 Stanislav Ievlev <inger@altlinux.ru> 5.63-alt1
- 5.63

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 5.53-alt1
- 5.53

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 5.50-ipl2mdk
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Mon Jan 29 2001 Mikhail Zabaluev <zabaluev@parascript.com> 5.50-ipl1mdk
- Updated:
  + version 5.50
- Changed:
  + spec file adapted for Sisyphus
- Fixed:
  + perl path in LWP/Debug.pm

* Wed Jun 28 2000 Mikhail Zabaluev <mookid@sigent.ru> 5.48-1mdk_mhz
- changed file list and installation
- added description from README
- force build architecture to noarch

* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 5.47-3mdk
- fixed release tag

* Fri Mar 31 2000 Pixel <pixel@mandrakesoft.com> 5.47-2mdk
- remove file list
- rebuild for 5.6.0

* Mon Jan  3 2000 Jean-Michel Dault <jmdault@netrevolution.com>
- final cleanup for Mandrake 7

* Thu Dec 30 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- updated to 5.47

* Sun Aug 29 1999 Jean-Michel Dault <jmdault@netrevolution.com>
- bzip2'd sources
- updated to 5.44

* Tue May 11 1999 root <root@alien.devel.redhat.com>
- Spec file was autogenerated.
