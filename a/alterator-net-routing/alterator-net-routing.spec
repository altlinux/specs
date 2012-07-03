%define _altdata_dir %_datadir/alterator

Name: alterator-net-routing
Version: 0.4.1
Release: alt1

Packager: Sergey V Turchin <zerg@altlinux.org>

Source:%name-%version.tar

Summary: alterator module for network routing administration
License: GPL
Group: System/Configuration/Other
Requires: alterator >= 2.8

BuildArch: noarch
BuildPreReq: alterator >= 2.9-alt0.3, alterator-fbi >= 0.7-alt1
BuildRequires: alterator-fbi

%description
alterator module for network routing administration

%prep
%setup -q

%build
%make_build libdir=%_libdir

%install
%makeinstall HTMLROOT=%buildroot%_var/www/
%find_lang %name

%files -f %name.lang
#current
%_bindir/*
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Mon Dec 27 2010 Sergey V Turchin <zerg at altlinux dot org> 0.4.1-alt1
- add header titles to web-interface
- fix to allow empty metric value input

* Wed Dec 22 2010 Sergey V Turchin <zerg at altlinux dot org> 0.4-alt1
- improve error reporting
- fix check metric
- dont flush interface address
- ignore bridge hosts interfaces
- fix routing view content

* Tue Dec 21 2010 Sergey V Turchin <zerg at altlinux dot org> 0.3-alt1
- ignore loopback interface
- fix applying changes
- increase view size

* Mon Dec 20 2010 Sergey V Turchin <zerg at altlinux dot org> 0.2-alt1
- add web ui

* Thu Dec 16 2010 Sergey V Turchin <zerg at altlinux dot org> 0.1-alt1
- initial release
