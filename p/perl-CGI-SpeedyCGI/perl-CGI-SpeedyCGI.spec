%def_with test
%define dist CGI-SpeedyCGI
Name: perl-%dist
Version: 2.22
Release: alt7

Summary: Speed up perl scripts by running them persistently
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Patches from Fedora
Patch0:		perl-CGI-SpeedyCGI-2.22-documentation.patch
Patch1:		perl-CGI-SpeedyCGI-2.22-empty_param.patch
Patch2:		perl-CGI-SpeedyCGI-2.22-strerror.patch
Patch3:		perl-CGI-SpeedyCGI-2.22-brigade_foreach.patch
Patch4:		perl-CGI-SpeedyCGI-2.22-exit_messages.patch
Patch5:		perl-CGI-SpeedyCGI-2.22-perl_510.patch
Patch6:		perl-CGI-SpeedyCGI-2.22-c99_inline.patch
Patch7:         CGI-SpeedyCGI-2.22-Fix-building-on-Perl-without-dot-in-INC.patch
# Patches from Debian
Patch10: 10big-socket-buffers.patch
Patch20: 20makefile-manpage.patch    
Patch30: 30empty-param.patch 
Patch40: 40strerror.patch
Patch50: 50log-exit-messages-on-die.patch
Patch60: 60apache-docs.patch        
Patch70: 70apache2.2.patch       
Patch80: 80strip-backend-libs.patch
Patch85: 85test-timeout.patch
Patch90: 90speedy_unsafe_putenv.patch
Patch95: 95perl5.10.patch
Patch96: 96perl_sys_init.patch
Patch97: 97uninit-crash.patch

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: perl-CGI perl-devel perl-threads

%description
SpeedyCGI is a way to run perl scripts persistently, which usually makes
them run much more quickly because it avoids the overhead of starting
up a new perl interpreter and compiling the perl code.  It is most
often used for CGI scripts but it can be used to speed up most perl
programs.

%prep
%setup -q -n %dist-%version
%if 0
%patch10 -p1
%patch20 -p1
%patch30 -p1
%patch40 -p1
%patch50 -p1
%patch60 -p1
%patch70 -p1
%patch80 -p1
%patch85 -p1
%patch90 -p1
%patch95 -p1
%patch96 -p1
%patch97 -p1
%endif
%patch0 -p1 -b .documentation
%patch1 -p1 -b .empty_param
%patch2 -p1 -b .strerror
%patch3 -p1 -b .brigade_foreach
%patch4 -p1 -b .exit_messages
%patch5 -p1 -b .perl_510
%patch6 -p1 -b .c99_inline
%patch7 -p1 -b .inc

# unfortunately. let's wait for a patch
[ %version = 2.22 ] && 	rm speedy/t/be_memleak.t

%build
# Hackaround for SMP build
NPROCS=1
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README* docs
%_bindir/speedy*
%perl_vendor_privlib/CGI

%changelog
* Thu Dec 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.22-alt7
- fixes for perl 5.26

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 2.22-alt6
- perl 5.24 fixes

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.22-alt5.1.1.1
- rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.22-alt5.1.1
- hack; disabled patches for rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt5.1
- rebuild with new perl 5.22.0

* Wed Nov 18 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt5
- updated patches from fedora

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.22-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.22-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 2.22-alt3
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 2.22-alt2.2
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 2.22-alt2.1
- rebuilt with perl 5.12
- applied patches from Debian

* Thu Sep 01 2005 Igor Vlasenko <viy@altlinux.ru> 2.22-alt2
- spec cleanup

* Thu Dec 09 2004 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- new version 2.22

* Fri Apr 11 2003 Sir Raorn <raorn@altlinux.ru> 2.21-alt1
- Built for Sisyphus
