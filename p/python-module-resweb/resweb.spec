%define oname resweb

%def_with python3

Name: python-module-%oname
Version: 0.1.7
Release: alt1.git20130813.1
Summary: Pyres web interface
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/resweb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Pyres/resweb.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pyres python-module-flask
#BuildPreReq: python-module-setproctitle python-module-simplejson
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pyres python3-module-flask
#BuildPreReq: python3-module-setproctitle python3-module-simplejson
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-jinja2 python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-jinja2 python3-module-pytest python3-module-setuptools
BuildRequires: python-module-flask python-module-pyres python-module-setproctitle python-module-setuptools-tests python3-module-flask python3-module-pyres python3-module-setproctitle python3-module-setuptools-tests rpm-build-python3 time

%description
Resweb originally started as part of the pyres project. However, I
realized that for many reasons, both it and pyres would benefit from
being their own projects. Hopefully this will help the release schedule
of both pyres and resweb.

%package -n python3-module-%oname
Summary: Pyres web interface
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Resweb originally started as part of the pyres project. However, I
realized that for many reasons, both it and pyres would benefit from
being their own projects. Hopefully this will help the release schedule
of both pyres and resweb.

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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.7-alt1.git20130813.1
- NMU: Use buildreq for BR.

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.7-alt1.git20130813
- Initial build for Sisyphus

