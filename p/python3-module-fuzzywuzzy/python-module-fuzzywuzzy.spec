%define oname fuzzywuzzy

%def_with check

Name: python3-module-%oname
Version: 0.18.0
Release: alt2

Summary: Fuzzy string matching in Python
License: GPL-2.0
Group: Development/Python3
URL: https://pypi.org/project/fuzzywuzzy/
VCS: https://github.com/seatgeek/fuzzywuzzy

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-pycodestyle
BuildRequires: python3-module-Levenshtein
BuildRequires: python3-module-pytest
%endif

%description
Fuzzy string matching like a boss. It uses Levenshtein Distance to calculate
the differences between sequences in a simple-to-use package.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -k 'not test_process_warning'

%files
%doc LICENSE.txt *.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/%oname-%version.dist-info


%changelog
* Tue Jan 23 2024 Anton Vyatkin <toni@altlinux.org> 0.18.0-alt2
- Fix FTBFS.

* Wed Mar 29 2023 Anton Vyatkin <toni@altlinux.org> 0.18.0-alt1
- New version 0.18.0.

* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.17.0-alt1
- Version updated to 0.17.0
- porting on python3.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt1.git775dfb
- Initial build for Sisyphus.

