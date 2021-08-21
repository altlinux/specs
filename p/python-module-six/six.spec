%define _unpackaged_files_terminate_build 1
%define oname six

%def_with check

Name: python-module-%oname
Version: 1.16.0
Release: alt1

Summary: Python 2 and 3 compatibility utilities
License: MIT
Group: Development/Python

BuildArch: noarch
Url: http://pypi.python.org/pypi/six

# Url: https://github.com/benjaminp/six
Source: %name-%version.tar
Source2: move.list

%define move_list %(echo `cat %{SOURCE2}`)

%py_provides %move_list

BuildRequires(pre): rpm-build-python3

# for test suite
%if_with check
BuildRequires: python3-modules-tkinter
BuildRequires: python3-module-tox
%endif

%description
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions. See the documentation for more information on what is
provided.

%package -n python3-module-%oname
Summary: Python 2 and 3 compatibility utilities
Group: Development/Python3
%py3_provides %move_list

%description -n python3-module-%oname
Six is a Python 2 and 3 compatibility library. It provides utility
functions for smoothing over the differences between the Python versions
with the goal of writing Python code that is compatible on both Python
versions. See the documentation for more information on what is
provided.

%prep
%setup

rm -rf ../python3
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
# check actual state of things regarding to provides
set -o pipefail
PYTHONPATH="$(pwd)" python3 -c "import six;assert six.__version__==\"%version\";modules=six._importer.known_modules.keys();print(*modules, sep='\n')" | sort > move.actual.list
set +o pipefail
cat %SOURCE2 | sort > move.expected.list
diff -y move.expected.list move.actual.list

%check
export PIP_NO_INDEX=YES
export TOXENV=py3
tox.py3 --sitepackages -vvr -s false

%files
%doc README.rst documentation/index.rst
%python_sitelibdir/six.py*
%python_sitelibdir/%oname-%version-py%_python_version.egg-info/

%files -n python3-module-%oname
%doc README.rst documentation/index.rst
%python3_sitelibdir/six.py
%python3_sitelibdir/__pycache__/
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/

%changelog
* Fri Aug 20 2021 Stanislav Levin <slev@altlinux.org> 1.16.0-alt1
- 1.15.0 -> 1.16.0 (closes: #40787).

* Tue Apr 27 2021 Stanislav Levin <slev@altlinux.org> 1.15.0-alt2
- Disabled testing for Python2.

* Mon Aug 03 2020 Stanislav Levin <slev@altlinux.org> 1.15.0-alt1
- 1.14.0 -> 1.15.0.

* Tue May 12 2020 Stanislav Levin <slev@altlinux.org> 1.14.0-alt1
- 1.13.0 -> 1.14.0.

* Mon Nov 11 2019 Stanislav Levin <slev@altlinux.org> 1.13.0-alt1
- 1.12.0 -> 1.13.0.

* Sat Jan 20 2019 Stanislav Levin <slev@altlinux.org> 1.12.0-alt1
- 1.11.0 -> 1.12.0.

* Wed Aug 29 2018 Stanislav Levin <slev@altlinux.org> 1.11.0-alt2
- Fix build with new pytest-3.7.

* Fri May 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.11.0-alt1
- Updated to upstream version 1.11.0.

* Mon May 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.10.0-alt9
- Add unquote_to_bytes to moved urllib.parse.
- Adapt tests for python 3.6.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.10.0-alt8.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
- Enable tests at Build time

* Fri Jun 16 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt8
- add six.moves.urllib_parse and six.moves.urllib_error to provides

* Mon May 29 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt7
- update provides from documentation

* Fri May 26 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt6
- add python3 provides six.moves.urllib_robotparser, six.moves.xmlrpc_client, six.moves.xmlrpc_server

* Thu Apr 13 2017 Anton Midyukov <antohami@altlinux.org> 1.10.0-alt5
- enable check
- add python3 provides six.moves.urllib.response, six.moves.urllib.error, six.moves.urllib.robotparser

* Wed Mar 01 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt4
- fix python3 provides

* Mon Feb 27 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt3
- update BR:, fix upgrade package (ALT #33167)

* Wed Feb 22 2017 Alexey Shabalin <shaba@altlinux.ru> 1.10.0-alt2
- add python3 provides six.moves, six.moves.urllib, six.moves.urllib.parse

* Tue Jan 03 2017 Anton Midyukov <antohami@altlinux.org> 1.10.0-alt1
- New version 1.10.0

* Mon Jan 02 2017 Michael Shigorin <mike@altlinux.org> 1.9.0-alt1.hg20150430.1.2
- BOOTSTRAP: avoid python-module-setuptools-tests if skipping %%check

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.hg20150430.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.9.0-alt1.hg20150430.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.hg20150430
- New snapshot

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.hg20150105
- Version 1.9.0

* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.hg20141209
- New snapshot
- Added chr (ALT #30557)

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.0-alt1.hg20141030
- Version 1.8.0

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.3-alt1.hg20140713
- Version 1.7.3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1
- Version 1.4.1

* Wed Mar 06 2013 Aleksey Avdeev <solo@altlinux.ru> 1.2.0-alt1
- Version 1.2.0

* Mon Apr 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added module for Python 3

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

