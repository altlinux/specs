%define mname xstatic
%define oname %mname-jquery-ui
%define pypi_name XStatic-jquery-ui

Name:       python3-module-%oname
Version:    1.13.0.1
Release:    alt1

Summary:    jquery-ui (XStatic packaging standard)
License:    MIT
Group:      Development/Python3
Url:        https://pypi.python.org/pypi/%pypi_name/
Source:     %pypi_name-%version.tar.gz

BuildArch:  noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname python3-module-%mname-jquery

%py3_provides %mname.pkg.jquery_ui
%py3_requires %mname.pkg.jquery


%description
jquery-ui javascript library packaged for setuptools (easy_install) /
pip.

This package is intended to be used by any project that needs these
files.

%prep
%setup -n %pypi_name-%version

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt
%python3_sitelibdir/%mname/pkg/*
%python3_sitelibdir/*.egg-info
%exclude %python3_sitelibdir/*.pth


%changelog
* Tue Feb 06 2024 Ilfat Aminov <aminov@altlinux.org> 1.13.0.1-alt1
- 1.13.0.1

* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.12.0.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.12.0.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.12.0.1-alt1
- 1.12.0.1
- build as noarch

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0.1-alt1.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.11.0.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.11.0.1-alt1.1
- NMU: Use buildreq for BR.

* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.11.0.1-alt1
- Initial build for Sisyphus

