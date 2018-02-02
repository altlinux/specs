%define oname scour

%def_with python3

Name: python-module-%oname
Version: 0.29
Release: alt1.git20140726.1.1.1
Summary: Scour SVG Optimizer
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/scour/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/oberstet/scour.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
Scour is a SVG optimizer/sanitizer that can be used to produce SVGs for
Web deployment.

%package -n python3-module-%oname
Summary: Scour SVG Optimizer
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Scour is a SVG optimizer/sanitizer that can be used to produce SVGs for
Web deployment.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.29-alt1.git20140726.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.29-alt1.git20140726.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.29-alt1.git20140726.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.29-alt1.git20140726
- Initial build for Sisyphus

