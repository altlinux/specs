%define  modulename lazy_object_proxy
%def_with python3

Name:    python-module-%modulename
Version: 1.2.1
Release: alt1

Summary: A fast and through lazy object proxy
License: BSD
Group:   Development/Python
URL:     https://github.com/ioelmc/python-lazy-object-proxy

Packager: Denis Medvedev <nbr@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-distribute
BuildRequires: python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
%endif

Source:  %modulename-%version.tar

%description
A fast and through lazy object proxy

%if_with python3
%package -n python3-module-%modulename
Summary: A fast and through lazy object proxy
Group: Development/Python3
%description -n python3-module-%modulename
 A fast and through lazy object proxy
%endif

%prep
%setup -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif


%files
%python_sitelibdir/%modulename/
%python_sitelibdir/*.egg-info
%doc CHANGELOG.rst README.rst CONTRIBUTING.rst AUTHORS.rst LICENSE

%if_with python3
%files -n python3-module-%modulename
%doc CHANGELOG.rst README.rst CONTRIBUTING.rst AUTHORS.rst LICENSE
%python3_sitelibdir/%modulename/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Mon Mar 14 2016 Denis Medvedev <nbr@altlinux.org> 1.2.1-alt1
Initial import.
