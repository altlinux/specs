%define oname crcmod

Name:    python3-module-%oname
Version: 1.7
Release: alt2

Summary: CRC Generator

Group:   Development/Python3
License: MIT
URL:     https://pypi.org/project/%oname/

Source0: %oname-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools python3-module-wheel

%description
The software in this package is a Python module for generating objects that
compute the Cyclic Redundancy Check (CRC).

%prep
%setup -n %oname-%version

%build
%pyproject_build

%install
%pyproject_install

%check
for test in test/*; do
  PYTHONPATH="%buildroot%python3_sitelibdir" %__python3 $test
done

%files
%doc README changelog
%python3_sitelibdir/%oname
%python3_sitelibdir/%{oname}*-%version.dist-info

%changelog
* Sun Jun 01 2025 L.A. Kostis <lakostis@altlinux.ru> 1.7-alt2
- Resurrect from orphaned.
- Drop documentation.

* Wed Apr 06 2022 Anton Midyukov <antohami@altlinux.org> 1.7-alt1
- Initial build for Sisyphus
