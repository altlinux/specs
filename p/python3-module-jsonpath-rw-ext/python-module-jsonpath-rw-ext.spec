%global oname jsonpath-rw-ext

Name: python3-module-%oname
Version: 1.2.2
Release: alt2

Summary: Extensions for JSONPath RW
License: ASL 2.0
Group: Development/Python3
Url: https://github.com/kennknowles/python-jsonpath-rw

BuildArch: noarch

Source: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pbr

%description
jsonpath-rw-ext extends json-path-rw capabilities by adding multiple extensions.
'len' that allows one to get the length of a list.
'sorted' that returns a sorted version of a list, 
'arithmetic' that permits one to make math operation between elements and 'filter' to select only certain elements of a list.

%package doc
Summary: Documentation for %name
Group:  Development/Documentation

%description doc
Documentation for %name.

%prep
%setup -q -n %oname-%version

%build
%python3_build

%install
%python3_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

%files
%doc README.rst
%python3_sitelibdir/*

%changelog
* Fri Apr 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- Build for python2 disabled.

* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 1.2.2-alt1
- Build new version.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.1.9-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1.9-alt1.1
- NMU: Use buildreq for BR.

* Tue Nov 03 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1.9-alt1
- Initial build.
