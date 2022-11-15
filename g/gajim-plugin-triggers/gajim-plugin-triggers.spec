%define oname triggers

Name: gajim-plugin-triggers
Version: 1.4.7
Release: alt1.1

Summary: Configure Gajim's behavior on some events

License: GPL-3.0-only
Group: Networking/Instant messaging
Url: https://dev.gajim.org/gajim/gajim-plugins/-/wikis/TriggersPlugin

# repacked https://ftp.gajim.org/plugins_releases/triggers_%version.zip
Source: %oname-%version.zip
Source1: %oname.watch
Source2: plugin-manifest.json

Requires: python3-module-gajim-triggers

BuildRequires(pre): jq
BuildRequires: rpm-build-python3 unzip
BuildArch: noarch

%description
%summary.

%add_python3_self_prov_path %buildroot%python3_sitelibdir_noarch/gajim/data/plugins/%oname

%package -n python3-module-gajim-triggers
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch
Requires: %(jq '.requirements[]' %SOURCE2 |sed -E 's,",,g;s,([>=]+), \1 ,g')

%description -n python3-module-gajim-triggers
%summary.

%prep
%setup -n %oname-%version

%install
mkdir -p %buildroot%python3_sitelibdir_noarch/gajim/data/plugins/%oname/
cp -a * %buildroot%python3_sitelibdir_noarch/gajim/data/plugins/%oname/

%files

%files -n python3-module-gajim-triggers
%python3_sitelibdir_noarch/gajim/data/plugins/%oname

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.7-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Oct 11 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.7-alt1
- Updated to 1.4.7.

* Fri Sep 23 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.5-alt2
- Drop needless conflict.

* Thu Jun 02 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.5-alt1
- Updated to 1.4.5.

* Sat May 14 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Wed Mar 23 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.1-alt1
- Initial build for ALT Sisyphus.
