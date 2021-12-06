%define oname django-environ

Name: python3-module-%oname
Version: 0.8.1
Release: alt1

Summary: Django-environ allows you to utilize 12factor inspired environment variables to configure your Django application.
License: MIT
Group: Development/Python3
Url: https://django-environ.readthedocs.io/en/latest/
BuildArch: noarch

# VCS:https://github.com/joke2k/django-environ
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%description
The idea of this package is to unify a lot of packages that make the same stuff:
Take a string from os.environ, parse and cast it to some of useful python typed
variables. To do that and to use the 12factor approach, some connection strings
are expressed as url, so this package can parse it and return a urllib.parse.ParseResult.
These strings from os.environ are loaded from a .env file and filled in os.environ with
setdefault method, to avoid to overwrite the real environ.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
python3 -m pytest tests

%files
%doc *.rst LICENSE.txt
%python3_sitelibdir/*


%changelog
* Thu Dec 02 2021 Dmitry Lyalyaev <fruktime@altlinux.org> 0.8.1-alt1
- Initial build for ALT Linux
