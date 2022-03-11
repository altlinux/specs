%define _unpackaged_files_terminate_build 1
%define oname moto

%def_with check
# full testsuite takes too long for now, run it locally
# name                      aarch64   armh   i586  ppc64le  x86_64
# python3-module-moto         20:32  35:22  12:18    25:10   12:09
%def_without full_testsuite

Name: python3-module-%oname
Version: 3.0.7
Release: alt1

Summary: A library that allows your python tests to easily mock out the boto library
License: Apache-2.0
Group: Development/Python3
Url: https://pypi.org/project/moto/

BuildArch: noarch

# https://github.com/spulec/moto.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(boto3)
BuildRequires: python3(botocore)
BuildRequires: python3(cryptography)
BuildRequires: python3(requests)
BuildRequires: python3(xmltodict)
BuildRequires: python3(werkzeug)
BuildRequires: python3(pytz)
BuildRequires: python3(dateutil)
BuildRequires: python3(responses)
BuildRequires: python3(jinja2)

BuildRequires: python3(sure)
BuildRequires: python3(freezegun)
BuildRequires: python3(flask)
BuildRequires: python3(flask_cors)
BuildRequires: python3(jose)
BuildRequires: python3(aws_xray_sdk)
BuildRequires: python3(yaml)
BuildRequires: python3(jsondiff)
BuildRequires: python3(docker)

BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

# not detected external dep
%py3_requires responses

%description
Moto is a library that allows your python tests to easily mock out the
boto library.

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
    pytest {posargs:-vra}
EOF
export PIP_NO_BUILD_ISOLATION=no
export PIP_NO_INDEX=YES
export NO_INTERNET=YES
export NO_DOCKERD=YES
export TOXENV=py3
export TOX_TESTENV_PASSENV='NO_INTERNET NO_DOCKERD'
%if_with full_testsuite
export TESTS=tests
%else
export TESTS=tests/test_core
%endif
# test_batch_jobs requires internet
tox.py3 --sitepackages --console-scripts -vvr -s false --develop -- \
    -vra $TESTS \
    -m 'not network' \
    --ignore tests/test_batch/test_batch_jobs.py

%files
%doc LICENSE
%doc *.md
%_bindir/moto_server
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py*.egg-info

%changelog
* Wed Mar 09 2022 Stanislav Levin <slev@altlinux.org> 3.0.7-alt1
- 3.0.5 -> 3.0.7.

* Sat Mar 05 2022 Stanislav Levin <slev@altlinux.org> 3.0.5-alt1
- 1.3.16 -> 3.0.5.

* Fri Oct 23 2020 Stanislav Levin <slev@altlinux.org> 1.3.16-alt1
- 1.3.15 -> 1.3.16.

* Tue Sep 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.15-alt1
- Updated to upstream version 1.3.15.

* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.10-alt2
- python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.4.10-alt1.git20150808.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.10-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.10-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sun Aug 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.10-alt1.git20150808
- Version 0.4.10

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.7-alt1.git20150722
- Version 0.4.7

* Tue Feb 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150222
- Version 0.4.1

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git201500203
- Version 0.4.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.9-alt1.git20150117
- Initial build for Sisyphus

