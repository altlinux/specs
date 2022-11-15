%define oname pgp

%filter_from_requires /^python3(gajim.gui.dialogs)/d

Name: gajim-plugin-pgp
Version: 1.4.9
Release: alt1.1

Summary: PGP encryption via XEP-0027 for Gajim

License: GPL-3.0-only
Group: Networking/Instant messaging
Url: https://dev.gajim.org/gajim/gajim-plugins/-/wikis/pgpplugin

# repacked https://ftp.gajim.org/plugins_releases/pgp_%version.zip
Source: %oname-%version.zip
Source1: %oname.watch
# extracted from zip archive
Source2: plugin-manifest.json

BuildRequires(pre): jq
BuildRequires: rpm-build-python3
BuildRequires: unzip
BuildArch: noarch

Requires: python3-module-gajim-pgp
Requires: %(jq '.requirements[]' %SOURCE2 |sed -E 's,",,g;s,([>=]+), \1 ,g')

%description
%summary.

%package -n python3-module-gajim-pgp
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch

%add_python3_self_prov_path %buildroot%python3_sitelibdir_noarch/gajim/data/plugins/%oname

%description -n python3-module-gajim-pgp
%summary.

%prep
%setup -n %oname-%version

%install
mkdir -p %buildroot%python3_sitelibdir_noarch/gajim/data/plugins/%oname/
cp -a * %buildroot%python3_sitelibdir_noarch/gajim/data/plugins/%oname/

%files

%files -n python3-module-gajim-pgp
%python3_sitelibdir_noarch/gajim/data/plugins/%oname

%changelog
* Sat Nov 12 2022 Daniel Zagaynov <kotopesutility@altlinux.org> 1.4.9-alt1.1
- NMU: used %%add_python3_self_prov_path macro to skip self-provides from dependencies.

* Tue Oct 11 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.9-alt1
- Updated to 1.4.9.

* Fri Sep 23 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.6-alt2
- Drop needless conflict.

* Thu Jun 02 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.6-alt1
- Updated to 1.4.6.
- Dropped cycle dependency.

* Sat May 14 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Mon Feb 07 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.6-alt1
- Initial build for ALT Sisyphus.
