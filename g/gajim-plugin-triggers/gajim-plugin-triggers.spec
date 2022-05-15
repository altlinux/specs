%define oname triggers

Name: gajim-plugin-triggers
Version: 1.4.4
Release: alt1

Summary: Configure Gajim's behavior on some events

License: GPL-3.0-only
Group: Networking/Instant messaging
Url: https://dev.gajim.org/gajim/gajim-plugins/-/wikis/TriggersPlugin

# repacked https://ftp.gajim.org/plugins_releases/triggers_%version.zip
Source: %oname-%version.zip
Source1: %oname.watch
Source2: manifest.ini

Requires: python3-module-gajim-triggers

BuildRequires: rpm-build-python3 unzip
BuildArch: noarch

%description
%summary.

%package -n python3-module-gajim-triggers
Summary: Python module for %name
Group: Development/Python
BuildArch: noarch
Requires: gajim >= %(sed -n 's/^min_gajim_version:\s*\([[:digit:].]\+\).*$/\1/p' %SOURCE2)
Conflicts: gajim > %(sed -n 's/^max_gajim_version:\s*\([[:digit:].]\+\).*$/\1/p' %SOURCE2)

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
* Sat May 14 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.4.4-alt1
- Updated to 1.4.4.

* Wed Mar 23 2022 Vladimir D. Seleznev <vseleznv@altlinux.org> 1.3.1-alt1
- Initial build for ALT Sisyphus.
