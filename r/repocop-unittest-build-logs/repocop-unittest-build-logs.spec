# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/Repocop/ExternalTest.pm)
# END SourceDeps(oneline)
%define testname build-logs

Name: repocop-unittest-%testname
Version: 0.07
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %testname unit tests for repocop test platform
Group: Development/Other
License: GPL or Artistic
Url: http://repocop.altlinux.org
Requires: repocop >= 0.65

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
   repocop-rsync-beehive-logs \
   repocop-process-build-logs \
   $RPM_BUILD_ROOT%_bindir/

for i in *.pl; do
    install -pD -m 755 $i %buildroot%_datadir/repocop/fixscripts/$i
done

for log_arch in i586 x86_64; do
    mkdir -p %buildroot%_datadir/repocop/srccollectors/repocop-process-build-logs-$log_arch/
    ln -s ../../common/purge-keydir \
    %buildroot%_datadir/repocop/srccollectors/repocop-process-build-logs-$log_arch/purge
done

%files
#doc README ChangeLog
%_bindir/repocop-*
%_datadir/repocop/fixscripts/*
%_datadir/repocop/srccollectors/*

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- fixed build with perl 5.26

* Fri Feb 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- dropped beehive-log-non-strict-dependency patch generator
- TODO: drop collector

* Wed Jan 23 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- added beehive-log-non-strict dependency test

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- support for serial in patchgenerator

* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- bugfix release

* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added beehive-log-dependency-needs-epoch test
- added beehive-log-dependency-needs-epoch patchgenerator

* Thu May 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- First build for Sisyphus.
