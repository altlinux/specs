Name: installer-feature-vm-lucky
Version: 0.1
Release: alt1

Summary: Automatic partitioning
License: GPL
Group: System/Configuration/Other

Url: http://wiki.sisyphus.ru/devel/installer/features
Packager: Michael Shigorin <mike@altlinux.org>
BuildArch: noarch

%description
%summary

%package stage2
Summary: Automatic partitioning
License: GPL
Group: System/Configuration/Other
Requires: installer-stage2
Requires: alterator-vm >= 0.3-alt24

%description stage2
%summary

%post stage2
sed -i 's,^\(X-Alterator-URI=\).*$,\1/vm/lucky,' %_datadir/install2/steps/vm.desktop

%files stage2

# TODO:
# - can it be made into a proper package not a hack?
#   (seems like currently all steps belong to installer
#   so they can be counted)

%changelog
* Thu Apr 10 2008 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- init with installer-sdk

