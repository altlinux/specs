%define _unpackaged_files_terminate_build 1

%define oname pretend

Name: python3-module-%oname
Version: 1.0.9
Release: alt1
Summary: A library for stubbing in Python
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.python.org/pypi/pretend

BuildArch: noarch

# https://github.com/alex/pretend.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pytest

%description
Pretend is a library to make stubbing with Python easier.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
py.test3 -v

%files
%doc LICENSE.rst
%doc README.rst
%python3_sitelibdir/%{oname}.py
%python3_sitelibdir/__pycache__/%{oname}.*
%python3_sitelibdir/%oname-%version-py%{_python3_version}.egg-info

%changelog
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
