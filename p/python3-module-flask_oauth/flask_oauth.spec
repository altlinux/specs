%define oname flask_oauth

Name: python3-module-%oname
Version: 0.13
Release: alt2

Summary: Adds OAuth support to Flask
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-OAuth/
# https://github.com/mitsuhiko/flask-oauth.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-flask python3-module-oauth2
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Implements basic OAuth support for Flask.  Currently it can only
be used to hook up with external OAuth services.  It does not yet
support implementing providers.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc README example docs/*.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.13-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.13-alt1.git20121006.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.13-alt1.git20121006.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20121006
- Initial build for Sisyphus

