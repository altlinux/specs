%define realname firefox

Summary: The Mozilla Firefox project is a redesign of Mozilla's browser
Name: %realname-unmet-holder
Version: 99.0
Release: alt1
Group: Networking/WWW
License: GPL-3.0
Provides: %realname = %version-%release
ExclusiveArch: ppc64le

%description
%summary

%package wayland
Summary: Firefox Wayland launcher.
Group: Networking/WWW
Provides: %realname = %version-%release

%description wayland
The firefox-wayland package contains launcher and desktop file
to run Firefox natively on Wayland.

%package -n rpm-build-firefox
Summary: RPM helper macros to rebuild firefox packages
Group: Development/Other

%description -n rpm-build-firefox
These helper macros provide possibility to rebuild
firefox packages by some Alt Linux Team Policy compatible way.

%package -n firefox-config-privacy
Summary: Firefox configuration with the paranoid privacy settings
Group: System/Configuration/Networking

%description -n firefox-config-privacy
Settings disable:
* obsolete ssl protocols;
* safebrowsing, trackingprotection and other requests to third-party services;
* telemetry;
* webrtc;
* the social features;
* dns and network predictors/prefetch;
* and some more...

Most likely you don't need to use this package.

%files

%files wayland

%files -n rpm-build-firefox

%files -n firefox-config-privacy

%changelog
* Wed Apr 06 2022 Alexey Gladkov <legion@altlinux.ru> 99.0-alt1
- New release (99.0).

* Tue Sep 08 2020 Alexey Gladkov <legion@altlinux.ru> 80.0.1-alt2
- New release (80.0.1).

* Sat Aug 29 2020 Alexey Gladkov <legion@altlinux.ru> 80.0-alt2
- New release (80.0).

* Mon Aug 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 79.0-alt3
- drop armh from build arches

* Thu Jul 30 2020 Alexey Gladkov <legion@altlinux.ru> 79.0-alt2
- New release (79.0).
