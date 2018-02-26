Name: perl-Fuse
Version: 0.14
Release: alt1

Summary: Write filesystems in Perl using FUSE
License: GPLv2, LGPLv2.1
Group: Development/Perl

URL: http://search.cpan.org/dist/Fuse/
Source: Fuse-%version.tar.gz

# Automatically added by buildreq on Tue Oct 18 2011
BuildRequires: libfuse-devel perl-Filesys-Statvfs perl-Lchown perl-Unix-Mknod perl-devel

%description
Fuse is combination of Linux kernel module and user space library which
enables you to write user-space filesystems. This module enables you to
write filesystems using perl.

%prep
%setup -q -n Fuse-%version

# XXX does it even work?
%def_without test

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc AUTHORS Changes README 
%perl_vendor_archlib/Fuse*
%perl_vendor_autolib/Fuse

%changelog
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
