Name: python-module-augeas
Version: 0.4.1
Release: alt1
Summary: Python bindings to augeas
Group: Development/Python
License: LGPLv2+
Url: http://augeas.net/
Source0: %name-%version.tar

BuildArch: noarch

BuildRequires: python-module-setuptools python-devel libaugeas-devel

%description
python-augeas is a set of Python bindings around augeas.

%prep
%setup

%build
%python_build

%install
%python_install

%check
%make check

%files
%doc COPYING AUTHORS README.txt
%python_sitelibdir/augeas.py*
%python_sitelibdir/*augeas*.egg-info

%changelog
* Mon Aug 12 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 0.4.1-alt1
- build for ALT
