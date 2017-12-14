%define  modulename pyvmomi
%def_with python3

Name:    python-module-%modulename
Version: 6.5.0.2017.5
Release: alt1

Summary: VMware vSphere API Python Bindings
License: Apache-2.0
Group:   Development/Python
URL:     https://github.com/vmware/pyvmomi

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildPreReq: rpm-build-python python-module-setuptools
%if_with python3
BuildPreReq: rpm-build-python3 python3-module-setuptools
%endif

%setup_python_module %modulename

BuildArch: noarch

Source:  %modulename-%version.tar

%description
pyVmomi is the Python SDK for the VMware vSphere API that allows you to
manage ESX, ESXi, and vCenter.

%if_with python3
%package -n python3-module-%modulename
Summary: VMware vSphere API Python Bindings
Group: Development/Python3

%description -n python3-module-%modulename
pyVmomi is the Python SDK for the VMware vSphere API that allows you to
manage ESX, ESXi, and vCenter.
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
%python_sitelibdir/pyV*
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%modulename
%python3_sitelibdir/pyV*
%python3_sitelibdir/*.egg-*
%endif

%changelog
* Wed Dec 13 2017 Andrey Cherepanov <cas@altlinux.org> 6.5.0.2017.5-alt1
- Initial build for Sisyphus
