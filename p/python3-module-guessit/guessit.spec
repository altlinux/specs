%define _unpackaged_files_terminate_build 1
%define oname guessit

%def_with check

Name: python3-module-%oname
Version: 3.4.3
Release: alt1

Summary: GuessIt - a library for guessing information from video files

License: LGPLv3
Group: Development/Python3
Url: https://pypi.org/project/guessit/

# https://github.com/guessit-io/guessit.git
Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
# install_requires=
BuildRequires: python3(rebulk)
BuildRequires: python3(babelfish)
BuildRequires: python3(dateutil)

BuildRequires: python3(yaml)
BuildRequires: python3(pytest)
BuildRequires: python3(pytest_mock)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
GuessIt is a python library that extracts as much information as
possible from a video file.

It has a very powerful filename matcher that allows to guess a lot of
metadata from a video using its filename only. This matcher works with
both movies and tv shows episodes.

%prep
%setup
%autopatch -p1

# remove mimetypes from test data, see https://github.com/guessit-io/guessit/pull/515
# TODO: consider removing following line on next release after 2.1.4
sed -i -e '/mimetype:/d' guessit/test/*.yml

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
%doc *.md
%_bindir/guessit
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%exclude %python3_sitelibdir/*/test/

%changelog
* Wed Feb 09 2022 Stanislav Levin <slev@altlinux.org> 3.4.3-alt1
- 3.3.1 -> 3.4.3.

* Sat Aug 14 2021 Vitaly Lipatov <lav@altlinux.ru> 3.3.1-alt2
- drop unused BR

* Wed Jun 09 2021 Grigory Ustinov <grenka@altlinux.org> 3.3.1-alt1
- Automatically updated to 3.3.1.
- Build without docs (upstream removed them).

* Tue Oct 20 2020 Stanislav Levin <slev@altlinux.org> 3.1.1-alt2
- Dropped buildtime dependency on pytest_capturelog.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 3.1.1-alt1
- Automatically updated to 3.1.1.

* Wed Nov 13 2019 Grigory Ustinov <grenka@altlinux.org> 3.1.0-alt1
- New version 3.1.0.
- Build without python2.

* Wed Aug 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 3.0.0-alt1
- Updated to upstream version 3.0.0.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.1.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.1.4-alt1
- Updated to upstream version 2.1.4.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.10.4-alt1.dev0.git20150427.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.10.4-alt1.dev0.git20150427.1
- NMU: Use buildreq for BR.

* Wed Apr 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.4-alt1.dev0.git20150427
- Version 0.10.4.dev0

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.5-alt1.dev0.git20141110
- Version 0.9.5.dev0

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.dev0.git20141009
- Initial build for Sisyphus

