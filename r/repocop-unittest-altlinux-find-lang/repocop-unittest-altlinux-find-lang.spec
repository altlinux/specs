Name: repocop-unittest-altlinux-find-lang
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>
Url: http://repocop.altlinux.org

Summary: repocop package checks for conformance with FindLangPolicy.
Group: Development/Other
License: GPL or Artistic
Source: %name-%version.tar

Requires: repocop >= 0.10
#Requires: repocop-collector-specfile

%description
set of ALTLinux-specific integration tests for repocop test platform.
The tests checks packages for conformance with FindLangPolicy.

%prep
%setup

%build

%install
for i in *.posttest; do
    testname=`echo $i | sed -e s,.posttest\$,,`
    install -pD -m 755 $testname.posttest %buildroot%_datadir/repocop/pkgtests/$testname/posttest
done

install -d -m 755 %buildroot%_datadir/repocop/fixscripts/
#install -m 644 *.pl %buildroot%_datadir/repocop/fixscripts/

%files
#doc README ChangeLog
%_datadir/repocop/pkgtests/*
#%_datadir/repocop/fixscripts/*

%changelog
* Fri Mar 19 2010 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- removed flphoto exception

* Thu Mar 18 2010 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- fixed summary and description thanks to php_coder@.

* Wed Mar 17 2010 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
