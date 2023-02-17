%define _unpackaged_files_terminate_build 1
%define pypi_name ezdxf
%define mod_name %pypi_name

%def_with check

Name: python3-module-%pypi_name
Version: 1.0.1
Release: alt1
Summary: Python 3 package for manipulating DXF drawings
License: MIT
Group: Development/Python3
URL: https://ezdxf.mozman.at/
VCS: https://github.com/mozman/ezdxf.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)
BuildRequires: python3(Cython)

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
%doc README.md
%_bindir/ezdxf
%python3_sitelibdir/%mod_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Tue Feb 07 2023 Stanislav Levin <slev@altlinux.org> 1.0.1-alt1
- 0.16.3 -> 1.0.1.

* Fri Jul 30 2021 Anton Midyukov <antohami@altlinux.org> 0.16.3-alt1
- Initial build
