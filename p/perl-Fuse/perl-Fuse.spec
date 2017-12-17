%define _unpackaged_files_terminate_build 1
Name: perl-Fuse
Version: 0.16
Release: alt1.1

Summary: Write filesystems in Perl using FUSE
License: GPLv2, LGPLv2.1
Group: Development/Perl

URL: http://search.cpan.org/dist/Fuse/
Source0: http://www.cpan.org/authors/id/D/DP/DPATES/Fuse-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: libfuse-devel perl-Filesys-Statvfs perl-Lchown perl-Unix-Mknod perl-devel

%description
Fuse is combination of Linux kernel module and user space library which
enables you to write user-space filesystems. This module enables you to
write filesystems using perl.

%prep
%setup -q -n Fuse-%{version}

# XXX does it even work?
%def_without test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS Changes README examples
%perl_vendor_archlib/Fuse*
%perl_vendor_autolib/Fuse

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1.1
- rebuild with new perl 5.26.1

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.15-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt2
- rebuilt for perl-5.16

* Tue Oct 18 2011 Alexey Tourbin <at@altlinux.ru> 0.14-alt1
- 0.13 -> 0.14
- built for perl-5.14

* Tue Jul 19 2011 Vladimir Lettiev <crux@altlinux.ru> 0.13-alt1
- new version 0.13
- spec cleanup
- fixed linking
- disabled tests

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.09_3-alt1.1
- rebuilt with perl 5.12

* Wed Dec 02 2009 Ilya Shpigor <elly@altlinux.org> 0.09_3-alt1
- initial build for ALT Linux Sisyphus
