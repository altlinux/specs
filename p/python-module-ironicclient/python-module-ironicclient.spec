Name:		python-module-ironicclient
Version:	0.9.0
Release:	alt1
Summary:	Client for OpenStack bare metal Service - Python 2.7
Group:          Development/Python

License:	ASL 2.0
URL:		https://pypi.python.org/pypi/python-ironicclient
Source0:	%name-%version.tar
Patch0:		ironicclient-pbr-minimum-ver-1.3.patch

BuildArch:	noarch

BuildRequires:	python-devel
BuildRequires:	python-module-pbr
BuildRequires:	python-module-setuptools

%description
Client for OpenStack bare metal Service - Python 2.7
Ironic provision bare metal machines instead of virtual machines. It is a fork
of the Nova Baremetal driver. It is best thought of as a bare metal hypervisor
API and a set of plugins which interact with the bare metal hypervisors. By
default, it will use PXE and IPMI in concert to provision and turn on/off
machines, but Ironic also supports vendor-specific plugins which may
implement
additional functionality.

This is a client for the OpenStack Ironic API. There's a Python API
(the "ironicclient" module), and a command-line script ("ironic").

Installing this package gets you a shell command, that you can use to
interact with Ironic's API.

This package provides the Python 2.7 support.

%prep
%setup
%patch0 -p2

%build
%python_build

%install
%python_install

%files
%doc LICENSE README.rst
%_bindir/*
%python_sitelibdir/ironicclient*
%python_sitelibdir/python_ironicclient*

%changelog
* Fri Oct 02 2015 Lenar Shakirov <snejok@altlinux.ru> 0.9.0-alt1
- 0.9.0

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.3.1-alt1
- First build for ALT (based on Fedora 0.3.1-3.fc23.src)
