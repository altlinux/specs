%define dist Devel-Leak
Name: perl-%dist
Version: 0.03
Release: alt2.3

Summary: Utility for looking for perl objects that are not reclaimed
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Thu Oct 06 2011
BuildRequires: perl-devel

%description
Devel::Leak is a utility for looking for Perl objects that are not
reclaimed.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_archlib/Devel*
%perl_vendor_autolib/Devel*

%changelog
* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 0.03-alt2.3
- rebuilt for perl-5.14

* Tue Sep 21 2010 Alexey Tourbin <at@altlinux.ru> 0.03-alt2.2
- rebuilt for perl-5.12

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 0.03-alt2.1
- rebuilt for perl-5.12

* Thu Oct 26 2006 Alexey Tourbin <at@altlinux.ru> 0.03-alt2
- imported sources into git and built with gear
- fixed SEGV when re-using $handle several times (cpan #19067);
  explicitly reset the handle so it is not reused by mistake

* Sat Apr 02 2005 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- initial revision (for finding leaks in perl-RPM)
