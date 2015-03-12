Name: python-module-pyngus
Version: 1.2.0
Release: alt1
Summary: Callback API implemented over Proton
Group: Development/Python
License: ASL 2.0
Url: http://pypi.python.org/pypi/pyngus/%version
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel
BuildRequires: python-module-setuptools

%description
A connection oriented messaging framework using QPID Proton.
It provides a callback-based API for message passing.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/pyngus
%python_sitelibdir/pyngus-*.egg-info

%changelog
* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 1.2.0-alt1
- Initial build.
