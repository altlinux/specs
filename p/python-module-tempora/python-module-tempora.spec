%define  modulename tempora
%def_with python3

Name:    python-module-%modulename
Version: 1.11
Release: alt1

Summary: Objects and routines pertaining to date and time (tempora)
License: MIT
Group:   Development/Python
URL:     https://github.com/jaraco/tempora

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires: rpm-build-python
BuildRequires: python-devel
BuildRequires: python-module-setuptools_scm
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools_scm
%endif

BuildArch: noarch

Source:  %modulename-%version.tar

%description
Objects and routines pertaining to date and time (tempora).

%if_with python3
%package -n python3-module-%modulename
Summary: Objects and routines pertaining to date and time (tempora)
Group: Development/Python3

%description -n python3-module-%modulename
Objects and routines pertaining to date and time (tempora).
%endif

%prep
%setup -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%version
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%python_sitelibdir/%{modulename}*

%if_with python3
%files -n python3-module-%modulename
%_bindir/calc-prorate
%python3_sitelibdir/%{modulename}*
%endif

%changelog
* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.11-alt1
- Initial build for Sisyphus
