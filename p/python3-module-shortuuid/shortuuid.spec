%define _unpackaged_files_terminate_build 1
%define oname shortuuid

%def_with check

Name: python3-module-%oname
Version: 1.0.8
Release: alt1

Summary: A generator library for concise, unambiguous and URL-safe UUIDs

License: BSD
Group: Development/Python3
Url: https://pypi.org/project/shortuuid/

# Source-url: https://github.com/skorokithakis/shortuuid.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

BuildArch: noarch

%if_with check
BuildRequires: python3(tox)
%endif

%description
A library that generates short, pretty, unambiguous unique IDs by using
an extensive, case-sensitive alphabet and omitting similar-looking
letters and numbers.

%prep
%setup

%build
%python3_build

%install
%python3_install
# strip tests
rm %buildroot%python3_sitelibdir/%oname/tests.py

%check
cat > tox.ini <<'EOF'
[testenv]
commands =
    python %oname/tests.py
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false --develop

%files
%doc README.md
%_bindir/%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Wed Mar 30 2022 Stanislav Levin <slev@altlinux.org> 1.0.8-alt1
- 1.0.0 -> 1.0.8.

* Fri Aug 06 2021 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version (1.0.0) with rpmgs script
- cleanup spec, disable packing tests

* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt2.git20140426.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2.git20140426
- Disabled test_pep8 (broken with new pep8)

* Mon Nov 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140426
- Initial build for Sisyphus

