Name:           python-module-pyremotevbox
Version:        0.5.0
Release:        alt1
Summary:        Python API to talk to a remote VirtualBox using VirtualBox WebService
Group:          Development/Python

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/pyremotevbox/
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pbr

%description
Python module to communicate with a remote virtualbox over webservice.

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
%python_sitelibdir/*

%changelog
* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.5.0-alt1
- First build for ALT

