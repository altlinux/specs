%define  modulename kubernetes-client

Name:     python3-module-%modulename
Version:  17.17.0
Release:  alt1

Summary:  Kubernetes Python Client
License:  Apache-2.0
Group:    Other
Url:      https://github.com/kubernetes-client/python
Vcs:      https://github.com/kubernetes-client/python.git
BuildArch:  noarch

Packager: Andrew A. Vasilyev <andy@altlinux.org>

Source:   %modulename-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
Python client for the kubernetes API.

%prep
%setup -n %modulename-%version

%build
#%%python3_build

%install
%__python3 setup.py install --root=%buildroot --prefix=%_prefix
rm -rf %buildroot/usr/requirements.txt
rm -rf %buildroot%python3_sitelibdir/kubernetes/leaderelection/example.py
rm -rf %buildroot%python3_sitelibdir/kubernetes/dynamic/test_discovery.py
rm -rf %buildroot%python3_sitelibdir/kubernetes/dynamic/test_client.py

%files
%doc *.md LICENSE *.txt
%python3_sitelibdir/*

%changelog
* Mon Jul 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 17.17.0-alt1
- Initial build for ALT

