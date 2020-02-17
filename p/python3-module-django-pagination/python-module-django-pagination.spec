%define module_name django-pagination

Name: python3-module-%module_name
Version: 1.0.7
Release: alt4

Summary: django-pagination allows for easy Digg-style pagination without modifying your views
License: BSD
Group: Development/Python3
Url: http://pypi.python.org/pypi/django-pagination

BuildArch: noarch

Source: %module_name-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
django-pagination allows for easy Digg-style pagination without
modifying your views.

%prep
%setup -n %module_name-%version
find  -type f -name '._*' -exec rm -f '{}' +

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

%install
%python3_install

%files
%doc *.txt docs/*
%python3_sitelibdir/django_pagination-*
%python3_sitelibdir/pagination*


%changelog
* Mon Feb 17 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.7-alt4
- Build for python2 disabled.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt3.qa1
- NMU: applied repocop patch

* Mon May 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt3
- NMU: rebuilt to regenerate dependencies.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.7-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.7-alt2
- Added module for Python 3

* Fri Apr 20 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.7-alt1
- Initial build for ALT Linux
