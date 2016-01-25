%define oname pycosat

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.6.1
Release: alt3.git20140610
Summary: Bindings to picosat (a SAT solver)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pycosat/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ContinuumIO/pycosat.git
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests libpicosat-devel
BuildRequires: libpicosat-devel python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
BuildRequires: python3-dev
%endif

%py_provides %oname

%description
PicoSAT is a popular SAT solver written by Armin Biere in pure C. This
package provides efficient Python bindings to picosat on the C level,
i.e. when importing pycosat, the picosat solver becomes part of the
Python process itself. For ease of deployment, the picosat source
(namely picosat.c and picosat.h) is included in this project. These
files have been extracted from the picosat source (picosat-954.tar.gz).

%package -n python3-module-%oname
Summary: Bindings to picosat (a SAT solver)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PicoSAT is a popular SAT solver written by Armin Biere in pure C. This
package provides efficient Python bindings to picosat on the C level,
i.e. when importing pycosat, the picosat solver becomes part of the
Python process itself. For ease of deployment, the picosat source
(namely picosat.c and picosat.h) is included in this project. These
files have been extracted from the picosat source (picosat-954.tar.gz).

%prep
%setup

rm -f picosat.*

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing -DDONT_INCLUDE_PICOSAT
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
export PYTHONPATH=%buildroot%python_sitelibdir
rm -fR build
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
rm -fR build
py.test-%_python3_version
popd
%endif

%files
%doc CHANGELOG *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/test*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/test*
%exclude %python3_sitelibdir/*/test*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.6.1-alt3.git20140610
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2.git20140610
- Built with external PicoSAT

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20140610
- Initial build for Sisyphus

