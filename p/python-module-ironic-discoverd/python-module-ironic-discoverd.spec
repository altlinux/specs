Name:           python-module-ironic-discoverd
Version:        1.1.0
Release:        alt1
Summary:        Hardware introspection for OpenStack Ironic
Group:          Development/Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/ironic-discoverd
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pbr

%description
Discovering hardware properties for OpenStack Ironic - Python 2.7
This is an auxiliary service for discovering hardware properties for a node
managed by OpenStack Ironic. Hardware introspection or hardware properties
discovery is a process of getting hardware parameters required for scheduling
from a bare metal node, given it's power management credentials (e.g. IPMI
address, user name and password).

A special discovery ramdisk is required to collect the information on a node.
The default one can be built using diskimage-builder and
ironic-discoverd-ramdisk element.

This package contains the Python 2.7 files.

%prep
%setup

# Remove bundled egg-info
rm -rf python_seamicroclient.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python_build

%install
%python_install

%files
%_bindir/ironic-discoverd
%python_sitelibdir/*

%changelog
* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 1.1.0-alt1
- First build for ALT
