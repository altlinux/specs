%define oname yamlsettings

Name: python3-module-%oname
Version: 0.2.0
Release: alt2

Summary: Yaml Settings Configuration Module
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/yamlsettings/
BuildArch: noarch

# https://github.com/KyleJamesWalker/yamlsettings.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-yaml python3-module-nose
BuildRequires: python3-module-mock

%py3_provides %oname
%py3_requires yaml


%description
A library to help manage project settings, without having to worry about
accidentally checking non-public information, like api keys. Along with
simple environment variable support.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.0-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.0-alt1.git20150210.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150210.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150210
- Initial build for Sisyphus

