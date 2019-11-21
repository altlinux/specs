%define mname xstatic
%define oname %mname-tv4
%define pypi_name XStatic-tv4

Name: python3-module-%oname
Version: 1.2.7.0
Release: alt4

Summary: Tiny Validator for v4 JSON Schema (XStatic packaging standard)
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/%pypi_name/
Source: %pypi_name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-%mname

%py3_provides %mname.pkg.tv4
%py3_requires %mname.pkg


%description
Use json-schema draft v4 to validate simple values and complex objects using a rich validation vocabulary.

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
* Thu Nov 21 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.2.7.0-alt4
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.7.0-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Alexey Shabalin <shaba@altlinux.ru> 1.2.7.0-alt2
- build as noarch

* Mon Oct 24 2016 Alexey Shabalin <shaba@altlinux.ru> 1.2.7.0-alt1
- Initial build for Sisyphus
