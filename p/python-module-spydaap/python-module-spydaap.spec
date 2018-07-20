%define modname spydaap
%def_disable python3

Name: python-module-%modname
Version: 0.2
Release: alt1

Summary: Spydaap is a media server supporting the DAAP protocol
Group: Development/Python
License: GPL
Url: https://github.com/egh/%modname

Source: https://pypi.io/packages/source/s/%modname/%modname-%version.tar.gz

BuildArch: noarch

Provides: %modname = %version-%release

BuildRequires(pre): rpm-build-python
BuildRequires: python-devel python-module-setuptools

%if_enabled python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
%endif

%description
Spydaap is a media server supporting the DAAP protocol (aka iTunes
sharing). It is written in Python, uses the mutagen media metadata
library, and either the Avahi or python-zeroconf implementation.

%package -n python3-module-%modname
Summary: Spydaap is a media server supporting the DAAP protocol
Group: Development/Python3
Provides: %modname = %version-%release

%description -n python3-module-%modname
Spydaap is a media server supporting the DAAP protocol (aka iTunes
sharing). It is written in Python, uses the mutagen media metadata
library, and either the Avahi or python-zeroconf implementation.

%prep
%setup -n %modname-%version -a0
%{?_enable_python3:cp -a %modname-%version py3build}

%build
%python_build

%if_enabled python3
pushd py3build
%python3_build
popd
%endif

%install
%python_install

%if_enabled python3
pushd py3build
%python3_install
popd
%endif

%files
%_bindir/%modname
%python_sitelibdir_noarch/%modname/
%exclude %python_sitelibdir_noarch/*.egg-info
%doc README*

%if_enabled python3
%files -n python3-module-%modname
%_bindir/%modname
%python3_sitelibdir_noarch/%modname/
%exclude %python3_sitelibdir_noarch/*.egg-info
%doc README*
%endif

%changelog
* Fri Jul 20 2018 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first build for Sisyphus


