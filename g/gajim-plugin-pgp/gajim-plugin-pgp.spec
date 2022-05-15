%define oname pgp

%filter_from_requires /^python3(gajim.gui.dialogs)/d

Name: gajim-plugin-pgp
Version: 1.4.4
Release: alt1

Summary: PGP encryption via XEP-0027 for Gajim

License: GPL-3.0-only
Group: Networking/Instant messaging
Url: https://dev.gajim.org/gajim/gajim-plugins/-/wikis/pgpplugin

# repacked https://ftp.gajim.org/plugins_releases/pgp_%version.zip
Source: %oname-%version.zip
Source1: %oname.watch
# extracted from zip archive
Source2: manifest.ini

Requires: python3-module-gajim-pgp
Requires: gajim >= %(sed -n 's/^min_gajim_version:\s*\([[:digit:].]\+\).*$/\1/p' %SOURCE2)
Conflicts: gajim > %(sed -n 's/^max_gajim_version:\s*\([[:digit:].]\+\).*$/\1/p' %SOURCE2)

BuildRequires: rpm-build-python3
BuildRequires: unzip
BuildArch: noarch

%description
%summary.

%package -n python3-module-gajim-pgp
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch
Requires: %name

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
* Sat May 14 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Mon Feb 07 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.6-alt1
- Initial build for ALT Sisyphus.
