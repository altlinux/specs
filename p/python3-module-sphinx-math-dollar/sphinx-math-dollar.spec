%define oname sphinx-math-dollar
%define realname sphinx_math_dollar

%def_with check

Name: python3-module-%oname
Version: 1.2.1
Release: alt1

Summary: Sphinx extension to let you write LaTeX math using $$

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/sphinx-math-dollar
VCS: https://github.com/sympy/sphinx-math-dollar

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-sphinx-tests
BuildRequires: python3-module-pytest-doctestplus
%endif

%description
sphinx-math-dollar is a Sphinx extension to let you write LaTeX math using $$.

%prep
%setup

# hotfix for python3.12
sed -i 's/SafeConfigParser/ConfigParser/' versioneer.py
sed -i 's/readfp/read_file/' versioneer.py
# fix egg-info
sed -i -e 's/\(^\s\+git_refnames = \).*$/\1"%version"/' %realname/_version.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc LICENSE README* CHANGELOG*
%python3_sitelibdir/%realname
%python3_sitelibdir/%realname-%version.dist-info

%changelog
* Sat May 18 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Thu Jan 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.2-alt2
- Fixed FTBFS.

* Tue Aug 24 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Updated to upstream version 1.2.

* Wed Jul 08 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Initial build for ALT.
