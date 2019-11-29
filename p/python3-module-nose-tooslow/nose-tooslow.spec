%define oname nose-tooslow

Name: python3-module-%oname
Version: 0.1
Release: alt2

Summary: Treat tests that execute too slowly as failed
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/nose-tooslow/
BuildArch: noarch

# https://github.com/mpirnat/nose-tooslow.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python-tools-2to3

%py3_provides tooslow


%description
Plugin for the Nose test framework that treats tests that take too long
to execute as errors.

The maximum allowable time defaults to 1.0 seconds or may be configured
as desired.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1-alt1.git20141104.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.git20141104.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 06 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20141104
- Initial build for Sisyphus

