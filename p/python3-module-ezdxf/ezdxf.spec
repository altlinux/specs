%define _unpackaged_files_terminate_build 1
%define pypi_name ezdxf

%def_with check

Name: python3-module-%pypi_name
Version: 1.3.0
Release: alt1

Summary: Python 3 package for manipulating DXF drawings

License: MIT
Group: Development/Python3
URL: https://pypi.org/project/ezdxf
VCS: https://github.com/mozman/ezdxf

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)
BuildRequires: python3(fontTools)

%if_with check
# dependencies
BuildRequires: python3(pyparsing)
BuildRequires: python3(typing_extensions)

BuildRequires: python3(pytest)
BuildRequires: python3(geomdl)
%endif

%description
A Python package to create and modify DXF drawings, independent from the
DXF version.

%prep
%setup
# remove unused script interpreter line
sed -i '1 {/env python/ d}' src/ezdxf/addons/drawing/qtviewer.py

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest -ra tests integration_tests

%files
%doc LICENSE README.md
%_bindir/ezdxf
%python3_sitelibdir/%pypi_name
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Thu May 02 2024 Grigory Ustinov <grenka@altlinux.org> 1.3.0-alt1
- Automatically updated to 1.3.0.

* Tue Mar 05 2024 Grigory Ustinov <grenka@altlinux.org> 1.2.0-alt1
- Automatically updated to 1.2.0.

* Fri Jan 26 2024 Grigory Ustinov <grenka@altlinux.org> 1.1.4-alt1
- Automatically updated to 1.1.4.

* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 0.16.3 -> 1.0.1.

* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 0.16.3-alt1
- Initial build
