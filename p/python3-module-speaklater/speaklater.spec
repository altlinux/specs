%define oname speaklater

Name: python3-module-%oname
Version: 1.3
Release: alt2

Summary: Implements a lazy string for python useful for use with gettext
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/speaklater/
BuildArch: noarch

# https://github.com/mitsuhiko/speaklater.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
A module that provides lazy strings for translations. Basically you get
an object that appears to be a string but changes the value every time
the value is evaluated based on a callable you provide.

For example you can have a global lazy_gettext function that returns a
lazy string with the value of the current set language.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc README
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.3-alt1.git20120701.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt1.git20120701.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20120701
- Initial build for Sisyphus

