%define _altdata_dir %_datadir/alterator

Name: alterator-audit
Version: 0.3.1
Release: alt1
BuildArch: noarch

Packager: Andrey Kolotov <qwest@altlinux.org>

Source:%name-%version.tar

Summary: alterator module for audit system
License: GPL
Group: System/Configuration/Other

BuildRequires: alterator >= 4.10-alt5

Requires: alterator >= 4.10-alt5
Requires: audit gawk

%description
Alterator module for audit system

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall DESTDIR=%buildroot

%post
test -e %_sysconfdir/sysconfig/alterator-audit/rules || install -Dpm640 /dev/null %_sysconfdir/sysconfig/alterator-audit/rules
test -e %_sysconfdir/audit/audit.rules && mv %_sysconfdir/audit/audit.rules %_sysconfdir/audit/audit.rules.old ||:
ln -s %_sysconfdir/sysconfig/alterator-audit/rules %_sysconfdir/audit/audit.rules

%preun
rm -f %_sysconfdir/audit/audit.rules
test -e %_sysconfdir/audit/audit.rules.old && mv %_sysconfdir/audit/audit.rules.old %_sysconfdir/audit/audit.rules ||:

%files
%_sysconfdir/sysconfig/alterator-audit/*
%_altdata_dir/ui/*
%_altdata_dir/applications/*
%_alterator_backend3dir/*

%changelog
* Tue Feb 21 2017 Sergey V Turchin <zerg@altlinux.org> 0.3.1-alt1
- Fix aureport datetime options usage

* Thu Feb 13 2014 Andrey Kolotov <qwest@altlinux.org> 0.3.0-alt1
- Fix bugs in the interface of settings rules
- Restored expert mode from rule interface
- Added button to activation daemon auditd

* Tue Dec 31 2013 Andrey Kolotov <qwest@altlinux.org> 0.2.0-alt1
- Templates for rules
- Search for audit log
- Remove expert mode from rule interface
- Save output audit log in file
- Cache on the 1000 lines for log

* Tue Nov 26 2013 Andrey Kolotov <qwest@altlinux.org> 0.1.1-alt1
- Automatic creation of rules from a file
- Fixed being able create, delete rules

* Tue Nov 26 2013 Andrey Kolotov <qwest@altlinux.org> 0.1.0-alt1
- Worked out the main interface
- Added simple mode to create rules

* Fri Oct 18 2013 Andrey Kolotov <qwest@altlinux.org> 0.0.2-alt1
- Added management rules.

* Fri Oct 11 2013 Andrey Kolotov <qwest@altlinux.org> 0.0.1-alt1
- Initial release
