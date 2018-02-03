%define oname html5print

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20161101.1.1

Summary: HTML5, CSS, Javascript Pretty Print

License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/html5print/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-git: https://github.com/berniey/html5print.git
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: python-module-chardet python-module-html5lib python-module-ndg-httpsclient python-module-ntlm python-module-setuptools python-module-slimit

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-BeautifulSoup4 python-module-chardet
#BuildPreReq: python-module-html5lib python-module-requests
#BuildPreReq: python-module-slimit python-module-tinycss2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-BeautifulSoup4 python3-module-chardet
#BuildPreReq: python3-module-html5lib python3-module-requests
#BuildPreReq: python3-module-slimit python3-module-tinycss2
BuildRequires: python3-module-chardet python3-module-html5lib python3-module-setuptools python3-module-slimit python3-module-urllib3
%endif

%py_provides %oname
#%py_requires bs4 chardet html5lib requests slimit tinycss2

%description
This tool pretty print your HTML, CSS and JavaScript file. The package
comes with two parts:

* a command line tool, html5-print
* a python module, html5print

%package -n python3-module-%oname
Summary: HTML5, CSS, Javascript Pretty Print
Group: Development/Python3
%py3_provides %oname
#%py3_requires bs4 chardet html5lib requests slimit tinycss2

%description -n python3-module-%oname
This tool pretty print your HTML, CSS and JavaScript file. The package
comes with two parts:

* a command line tool, html5-print
* a python module, html5print

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/*.rst
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.2-alt1.git20161101.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 26 2017 Vitaly Lipatov <lav@altlinux.ru> 0.1.2-alt1.git20161101.1
- build latest code from 489e8b6046a7332405d4d8025c783018f5025faf commit

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.git20140927.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.1-alt2.git20140927
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140927
- Initial build for Sisyphus

