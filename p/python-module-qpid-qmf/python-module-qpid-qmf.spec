
Name: python-module-qpid-qmf
Version: 0.32
Release: alt1
Summary: The QPID Management Framework bindings for python

License: ASL 2.0
Group: Development/Python
Url: http://qpid.apache.org
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
The QPID Management Framework bindings for python

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Tue Mar 24 2015 Alexey Shabalin <shaba@altlinux.ru> 0.32-alt1
- Initial release for Sisyphus
