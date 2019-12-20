%define _unpackaged_files_terminate_build 1
%define mname martian

%def_without check

Name: python3-module-%mname
Version: 1.3
Release: alt1

Summary: A library to grok configuration from Python code
License: ZPLv2.1
Group: Development/Python3
# Source-git: https://github.com/zopefoundation/martian.git
Url: http://pypi.python.org/pypi/martian
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-zope.interface

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-virtualenv
BuildRequires: python3-module-zope.testing
BuildRequires: python3-module-zope.testrunner
BuildRequires: python3-module-coverage
%endif


%description
Martian is a library that allows the embedding of configuration
information in Python code. Martian can then grok the system and do the
appropriate configuration registrations. One example of a system that
uses Martian is the system where it originated: Grok
(http://grok.zope.org)

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
export PIP_INDEX_URL=http://host.invalid./

export PYTHONPATH=%buildroot%python3_sitelibdir_noarch:%python3_sitelibdir_noarch:%_libdir/python3/site-packages
TOX_TESTENV_PASSENV='PYTHONPATH' tox.py3 -e py%{python_version_nodots python3} -v

%files
%doc *.txt *.rst
%python3_sitelibdir/%mname
%python3_sitelibdir/%mname-%version-*.egg-info


%changelog
* Fri Dec 20 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt1
- Version updated to 1.3
- build for python2 disabled

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2
- NMU: remove %ubt from release

* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1%ubt
- Updated to upstream version 1.2.

* Wed Feb 14 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt2%ubt
- Fix BuildRequires to run tests

* Thu Jan 25 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1%ubt
- 0.14 -> 1.1

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.14-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt2
- Added necessary requirements

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14-alt1
- Initial build for Sisyphus

