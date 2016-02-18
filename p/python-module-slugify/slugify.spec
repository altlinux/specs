%define oname slugify

%def_with python3

Name: python-module-%oname
Version: 0.1.0
Release: alt1.git20141016.1
Summary: Returns a unicode slugs
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-slugify/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/un33k/python-slugify.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-unidecode python-tools-pep8
#BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-unidecode python3-tools-pep8
#BuildPreReq: python3-module-nose python-tools-2to3
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: python-module-nose python-module-pytest python-module-unidecode python-tools-pep8 python3-module-nose python3-module-unidecode python3-tools-pep8 rpm-build-python3 time

%description
A Python Slugify application that handles Unicode.

%package -n python3-module-%oname
Summary: Returns a unicode slugs
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Python Slugify application that handles Unicode.

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|pep8|python3-pep8|g' ../python3/pep8.sh
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
nosetests
./pep8.sh
%if_with python3
pushd ../python3
nosetests3
./pep8.sh
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.0-alt1.git20141016.1
- NMU: Use buildreq for BR.

* Thu Oct 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.git20141016
- Initial build for Sisyphus

