%define oname flask_mail

Name: python3-module-%oname
Version: 0.9.1
Release: alt2

Summary: Flask extension for sending email
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-Mail/
# https://github.com/mattupstate/flask-mail.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose
BuildRequires: python3-module-flask
BuildRequires: python3-module-blinker
BuildRequires: python3-module-speaklater
BuildRequires: python3-module-mock

%py3_provides %oname


%description
Flask-Mail is a Flask extension providing simple email sending
capabilities.

Documentation: http://packages.python.org/Flask-Mail

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test

%files
%doc CHANGES *.rst docs/*.rst
%python3_sitelibdir/*


%changelog
* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.git20141015.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20141015.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20141015
- Initial build for Sisyphus

