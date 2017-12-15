%define dist qa-cache
Name: perl-%dist
Version: 0.11
Release: alt4.1.1.1.1

Summary: Simple and efficient cache for memoization
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libqacache-devel perl-devel

%description
qa::cache module provides Perl interface to libqacache library.
qa::memoize implements caching for file processing routines.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/qa
%perl_vendor_autolib/qa

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt3
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- qa/cache.pm: added clean() method

* Wed Sep 07 2011 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- reimplemented using libqacache library - new cache format not
  compatible with earlier releases, ~/.qa-cache must be removed

* Tue Dec 21 2010 Alexey Tourbin <at@altlinux.ru> 0.08-alt1
- qa/cache.pm: further increased db/fs threshold size up to 64K

* Sun Aug 15 2010 Alexey Tourbin <at@altlinux.ru> 0.07-alt1
- qa/cache.pm: increase db/fs theshold size (1/2 -> 3/4 pagesize)

* Tue Aug 10 2010 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- qa/cache.pm: set -MsgFile => \*STDERR
- qa/cache.pm: downgrade db_put error to a warning
- qa/cache.pm: require non-leaking Digest::SHA1 2.13

* Mon Aug 17 2009 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- qa/cache.pm: better diagnostics on db_put failure

* Mon Jul 20 2009 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- qa/cache.pm: serialize dbenv open by locking topdir fd

* Fri May 22 2009 Alexey Tourbin <at@altlinux.ru> 0.03-alt1
- qa/cache.pm: updated BerkeleyDB code
  + enabled automatic recovery for stale read locks
  + reimplemented signal handling for write ops

* Sun Apr 05 2009 Alexey Tourbin <at@altlinux.ru> 0.02-alt1
- qa/memoize.pm: implemented (basename,size,mtime) mode
- qa/cache.pm: cleanup and better error handling

* Mon Feb 16 2009 Alexey Tourbin <at@altlinux.ru> 0.01-alt1
- initial release, based on Mar 2006 version
