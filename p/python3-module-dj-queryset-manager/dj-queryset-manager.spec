%define oname dj-queryset-manager

Name: python3-module-%oname
Version: 0.1.3
Release: alt2

Summary: Stop writing Django querysets
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/dj-queryset-manager/
BuildArch: noarch

# https://github.com/nosamanuel/dj-queryset-manager.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
A Django utility that makes it simple to write DRY queryset methods.

Warning:

dj-queryset-manager only works with Django versions 1.2 through 1.6.

In Django 1.7 it has been superseded by QuerySet.as_manager().

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt2
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.3-alt1.git20140628.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.3-alt1.git20140628.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.3-alt1.git20140628
- Initial build for Sisyphus

