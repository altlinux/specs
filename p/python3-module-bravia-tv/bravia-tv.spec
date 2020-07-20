Name: python3-module-bravia-tv
Version: 1.0.6
Release: alt1

Summary: Python library to communicate with TV set
License: BSD
Group: Development/Python
Url: https://pypi.org/project/python-bravia-tv/

Source0: %name-%version-%release.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Python Bravia TV is a Python library to perform remote communication
via http protocol with Sony Bravia TVs 2013 and newer.

%prep
%setup

%build
%python3_build

%install
%python3_install

%files
%python3_sitelibdir/bravia_tv
%python3_sitelibdir/bravia_tv-%version-*-info

%changelog
* Mon Jul 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.0.6-alt1
- initial

