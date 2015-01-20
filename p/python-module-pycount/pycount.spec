%define oname pycount

%def_with python3

Name: python-module-%oname
Version: 0.6.2
Release: alt1.git20150120
Summary: A simple python LOC count tool
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/pycount/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/tsaulic/pycount.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-binaryornot python-module-pygal
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-binaryornot python3-module-pygal
%endif

%py_provides %oname
%py_requires binaryornot pygal

%description
* experimental LOC tool (lines of code, a.k.a. SLOC)
* doing this for python learning purposes and general OO practicing as
  I'm a newbie
* feel free to raise issues if you find something unusual (the
  likelyhood of someone even looking at this is very close to zero, so
  I'm not expecting anything :D)

%package -n python3-module-%oname
Summary: A simple python LOC count tool
Group: Development/Python3
%py3_provides %oname
%py3_requires binaryornot pygal

%description -n python3-module-%oname
* experimental LOC tool (lines of code, a.k.a. SLOC)
* doing this for python learning purposes and general OO practicing as
  I'm a newbie
* feel free to raise issues if you find something unusual (the
  likelyhood of someone even looking at this is very close to zero, so
  I'm not expecting anything :D)

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
export PATH=$PATH:%buildroot%_bindir
python setup.py test
export PYTHONPATH=$PWD
%oname
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
%oname.py3
popd
%endif

%files
%doc LICENSE *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc LICENSE *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.2-alt1.git20150120
- Version 0.6.2

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1.git20150119
- Version 0.6.1

* Fri Jan 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt1.git20150116
- Initial build for Sisyphus

