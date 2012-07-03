Name: repocop-unittest-freedesktop
Version: 0.19
Release: alt3
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: desktop packaging test
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop > 0.55
Requires: repocop-collector-freedesktop-desktop
Provides: repocop-unittest-freedesktop-desktop-exec-fill-code = 0.04
Obsoletes: repocop-unittest-freedesktop-desktop-exec-fill-code < 0.04
Provides: repocop-unittest-freedesktop-categories = 0.06
Obsoletes: repocop-unittest-freedesktop-categories < 0.06

Source: %name-%version.tar
BuildRequires: perl-devel perl-DBI

%description
integration test for repocop test platform.
Includes the following tests:
* desktop-exec-fill-code
 verifies packaging of .desktop files with MimeType entry
 and Exec (%%f|%%F|%%U|%%u) specifier.
 according to  http://www.freedesktop.org/Standards/desktop-entry-spec
 (see also draft of Sergey N. Yatskevich
 http://lists.altlinux.org/pipermail/devel/2008-March/071791.html)

%prep
%setup -q

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

for i in *.pl; do
    install -pD -m 644 $i %buildroot%_datadir/repocop/fixscripts/$i
done

%files
%_datadir/repocop/pkgtests/*
%_datadir/repocop/fixscripts/*

%changelog
* Sat May 05 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt3
- maintainance release

* Fri Nov 11 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt2
- fixscript cleanup

* Thu Nov 10 2011 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- adapted for new fixscript syntax

* Tue May 24 2011 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- patchgen improvements

* Wed May 18 2011 Igor Vlasenko <viy@altlinux.ru> 0.17-alt1
- patchgen improvements

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- cleanup for lyx patch

* Mon May 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- more generated category patches

* Sat May 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- bugfix release

* Sat May 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- added generated category patches

* Mon Apr 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- added some X- subcategories

* Sun Mar 27 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- added Science; category

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- kde3/4 share support

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- posttests migration

* Sat May 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt4
- real bugfix

* Fri May 29 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt3
- bugfix (thanks to drool@)

* Fri May 08 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt2
- bugfix release

* Thu May 07 2009 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- added freedesktop-categories

* Mon Mar 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixed desktop-exec-fill-code (thanks to REAL@)

* Mon Nov 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt4
- message cleanup in the rest of tests

* Sun Nov 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3
- message cleanup

* Sat Aug 02 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2
- bugfix (incompete SQL in desktop-misplaced-type-servicetype)

* Thu Jul 10 2008 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- bugfix for case no packages found

* Tue Jul 08 2008 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added 
  + desktop-misplaced-type-application.done
  + desktop-misplaced-type-service.done
  + desktop-misplaced-type-servicetype.done

* Mon Jul 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- First build for Sisyphus.
