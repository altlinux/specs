%define oname closure-soy

Name: python3-module-%oname
Version: 20121221
Release: alt2

Summary: Google Closure's Soy templates packaged for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/closure-soy/
BuildArch: noarch

# https://github.com/Emsu/python-soy.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-closure

%py3_provides closure_soy
%py3_requires closure


%description
Closure Templates is a client and server side templating system for
building reusable HTML and UI elements. Closure's templating system is
also commonly known as Soy templates.

This is a Java-based tool. This package, based on the Closure Compiler
package, provides a simple way to install and use the the Closure
Template compiler from Python, bundling the soy.jar with the Python
package.

%prep
%setup

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
* Thu Feb 06 2020 Andrey Bychkov <mrdrew@altlinux.org> 20121221-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 20121221-alt1.git20130118.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 20121221-alt1.git20130118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Feb 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20121221-alt1.git20130118
- Initial build for Sisyphus

