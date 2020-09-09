%define oname flask-cors

Name: python3-module-%oname
Version: 3.0.9
Release: alt1

Summary: Cross Origin Resource Sharing ( CORS ) support for Flask
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/Flask-Cors/

BuildArch: noarch

# https://github.com/wcdolphin/flask-cors.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
A Flask extension for handling Cross Origin Resource Sharing (CORS), making
cross-origin AJAX possible.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst docs/*.rst examples
%python3_sitelibdir/*

%changelog
* Wed Sep 09 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.0.9-alt1
- Initial build.

