
Name: python-module-warlock
Version: 1.3.0
Release: alt1
Summary: Python object model built on top of JSON schema

Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/warlock
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-jsonschema >= 0.7
BuildRequires: python-module-jsonpatch >= 0.10
BuildRequires: python-module-six

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-jsonschema >= 0.7
BuildRequires: python3-module-jsonpatch >= 0.10
BuildRequires: python3-module-six

%package -n python3-module-warlock
Summary: Python object model built on top of JSON schema
Group: Development/Python3

%description -n python3-module-warlock
Build self-validating python objects using JSON schemas

%description
Build self-validating python objects using JSON schemas

%prep
%setup
# Remove bundled egg-info
rm -rf warlock.egg-info
# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -f requirements.txt
rm -rf ../python3
cp -a . ../python3

%build
%python_build
pushd ../python3
%python3_build
popd

%install
%python_install
pushd ../python3
%python3_install
popd

%files
%doc README.md LICENSE.txt
%python_sitelibdir/*

%files -n python3-module-warlock
%python3_sitelibdir/*

%changelog
* Mon Dec 10 2018 Alexey Shabalin <shaba@altlinux.org> 1.3.0-alt1
- 1.3.0

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.1.0-alt1.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.1.0-alt1.1
- NMU: Use buildreq for BR.

* Tue Mar 10 2015 Alexey Shabalin <shaba@altlinux.ru> 1.1.0-alt1
- 1.1.0
- add python3 package

* Mon Sep 30 2013 Pavel Shilovsky <piastry@altlinux.org> 0.4.0-alt2
- Fix check section in spec

* Mon Sep 17 2012 Pavel Shilovsky <piastry@altlinux.org> 0.4.0-alt1
- Initial release for Sisyphus (based on Fedora)
