Name: lightdm-profiles
Version: 0.1.1
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
Requires: lightdm-gtk-greeter >= 2.0.1-alt11

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
* Mon Jan 21 2019 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt2
- Require lightdm-gtk-greeter >= 2.0.1-alt11 (which incorporates the
  "-pd" version).

* Wed Aug 22 2018 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Depend on lightdm-gtk-greeter-pd >= 1:2.0.1.5 (no release version).
- Activate the "hide-cancel-noprompt" option in the "zastava" profile.

* Mon Nov 27 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt2
- Build noarch package.
- Fixed control script.

* Thu Nov 23 2017 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build.
