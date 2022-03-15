%define _altdata_dir %_datadir/alterator

Name: alterator-osec
Version: 0.2.1
Release: alt1

Summary: alterator module for osec
License: GPL
Group: System/Configuration/Other
Url: http://wiki.sisyphus.ru/Alterator

Source: %name-%version.tar
Source1: dirs.conf
Source2: pipe.conf
Source3: osec.logrotate
Source4: run-osec

BuildArch: noarch

BuildPreReq: alterator >= 3.1-alt6 alterator-fbi >= 0.15-alt3 
BuildPreReq: alterator-sh-functions >= 0.1-alt3
Requires: alterator >= 3.1-alt6 alterator-fbi >= 0.15-alt3
Requires: alterator-sh-functions >= 0.1-alt3 osec >= 1.1.0-alt1
Requires: osec-mailreport >= 1.1.0-alt1
# Conflicts: osec-cronjob

%description
System integrity test control alterator module

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall HTMLROOT=%buildroot%_var/www/
install -D -m644 applications/osec.desktop %buildroot/%_datadir/alterator/applications/osec.desktop
%find_lang %name

%__install -pD -m644 %SOURCE2 $RPM_BUILD_ROOT%_sysconfdir/osec/alterator-pipe.conf
%__install -pD -m644 %SOURCE3 $RPM_BUILD_ROOT%_sysconfdir/osec/logrotate
%__install -pD -m755 %SOURCE4 $RPM_BUILD_ROOT%_sysconfdir/osec/run-osec

%files -f %name.lang
%_altdata_dir/ui/*/
%_altdata_dir/help/*/*
%_alterator_backend3dir/*
%_altdata_dir/applications/*
%config(noreplace) %_sysconfdir/osec/*.conf
%config(noreplace) %_sysconfdir/osec/logrotate
%_sysconfdir/osec/run-osec

%changelog
* Tue Mar 15 2022 Paul Wolneykien <manowar@altlinux.org> 0.2.1-alt1
- Fix: State that only the Web UI is implemented for the module.

* Mon Oct 27 2014 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt3
- Rebuild for Sisyphus

* Wed Aug 29 2012 Paul Wolneykien <manowar@altlinux.ru> 0.2-alt2
- Update Russian translations (thx Andriy Stepanov and ua2fgb).

* Wed Jul 25 2012 Paul Wolneykien <manowar@altlinux.ru> 0.2-alt1
- Adapt to the current Alterator/workflow (thx Andriy Stepanov).
- Add  the help page (thx Andriy Stepanov).
- Remove conflicts with osec-cronjob (thx Andriy Stepanov).

* Mon Jul 04 2008 Pavel Wolneykien <manowar@altlinux.org> 0.1-alt1
- Initial release
