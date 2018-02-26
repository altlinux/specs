%define dist CGI-SpeedyCGI
Name: perl-%dist
Version: 2.22
Release: alt2.2

Summary: Speed up perl scripts by running them persistently
License: GPL
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
