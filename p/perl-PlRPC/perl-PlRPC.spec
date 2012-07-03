%define dist PlRPC
Name: perl-%dist
Version: 0.2020
Release: alt2

Summary: Perl RPC (Remote Procedure Call)
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Oct 04 2011
BuildRequires: perl-Crypt-DES perl-IO-Compress perl-Net-Daemon perl-devel

%description
PlRPC (Perl RPC) is a package for implementing servers and clients
that are written in Perl entirely. The name is borrowed from Sun's
RPC (Remote Procedure Call), but it could as well be RMI like Java's
"Remote Method Interface), because PlRPC gives you the complete power
of Perl's OO framework in a very simple manner.

%prep
%setup -q -n %dist

# disable README update
sed -i- '/^sub postamble/s/post/no_post/' Makefile.PL

%build
%if "%(logger -d -u /dev/log -p user.debug test &>/dev/null || echo no)" == "no"
%def_without test
%endif
%perl_vendor_build

%install
%perl_vendor_install

rm %buildroot%perl_vendor_privlib/Bundle/PlRPC.pm

%files
%doc ChangeLog README
%perl_vendor_privlib/RPC

%changelog
* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 0.2020-alt2
- rebuilt

* Sat Mar 01 2008 Alexey Tourbin <at@altlinux.ru> 0.2020-alt1
- 0.2018 -> 0.2020

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.2018-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Jul 30 2004 Alexey Tourbin <at@altlinux.ru> 0.2018-alt1
- 0.2017 -> 0.2018
- updated description

* Wed Oct 08 2003 Stanislav Ievlev <inger@altlinux.ru> 0.2017-alt1.1
- fix building in hasher

* Thu Jun 26 2003 Stanislav Ievlev <inger@altlinux.ru> 0.2017-alt1
- 0.2017

* Fri Nov 01 2002 Stanislav Ievlev <inger@altlinux.ru> 0.2016-alt1
- Inital build for ALT.
