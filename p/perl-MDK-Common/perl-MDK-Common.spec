Name: perl-MDK-Common
Version: 1.1.23
Release: alt1.1

Summary: Various simple Perl functions
License: GPL
Group: Development/Perl

URL: http://cvs.mandrakesoft.com/cgi-bin/cvsweb.cgi/soft/perl-MDK-Common/
Source: %name-%version.tar.bz2

BuildArch: noarch

# Added by buildreq2 on Fri Apr 29 2005
BuildRequires: perl-devel

%description
Various simple perl functions created for DrakX.

%prep
%setup -q -n %name
%__mv MDK/Common.pm.pl MDK/Common.pm.in

%build
%__perl MDK/Common.pm.in >MDK/Common.pm
touch -r MDK/Common.pm.in MDK/Common.pm

cd MDK
echo 'use ExtUtils::MakeMaker; WriteMakefile NAME => "MDK::Common";' >Makefile.PL
%perl_vendor_build

%install
cd MDK
%perl_vendor_install

%files
%dir %perl_vendor_privlib/MDK
%perl_vendor_privlib/MDK/Common.pm
%dir %perl_vendor_privlib/MDK/Common
%perl_vendor_privlib/MDK/Common/*.pm

%changelog
* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1.23-alt1.1
- rebuilt with perl 5.12

* Mon May 30 2005 Alexey Tourbin <at@altlinux.ru> 1.1.23-alt1
- 1.1.22 -> 1.1.23

* Fri Apr 29 2005 Alexey Tourbin <at@altlinux.ru> 1.1.22-alt1
- 1.0.3 -> 1.1.22
- %name-devel not packaged so far

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.3-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 1.0.3-alt2
- in sync with 1.0.3-16mdk
- buildreq applied (fixes build in the hasher)

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 1.0.3-alt1
- rebuild with new perl
- update (only bugfixes in this release)

* Sun Nov 18 2001 Dmitry V. Levin <ldv@alt-linux.org> 1.0.2-alt2
- Specfile cleanup.
- Fixed buildarch.

* Wed Nov 08 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.2-alt1
- First build for Sisyphus

* Mon Sep 17 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-7mdk
- (cp_af): fix typo

* Sun Sep 16 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-6mdk
- add output_p, cp_af, rm_rf

* Sun Sep 16 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-5mdk
- add mkdir_p

* Mon Sep 10 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-4mdk
- DataStructure::uniq : keep the order
- String::warp_text : fixed

* Thu Sep  6 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-3mdk
- substInFile works on empty files

* Mon Aug 27 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-2mdk
- create perl-MDK-Common-devel
- fix warp_text

* Thu Aug  9 2001 Pixel <pixel@mandrakesoft.com> 1.0.2-1mdk
- each_index added
- a few more checks in perl_checker

* Sat Aug  4 2001 Pixel <pixel@mandrakesoft.com> 1.0.1-1mdk
- add some arch() stuff

* Fri Aug  3 2001 Pixel <pixel@mandrakesoft.com> 1.0-1mdk
- doc finished
- index.html added (nicer than perldoc)

* Fri Aug  3 2001 Pixel <pixel@mandrakesoft.com> 1.0-0.3mdk
- much doc added

* Wed Jul 25 2001 Pixel <pixel@mandrakesoft.com> 1.0-0.2mdk
- another pre-release: some doc added, some fixes

* Tue Jul 24 2001 Pixel <pixel@mandrakesoft.com> 1.0-0.1mdk
- first version
