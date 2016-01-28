%define oname netCDF4

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.1.9
Release: alt1.git20150728.1
Summary: Python/numpy interface to netCDF library (versions 3 and 4)
License: BSD / MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/netCDF4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Unidata/netcdf4-python.git
Source: %name-%version.tar
Source1: setup.cfg

#BuildPreReq: libnetcdf-devel zlib-devel libjpeg-devel libcurl-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
#BuildPreReq: python-module-epydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libhdf5-8-seq libhdf5-devel libnetcdf7-seq python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: libnetcdf-devel libnumpy-devel python-module-Cython python-module-epydoc python-module-html5lib python-module-notebook python-module-numpy-testing python-module-pytest python3-module-Cython python3-module-html5lib python3-module-notebook python3-module-numpy-testing rpm-build-python3 time

%description
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

This package contains documentation for %oname.

%package -n python3-module-%oname
Summary: Python/numpy interface to netCDF library (versions 3 and 4)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
netCDF version 4 has many features not found in earlier versions of the
library and is implemented on top of HDF5. This module can read and
write files in both the new netCDF 4 and the old netCDF 3 format, and
can create files that are readable by HDF5 clients. The API modelled
after Scientific.IO.NetCDF, and should be familiar to users of that
module.

Most new features of netCDF 4 are implemented, such as multiple
unlimited dimensions, groups and zlib data compression. All the new
numeric data types (such as 64 bit and unsigned integer types) are
implemented. Compound and variable length (vlen) data types are
supported, but the enum and opaque data types are not. Mixtures of
compound and vlen data types (compound types containing vlens, and vlens
containing compound types) are not supported.

%prep
%setup

install -m644 %SOURCE1 ./
rm -f *.c netCDF4.c netcdftime/.c

%ifarch x86_64
sed -i "s|'lib'|'lib64'|g" setup.py
%endif

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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

export PYTHONPATH=%buildroot%python_sitelibdir
chmod +x create_docs.sh
cd docs
../create_docs.sh

%check
python setup.py test
pushd test
export PYTHONPATH=%buildroot%python_sitelibdir
python run_all.py
popd
%if_with python3
pushd ../python3
python3 setup.py test
pushd test
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 run_all.py
popd
popd
%endif

%files
%doc Changelog *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%files docs
%doc docs/html examples

%if_with python3
%files -n python3-module-%oname
%doc Changelog *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.9-alt1.git20150728.1
- NMU: Use buildreq for BR.

* Sun Aug 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.git20150728
- New snapshot

* Mon Jul 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.9-alt1.git20150722
- Version 1.1.9

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.8-alt1.git20150416
- Version 1.1.8

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.5-alt1.git20150303
- Version 1.1.5

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.git20141218
- Version 1.1.3

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.2-alt1.git20141116
- Initial build for Sisyphus

