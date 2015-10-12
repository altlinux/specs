%define pypi_name taskflow

Name:           python-module-%{pypi_name}
Version:        0.7.1
Release:        alt1
Epoch:          1
Summary:        Taskflow structured state management library

Group:          Development/Python
License:        ASL 2.0
URL:            https://launchpad.net/taskflow
Source0:        %name-%version.tar
BuildArch:      noarch

BuildRequires: python-devel
BuildRequires: python-module-pbr
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-six
BuildRequires: python-module-jsonschema
BuildRequires: python-module-networkx
BuildRequires: python-module-stevedore
BuildRequires: python-module-futures
BuildRequires: python-module-oslo.serialization
BuildRequires: python-module-oslo.utils

Requires: python-module-six
Requires: python-module-jsonschema
Requires: python-module-networkx-core
Requires: python-module-stevedore
Requires: python-module-futures
Requires: python-module-oslo.serialization
Requires: python-module-oslo.utils

%description
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.

%package doc
Summary:          Documentation for Taskflow
Group:            Development/Documentation

%description doc
A library to do [jobs, tasks, flows] in a HA manner using
different backends to be used with OpenStack projects.
This package contains the associated documentation.

%prep
%setup

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
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python_sitelibdir/*/test*
rm -fr %buildroot%python_sitelibdir/*/examples

%files
%doc README.rst LICENSE ChangeLog
%python_sitelibdir/*

%files doc
%doc html

%changelog
* Mon Oct 12 2015 Alexey Shabalin <shaba@altlinux.ru> 1:0.7.1-alt1
- downgrade to 0.7.1

* Tue Mar 31 2015 Alexey Shabalin <shaba@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 0.1.2-alt1
- First build for ALT (based on Fedora 0.1.2-7.fc21.src)

