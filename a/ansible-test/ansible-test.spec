Name:    ansible-test
Version: 1.0.1
Release: alt1

Summary: An Ansible Testing Framework for Humans
License: MIT
Group:   Development/Python
URL:     https://github.com/nylas/ansible-test

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute

BuildArch: noarch

# Build from commit 3ca8d5aa8984e9a82946d4a68063ca7841c4d4a4
Source:  %name-%version.tar

%description
Ansible-test is a tool for testing your automation on local docker images. You
can think of this as a slim version of Chef's test-kitchen.

%prep
%setup -n %name-%version

%build
%python_build

%install
%python_install

%files
%_bindir/%name
%python_sitelibdir/ansible_test
%python_sitelibdir/*.egg-info

%changelog
* Tue Aug 01 2017 Mikhail Gordeev <obirvalger@altlinux.org> 1.0.1-alt1
- Initial build for Sisyphus
