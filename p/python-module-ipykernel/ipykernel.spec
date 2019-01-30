%define oname ipykernel

%def_with python3
#def_disable check
%def_with bootstrap

Name: python-module-%oname
Version: 4.6.1
Release: alt4
Summary: IPython Kernel for Jupyter
License: BSD
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/ipykernel

Source: %name-%version.tar
Patch1: ipykernel-4.6.1-update-use-of-tornado-current.patch
Patch2: ipykernel-4.6.1-only-enter-eventloop-when-there-is-one.patch
Patch3: ipykernel-4.6.1-run-pre-post-handler-hooks-around-eventloop-dispatch.patch

BuildRequires: python-module-html5lib python-module-ipyparallel python-module-mock python-module-nose python-module-numpy-testing
BuildRequires: python-module-pytest
BuildRequires: python-module-pathlib2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-html5lib python3-module-nose python3-module-notebook python3-module-numpy-testing python3-module-pbr
BuildRequires: python3-module-unittest2 python3-module-pytest
BuildRequires: python3-module-pathlib2
%endif

%py_provides %oname
%py_requires traitlets jupyter_client

%if_with bootstrap
%py_requires IPython
%endif


%description
This package provides the IPython kernel for Jupyter.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package provides the IPython kernel for Jupyter.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: IPython Kernel for Jupyter
Group: Development/Python3
%py3_provides %oname
%py3_requires traitlets jupyter_client

%if_with bootstrap
%py3_requires IPython
%endif

%add_python3_req_skip gtk

%description -n python3-module-%oname
This package provides the IPython kernel for Jupyter.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package provides the IPython kernel for Jupyter.

This package contains tests for %oname.
%endif

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
rm -fR build
PYTHONPATH=$(pwd) py.test -vv

%if_with python3
pushd ../python3
rm -fR build
PYTHONPATH=$(pwd) py.test3 -vv
popd
%endif

%files
%doc *.md examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.md examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Wed Jan 30 2019 Stanislav Levin <slev@altlinux.org> 4.6.1-alt4
- Fixed testing (applied upstream patches for support for tornado5,
  closes: #35981).

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.6.1-alt3.1
- rebuild with all requires

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 4.6.1-alt3
- rebuild with python3.6

* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.1-alt1
- Updated to upstream version 4.6.1.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.3-alt3
- Fixed build

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.3-alt2.1
- NMU: Use buildreq for BR.

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt2
- Enabled check

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Initial build for Sisyphus

