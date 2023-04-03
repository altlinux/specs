%define _unpackaged_files_terminate_build 1
#set_perl_req_method relaxed
#define _without_test 1
BuildRequires: perl-podlators
Epoch: 3
%define dist IO-AIO
Name: perl-%dist
Version: 4.8
Release: alt1.1

Summary: Asynchronous Input/Output
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/M/ML/MLEHMANN/%{dist}-%{version}.tar.gz
Patch0:		IO-AIO-4.4-shellbang.patch

# patch1&2: for perl7
Patch1:		IO-AIO-4.75-alt-add-not-defined.patch
Patch2:		IO-AIO-4.75-alt-import-add.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-common-sense perl-devel perl(Canary/Stability.pm)
# in perl-devel
BuildRequires: %{perl_libdb_pkgname}-devel libgdbm-devel

%description
This module implements asynchronous I/O using whatever means your
operating system supports.

Asynchronous means that operations that can normally block your program
(e.g. reading from disk) will be done asynchronously: the operation
will still block, but you can do something else in the meantime. This
is extremely useful for programs that need to stay interactive even
when doing heavy I/O (GUI programs, high performance network servers
etc.), but can also be used to easily do operations in parallel that are
normally done sequentially, e.g. stat'ing many files, which is much faster
on a RAID volume or over NFS when you do a number of stat operations
concurrently.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %name = %{?epoch:%epoch:}%version-%release
BuildArch: noarch

%description scripts
scripts for %name


%prep
%setup -q -n %{dist}-%{version}

# Fix shellbang in treescan (perl 5.32 syntax)
%patch0

# an attempt of perl7 support
#patch1 -p1
#patch2 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/IO
%perl_vendor_archlib/IO

%files scripts
%_bindir/*
%_man1dir/*


%changelog
* Mon Apr 03 2023 Igor Vlasenko <viy@altlinux.org> 3:4.8-alt1.1
- automated CPAN update

* Tue Sep 27 2022 Igor Vlasenko <viy@altlinux.org> 2:4.79-alt1
- automated CPAN update

* Wed Sep 07 2022 Igor Vlasenko <viy@altlinux.org> 2:4.78-alt1.1
- automated CPAN update

* Tue Sep 06 2022 Igor Vlasenko <viy@altlinux.org> 2:4.78-alt1
- automated CPAN update

* Mon Sep 05 2022 Igor Vlasenko <viy@altlinux.org> 2:4.77-alt1
- automated CPAN update

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 2:4.76-alt1
- automated CPAN update

* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 2:4.75-alt5
- no need for perl 7 patches

* Mon Jun 21 2021 Igor Vlasenko <viy@altlinux.org> 2:4.75-alt4
- completely patched IO-AIO for perl 5.32+
- enabled tests

* Sat Jun 19 2021 Igor Vlasenko <viy@altlinux.org> 2:4.75-alt3
- removed set req method to relaxed

* Sat May 29 2021 Igor Vlasenko <viy@altlinux.org> 2:4.75-alt2
- fixed shebang in script
- disabled tests and set req method to relaxed to pass perl 5.32 rebuild

* Wed Jan 06 2021 Igor Vlasenko <viy@altlinux.ru> 2:4.75-alt1
- automated CPAN update

* Wed Dec 30 2020 Igor Vlasenko <viy@altlinux.ru> 2:4.74-alt1
- automated CPAN update

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 2:4.73-alt1
- automated CPAN update

* Sun Sep 27 2020 Igor Vlasenko <viy@altlinux.ru> 2:4.72-alt3
- fixed warning: scripts should be .noarch

* Fri Apr 24 2020 Igor Vlasenko <viy@altlinux.ru> 2:4.72-alt2
- added explicit BR: on libdb{perl}-devel

* Wed Apr 03 2019 Igor Vlasenko <viy@altlinux.ru> 2:4.72-alt1
- automated CPAN update

* Tue Mar 12 2019 Igor Vlasenko <viy@altlinux.ru> 2:4.71-alt1
- automated CPAN update

* Wed Mar 06 2019 Igor Vlasenko <viy@altlinux.ru> 2:4.7-alt1
- automated CPAN update

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 2:4.6-alt1.1
- rebuild with new perl 5.28.1

* Sun Sep 02 2018 Igor Vlasenko <viy@altlinux.ru> 2:4.6-alt1
- automated CPAN update

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 2:4.5-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 2:4.4-alt1
- automated CPAN update

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.34-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.34-alt1.1
- rebuild with new perl 5.24.1

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.34-alt1
- automated CPAN update

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 1:4.33-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:4.32-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1:4.32-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.31-alt1.1
- rebuild with new perl 5.20.1

* Tue Jun 10 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.31-alt1
- automated CPAN update

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.3-alt1
- automated CPAN update

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 1:4.2-alt2
- bumped serial

* Sat Jan 25 2014 Igor Vlasenko <viy@altlinux.ru> 4.2-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 4.18-alt2
- built for perl 5.18

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 4.18-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 4.15-alt1
- 4.0 -> 4.15
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 4.0-alt2
- rebuilt for perl-5.14

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 4.0-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 3.65-alt1.1
- rebuilt with perl 5.12

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> 3.65-alt1
- automated CPAN update

* Sat Jun 27 2009 Michael Bochkaryov <misha@altlinux.ru> 3.25-alt1
- 3.25 version build

* Wed Sep 17 2008 Michael Bochkaryov <misha@altlinux.ru> 3.07-alt1
- 3.07 version build
- fix directory ownership violation

* Mon Apr 28 2008 Michael Bochkaryov <misha@altlinux.ru> 2.62-alt1
- first build for ALT Linux Sisyphus
