%define _unpackaged_files_terminate_build 1

%define pypi_name docx2txt

Name: python3-module-%pypi_name
Version: 0.9
Release: alt1

Summary: Pure python based utility to extract text and images from docx files
License: MIT
Group: Development/Python3
URL: https://github.com/ankushshah89/python-docx2txt

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-wheel

BuildArch: noarch

Source: %pypi_name-%version.tar

%description
%summary.

%prep
%setup -n %pypi_name-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%doc README.md
%_bindir/docx2txt
%python3_sitelibdir/%pypi_name/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}

%changelog
* Sat Jan 24 2026 Nikolay Strelkov <snk@altlinux.org> 0.9-alt1
- Initial build for Sisyphus
