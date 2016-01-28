%define oname msgpack

%def_with python3

Name: python-module-%oname
Version: 0.4.6
Release: alt1.git20150323.1

Summary: A Python MessagePack (de)serializer

Group: Development/Python
License: ASL 2.0
URL: http://pypi.python.org/pypi/msgpack-python/

# https://github.com/msgpack/msgpack-python.git
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils ipython ipython3 libstdc++-devel python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-coverage python-module-cryptography python-module-cssselect python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-matplotlib python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-pexpect python-module-ptyprocess python-module-pyasn1 python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytz python-module-setuptools python-module-snowballstemmer python-module-sphinx python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-cffi python3-module-chardet python3-module-coverage python3-module-cssselect python3-module-docutils python3-module-future python3-module-genshi python3-module-greenlet python3-module-ipykernel python3-module-ipyparallel python3-module-ipython_genutils python3-module-jinja2 python3-module-jsonschema python3-module-jupyter_client python3-module-jupyter_core python3-module-matplotlib python3-module-nbconvert python3-module-nbformat python3-module-numpy python3-module-pexpect python3-module-ptyprocess python3-module-pycares python3-module-pycparser python3-module-pygobject3 python3-module-pyparsing python3-module-pytz python3-module-setuptools python3-module-snowballstemmer python3-module-sphinx python3-module-terminado python3-module-tornado_xstatic python3-module-traitlets python3-module-xstatic python3-module-xstatic-term.js python3-module-yieldfrom.http.client python3-module-yieldfrom.requests python3-module-yieldfrom.urllib3 python3-module-zmq python3-module-zope python3-module-zope.interface
BuildRequires: gcc-c++ python-module-Cython python-module-html5lib python-module-nose python-module-notebook python3-module-Cython python3-module-html5lib python3-module-nose python3-module-notebook rpm-build-python3

#BuildRequires: python-module-distribute python-module-Cython python-module-nose
#BuildPreReq: gcc-c++

%description
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python (de)serializer for MessagePack.

%if_with python3
%package -n python3-module-%oname
Group: Development/Python3
Summary: A Python3 MessagePack (de)serializer
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute python3-module-Cython python3-module-nose

%description -n python3-module-%oname
MessagePack is a binary-based efficient data interchange format that is
focused on high performance. It is like JSON, but very fast and small.
This is a Python3 (de)serializer for MessagePack.
%endif

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build
%if_with python3
pushd ../python3
%python3_build
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
%if_with python3
pushd ../python3
popd
%endif

%files
%doc COPYING
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.6-alt1.git20150323.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6-alt1.git20150323
- Version 0.4.6

* Mon Jan 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.git20150126
- Version 0.4.5

* Sun Jan 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20140326
- Version 0.4.2

* Tue Mar 26 2013 Aleksey Avdeev <solo@altlinux.ru> 0.2.2-alt1.1
- Rebuild with Python-3.3

* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 0.2.2-alt1
- New version

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.12-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Fri Feb 10 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.12-alt1
- initial
