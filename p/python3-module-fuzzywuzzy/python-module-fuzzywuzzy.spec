%define oname fuzzywuzzy

Name: python3-module-%oname
Version: 0.17.0
Release: alt1

Summary: Fuzzy string matching in Python
License: MIT
Group: Development/Python3
URL: https://github.com/seatgeek/fuzzywuzzy/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-hypothesis
BuildRequires: python3-module-nose
BuildRequires: python3-module-pycodestyle


%description
Fuzzy string matching like a boss.

%prep
%setup
rm fuzzywuzzy/StringMatcher.py

%build
%python3_build

%install
%python3_install

%check
%if 0
nosetests3
%endif

%files
%doc LICENSE.txt README.rst
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info


%changelog
* Mon Jan 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.17.0-alt1
- Version updated to 0.17.0
- porting on python3.

* Sun Nov 04 2012 Ivan A. Melnikov <iv@altlinux.org> 0.1-alt1.git775dfb
- Initial build for Sisyphus.

