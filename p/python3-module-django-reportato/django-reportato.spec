%define oname django-reportato

%def_disable check

Name: python3-module-%oname
Version: 1.0
Release: alt3

Summary: Very simple CSV reports with Django
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-reportato/
BuildArch: noarch

# https://github.com/potatolondon/reportato.git
Source: %name-%version.tar
Patch0: port-on-new-django.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
The goal of Reportato is to provide a Django-ish approach to easily get
CSV or Google Spreadsheet generated reports.

%prep
%setup
%patch0 -p1

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 runtests.py

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt3
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2.git20140707.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt2.git20140707.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 1.0-alt2.git20140707
- Rebuild with "def_disable check"
- Cleanup build deps

* Tue Sep 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20140707
- Initial build for Sisyphus

