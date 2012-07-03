Name: alterator-moodle-install
Version: 1.8
Release: alt1

BuildArch: noarch

Source:%name-%version.tar

Summary: Alterator module for Moodle service configuration
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 4.8-alt1
Requires: alterator-fbi >= 5.11-alt2
Requires: moodle-install-tools >= 0.9

BuildRequires(Pre): rpm-macros-alterator

# Automatically added by buildreq on Wed Apr 08 2009
BuildRequires: alterator rpm-macros-fillup

%description
Alterator module for Moodle service configuration

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/moodle-install
%_alterator_backend3dir/moodle-install

%changelog
* Sun May 06 2012 Aleksey Avdeev <solo@altlinux.ru> 1.8-alt1
- Fix use --dbsocket for mt-install

* Sun Apr 22 2012 Aleksey Avdeev <solo@altlinux.ru> 1.7-alt1
- The field of "DB name:" changed to "Base DB name:"
- Removed fields:
  + "DB administrator:"
  + "DB administrator password:"
  + "Data directory:"

* Sat Mar 17 2012 Aleksey Avdeev <solo@altlinux.ru> 1.6-alt1
- Add use mt-install-lslangs

* Fri Mar 16 2012 Aleksey Avdeev <solo@altlinux.ru> 1.5-alt1
- Fix active config sets
  (thanks to Paul Wolneykien <manowar altlinux.ru>)

* Thu Mar 15 2012 Aleksey Avdeev <solo@altlinux.ru> 1.4-alt1
- Fix active config sets

* Tue Mar 13 2012 Aleksey Avdeev <solo@altlinux.ru> 1.3-alt1
- Fix backend3 (list_configs() function)

* Tue Mar 13 2012 Aleksey Avdeev <solo@altlinux.ru> 1.2-alt1
- Add use mt-install-lsconfigs and mt-install-setconfig

* Sun Mar 11 2012 Aleksey Avdeev <solo@altlinux.ru> 1.1-alt1
- Add use mt-install-lsdefaults

* Thu Mar 08 2012 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial draft release.
