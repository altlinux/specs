%define modulename crc

Name:    python3-module-%modulename
Version: 6.1.1
Release: alt1

Summary: Calculate and verify predefined & custom CRC's
License: BSD-2-Clause
Group:   Development/Python3
Url:     https://github.com/Nicoretti/crc

# Source-url: https://github.com/Nicoretti/crc/releases/download/%version/crc-%version.tar.gz
Source: %modulename-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-macros-python3
BuildRequires: rpm-build-python3
BuildRequires: python3-dev
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-setuptools_scm
BuildRequires: python3(wheel)
BuildRequires: python3(poetry)
BuildRequires: python3(poetry.core)

%description
%summary.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install

%files
%python3_sitelibdir/%modulename
%python3_sitelibdir/%modulename-%version.dist-info
%doc *.md LICENSE.txt

%changelog
* Mon Mar 18 2024 Anton Midyukov <antohami@altlinux.org> 6.1.1-alt1
- Initial build
