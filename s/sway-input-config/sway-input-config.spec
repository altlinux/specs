Name: sway-input-config
Version: 1.3.2.2
Release: alt1
Summary: Sway Input Configurator
Group: Graphical desktop/Other
License: GPL-3.0
Url: https://github.com/Sunderland93/sway-input-config

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%description
%summary.

%prep
%setup -n %name-%version

%build
%python3_build

%install
%python3_install

rm -rf -- %buildroot%_datadir/metainfo

%files
%_bindir/sway-input-config
%_datadir/applications/sway-input-config.desktop
%_iconsdir/hicolor/*/apps/sway-input-config.png
%python3_sitelibdir/sway_input_config
%python3_sitelibdir/sway_input_config-*.egg-info

%changelog
* Thu Jan 04 2024 Alexey Gladkov <legion@altlinux.ru> 1.3.2.2-alt1
- New version (1.3.2.2).

* Mon Oct 31 2022 Alexey Gladkov <legion@altlinux.ru> 1.1.2-alt1
- Initial build (1.1.2).
