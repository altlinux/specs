Name:     installer-feature-cert
Version:  0.4.2
Release:  alt3

Summary:  Installer settings for certified distro
License:  GPLv2
Group:    System/Configuration/Other
Url:      http://git.altlinux.org/people/nbr/packages/installer-feature-cert.git

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildArch: noarch

%description
Installer settings for certified distro.

%package stage2
Summary: Installer settings for certified distro (installer files)
Group: System/Configuration/Other

%description stage2
Installer settings for certified distro (installer files).

%prep
%setup

%install
install -D -m 0755 65-settings-cert.sh %buildroot%_datadir/install2/postinstall.d/65-settings-cert.sh

%files stage2
%_datadir/install2/postinstall.d/65-settings-cert.sh

%changelog
* Fri Nov 03 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt3
- Rename to installer-feature-cert (was: installer-settings-cert).

* Wed Nov 01 2023 Paul Wolneykien <manowar@altlinux.org> 0.4.2-alt2
- Extract integalert to separate package. Rename package to
  installer-settings-cert (was: settings-s).
