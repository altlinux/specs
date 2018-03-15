Name: python-module-sane
Version: 2.0.1
Release: alt1.4
%setup_python_module sane

Summary: Pyhon interface for Sane
License: BSDLike 
Group: Development/Python
Url: https://github.com/python-pillow/Sane

Source: pysane-%version.tar

BuildPreReq: python-devel rpm-build-python python-module-setuptools
BuildRequires: libsane-devel python-module-Pillow-devel
Requires: python-module-Pillow

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
* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1.4
- NMU: added URL

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.3
- Fixed build

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.2
- Rebuilt

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.1-alt1.1
- Rebuild with Python-2.7

* Thu Oct 20 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 2.0.1-alt1
- initial build for sisyphus

