Name: alterator-gpupdate
Version: 1.3
Release: alt2

Url: http://altlinux.org/alterator
Source: %name-%version.tar

Summary: Alterator module for group policy settings
License: GPLv2+
Group: System/Configuration/Other

Requires: alterator >= 4.7-alt4
Requires: alterator-l10n >= 2.9.67
Requires: gpupdate

BuildRequires(pre): alterator >= 5.0
BuildRequires(pre): alterator-lookout
BuildRequires: guile22-devel

%description
Alterator module for group policy settings

%prep
%setup

%build
%make_build libdir=%_libdir

%install
export GUILE_LOAD_PATH=/usr/share/alterator/lookout
%makeinstall

%files
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/
%_alterator_libdir/ui/gpupdate/*.go
%_alterator_backend3dir/*

%changelog
* Thu Jun 27 2024 Michael Shigorin <mike@altlinux.org> 1.3-alt2
- NMU:
  + use guile22 on e2k too
  + clarify License:
  + add Url:
  + minor spec cleanup

* Mon Aug 03 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.3-alt1
- Add support of alterator web interface aka ajax support
- Remove BuildArch is noarch due ajax part of module

* Wed Apr 22 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.2-alt1
- Add predefined profile name for ad-domain-controller
- Improve popup information after group policy management apply
- Require appropriate alterator-l10n version

* Mon Apr 20 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.1-alt2
- Update desktop file l10n
- Set BuildArch to noarch as whole source package should be made noarch

* Mon Apr 20 2020 Evgeny Sinelnikov <sin@altlinux.org> 1.1-alt1
- Adapted backend for gpupdate-setup CLI
- Add support for multiple profiles
- Improve ui display

* Thu Apr 02 2020 Rustem Bapin <rbapin@altlinux.org> 1.0-alt1
- First working version

