%define  modulename kubernetes-client

Name:     python3-module-%modulename
Version:  30.1.0
Release:  alt1

Summary:  Kubernetes Python Client
License:  Apache-2.0
Group:    Other
Url:      https://github.com/kubernetes-client/python
Vcs:      https://github.com/kubernetes-client/python.git
BuildArch:  noarch

Source:   %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
Python client for the kubernetes API.

%prep
%setup -n %modulename-%version

%build
%pyproject_build

%install
%pyproject_install
cp -pr kubernetes/test %buildroot%python3_sitelibdir/kubernetes/
cp -pr kubernetes/e2e_test %buildroot%python3_sitelibdir/kubernetes/

%files
%doc README.md LICENSE *.txt
%python3_sitelibdir/*

%changelog
* Mon Aug 19 2024 Andrew A. Vasilyev <andy@altlinux.org> 30.1.0-alt1
- 30.1.0

* Sat Jan 20 2024 Andrew A. Vasilyev <andy@altlinux.org> 29.0.0-alt1
- 29.0.0
- change building scheme, python-base now in main tree

* Thu Nov 24 2022 Andrew A. Vasilyev <andy@altlinux.org> 25.3.0-alt1
- 25.3.0

* Wed Jan 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 21.7.0-alt1
- 21.7.0

* Mon Jul 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 17.17.0-alt1
- Initial build for ALT

