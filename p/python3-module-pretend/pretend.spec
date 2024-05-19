%define oname pretend

%def_with check

Name: python3-module-%oname
Version: 1.0.9
Release: alt2
Summary: A library for stubbing in Python
License: BSD-3-Clause
Group: Development/Python3
URL: https://pypi.org/project/pretend
VCS: https://github.com/alex/pretend

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

%description
Pretend is a library to make stubbing with Python easier.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE.rst README.rst
%python3_sitelibdir/%{oname}.py
%python3_sitelibdir/__pycache__/%{oname}.*
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Sun May 19 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.9-alt2
- Moved on modern pyproject macros.

* Tue Jun 22 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.9-alt1
- Updated to upstream version 1.0.9.
- Disabled module for python-2.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt2.qa1
- NMU: remove %%ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.8-alt1.qa1
- NMU: applied repocop patch

* Tue Oct 10 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.8-alt1
- Initial build for ALT.
