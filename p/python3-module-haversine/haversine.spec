%define _unpackaged_files_terminate_build 1
%define oname haversine

%def_with check

Name: python3-module-%oname
Version: 2.5.1
Release: alt1

Summary: Calculate the distance between 2 points on Earth
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/haversine/
# https://github.com/mapado/haversine.git

Source0: %name-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(numpy.testing)
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Calculate the distance (in km or in miles) between two points on Earth,
located by their latitude and longitude.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
cat > tox.ini <<'EOF'
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc README.md
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Mon Jan 17 2022 Stanislav Levin <slev@altlinux.org> 2.5.1-alt1
- 0.4.5 -> 2.5.1.

* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.5-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150615.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150615
- Version 0.4.2

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130720
- Initial build for Sisyphus

