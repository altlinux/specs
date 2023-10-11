%define _unpackaged_files_terminate_build 1

%define oname jupyter_core

%def_with check

Name: python3-module-%oname
Version: 5.4.0
Release: alt1
Summary: Jupyter core package
License: BSD-3-Clause
Group: Development/Python3
Url: https://pypi.org/project/jupyter-core
Vcs: https://github.com/jupyter/jupyter_core.git
BuildArch: noarch
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hatchling
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-platformdirs
BuildRequires: python3-module-traitlets
BuildRequires: python3-module-pip
%endif

%description
Jupyter core package. A base package on which Jupyter projects rely.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
export LC_ALL=en_US.UTF-8
%pyproject_run_pytest -v

%files
%doc *.md
%_bindir/*
%python3_sitelibdir/jupyter.py
%python3_sitelibdir/__pycache__/jupyter.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version.dist-info

%changelog
* Wed Oct 11 2023 Anton Vyatkin <toni@altlinux.org> 5.4.0-alt1
- New version 5.4.0.

* Thu Sep 28 2023 Anton Vyatkin <toni@altlinux.org> 5.3.2-alt1
- New version 5.3.2.
- Remove tests subpackage.

* Mon Jul 03 2023 Anton Vyatkin <toni@altlinux.org> 5.3.1-alt1
- New version 5.3.1.

* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 5.2.0-alt1
- 5.1.0 -> 5.2.0

* Mon Dec 05 2022 Anton Farygin <rider@altlinux.ru> 5.1.0-alt1
- 4.7.1 -> 5.1.0

* Thu Aug 19 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 4.7.1-alt1
- Updated to upstream version 4.7.1.

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 4.6.3-alt1
- Updated to upstream version 4.6.3.
- Disabled build for python-2.

* Fri Feb 16 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt2
- Updated build dependencies.

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.4.0-alt1
- Updated to upstream version 4.4.0.
- Enabled tests.

* Wed Feb 15 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt2
- added conflict on python-module-jupyter

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.4-alt2.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 4.0.4-alt2.1
- NMU: Use buildreq for BR.

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 4.0.4-alt2
- Rebuild with "def_disable check"
- Cleanup buildreq

* Fri Aug 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.4-alt1
- Initial build for Sisyphus

