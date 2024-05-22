%define oname apply

%def_with check

Name: python3-module-%oname
Version: 1.7
Release: alt1

Summary: An apply function for Python 2 and 3.
License: BSD-2-Clause
Group: Development/Python3
Url: https://pypi.org/project/apply
Vcs: https://github.com/stefanholek/apply
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
%summary.

%prep
%setup

sed -i '/^tag_build =.*/d' setup.cfg

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_unittest discover -v

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}


%changelog
* Wed May 22 2024 Anton Vyatkin <toni@altlinux.org> 1.7-alt1
- New version 1.7.

* Mon Feb 03 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.5-alt1
- Initial build.

