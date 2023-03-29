%define _unpackaged_files_terminate_build 1
%define oname mmh3

%def_enable check

Name:        python3-module-%oname
Version:     3.1.0
Release:     alt1

Summary:     Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust hash functions.
License:     CC0-1.0
Group:       Development/Python3
Url:         https://github.com/hajimes/mmh3
VCS:         https://github.com/hajimes/mmh3.git

Source:      %name-%version.tar
Patch0:      %name-%version-%release.patch

BuildRequires(pre): rpm-build-python3
BuildRequires:      python3-devel
BuildRequires:      python3-module-setuptools
BuildRequires:      python3-module-wheel
BuildRequires:      gcc-c++

%if_enabled check
BuildRequires:      python3-module-tox
BuildRequires:      python3-module-numpy
BuildRequires:      python3-module-pytest
%endif


%description
Python wrapper for MurmurHash (MurmurHash3), a set of fast and robust 
non-cryptographic hash functions invented by Austin Appleby.

Combined with probabilistic techniques like a Bloom filter, MinHash, 
and feature hashing, mmh3 allows you to develop high-performance systems 
in fields such as data mining, machine learning, and natural language processing.

%prep
%setup
%autopatch -p1

%build
%pyproject_build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -vra test_mmh3.py

%files
%doc LICENSE README.md
%python3_sitelibdir/%oname.*.so
%python3_sitelibdir/%oname-%version.dist-info/

%changelog
* Wed Mar 29 2023 Danil Shein <dshein@altlinux.org> 3.1.0-alt1
- new version 3.1.0
  + delete 32bit archs patch (merged by upstream)

* Tue Nov 08 2022 Danil Shein <dshein@altlinux.org> 3.0.0-alt1
- new version 3.0.0
  + actually enable tests
  + fix 32bit hash calculations on 32bit platforms
  + migrate to pyproject
  + build from upstream git

* Tue Oct 22 2019 Ivan Razzhivin <underwit@altlinux.org> 2.5.1-alt2
- enable tests

* Wed Aug 14 2019 Ivan Razzhivin <underwit@altlinux.org> 2.5.1-alt1
- Initial build for ALT Linux Sisyphus


