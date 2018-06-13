%define  modulename portend
%def_with python3

Name:    python-module-%modulename
Version: 2.3
Release: alt1

Summary: Use portend to monitor TCP ports for bound or unbound states
License: MIT
Group:   Development/Python
URL:     https://github.com/jaraco/portend

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
Use portend to monitor TCP ports for bound or unbound states.

%if_with python3
%package -n python3-module-%modulename
Summary: Use portend to monitor TCP ports for bound or unbound states
Group: Development/Python3

%description -n python3-module-%modulename
Use portend to monitor TCP ports for bound or unbound states.
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
%python3_sitelibdir/%{modulename}*
%python3_sitelibdir/__pycache__/%{modulename}*.pyc
%endif

%changelog
* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- New version.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 2.2-alt1
- Initial build for Sisyphus
