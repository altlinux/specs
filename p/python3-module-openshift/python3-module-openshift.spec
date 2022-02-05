%define  modulename openshift

Name:    python3-module-%modulename
Version:  0.13.0
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
BuildRequires: python3-devel python3-module-setuptools python3-module-flake8 pytest3 python3-module-openshift

%description
Python client for the Kubernetes and OpenShift APIs.

%prep
%setup -n %modulename-%version
sed -i -e 's/pytest/pytest3/' Makefile tox.ini
# Remove unknown options
sed -i -e 's/--cov-append/--import-mode=append/' -e '/--cov-report=html/d' -e '/--cov=openshift/d' setup.cfg
rm -f test/unit/test_diff.py
# No kubernetes here
sed -i -e 's/ test-integration$//' Makefile

%build
%python3_build

%install
%python3_install
rm -rf %buildroot/usr/requirements.txt

%check
make test PYTHON=%__python3

%files
%doc *.md LICENSE *.txt
%python3_sitelibdir/*

%changelog
* Sat Feb 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.13.0-alt1
- 0.13.0

* Mon Jul 19 2021 Andrew A. Vasilyev <andy@altlinux.org> 0.12.1-alt1
- Initial build for ALT

