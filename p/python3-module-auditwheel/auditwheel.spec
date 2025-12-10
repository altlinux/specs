#Unpackaged files in buildroot should terminate build
%define _unpackaged_files_terminate_build 1

%define modulename auditwheel

%ifnarch %ix86
%def_with check
%else
%def_without check
%endif

Name: python3-module-%modulename
Version: 6.5.0
Release: alt1
Summary: A python library to auditing and relabeling cross-distribution Linux wheels
Group: Development/Python3
License: MIT

URL: https://pypi.org/project/auditwheel
VCS: https://github.com/pypa/auditwheel

Source: %name-%version.tar
BuildArch: noarch

Buildrequires(pre): rpm-macros-python3
Buildrequires: rpm-build-python3
Buildrequires: python3-module-setuptools
Buildrequires: python3-module-setuptools_scm

%if_with check
Buildrequires: python3-module-elftools
Buildrequires: python3-module-pretend
%endif

%description
auditwheel is a command line tool to facilitate the creation of Python wheel
packages for Linux (containing pre-compiled binary extensions) that are
compatible with a wide variety of Linux distributions, consistent with the
PEP 600 manylinux_x_y, PEP 513 manylinux1, PEP 571 manylinux2010 and
PEP 599 manylinux2014 platform tags.

%prep
%setup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%pyproject_build

%install
%pyproject_install

%if_with check
%check
%pyproject_run_pytest tests/unit
%endif

%files
%doc CHANGELOG.md LICENSE
%_bindir/%modulename
%python3_sitelibdir_noarch/%modulename
%python3_sitelibdir_noarch/%modulename-%version.dist-info

%changelog
* Wed Dec 10 2025 Polina Poidenko <polipoki@altlinux.org> 6.5.0-alt1
- Initial build for Sisyphus.
