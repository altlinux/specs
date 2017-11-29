Name:     settings-s
Version:  0.1
Release:  alt1

Summary:  settings for custom distro
License:  GPLv2
Group:    Other
Url:      http://git.altlinux.org/people/nbr/packages/settings-s.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
These are settings for custom distro.

%prep
%setup

%install
mkdir -p %buildroot/%_sysconfdir/firsttime.d/
install -Dm 0644 65-settings.sh  %buildroot%_sysconfdir/firsttime.d/


%files
%_sysconfdir/firsttime.d/65-settings.sh



%changelog
* Wed Nov 29 2017 Denis Medvedev <nbr@altlinux.org> 0.1-alt1
Initial release
