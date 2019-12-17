%define _unpackaged_files_terminate_build 1

%define oname django-sites-groups

Name: python3-module-%oname
Version: 1.9.2
Release: alt2

Summary: Organize sites from the Django sites framework into groups
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-sites-groups/
BuildArch: noarch

# https://github.com/praekelt/django-sites-groups.git
Source0: https://pypi.python.org/packages/96/a6/83111bfd4f057ff5ae1ee1c02383ca4ce50c50d5a6c3a58378b1db6ac978/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3


%description
Organize sites from the Django sites framework into groups.

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
* Tue Dec 17 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.9.2-alt2
- build for python2 disabled

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.9.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.2-alt1.git20120513.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Sep 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20120513
- Initial build for Sisyphus

