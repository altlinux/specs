%define _unpackaged_files_terminate_build 1
%define dist IO-Socket-SSL
Name: perl-%dist
Version: 2.054
Release: alt1

Summary: SSL socket interface class
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/S/SU/SULLR/%{dist}-%{version}.tar.gz
Patch: IO-Socket-SSL-2.020-alt-deps.patch

BuildArch: noarch

BuildRequires: perl-Encode perl-IO-Socket-IP perl-Net-IDN-Encode perl-Net-SSLeay perl-devel perl-unicore

%description
IO::Socket::SSL is a class implementing an object oriented
interface to SSL sockets. The class is a descendent of
IO::Socket::INET and provides a subset of the base class's
interface methods.

%prep
%setup -q -n %{dist}-%{version}
#%patch -p0
# needs internet connection
rm t/external/*.t
# needs network (share_network=1)
rm -f t/auto_verify_hostname.t t/cert_no_file.t t/acceptSSL-timeout.t t/core.t
# some tests hang for a long time w/o network
rm t/[d-z]*t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc BUGS Changes README README.Win32 docs example
%perl_vendor_privlib/IO

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 2.054-alt1
- automated CPAN update

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 2.052-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 2.051-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 2.050-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.049-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 2.048-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 2.047-alt1
- automated CPAN update

* Tue Feb 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.045-alt1
- automated CPAN update

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 2.043-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.040-alt1
- automated CPAN update

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 2.039-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.038-alt1
- automated CPAN update

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.033-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.029-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 2.027-alt1
- automated CPAN update

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 2.025-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 2.024-alt1
- automated CPAN update

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.022-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.021-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 2.020-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.012-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 2.011-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.010-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.008-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 2.007-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.998-alt1
- automated CPAN update

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.997-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.994-alt1
- automated CPAN update

* Sat Mar 29 2014 Igor Vlasenko <viy@altlinux.ru> 1.973-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 1.972-alt1
- automated CPAN update

* Mon Mar 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.969-alt1
- automated CPAN update

* Sat Mar 15 2014 Igor Vlasenko <viy@altlinux.ru> 1.968-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 1.967-alt1
- automated CPAN update

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.963-alt1
- automated CPAN update

* Thu Nov 28 2013 Igor Vlasenko <viy@altlinux.ru> 1.962-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.960-alt1
- automated CPAN update

* Sat Oct 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.955-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.954-alt1
- automated CPAN update

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.953-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.77-alt1
- automated CPAN update

* Tue Sep 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.76-alt1
- 1.49 -> 1.76
- use perl-IO-Socket-IP instead of IO::Socket::INET6
- updated alt-deps patch

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 1.49-alt1
- 1.44 -> 1.49
- enabled dependency on Net::IDN::Encode

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.44-alt1
- automated CPAN update

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 1.39-alt1
- 1.37 -> 1.39

* Fri Dec 24 2010 Alexey Tourbin <at@altlinux.ru> 1.37-alt1
- 1.33 -> 1.37

* Thu Apr 08 2010 Alexey Tourbin <at@altlinux.ru> 1.33-alt1
- 1.31 -> 1.33

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 1.31-alt1
- 1.26 -> 1.31

* Fri Jul 17 2009 Alexey Tourbin <at@altlinux.ru> 1.26-alt1
- 1.24 -> 1.26

* Wed Apr 22 2009 Alexey Tourbin <at@altlinux.ru> 1.24-alt1
- 1.16 -> 1.24
- enabled IPv6 support by default

* Wed Sep 24 2008 Alexey Tourbin <at@altlinux.ru> 1.16-alt1
- 1.15 -> 1.16

* Thu Sep 11 2008 Alexey Tourbin <at@altlinux.ru> 1.15-alt1
- 1.14 -> 1.15

* Tue Aug 05 2008 Alexey Tourbin <at@altlinux.ru> 1.14-alt1
- 1.13_5 -> 1.14

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.13_5-alt1
- 1.13_4 -> 1.13_5

* Sun Mar 09 2008 Alexey Tourbin <at@altlinux.ru> 1.13_4-alt1
- 0.95 -> 1.13_4
- SSL.pm (import): fixed inet4/inet6 setup (rt.cpan.org #33921)

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.95-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Oct 20 2003 Grigory Milev <week@altlinux.ru> 0.95-alt1
- new version released

* Thu Jun 26 2003 Grigory Milev <week@altlinux.ru> 0.93-alt1
- new version released
- spec fixed due new macros

* Tue May 28 2002 Grigory Milev <week@altlinux.ru> 0.81-alt1
- new version released

* Mon Sep 03 2001 Grigory Milev <week@altlinux.ru> 0.80-alt1
- New version released.

* Tue Jul 31 2001 Grigory Milev <week@altlinux.ru> 0.79-alt1
- First build for Sisyphus

