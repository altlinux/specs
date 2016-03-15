%define oname spambayes

%def_with python3

Name: python-module-%oname
Version: 1.1b1
Release: alt2.1
Summary: Spam classification system
License: Python
Group: Development/Python
Url: http://pypi.python.org/pypi/spambayes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%add_python_req_skip pywintypes win32com

%description
The SpamBayes project is working on developing a statistical (commonly,
although a little inaccurately, referred to as Bayesian) anti-spam
filter, initially based on the work of Paul Graham. The major difference
between this and other, similar projects is the emphasis on testing
newer approaches to scoring messages. While most anti-spam projects are
still working with the original graham algorithm, we found that a number
of alternate methods yielded a more useful response.

%package -n python3-module-%oname
Summary: Spam classification system
Group: Development/Python3
%add_python3_req_skip pywintypes win32com

%description -n python3-module-%oname
The SpamBayes project is working on developing a statistical (commonly,
although a little inaccurately, referred to as Bayesian) anti-spam
filter, initially based on the work of Paul Graham. The major difference
between this and other, similar projects is the emphasis on testing
newer approaches to scoring messages. While most anti-spam projects are
still working with the original graham algorithm, we found that a number
of alternate methods yielded a more useful response.

%prep
%setup

%if_with python3
cp -fR . ../python3
export LC_ALL=en_US.UTF-8
#find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
for i in $(find ../python3 -type f -name '*.py'); do
	2to3 -w -n $i ||:
rm -f ../python3/spambayes/resources/junk.py
done
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i ${i}3
done
popd
ln -s %_bindir/sb_server.py3 %buildroot%python3_sitelibdir/sb_server.py
%endif

%python_install

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1b1-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1b1-alt2
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1b1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1b1-alt1
- Initial build for Sisyphus

