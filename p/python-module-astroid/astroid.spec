%define _unpackaged_files_terminate_build 1
%define oname astroid

%def_with check

Name: python-module-%oname
Version: 1.6.4
Release: alt1%ubt

Summary: Python Abstract Syntax Tree New Generation
License: LGPLv2.1+
Group: Development/Python
# Source-git: https://github.com/PyCQA/astroid.git
Url: https://pypi.org/project/astroid

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-ubt
BuildRequires(pre): rpm-build-python3

BuildRequires: python-module-setuptools
BuildRequires: python-module-pytest-runner
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pytest-runner

%if_with check
BuildRequires: python3-module-tox
BuildRequires: python3-module-lazy_object_proxy
BuildRequires: python3-module-coverage
BuildRequires: python3-module-pytest
BuildRequires: python3-module-wrapt
BuildRequires: python3-module-nose
BuildRequires: python3-module-numpy
BuildRequires: python3-module-dateutil
%endif

BuildArch: noarch

Provides: python-module-logilab-astng = %EVR
Obsoletes: python-module-logilab-astng <= 0.24.2

%py_requires backports.functools_lru_cache
%py_requires enum34
%py_requires singledispatch

%description
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentialy governed by
pylint's needs.
It extends class defined in the compiler.ast [1] module (python <= 2.4)
or in the builtin _ast module (python >= 2.5) with some additional
methods and attributes. Instance attributes are added by a builder
object, which can either generate extended ast (let's call them astng ;)
by visiting an existant ast tree or by inspecting living object. Methods
are added by monkey patching ast classes.

%package -n python3-module-%oname
Summary: Python 3 Abstract Syntax Tree New Generation
Group: Development/Python3

Provides: python3-module-logilab-astng = %EVR
Obsoletes: python3-module-logilab-astng <= 0.24.2

%description -n python3-module-%oname
The aim of this module is to provide a common base representation of
python source code for projects such as pychecker, pyreverse, pylint...
Well, actually the development of this library is essentialy governed by
pylint's needs.
It extends class defined in the compiler.ast [1] module (python <= 2.4)
or in the builtin _ast module (python >= 2.5) with some additional
methods and attributes. Instance attributes are added by a builder
object, which can either generate extended ast (let's call them astng ;)
by visiting an existant ast tree or by inspecting living object. Methods
are added by monkey patching ast classes.

%prep
%setup
%patch0 -p1
# python attr module is not packaged
sed -i '/[[:space:]]*attr\([[:space:]]\|$\)/d;
       s/python -Wi {envsitepackagesdir}\/coverage/python -m coverage/g' tox.ini
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
%define python_version_nodots() %(%1 -Esc "import sys; sys.stdout.write('{0.major}{0.minor}'.format(sys.version_info))")
export PIP_INDEX_URL=http://host.invalid./

# python 2.7 tests are not supported more

pushd ../python3
tox.py3 --sitepackages -e py%{python_version_nodots python3} -v -- -v
popd

%files
%doc ChangeLog README.rst
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%oname/test*

%files -n python3-module-%oname
%doc ChangeLog README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/%oname/*/test*
%exclude %python3_sitelibdir/%oname/test*

%changelog
* Fri May 25 2018 Stanislav Levin <slev@altlinux.org> 1.6.4-alt1%ubt
- 1.5.3 -> 1.6.4

* Fri Oct 20 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.3-alt3
- Updated runtime dependencies.

* Thu Aug 17 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.3-alt2
- Fixed build.

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5.3-alt1
- Updated to upstream version 1.5.3.

* Mon Mar 14 2016 Denis Medvedev <nbr@altlinux.org> 1.4.4-alt1
- Upstream switched to git. New version 1.4.4

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.3.8-alt1.1
- NMU: Use buildreq for BR.

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.8-alt1
- Version 1.3.8

* Thu Dec 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2 (ALT #30535)

* Wed Mar 19 2014 Timur Aitov <timonbl4@altlinux.org> 1.0.1-alt1
- Version 1.0.1

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.24.2-alt1.hg20130227
- Version 0.24.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.23.1-alt1.hg20120119.1
- Rebuild with Python-3.3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.1-alt1.hg20120119
- Version 0.23.1
- Added module for Python 3

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.23.0-alt1
- Version 0.23.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.20.3-alt1.1
- Rebuild with Python-2.7

* Wed Sep 29 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.20.3-alt1
- 0.20.3

* Mon Sep 13 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.20.2-alt1
- 0.20.2

* Mon Sep 06 2010 Andrey Rahmatullin <wrar@altlinux.org> 0.20.1-alt2
- run tests

* Fri May 14 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.20.1-alt1
- 0.20.1

* Fri Mar 26 2010 Andrey Rahmatullin <wrar@altlinux.ru> 0.20.0-alt1
- 0.20.0

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.3-alt1
- 0.19.3

* Fri Dec 18 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.2-alt1
- 0.19.2

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19.1-alt1.1
- Rebuilt with python 2.6

* Fri Sep 04 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.1-alt1
- 0.19.1

* Thu Mar 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.19.0-alt1
- 0.19.0

* Sun Mar 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.18.0-alt1
- 0.18.0

* Sun Feb 22 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.4-alt2
- use %%python_{build,install}

* Tue Dec 02 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.4-alt1
- 0.17.4

* Sun Oct 12 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.17.3-alt1
- 0.17.3
- spec cleanup
- probably fix automatic dependency search
- don't package tests

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.16.3-alt1.1
- Rebuilt with python-2.5.

* Wed Dec 6 2006 Andrey Khavryuchenko <akhavr@altlinux.org> 0.16.3-alt1
- Initial build for ALT Linux
