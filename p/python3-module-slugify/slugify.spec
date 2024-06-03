%define  modulename slugify

%def_with check

Name:    python3-module-%modulename
Version: 8.0.4
Release: alt1

Summary: Returns unicode slugs
License: MIT
Group:   Development/Python3
URL:     https://pypi.org/project/python-slugify
VCS:     https://github.com/un33k/python-slugify

Provides: python3-module-python-%modulename = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%if_with check
BuildRequires: python3(text_unidecode)

BuildRequires: python3(tox)
%endif

BuildArch: noarch

Source: %name-%version.tar

# try-except import
%py3_requires text_unidecode

%description
A Python slugify application that handles unicode.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
python3 test.py

%files
%_bindir/%modulename
%python3_sitelibdir/%modulename
%python3_sitelibdir/python_slugify-%version.dist-info

%changelog
* Mon Jun 03 2024 Grigory Ustinov <grenka@altlinux.org> 8.0.4-alt1
- Automatically updated to 8.0.4.

* Sat Jan 27 2024 Grigory Ustinov <grenka@altlinux.org> 6.1.1-alt3
- Moved on modern pyproject macros.

* Sun Aug 27 2023 Alexandr Shashkin <dutyrok@altlinux.org> 6.1.1-alt2
- added provide to normalized project name for compability with Python
  ecosystem

* Fri Mar 11 2022 Stanislav Levin <slev@altlinux.org> 6.1.1-alt1
- 4.0.1 -> 6.1.1.

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.1-alt1
- 4.0.1 released

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.0.0-alt1
- 4.0.0 released

* Thu Feb 08 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.2.4-alt1
- Separate build for Sisyphus
