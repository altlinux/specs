%define _unpackaged_files_terminate_build 1
%define pypi_name Arpeggio
%define mod_name arpeggio
%def_with check

Name: python3-module-%mod_name
Version: 2.0.0
Release: alt2

Summary: Parser interpreter based on PEG grammars written in Python
License: MIT
Group: Development/Python3
Url: https://github.com/igordejanovic/Arpeggio
BuildArch: noarch

Source0: Arpeggio-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

# docs build
BuildRequires: python3(mike)

%if_with check
BuildRequires: python3(pytest)
%endif

%py3_provides %pypi_name

%description
Arpeggio is a recursive descent parser with memoization based on PEG
grammars (aka Packrat parser).

%package tests
Summary: Test suite for %name
Group: Development/Python3
%description tests
%summary

%prep
%setup -n Arpeggio-%version
# A bit of hack here
## python3 -c "import configparser; config = configparser.ConfigParser(); config.read('setup.cfg'); config['options']['setup_requires']=''; print(config['options']['setup_requires']); config.write(open('setup.cfg', 'w'))"

%build
%pyproject_build
mkdocs build

%install
%pyproject_install

%check
%tox_create_default_config
%tox_check_pyproject -- -vra arpeggio/tests

%files
%doc site examples
%python3_sitelibdir/%mod_name
%exclude %python3_sitelibdir/%mod_name/tests/
%python3_sitelibdir/%pypi_name-%version.dist-info/

%files tests
%python3_sitelibdir_noarch/%mod_name/tests/

%changelog
* Thu Nov 10 2022 Stanislav Levin <slev@altlinux.org> 2.0.0-alt2
- Fixed FTBFS (flit_core 3.7.1).

* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 2.0.0-alt1
- Autobuild version bump to 2.0.0
- Switch to modern build scheme
- Introduce tests

* Tue Sep 21 2021 Fr. Br. George <george@altlinux.ru> 1.10.2-alt1
- Autobuild version bump to 1.10.2
- Separate tests submodule

* Wed Mar 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt5
- Fixed FTBFS.

* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.2-alt4
- Docs build fixed.

* Wed Feb 05 2020 Stanislav Levin <slev@altlinux.org> 1.9.2-alt3
- Fixed FTBS.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.ru> 1.9.2-alt2
- disable python2

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Mon Jan 28 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Initial build for ALT

