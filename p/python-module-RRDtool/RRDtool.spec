%define oname RRDtool

%def_with python3

Name: python-module-%oname
Version: 0.1.12
Release: alt1.1
Summary: rrdtool bindings for Python
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/rrdtool/

# https://github.com/commx/python-rrdtool.git
Source: %name-%version.tar

BuildRequires: librrd-devel
BuildRequires: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
%endif

%py_provides %oname rrdtool
Conflicts: python-module-rrd python-module-rrdtool

%description
rrdtool binding for Python 2.6+ and 3.3+.

This bindings are based on the original Python rrdtool bindings from
Hye-Shik Chang and are slightly modified to support Python 3.3+ and 2.6+
in the same code base.

%if_with python3
%package -n python3-module-%oname
Summary: rrdtool bindings for Python
Group: Development/Python3
%py3_provides %oname rrdtool
Conflicts: python3-module-rrd python3-module-rrdtool

%description -n python3-module-%oname
rrdtool binding for Python 2.6+ and 3.3+.

This bindings are based on the original Python rrdtool bindings from
Hye-Shik Chang and are slightly modified to support Python 3.3+ and 2.6+
in the same code base.
%endif

%prep
%setup

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

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.12-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 18 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.12-alt1
- Updated to upstream version 0.1.12.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20141011.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 0.1.1-alt1.git20141011.1
- NMU: Use buildreq for BR.

* Sat Feb 07 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20141011
- Initial build for Sisyphus

