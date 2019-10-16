%define oname isort

Name:           python-module-%oname
Version:        4.2.15
Release:        alt4
Summary:        Python utility / library to sort Python imports
Group:          Development/Python
License:        MIT
URL:            https://github.com/timothycrosley/isort
BuildArch:      noarch

# https://github.com/timothycrosley/isort.git
Source: %name-%version.tar

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-pytest python-module-mock

%description
Python utility / library to sort Python imports

%prep
%setup

%build
%python_build

%install
%python_install

%check
python setup.py test

%files
%doc README.rst LICENSE
%_bindir/*
%python_sitelibdir/%oname
%python_sitelibdir/%oname-%version-py2*.egg-info

%changelog
* Thu Oct 17 2019 Stanislav Levin <slev@altlinux.org> 4.2.15-alt4
- NMU: moved Python3 out to its own package.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt2.qa1
- NMU: remove %ubt from release

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.15-alt1.qa1%ubt
- NMU: applied repocop patch

* Wed Nov 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.15-alt1%ubt
- Initial build for ALT.
