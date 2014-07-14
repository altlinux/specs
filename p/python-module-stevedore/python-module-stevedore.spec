Name:           python-module-stevedore
Version:        0.14
Release:        alt1
Summary:        Manage dynamic plugins for Python applications

Group:		Development/Python
License:        ASL 2.0
URL:            https://github.com/dreamhost/stevedore
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-setuptools
BuildRequires:  python-module-pbr

%description
Manage dynamic plugins for Python applications

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README.rst LICENSE
%{python_sitelibdir}/stevedore
%{python_sitelibdir}/stevedore-%{version}-py?.?.egg-info

%changelog
* Mon Jul 14 2014 Lenar Shakirov <snejok@altlinux.ru> 0.14-alt1
- First build for ALT (based on Fedora 0.14-1.fc21.src)

