# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/Repocop/ExternalTest.pm)
# END SourceDeps(oneline)
%define testname build-logs

Name: repocop-unittest-%testname
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname unit tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.40

Source0: %name-%version.tar

%description
%summary

%prep
%setup

%build

%install
mkdir -p $RPM_BUILD_ROOT%_bindir/
install -m 755 \
   repocop-unittest-build-log \
   repocop-process-build-logs \
   $RPM_BUILD_ROOT%_bindir/

for i in *.pl; do
    install -pD -m 644 $i %buildroot%_datadir/repocop/fixscripts/$i
done

%files
#doc README ChangeLog
%_bindir/repocop-*
%_datadir/repocop/fixscripts/*

%changelog
* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfix release

* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added beehive-log-dependency-needs-epoch test
- added beehive-log-dependency-needs-epoch patchgenerator

* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
