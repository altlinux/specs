%define oname yamlsettings

%def_with check

Name: python3-module-%oname
Version: 2.1.0
Release: alt1

Summary: Yaml Settings Configuration Module
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/yamlsettings/
Vcs: https://github.com/KyleJamesWalker/yamlsettings.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pip
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pyaml
BuildRequires: python3-module-pytest-cov
BuildRequires: python3-module-mock
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-flake8
%endif

%py3_provides %oname

%description
A library to help manage project settings, without having to worry about
accidentally checking non-public information, like api keys. Along with
simple environment variable support.

%prep
%setup

sed -i '/"nose",/d' setup.py
sed -i '/"pytest-runner",/d' setup.py

%build
%python3_build

%install
%python3_install

%check
%tox_check

%files
%doc *.rst LICENSE
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-*.egg-info


%changelog
* Mon Mar 27 2023 Anton Vyatkin <toni@altlinux.org> 2.1.0-alt1
- New version 2.1.0.

* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150210.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150210
- Initial build for Sisyphus

