%define _unpackaged_files_terminate_build 1

%define oname closure

Name: python3-module-%oname
Version: 20161201
Release: alt2

Summary: Closure compiler packaged for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/closure/
BuildArch: noarch

# https://github.com/miracle2k/python-closure.git
Source0: https://pypi.python.org/packages/0e/fb/877df05e79e4f719971e3cef9da6707b5f07ac29f223e80e6d5996c84b3b/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
Requires: closure-compiler

Conflicts: python-module-%oname


%description
The Closure Compiler is a tool for reducing the size of Javascript files
to make them download and run faster.

It's a Java-based tool. This package, in the spirit of the yuicompressor
package, provides a simple way to install and use the the Closure
compiler from Python, bundling the closure.jar with the Python package.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%_bindir/*
%python3_sitelibdir/*


%changelog
* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 20161201-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 20161201-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 20161201-alt1
- automated PyPI update

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 20160517-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 20140110-alt1.git240319.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 20140110-alt1.git240319.1
- NMU: Use buildreq for BR.

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20140110-alt1.git240319
- Initial build for Sisyphus

