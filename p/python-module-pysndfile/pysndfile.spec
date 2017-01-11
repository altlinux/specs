%define _unpackaged_files_terminate_build 1
%define oname pysndfile

%def_with python3

Name: python-module-%oname
Version: 0.2.11
Release: alt1
Summary: Cython wrapper class for reading/writing soundfiles using libsndfile
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pysndfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/88/63/a874ab001fa26dcf5dfbd382210f78ad0f99194fb09b06e23d91204207ec/%{oname}-%{version}.tar.gz

#BuildPreReq: gcc-c++ clang-devel libsndfile-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Cython libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Cython libnumpy-py3-devel
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 llvm python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: clang libnumpy-devel libsndfile-devel libstdc++-devel python-module-Cython python-module-html5lib python-module-notebook python-module-numpy-testing python-module-setuptools-tests python3-module-Cython python3-module-html5lib python3-module-notebook python3-module-numpy-testing python3-module-setuptools-tests rpm-build-python3

%description
pysndfile is a python package providing PySndfile, a Cython wrapper
class around libsndfile. PySndfile provides methods for reading and
writing a large variety of soundfile formats on a variety of plattforms.
PySndfile provides a rather complete access to the different sound file
manipulation options that are available in libsndfile.

Due to the use of libsndfile nearly all sound file formats, (besides mp3
and derived formats) can be read and written with PySndfile.

%package -n python3-module-%oname
Summary: Cython wrapper class for reading/writing soundfiles using libsndfile
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
pysndfile is a python package providing PySndfile, a Cython wrapper
class around libsndfile. PySndfile provides methods for reading and
writing a large variety of soundfile formats on a variety of plattforms.
PySndfile provides a rather complete access to the different sound file
manipulation options that are available in libsndfile.

Due to the use of libsndfile nearly all sound file formats, (besides mp3
and derived formats) can be read and written with PySndfile.

%prep
%setup -q -n %{oname}-%{version}

rm -f *.cpp

%if_with python3
cp -fR . ../python3
%endif

%build
export CC=clang
export CXX=clang++
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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc ChangeLog README.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.11-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.10-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.10-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.10-alt1
- Initial build for Sisyphus

