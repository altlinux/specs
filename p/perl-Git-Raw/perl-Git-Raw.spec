Name: perl-Git-Raw
Version: 0.40.1
Release: alt2

Summary: Perl bindings to the Git linkable library (libgit2)
Group: Development/Perl
License: perl

Url: %CPAN Git-Raw
Source: %name-%version.tar
Patch: %name-%version-%release.patch
Patch1: perl-Git-Raw-0.40.1-quickfix.patch

BuildRequires: libssh2-devel libssl-devel zlib-devel libgit2-devel perl-Capture-Tiny perl-devel perl-File-Slurp perl-Devel-CheckLib

%description
%summary

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_autolib/Git/Raw*
%perl_vendor_archlib/Git/Raw*
%doc Changes TODO

%changelog
* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.40.1-alt2
- quick fix; we need to rebuild it with perl 5.20.1

* Tue Jul 01 2014 Vladimir Lettiev <crux@altlinux.ru> 0.40.1-alt1
- upstream snapshot e660a31c

* Sun Mar 30 2014 Vladimir Lettiev <crux@altlinux.ru> 0.29-alt1
- 0.29

* Mon Sep 02 2013 Vladimir Lettiev <crux@altlinux.ru> 0.24-alt2
- built for perl 5.18

* Tue Jul 23 2013 Alexey Shabalin <shaba@altlinux.ru> 0.24-alt1.git.5224e
- upstream snapshot 5224e5487c7e19f55ac2c0d50ccb6425715ed8f8

* Sun Oct 21 2012 Vladimir Lettiev <crux@altlinux.ru> 0.14-alt1
- 0.13 -> 0.14

* Wed Oct 10 2012 Buildbot <buildbot@altlinux.org> 0.13-alt1
- initial build for ALTLinux

