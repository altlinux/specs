%define  modulename openshift

Name:    python3-module-%modulename
Version:  0.12.1
Release:  alt1

Summary:  OpenShift python client
License:  Apache-2.0
Group:    Other
Url:      https://github.com/openshift/openshift-restclient-python
Vcs:      https://github.com/openshift/openshift-restclient-python.git
BuildArch:  noarch

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source:   %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Python client for the Kubernetes and OpenShift APIs.

%prep
%setup -n %modulename-%version

%build
%python3_build

%install
%python3_install
rm -rf %buildroot/usr/requirements.txt

%check
make test PYTHON=%__python3

%files
%doc *.md LICENSE *.txt
%_bindir/*
%python3_sitelibdir/*

%changelog
* Mon Jul 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.12.1-alt1
- Initial build for ALT

