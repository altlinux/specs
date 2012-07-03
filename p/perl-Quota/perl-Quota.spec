%define dist Quota
Name: perl-%dist
Version: 1.6.6
Release: alt1

Summary: Perl interface to file system quotas
License: GPL or Artistic
Group: Development/Perl

URl: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
The Quota module provides access to file system quotas.
The quotactl system call or ioctl is used to query or set quotas
on the local host, or queries are submitted via RPC to a remote host.
Mount tables can be parsed with getmntent and paths can be
translated to device files (or whatever the actual quotactl
implementations needs as argument) of the according file system.

%prep
%setup -q -n %dist-%version

# fixup for Linux 3.x
sed -i- 's/Linux 2/Linux/' Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README contrib
%perl_vendor_archlib/Quota*
%perl_vendor_autolib/Quota

%changelog
* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 1.6.6-alt1
- 1.6.4 -> 1.6.6
- built for perl-5.14
- fixed building for Linux 3.x

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.6.4-alt3.1
- rebuilt with perl 5.12

* Fri Mar 05 2010 Mikhail Pokidko <pma@altlinux.org> 1.6.4-alt3
- Adding man page

* Fri Mar 05 2010 Mikhail Pokidko <pma@altlinux.org> 1.6.4-alt2
- autosplit.ix placement fix. #23081

* Thu Mar 04 2010 Mikhail Pokidko <pma@altlinux.org> 1.6.4-alt1
- 1.6.4. Closed: #23069

* Fri Sep 05 2008 Mikhail Pokidko <pma@altlinux.org> 1.5.1-alt2
- sisyphus_check fixes

* Wed Nov 15 2006 Mikhail Pokidko <pma@altlinux.ru> 1.5.1-alt1
- first build for ALT Linux Sisyphus
