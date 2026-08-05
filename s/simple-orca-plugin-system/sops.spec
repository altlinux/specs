%define _unpackaged_files_terminate_build 1
%define githash dd1a949

Name: simple-orca-plugin-system
Version: 1.0.3
Release: alt1.%githash

Summary: Simple Orca Plugin System
License: LGPL-3.0
Group: Accessibility
Url: https://github.com/chrys87/simple-orca-plugin-system
Vcs: https://github.com/chrys87/simple-orca-plugin-system

BuildArch: noarch

Source0: %name-%version.tar

BuildRequires: rpm-build-python3

Requires: orca

%description
SOPS provides a simple way to write custom plugins for the Orca screen reader.
Plugins can be enabled or disabled per user and triggered via keyboard shortcuts.

After installation run as regular user:
  sh %_datadir/SOPS/install-for-current-user.sh

%package plugin-battery
Summary: Battery status plugin for SOPS
Group: Accessibility
Requires: %name = %EVR
Requires: acpi

%description plugin-battery
SOPS plugin that announces battery status.

%package plugin-clipboard
Summary: Clipboard plugin for SOPS
Group: Accessibility
Requires: %name = %EVR

%description plugin-clipboard
SOPS plugin for clipboard management.

%package plugin-f123
Summary: F123 plugins collection for SOPS
Group: Accessibility
Requires: %name = %EVR
Requires: python3
Requires: python3-module-pygobject3
AutoReqProv: no

%description plugin-f123
Collection of F123 accessibility plugins for SOPS.

%package plugin-nvda-speech
Summary: NVDA-style speech control plugins for SOPS
Group: Accessibility
Requires: %name = %EVR
Requires: python3
Requires: python3-module-pygobject3
AutoReqProv: no

%description plugin-nvda-speech
NVDA-style speech control plugins for SOPS:
up, down, left, right directional speech controls.

%package plugin-manager
Summary: Plugin manager for SOPS
Group: Accessibility
Requires: %name = %EVR

%description plugin-manager
Graphical plugin manager for SOPS.

%package plugin-workspacenumber
Summary: Workspace number plugin for SOPS
Group: Accessibility
Requires: %name = %EVR

%description plugin-workspacenumber
SOPS plugin that announces current workspace number.

%prep
%setup

%install
install -d %buildroot%_datadir/SOPS
install -Dm644 SimplePluginLoader.py \
    %buildroot%_datadir/SOPS/SimplePluginLoader.py
install -Dm644 README.md \
    %buildroot%_datadir/SOPS/README.md
install -Dm644 TODO \
    %buildroot%_datadir/SOPS/TODO
install -Dm755 install-for-current-user.sh \
    %buildroot%_datadir/SOPS/install-for-current-user.sh
cp -r plugins %buildroot%_datadir/SOPS/
find %buildroot%_datadir/SOPS/plugins -name "*.py" \
    -exec sed -i '1s|^#!/usr/bin/python.*|#!/usr/bin/python3|' {} \;
# Rename .py plugins to avoid python.prov processing
for f in F123Plugins \
         nvda-style-speech-control-down \
         nvda-style-speech-control-left \
         nvda-style-speech-control-right \
         nvda-style-speech-control-up; do
    mv %buildroot%_datadir/SOPS/plugins/plugins-available/${f}.py \
       %buildroot%_datadir/SOPS/plugins/plugins-available/${f}
done
cp -r tools %buildroot%_datadir/SOPS/
chmod 755 %buildroot%_datadir/SOPS/tools/ensop
chmod 755 %buildroot%_datadir/SOPS/tools/dissop
find %buildroot%_datadir/SOPS/plugins -name "*.sh" -exec chmod 755 {} \;
find %buildroot%_datadir/SOPS/plugins -name "*.py" -exec chmod 755 {} \;
find %buildroot%_datadir/SOPS/plugins -name "F123Plugins" \
     -name "nvda-style-*" -exec chmod 755 {} \;

%files
%_datadir/SOPS/SimplePluginLoader.py
%_datadir/SOPS/README.md
%_datadir/SOPS/TODO
%_datadir/SOPS/install-for-current-user.sh
%_datadir/SOPS/tools/

%files plugin-battery
%_datadir/SOPS/plugins/plugins-available/battery.sh

%files plugin-clipboard
%_datadir/SOPS/plugins/plugins-available/clipboard.py

%files plugin-f123
%_datadir/SOPS/plugins/plugins-available/F123Plugins

%files plugin-nvda-speech
%_datadir/SOPS/plugins/plugins-available/nvda-style-speech-control-down
%_datadir/SOPS/plugins/plugins-available/nvda-style-speech-control-left
%_datadir/SOPS/plugins/plugins-available/nvda-style-speech-control-right
%_datadir/SOPS/plugins/plugins-available/nvda-style-speech-control-up

%files plugin-manager
%_datadir/SOPS/plugins/plugins-available/plugin_manager.sh

%files plugin-workspacenumber
%_datadir/SOPS/plugins/plugins-available/workspacenumber.sh

%changelog
* Wed Aug 5 2026 Timofei Fedotov <sovtouch@altlinux.org> 1.0.3-alt1.dd1a949
- Initial build for ALT Sisyphus.
