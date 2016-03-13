%define _name configobj

Name: python-module-%_name
Version: 5.0.6
Release: alt1.1

Summary: a Python module for easy reading and writing of config files
License: BSD
Group: Development/Python
Url: http://configobj.readthedocs.org/

Source: https://pypi.python.org/packages/source/c/%_name/%_name-%version.tar.gz
# fc
Patch: configobj-5.0.5-fc-import-all-fix.patch

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: rpm-build-python3 python3-devel

%description
ConfigObj - a Python module for easy reading and writing of config
files.

%package -n python3-module-%_name
Summary: a Python3 module for easy reading and writing of config files
License: BSD
Group: Development/Python3
Requires: dbus

%description -n python3-module-%_name
ConfigObj - a Python3 module for easy reading and writing of config
files.

%prep
%setup -n %_name-%version -a0
%patch -p1
mv %_name-%version py3build
pushd py3build
%patch -p1
popd

%build
%python_build
pushd py3build
%python3_build
popd

%install
%python_install
pushd py3build
%python3_install
popd

%files
%python_sitelibdir/_version.py*
%python_sitelibdir/%_name.py*
%python_sitelibdir/validate.py*
%python_sitelibdir/%_name-*.egg-info

%files -n python3-module-%_name
%python3_sitelibdir/_version.py
%python3_sitelibdir/%_name.py
%python3_sitelibdir/validate.py
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/%_name-*.egg-info

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 11 2016 Yuri N. Sedunov <aris@altlinux.org> 5.0.6-alt1
- 5.0.6

* Thu Jul 03 2014 Yuri N. Sedunov <aris@altlinux.org> 5.0.5-alt1
- 5.0.5 (new upstream)
- new python3 subpackage

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.2-alt1.1
- Rebuild with Python-2.7

* Sat Oct 30 2010 Yuri N. Sedunov <aris@altlinux.org> 4.7.2-alt1
- new version (ALT #24462)

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.5.3-alt1.1
- Rebuilt with python 2.6

* Wed Oct 29 2008 Yuri N. Sedunov <aris@altlinux.org> 4.5.3-alt1
- first build for Sisyphus

