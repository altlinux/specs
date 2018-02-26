Name: perl-App-cpanminus
Version: 1.5013
Release: alt1

Summary: App::cpanminus - get, unpack, build and install modules from CPAN
Group: Development/Perl
License: Perl
Url: %CPAN App-cpanminus

# git://github.com/miyagawa/cpanminus.git
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-Module-Build perl-podlators

Requires: perl-base
%add_findreq_skiplist *usr/bin/cpanm

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/cpanm
%_man1dir/cpanm.1*
%doc Changes README 

%changelog
* Thu May 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5013-alt1
- 1.5010 -> 1.5013

* Mon Apr 09 2012 Vladimir Lettiev <crux@altlinux.ru> 1.5010-alt1
- New version 1.5010
- Source cloned from upstream git
- Don't pack App::cpanminus module

* Fri Dec 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.5006-alt1
- New version 1.5006

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.4008-alt1
- automated CPAN update

* Sat Mar 05 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3001-alt1
- New version 1.3001

* Thu Mar 03 2011 Vladimir Lettiev <crux@altlinux.ru> 1.3000-alt1
- New version 1.3000

* Sun Feb 06 2011 Vladimir Lettiev <crux@altlinux.ru> 1.1008-alt1
- New version 1.1008

* Mon Jan 10 2011 Vladimir Lettiev <crux@altlinux.ru> 1.1006-alt1
- New version 1.1006

* Fri Dec 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1004-alt1
- New version 1.1004

* Wed Nov 17 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1002-alt1
- New version 1.1002
- Fixed generation of man1 pages

* Sun Sep 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0015-alt1
- New version 1.0015

* Sun Sep 19 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0013-alt1
- New version 1.0013

* Sun Sep 12 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0012-alt1
- New version 1.0012
- Added manpage cpanm

* Mon Aug 02 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0010-alt1
- New version 1.0010

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 1.0006-alt1
- automated CPAN update

* Thu Jun 03 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0004-alt1
- New version 1.0004

* Mon Apr 26 2010 Vladimir Lettiev <crux@altlinux.ru> 1.0001-alt1
- New version 1.0001

* Thu Apr 15 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9935-alt1
- New version 0.9935

* Tue Apr 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.9932-alt1
- initial build
