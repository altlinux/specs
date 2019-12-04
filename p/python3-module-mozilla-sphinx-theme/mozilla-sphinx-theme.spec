%define oname mozilla-sphinx-theme

Name: python3-module-%oname
Version: 0.2
Release: alt2

Summary: A sandstone mozilla theme for sphinx
License: BSD
Group: Development/Python3
Url: https://github.com/ametaireau/mozilla-sphinx-theme
BuildArch: noarch

# https://github.com/ametaireau/mozilla-sphinx-theme.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx

%py3_provides mozilla_sphinx_theme


%description
This is a version of Mozilla's sandstone theme, for the Sphinx
documentation engine.

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
%python3_sitelibdir/*


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2-alt1.git20130808.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20130808.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130808
- Initial build for Sisyphus

