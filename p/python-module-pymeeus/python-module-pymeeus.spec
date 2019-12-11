%define modname pymeeus
%define _name PyMeeus
%def_enable python2

Name: python-module-%modname
Version: 0.3.6
Release: alt1

Summary: Library of astronomical algorithms in Python
Group: Development/Python
License: LGPL-3.0
Url: https://pypi.python.org/pypi/%_name

Source: https://pypi.io/packages/source/P/%_name/%_name-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%if_enabled python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools
%endif

%description
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book 
"Astronomical Algorithms, 2nd Edition, Willmann-Bell Inc. (1998)" by Jean Meeus.

%package -n python3-module-%modname
Summary: Library of astronomical algorithms in Python3
Group: Development/Python3

%description -n python3-module-%modname
PyMeeus is a Python implementation of the astronomical algorithms described
in the classical book 
"Astronomical Algorithms, 2nd Edition, Willmann-Bell Inc. (1998)" by Jean Meeus.

%prep
%setup -n %_name-%version %{?_enable_python2:-a0
cp -a %_name-%version py2build}

%build
%python3_build

%if_enabled python2
pushd py2build
%python_build
popd
%endif

%install
%python3_install

%if_enabled python2
pushd py2build
%python_install
popd
%endif

%if_enabled python2
%files
%python_sitelibdir_noarch/%modname/
%doc *.rst
%python_sitelibdir_noarch/*.egg-info
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc *.rst
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Wed Dec 11 2019 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- first build for Sisyphus



