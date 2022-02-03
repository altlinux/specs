%define _unpackaged_files_terminate_build 1
%define modulename FormEncode

%def_with check

Name: python3-module-%modulename
Version: 2.0.1
Release: alt1
Epoch: 1

Summary: HTML form validation, generation, and convertion package for Python
License: MIT
Group: Development/Python3

URL: http://formencode.org
BuildArch: noarch

# git://github.com/formencode/formencode.git
Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools_scm)
BuildRequires: python3(setuptools_scm_git_archive)

%if_with check
# install_requires=
BuildRequires: python3(six)

BuildRequires: python3(dns)
BuildRequires: python3(pytest)
BuildRequires: python3(pycountry)
BuildRequires: python3(tox)
BuildRequires: python3(tox_no_deps)
BuildRequires: python3(tox_console_scripts)
%endif

%description
FormEncode validates and converts nested structures. It allows for
a declarative form of defining the validation, and decoupled processes
for filling and generating forms.

%prep
%setup
%autopatch -p1

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python3_install

# don't ship tests
rm -r %buildroot/%python3_sitelibdir/formencode/tests/

%check
cat > tox.ini <<EOF
[testenv]
usedevelop=True
commands =
    {envbindir}/pytest {posargs:-vra}
EOF
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
export PIP_NO_INDEX=YES
export TOXENV=py3

# test_unicode_ascii_subgroup requires internet
tox.py3 --sitepackages --console-scripts --no-deps -vvr -s false -- \
-k 'not test_unicode_ascii_subgroup'

%files
%doc README.rst
%python3_sitelibdir/formencode/
%python3_sitelibdir/%modulename-%version-py%_python3_version.egg-info/

%changelog
* Thu Feb 03 2022 Stanislav Levin <slev@altlinux.org> 1:2.0.1-alt1
- 2.0.0 -> 2.0.1.

* Fri Sep 17 2021 Stanislav Levin <slev@altlinux.org> 1:2.0.0-alt1
- 1.3.1 -> 2.0.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 1:1.3.1-alt2
- Drop python2 support.

* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 1:1.3.1-alt1
- Version updated to 1.3.1

* Wed Feb 27 2019 Michael Shigorin <mike@altlinux.org> 1:1.3.0-alt1.git20150207.1.3
- introduce doc knob (on by default)

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.3.0-alt1.git20150207.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.3.0-alt1.git20150207.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1:1.3.0-alt1.git20150207.1
- NMU: Use buildreq for BR.

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20150207
- 1.3.0 released

* Thu Mar 21 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.3.0-alt1.git20130312
- New snapshot
- Added module for Python 3

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.0-alt1.git20130201
- Version 1.3.0

* Fri Sep 21 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.2.4-alt1.git20120914
- New snapshot

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.4-alt1.hg20110930
- Version 1.2.4

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.3-alt2.hg20100922.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt2.hg20100922
- New snapshot (svn -> hg)

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.3-alt1.svn20100511
- Version 1.2.3

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt2
- Rebuilt with python 2.6

* Sat Apr 04 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 1.2.2-alt1
- 1.2.2

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.4-alt2.1.0.1
- Rebuilt with python-2.5.

* Sun Mar 25 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.4-alt2.1.0
- Rebuilt with rpm-build-python-0.30-alt3.

* Thu Mar 02 2006 Maxim Bodyansky <maximbo@altlinux.ru> 0.4-alt2.1
- add_python_req_skip dispatch sqlobject pkg_resources

* Thu Nov 24 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.4-alt2
- new upstream's version

* Sun Nov 06 2005 Maxim Bodyansky <maximbo@altlinux.ru> 0.2.2-alt1
- Initial build for Sisyphus
