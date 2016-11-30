%define oname pysphere
%def_without python3

Summary: Python API for interaction with the vSphere Web Services SDK
Name: python-module-%oname
Version: 0.1.8
Release: alt3
Url: http://code.google.com/p/pysphere/
Source: %name-%version.tar
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
License: ZSI
Group: Development/Python

Patch1: python-module-pysphere-0.1.8-py3-value-error.patch

BuildArch: noarch
BuildRequires: python-devel python-module-setupdocs python-module-setuptools

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setupdocs python3-module-setuptools
%endif

%description
**Among other operations, PySphere provides easy interfaces to:**
- Connect to VMWare's ESX, ESXi, Virtual Center, Virtual Server hosts 
- Query hosts, datacenters, resource pools, virtual machines
- VMs: Power on, power off, reset, revert to snapshot, get properties, update 
vmware tools, clone, migrate.
- vSphere 5.0 Guest Operations: create/delete/move files and directories.
upload/download files from the guest system. List/start/stop processes in 
the guest system.
- Create and delete snapshots
- Get hosts statistics and monitor performance

%package -n python3-module-%oname
Summary: Python API for interacting with the vSphere Web Services SDK.
Group: Development/Python3

%description -n python3-module-%oname
Python3 API for interacting with the vSphere Web Services SDK.


%prep
%setup

%if_with python3
cp -fR . ../python3
pushd ../python3
%patch1 -p1
find . -type f -name "*.py" -exec 2to3 --write --nobackups  {} \;  -print 
popd
%endif



%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif


%install
%python_build_install --prefix=/usr

%if_with python3
pushd ../python3
%python3_install
popd
%endif


%files
%doc CHANGES MANIFEST README
%python_sitelibdir/*


%if_with python3
%files -n python3-module-%oname
%doc CHANGES MANIFEST README
%python3_sitelibdir/*
%endif


%changelog
* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt3
- Nothing changed just replaced python-dev with python-devel in BuildReq section

* Mon Feb 02 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt2
- Dropped py3 module caused dependiences issues

* Mon Nov 17 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 0.1.8-alt1
- Inital build for ALT

