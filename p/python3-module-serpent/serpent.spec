%define oname serpent

Name: python3-module-%oname
Version: 1.41
Release: alt1
Summary: Serializer for literal Python expressions
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/serpent

# https://github.com/irmen/Serpent.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3-module-attrs
BuildRequires: python3-module-flake8
BuildRequires: python3-module-pytz

%description
Serpent is a simple serialization library based on ast.literal_eval.

Because it only serializes literals and recreates the objects using
ast.literal_eval(), the serialized data is safe to transport to other
machines (over the network for instance) and de-serialize it there.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
python3 setup.py test

%files
%doc README.md
%python3_sitelibdir/%oname.py
%python3_sitelibdir/__pycache__/serpent.cpython-*.pyc
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sat Apr 15 2023 Anton Midyukov <antohami@altlinux.org> 1.41-alt1
- Updated to upstream version 1.41

* Mon Oct 19 2020 Stanislav Levin <slev@altlinux.org> 1.28-alt2
- Stopped Python2 package build.

* Sun Apr 21 2019 Anton Midyukov <antohami@altlinux.org> 1.28-alt1
- Updated to upstream version 1.28

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.23-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Oct 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.23-alt1
- Updated to upstream version 1.23.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11-alt2.git20150621.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 05 2016 Sergey Alembekov <rt@altlinux.ru> 1.11-alt2.git20150621
- cleanup buildreq

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11-alt1.git20150621
- Version 1.11

* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8-alt1.git20150108
- Version 1.8

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.git20140713
- Initial build for Sisyphus

