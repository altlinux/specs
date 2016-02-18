%define oname sysv_ipc
%def_with python3

Name: python-module-%oname
Version: 0.6.8
Release: alt1.1
Summary: System V IPC for Python - Semaphores, Shared Memory and Message Queues
Group: Development/Python
License: GPLv3+
Url: http://semanchuk.com/philip/%oname/
Source: %name-%version.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python3-devel rpm-build-python3

#BuildRequires: python-devel
#BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel
#BuildRequires: python3-module-setuptools
%endif

%description
The sysv_ipc module which gives Python access to System V inter-process
semaphores, shared memory and message queues on systems that support them.

%if_with python3
%package -n python3-module-%oname
Summary: System V IPC for Python - Semaphores, Shared Memory and Message Queues
Group: Development/Python3

%description -n python3-module-%oname
The sysv_ipc module which gives Python access to System V inter-process
semaphores, shared memory and message queues on systems that support them.
%endif

%package examples
Summary: Examples for Python sysv_ipc module
Group: Development/Python
Requires: %name = %version-%release
BuildArch: noarch

%description examples
This module comes with two demonstration apps. The first (in the directory
demo) shows how to use shared memory and semaphores. The second (in the
directory demo2) shows how to use message queues.

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
%doc INSTALL LICENSE README ReadMe.html VERSION
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%files examples
%doc demo demo2 demo4

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.8-alt1.1
- NMU: Use buildreq for BR.

* Fri Mar 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.6.8-alt1
- Initial build
