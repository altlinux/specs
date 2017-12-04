Name: lightdm-profiles
Version: 0.1.0
Release: alt2

Summary: Set of profiles for LightDM configuration
License: GPLv3+
Group: System/Configuration/Other

BuildArch: noarch

Source0: %name-%version.tar

%description
%summary

%package zastava
Summary: "Zastava" LightDM profile and configuration files
License: GPLv3+
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: lightdm >= 1.16.7-alt16
Requires: lightdm-gtk-greeter-pd >= 1:2.0.1.5-alt1

%description zastava
Contains profile and configuration files used for "Zastava" installation

%prep
%setup

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%_controldir/*

%files zastava
%_sysconfdir/lightdm/profile.d/zastava*
%_sysconfdir/lightdm/zastava*

%changelog
* Mon Nov 27 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Build noarch package.
- Fixed control script.

* Thu Nov 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build.
