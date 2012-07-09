%define testname unmet-dependency

Name: repocop-unittest-%testname
Version: 0.09
Release: alt1
BuildArch: noarch
Packager: Igor Vlasenko <viy@altlinux.ru>
Requires: repocop >= 0.19
Url: http://repocop.altlinux.org

Summary: %testname integration tests for repocop test platform.
Group: Development/Other
License: GPLv2+

Source: %name-%version.tar

%description
The test warns packages that contain unmet dependencies.

%prep
%setup

%build

%install
for i in *.distrotest; do
    testname=`echo $i | sed -e s,.distrotest\$,,`
    install -pD -m 755 $testname.distrotest %buildroot%_datadir/repocop/pkgtests/$testname/distrotest
done

install -m 755 archdiff %buildroot%_datadir/repocop/pkgtests/unmet-dependency-build-missing-package/_archdiff

%files
%_datadir/repocop/pkgtests/%testname-*/

%changelog
* Mon Jul 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- introduced distrotests

* Tue Jan 05 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- optimized archdiff script.

* Wed Sep 30 2009 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- distrotests migration

* Sat Aug 01 2009 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- fixed bug in substr

* Thu Mar 12 2009 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added _archdiff hack

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- repocop 0.09 interface

* Sun Dec 07 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- better error messages

* Sat Dec 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added tests for BuildRequires:

* Fri Dec 05 2008 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial version
