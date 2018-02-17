%define modname musicbrainzngs

Name: python-module-%modname
Version: 0.6
Release: alt1

Summary: Python bindings for the MusicBrainz NGS and the Cover Art Archive webservices
Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/%modname
Source: https://pypi.io/packages/source/m/%modname/%modname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools python-modules-json

BuildRequires: python3-devel rpm-build-python3
BuildRequires: python3-module-distribute

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
%setup -n %modname-%version -a0
cp -a %modname-%version py3build

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
%python_sitelibdir_noarch/%modname/
%doc README.rst COPYING PKG-INFO
%python_sitelibdir_noarch/*.egg-info

%files -n python3-module-%modname
%python3_sitelibdir_noarch/%modname/
%doc README.rst COPYING PKG-INFO
%python3_sitelibdir_noarch/*.egg-info

%changelog
* Sat Feb 17 2018 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

