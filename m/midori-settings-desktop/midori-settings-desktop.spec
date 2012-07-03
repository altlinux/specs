Name: midori-settings-desktop
Version: 5.0.2
Release: alt1
BuildArch: noarch

Source: %name-%version.tar

Summary:  Midori settings for 5.0.2 Desktop
License: GPL
Group: System/Configuration/Other
Packager: Anton V. Boyarshiniv <boyarsh@altlinux.org>

Requires: midori

%description
Midori settings for 5.0.2 Desktop

%prep
%setup -q

%install
mkdir -p %buildroot%_sysconfdir/skel/.config/midori
cp -a * %buildroot%_sysconfdir/skel/.config/midori/

%files
/etc/skel/.config/midori/


%changelog
* Thu Dec 09 2010 Radik Usupov <radik@altlinux.org> 5.0.2-alt1
- Initial build


