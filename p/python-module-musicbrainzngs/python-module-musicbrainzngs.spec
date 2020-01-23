%define modname musicbrainzngs
%def_enable python2

Name: python-module-%modname
Version: 0.7.1
Release: alt1

Summary: Python bindings for the MusicBrainz NGS and the Cover Art Archive webservices
Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/m/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute

%if_enabled python2
BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools python-modules-json
%endif

%description
This Python module implements webservice bindings for the Musicbrainz NGS
site, also known as /ws/2 and the Cover Art Archive.

%package -n python3-module-%modname
Summary: Python3 bindings for the MusicBrainz NGS and the Cover Art Archive webservices
Group: Development/Python3

%description -n python3-module-%modname
This Python3 module implements webservice bindings for the Musicbrainz NGS
site, also known as /ws/2 and the Cover Art Archive.

%prep
%setup -n %modname-%version %{?_enable_python2:-a0
cp -a %modname-%version py2build}

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
%doc README.rst COPYING PKG-INFO
%python_sitelibdir_noarch/*.egg-info
%endif

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc README.rst COPYING PKG-INFO
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Thu Jan 23 2020 Yuri N. Sedunov <aris@altlinux.org> 0.7.1-alt1
- 0.7.1
- made python2 module optional

* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

