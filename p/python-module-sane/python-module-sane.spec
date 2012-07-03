Name: python-module-sane
Version: 2.0.1
Release: alt1.1.1
%setup_python_module sane

Summary: Pyhon interface for Sane
License: BSDLike 
Group: Development/Python

Source: pysane-%version.tar

BuildPreReq: python-devel rpm-build-python python-module-setuptools
BuildRequires: libsane-devel python-module-imaging-devel
Requires: python-module-imaging

%description
Pyhon interface for Sane


%prep
%setup -q -n pysane-%version

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*py
%python_sitelibdir/*o


%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0.1-alt1
- initial build for sisyphus

