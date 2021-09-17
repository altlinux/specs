%define _unpackaged_files_terminate_build 1
%define oname tempita

%def_with check

Name: python3-module-%oname
Version: 0.5.3
Release: alt2.hg20131219.3
Summary: A very small text templating language
License: MIT
Group: Development/Python3
Url: http://pythonpaste.org/tempita/
BuildArch: noarch

# hg clone http://bitbucket.org/ianb/tempita
Source: Tempita-%version.tar.gz
Patch0: tempita-0.5.3-Drop-dynamic-conversion-with-2to3.patch
Patch1: tempita-0.5.3-Migrate-from-cgi.escape.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%if_with check
BuildRequires: python3(pytest)
BuildRequires: python3(tox)
BuildRequires: python3(tox_console_scripts)
%endif

%description
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
``string.Template`` or ``%%`` substitution.  It's small, it embeds
Python in strings, and it doesn't do much else.

%prep
%setup
%autopatch -p1

# remove snapshot tag
sed -i \
    -e 's/^tag_build[[:space:]]*=.*$/tag_build =/' \
    -e 's/^tag_date[[:space:]]*=.*$/tag_date =/' \
    -e 's/^tag_svn_revision[[:space:]]*=.*$/tag_svn_revision =/' \
setup.cfg

%build
find -type f -exec sed -i 's|%_bindir/python|%_bindir/python3|' -- '{}' +
find -type f -exec sed -i 's|%_bindir/env python|%_bindir/python3|' -- '{}' +
%python3_build

%install
%python3_install

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    pytest {posargs:-vra} tests
EOF
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages --console-scripts -vvr -s false

%files
%doc docs/*
%python3_sitelibdir/%oname/
%python3_sitelibdir/Tempita-%version-py%_python3_version.egg-info/

%changelog
* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 0.5.3-alt2.hg20131219.3
- Fixed FTBFS (setuptools 58).

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.5.3-alt1.hg20131219.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.3-alt1.hg20131219.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt1.hg20131219.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1.hg20131219.1
- NMU: Use buildreq for BR.

* Thu Jan 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.hg20131219
- Version 0.5.3

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.5.1-alt2.hg20110828.1
- Rebuild with Python-3.3

* Sat May 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt2.hg20110828
- Added module for Python 3

* Thu Dec 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.hg20110828
- Version 0.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5-alt1.hg20101221.1
- Rebuild with Python-2.7

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.hg20101221
- New snapshot

* Fri Nov 19 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.hg20100914
- Version 0.5

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.svn20090420.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.svn20090420
- Initial build for Sisyphus

