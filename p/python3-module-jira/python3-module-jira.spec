Name: python3-module-jira
Version: 3.5.2
Release: alt1
Summary: Python library for interacting with JIRA via REST APIs
Group: Development/Python
License: BSD-2-Clause
Url: https://github.com/pycontribs/jira

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
%summary.

%package -n jirashell
Group: Development/Python
Summary: Interactive Jira shell

%description -n jirashell
Interactive Jira shell using jira Python library.

%prep
%setup -n %name-%version

%build
%pyproject_build

%install
%pyproject_install
rm -rf -- %buildroot/%python3_sitelibdir_noarch/tests

%files
%python3_sitelibdir_noarch/jira
%python3_sitelibdir_noarch/jira*.dist-info

%files -n jirashell
%_bindir/jirashell

%changelog
* Wed Aug 30 2023 Alexey Gladkov <legion@altlinux.ru> 3.5.2-alt1
- Initial build.
