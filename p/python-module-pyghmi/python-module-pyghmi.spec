Name:           python-module-pyghmi
Version:        1.0.18
Release:        alt1
Summary:        Python General Hardware Management Initiative (IPMI and others)
Group:          Development/Python

License:        ASL 2.0
URL:            https://github.com/stackforge/pyghmi
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pbr

%description
This is a pure python implementation of the IPMI protocol.

%prep
%setup

# Remove bundled egg-info
rm -rf pyghmi.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python_build

%install
%python_install

%files
%doc README LICENSE
%python_sitelibdir/pyghmi
%python_sitelibdir/*.egg-info
%_bindir/pyghmicons
%_bindir/pyghmiutil
%_bindir/virshbmc

%changelog
* Thu Jun 22 2017 Lenar Shakirov <snejok@altlinux.ru> 1.0.18-alt1
- 1.0.18

* Wed Sep 23 2015 Lenar Shakirov <snejok@altlinux.ru> 0.5.9-alt1
- First build for ALT (based on Fedora 0.5.9-3.fc23.src

