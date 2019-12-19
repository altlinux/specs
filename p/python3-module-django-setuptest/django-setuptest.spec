%define _unpackaged_files_terminate_build 1
%define oname django-setuptest

Name: python3-module-%oname
Version: 0.2.1
Release: alt2

Summary: Simple test suite enabling Django app testing via $ python setup.py test
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-setuptest/
BuildArch: noarch

# https://github.com/praekelt/django-setuptest.git 
Source0: https://pypi.python.org/packages/93/5c/0a76e83e066942ca8caed6382095f218f14ae49b1631d16b262e4ce4ae89/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Simple test suite enabling Django app testing via $ python setup.py
test.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.1-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20140911
- Initial build for Sisyphus

