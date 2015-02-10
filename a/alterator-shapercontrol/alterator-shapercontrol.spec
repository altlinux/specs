%define _altdata_dir %_datadir/alterator

Name: alterator-shapercontrol
Version: 0.4.3
Release: alt1
License: %gpl2plus
Group: System/Configuration/Other
Summary: Alterator module for shapercontrol administration
Source: %name-%version.tar

Requires: alterator alterator-sh-functions alterator-net-functions alterator-hw-functions
Requires: alterator-net-iptables alterator-service-functions
Requires: alterator-l10n
Requires: shapercontrol

BuildPreReq: alterator
BuildPreReq: rpm-build-licenses

BuildArch: noarch

%description
Alterator module for shapercontrol administration.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*
%_libexecdir/%name/

%changelog
* Tue Feb 10 2015 Mikhail Efremov <sem@altlinux.org> 0.4.3-alt1
- Fix out_if in case of 'disable' value.

* Wed Feb 04 2015 Andriy Stepanov <stanv@altlinux.ru> 0.4.2-alt1
- Stop stopping service at visiting 'config' page

* Wed Jan 28 2015 Mikhail Efremov <sem@altlinux.org> 0.4.1-alt1
- Add 'kibit' word for translation.
- Fix bypass_int/bypass_ext.

* Mon Nov 10 2014 Andriy Stepanov <stanv@altlinux.ru> 0.4-alt3
- Service stop before each action. Add many comments. Add testing howto.

* Fri Oct 31 2014 Andriy Stepanov <stanv@altlinux.ru> 0.4-alt2
- List all interfaces at in/out fields

* Wed Sep 03 2014 Mikhail Efremov <sem@altlinux.org> 0.4-alt1
- Use alterator-service-functions.
- Add string to translation.
- Setup new sc.conf.
- Use iptables_helper for list external/internal interfaces.
- Add Russian name for module.
- Use netdev_read_mac() and read_iface_current_addr().
- Create SQLite database.

* Mon Jul 07 2014 Timur Aitov <timonbl4@altlinux.org> 0.3-alt1
- Fix apply state button
- Add Requires: shapercontrol

* Fri Jul 04 2014 Timur Aitov <timonbl4@altlinux.org> 0.2-alt1
- Fix get interfaces list

* Thu Jul 03 2014 Timur Aitov <timonbl4@altlinux.org> 0.1-alt1
- First build

