%define oname warlock

Name: python3-module-%oname
Version: 1.3.0
Release: alt2

Summary: Python object model built on top of JSON schema
License: ASL 2.0
Group: Development/Python3
Url: http://pypi.python.org/pypi/warlock
Source: %oname-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jsonschema >= 0.7
BuildRequires: python3-module-jsonpatch >= 0.10
BuildRequires: python3-module-six


%description
Build self-validating python objects using JSON schemas

%prep
%setup -q -n %oname-%version

# Remove bundled egg-info
rm -rf warlock.egg-info

# let RPM handle deps
sed -i '/setup_requires/d; /install_requires/d; /dependency_links/d' setup.py
rm -f requirements.txt

%build
%python3_build

%install
%python3_install

%files
%doc README.md LICENSE.txt
%python3_sitelibdir/*


%changelog
* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt2
- Build for python2 disabled.

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
