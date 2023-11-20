%define rname projectm
Name: projectm-common
Version: 0.1
Release: alt1

Group: System/Base
Summary: Common data for ProjectM
Url: http://projectm.sourceforge.net/
License: LGPL-3.0-or-later

BuildArch: noarch

%description
%{summary}.

%prep

%install
mkdir -p %buildroot/%_datadir/projectM/{fonts,presets,shaders}/

%files
%dir %_datadir/projectM/
%dir %_datadir/projectM/fonts/
%dir %_datadir/projectM/presets/
%dir %_datadir/projectM/shaders/

%changelog
* Fri Nov 17 2023 Sergey V Turchin <zerg@altlinux.org> 0.1-alt1
- initial build
