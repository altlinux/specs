%define oname spambayes
Name: python-module-%oname
Version: 1.1b1
Release: alt1.1
Summary: Spam classification system
License: Python
Group: Development/Python
Url: http://pypi.python.org/pypi/spambayes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%add_python_req_skip pywintypes win32com

%description
The SpamBayes project is working on developing a statistical (commonly,
although a little inaccurately, referred to as Bayesian) anti-spam
filter, initially based on the work of Paul Graham. The major difference
between this and other, similar projects is the emphasis on testing
newer approaches to scoring messages. While most anti-spam projects are
still working with the original graham algorithm, we found that a number
of alternate methods yielded a more useful response.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1b1-alt1.1
- Rebuild with Python-2.7

* Thu Jul 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1b1-alt1
- Initial build for Sisyphus

