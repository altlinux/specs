
%global pypi_name beren

Name: python3-module-%pypi_name
Version: 0.7.1
Release: alt1
Summary: Provides a REST client targeted at Orthanc REST API endpoints
License: GPLv3+
Group: Development/Python3
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: https://github.com/teffalump/beren
Source: https://files.pythonhosted.org/packages/source/b/%pypi_name/%pypi_name-%version.tar.gz
BuildRequires: rpm-build-python3 python3-module-setuptools rpm-macros-python3 pyproject-build  python3-module-build
BuildArch: noarch

%description
python-beren provides a REST client targeted at Orthanc REST API endpoints

%prep

%setup -n %pypi_name-%version
# remove the pinning from the metadata
sed -i 's/apiron==.*$/apiron/' requirements.txt

%build
%python3_build

%install
%python3_install

%files 
%doc README.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%pypi_name-%version-py?.??.egg-info/

%changelog
* Fri May 06 2022 Ilya Mashkin <oddity@altlinux.ru> 0.7.1-alt1
- Build for Sisyphus

* Tue Jan 11 2022 Dirk Müller <dmueller@suse.com>
- add python macro dependency
* Tue Aug 31 2021 Ben Greiner <code@bnavigator.de>
- skip python36: apiron on TW does not support Python 3.6 anymore
- remove apiron version pinning from Python sitelib metadata
  (upstream uses apiron==6.0.0)
* Thu Jul 22 2021 Axel Braun <axel.braun@gmx.de>
- version 0.7.1
  * no upstream changelog
* Tue Jan 19 2021 Steve Kowalik <steven.kowalik@suse.com>
- Use python_sitelib, rather than python3_sitelib when installing files.
* Tue Sep  1 2020 Steve Kowalik <steven.kowalik@suse.com>
- Update to 0.7.0:
  * No upstream changelog
- Update {Build,}Requires for apiron.
* Mon Oct 21 2019 Axel Braun <axel.braun@gmx.de>
- rename to python-beren
  version 0.6.2
* Mon Aug 26 2019 Axel Braun <axel.braun@gmx.de>
- version 0.5.6
  initial build on OBS
