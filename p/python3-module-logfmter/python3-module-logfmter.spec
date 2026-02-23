%define _unpackaged_files_terminate_build 1

%define pypi_name logfmter

%def_with check

Name: python3-module-%pypi_name
Version: 0.0.11
Release: alt1

Summary: A Python package which supports global logfmt formatted logging
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/logfmter
Vcs: https://github.com/josheppinette/python-logfmter

BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: golang >= 1.23
%endif

BuildArch: noarch

Source0: %name-%version.tar
Source1: vendor.tar

%description
Add logfmt structured logging using the stdlib logging module and without
changing a single log call.

%prep
%setup -n %name-%version -a 1

%build
%pyproject_build

%if_with check
pushd ./external/golang-logfmt-echo/
go build .
popd
%endif

%install
%pyproject_install

%check
%tox_check_pyproject

%files
%doc *.md
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Mon Feb 23 2026 Alexander Stepchenko <geochip@altlinux.org> 0.0.11-alt1
- Initial build.
