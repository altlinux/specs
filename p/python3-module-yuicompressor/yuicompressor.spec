%define oname yuicompressor

Name: python3-module-%oname
Version: 2.4.8
Release: alt2

Summary: YUI Compressor packaged for Python
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/yuicompressor/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides %oname
Requires: jre /proc


%description
YUI Compressor is a JavaScript and CSS minifier written in Java. This
package bundles the YUI Compressor JAR file to ease its use in Python
projects.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc CHANGES README
%_bindir/*
%python3_sitelibdir/*


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.4.8-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.4.8-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.4.8-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.4.8-alt1.1
- NMU: Use buildreq for BR.

* Fri Feb 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.8-alt1
- Initial build for Sisyphus

