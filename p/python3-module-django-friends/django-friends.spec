%define oname django-friends

%def_with bootstrap

Name: python3-module-%oname
Version: 0.1.5
Release: alt3

Summary: Friendship, contact and invitation management for the Django web framework
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-friends/
BuildArch: noarch

# https://github.com/jtauber/django-friends.git
Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
Friendship, contact and invitation management for the Django web
framework.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%files
%doc CHANGELOG *.md
%python3_sitelibdir/*


%changelog
* Mon Dec 30 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt3
- build for python2 disabled

* Sat May 19 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.5-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20130126.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Oct 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20130126
- Initial build for Sisyphus

