%define _unpackaged_files_terminate_build 1
%define pymodname debian
%def_with python3

Name:    python-module-%pymodname
Version: 0.1.34
Release: alt1

Summary: Modules for Debian-related data formats
License: GPLv2+ and GPLv3+
Group:   Development/Python
Url:     https://pypi.org/project/python-debian/
Source:  %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel

%if_with python3
BuildRequires: python3-devel
%endif

%define _description The `debian` Python modules work with Debian-related data formats, \
providing a means to read data from files involved in Debian packaging, \
and the distribution of Debian packages. The ability to create or edit \
the files is also available for some formats.

%description
%_description

%if_with python3
%package -n python3-module-%pymodname
Summary: Modules for Debian-related data formats
Group: Development/Python3
%description -n python3-module-%pymodname
%_description
%endif

%prep
%setup

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
%python_sitelibdir/debian/
%python_sitelibdir/debian_bundle/
%python_sitelibdir/python_debian-*-py%_python_version.egg-info/
%python_sitelibdir/deb*.py*
%doc README.rst

%if_with python3
%files -n python3-module-%pymodname
%python3_sitelibdir/debian/
%python3_sitelibdir/debian_bundle/
%python3_sitelibdir/__pycache__/*
%python3_sitelibdir/python_debian-*-py%_python3_version.egg-info/
%python3_sitelibdir/deb*.py*
%doc README.rst
%endif

%changelog
* Tue Jan 29 2019 Slava Aseev <ptrnine@altlinux.org> 0.1.34-alt1
- Initial build for ALT
