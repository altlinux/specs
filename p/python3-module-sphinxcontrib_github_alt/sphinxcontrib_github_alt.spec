%define _unpackaged_files_terminate_build 1
%define pypi_name sphinxcontrib_github_alt

Name:           python3-module-%pypi_name
Version:        1.2
Release:        alt2
Summary:        Github roles for Sphinx docs
Group:          Development/Python3
License:        BSD-2-Clause
URL:            https://github.com/jupyter/sphinxcontrib_github_alt

BuildArch:      noarch

# https://github.com/jupyter/sphinxcontrib_github_alt.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(flit_core)

%description
Link to GitHub issues, pull requests, commits and users for a particular project.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc COPYING.md
%doc README.rst
%python3_sitelibdir/sphinxcontrib_github_alt.py
%python3_sitelibdir/__pycache__/sphinxcontrib_github_alt.*
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 1.2-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 1.2-alt1
- Updated to upstream version 1.2.
- Disabled build for python-2.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 1.0-alt3.qa1
- NMU: remove rpm-build-ubt from BR:

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0-alt2.qa1
- NMU: applied repocop patch

* Tue May 15 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.0-alt2
- (NMU) rebuild with python3.6

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0-alt1%ubt
- Initial build for ALT.
