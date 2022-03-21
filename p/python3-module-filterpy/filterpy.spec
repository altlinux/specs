%define _unpackaged_files_terminate_build 1
%define oname filterpy

%def_with check

Name: python3-module-%oname
Version: 1.4.5
Release: alt2

Summary: Kalman filtering and optimal estimation library
License: MIT
Group: Development/Python3
BuildArch: noarch
Url: https://pypi.org/project/filterpy/

# https://github.com/rlabbe/filterpy.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(numpy)
BuildRequires: python3(scipy)
BuildRequires: python3(matplotlib)

BuildRequires: python3(numpy.testing)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
This library provides Kalman filtering and various related optimal and
non-optimal filtering software written in Python. It contains Kalman
filters, Extended Kalman filters, Unscented Kalman filters, Kalman
smoothers, Least Squares filters, fading memory filters, g-h filters,
discrete Bayes, and more.

%prep
%setup
%autopatch -p1

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr --develop

%files
%doc *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Mon Mar 21 2022 Stanislav Levin <slev@altlinux.org> 1.4.5-alt2
- Fixed FTBFS.

* Tue Aug 25 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.4.5-alt1
- Updated to upstream version 1.4.5.

* Mon Aug 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt4
- Build requires fixed.

* Fri Feb 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt3
- Build for python2 disabled.

* Wed Jun 12 2019 Stanislav Levin <slev@altlinux.org> 1.1.0-alt2
- Added missing dep on `numpy.testing`.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.16-alt1.git20150217.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.16-alt1.git20150217.1
- NMU: Use buildreq for BR.

* Wed Feb 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.16-alt1.git20150217
- Version 0.0.16

* Mon Dec 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.7-alt1.git20141130
- Version 0.0.7

* Mon Nov 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt2.git20141122
- Moved examples into tests subpackage

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.6-alt1.git20141122
- Initial build for Sisyphus

