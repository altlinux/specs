Name: perl-Net-SSH2
Version: 0.66
Release: alt1.1

Summary: Support for the SSH 2 protocol via libssh2
License: Perl
Group: Development/Perl

URL: http://search.cpan.org/dist/Net-SSH2/
Source: Net-SSH2-%version.tar
Patch: %name-%version-%release.patch

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: libssh2-devel libssl-devel perl-Module-Install-CheckLib zlib-devel

%description
Net::SSH2 is a perl interface to the libssh2 (http://www.libssh2.org)
library.  It supports the SSH2 protocol (there is no support for SSH1)
with all of the key exchanges, ciphers, and compression of libssh2.

%prep
%setup -q -n Net-SSH2-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README example
%perl_vendor_archlib/Net
%perl_vendor_autolib/Net

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1.1
- rebuild with new perl 5.26.1

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 0.66-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1.1
- rebuild with new perl 5.24.1

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.62-alt1
- automated CPAN update

* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.61-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.60-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.58-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1.1
- rebuild with new perl 5.22.0

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.56-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1.1
- rebuild with new perl 5.20.1

* Sun Jun 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.52-alt1
- 0.45 -> 0.52
- fixed build on x86

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.45-alt2
- rebuilt for perl-5.16

* Sun Aug 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.45-alt1
- New version 0.45 (support for ssh-agent, fix memory leak in password auth)

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 0.39-alt2
- rebilt for perl-5.14

* Tue Aug 23 2011 Vladimir Lettiev <crux@altlinux.ru> 0.39-alt1
- initial build
