%global pypi_name taskflow
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.1.2
Release:        alt1
Summary:        Taskflow structured state management library

Group:          Development/Python
License:        ASL 2.0
URL:            https://launchpad.net/taskflow
Source0:        %{name}-%{version}.tar
Patch0:         remove-pbr.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-module-pbr
BuildRequires:  python-module-sphinx

Requires:       python-module-anyjson
Requires:       python-module-iso8601
Requires:       python-module-six
Requires:       python-module-babel
Requires:       python-module-stevedore
Requires:       python-module-futures
Requires:       python-module-networkx

%description
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.

%package doc
Summary:          Documentation for Taskflow
Group:            Documentation

%description doc
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.
This package contains the associated documentation.

%prep
%setup

%patch0 -p1

sed -i 's/REDHATVERSION/%{version}/; s/REDHATRELEASE/%{release}/' %{pypi_name}/version.py

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

# Remove the requirements file so that pbr hooks don't add it
# to distutils requires_dist config
rm -rf {test-,}requirements.txt

%build
%python_build

%install
%python_install

# generate html docs
sphinx-build doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%files
%doc README.md LICENSE
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%files doc
%doc html

%changelog
* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.2-alt1
- First build for ALT (based on Fedora 0.1.2-7.fc21.src)

