%define oname htmltemplate
Name: python3-module-%oname
Version: 2.2.0
Release: alt1.2
Summary: A simple, powerful [X]HTML templating library for Python 3
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/htmltemplate/

Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel

%py3_provides %oname

%description
htmltemplate converts [X]HTML documents into simple template object
models easily manipulated using ordinary Python code. It is powerful,
flexible, and easy to use.

%package docs
Summary: Documentation and samples for %oname
Group: Development/Python3

%description docs
htmltemplate converts [X]HTML documents into simple template object
models easily manipulated using ordinary Python code. It is powerful,
flexible, and easy to use.

This package contains documentation and samples for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%python3_sitelibdir/*

%files docs
%doc doc sample

%changelog
* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.2.0-alt1.2
- Fixed build.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.2.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 2.2.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Nov 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Initial build for Sisyphus

