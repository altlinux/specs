Name: repocop-unittest-rpm-filetriggers
Version: 0.23
Release: alt3
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: test for obsolete calls in post/un sections
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org 

Requires: repocop > 0.55
Conflicts:  repocop-unittest-post_ldconfig >= 0.03
Obsoletes: repocop-unittest-post_ldconfig < 0.03
Provides:  repocop-unittest-altdesktop = 0.09
Obsoletes: repocop-unittest-altdesktop < 0.09
Conflicts: repocop-unittest-freedesktop-mime-test >= 0.04
Obsoletes: repocop-unittest-freedesktop-mime-test < 0.04
Requires: perl-RPM-Source-Editor >= 0.73

Source: %name-%version.tar

%description
integration test for repocop test platform.

%prep
%setup -q

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

mkdir -p %buildroot%_datadir/repocop/fixscripts/
install -m 644 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
%_datadir/repocop/pkgtests/*
%_datadir/repocop/fixscripts/*

%changelog
* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt3
- bugfixes

* Sun Mar 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2
- further adapted for new R::S::E syntax

* Thu Nov 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- adapted for new fixscript syntax

* Fri Aug 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- use R::S::E 0.66

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- postclean patchgen improvements
- removed support for dropped macros

* Fri Feb 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt7
- postclean patchgen improvement

* Mon Jan 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt6
- post_ldconfig patchgen improvement

* Fri Jan 15 2010 Igor Vlasenko <viy@altlinux.ru> 0.20-alt5
- postclean patchgen improvement

* Tue Nov 24 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt4
- postclean patchgen improvement

* Sat Nov 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt3
- shared-mime-info patchgen improvement

* Thu Nov 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt2
- obsolete-call-in-post-install-info improvement

* Sat Nov 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- added:
   + obsolete-call-in-post-gtk-update-icon-cache.pl
   + postclean-filetriggers.pl

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- posttests migration

* Thu May 21 2009 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- bugfix (thanks to @php-coder)

* Mon May 18 2009 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- added obsolete-call-in-post-install-info check

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- fixed bug in post*_ldconfig fixscripts (thanks to @ldv)

* Thu Dec 18 2008 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- support for requires alternatives >= 0:0.4

* Sun Dec 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- real support for %%force_update_alternatives macro:
  if package requires alternatives >= 0.4 no warning is issued.

* Sun Dec 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- improvements in fixscripts

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- accurate choice of triggers

* Wed Dec 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- update_menus in postun also cleaned up (thanks to mike@).

* Sun Nov 30 2008 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- support for %%force_update_alternatives macro:
  if package requires alternatives >= 0.4 no warning is issued.

* Fri Nov 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt2
- bugfixes in obsolete-call-in-post-alternatives

* Sun Nov 23 2008 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfixes in  obsolete-call-in-post-alternatives 

* Sun Nov 23 2008 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- bugfixes in  obsolete-call-in-post-alternatives 

* Fri Nov 21 2008 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added new test
  obsolete-call-in-post-alternatives-0.3

* Sun Nov 16 2008 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- support for Denis

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- cleanup and fixes

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- nice patches with no blank lines added

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added new tests:
   * obsolete-call-in-post-gtk-update-icon-cache
   * obsolete-call-in-post-scrollkeeper-update

* Sat Nov 15 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- multiple nightly bugs and misprints fixed

* Fri Nov 14 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed bug in from_section.pl

* Thu Nov 13 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
