%define testname fonts.alias
Name: repocop-unittest-%testname
Version: 0.03
Release: alt2
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: repocop %testname test
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org

Requires: repocop

Source: %name-%version.tar
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build

%install
install -pD -m 755 %testname.test %buildroot%_datadir/repocop/pkgtests/%testname/test
install -pD -m 644 %testname.filepattern %buildroot%_datadir/repocop/pkgtests/%testname/filepattern
install -pD -m 755 fonts.alias-verify.pl %buildroot%_bindir/fonts.alias-verify.pl

%files
%doc README.ru
%_datadir/repocop/pkgtests/*
%_bindir/*

%changelog
* Mon Aug 15 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- bump release

* Thu Jun 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- silent mode

* Thu Jun 02 2011 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- bugfix release 

* Wed Jun 01 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
