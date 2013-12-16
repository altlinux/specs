%global pypi_name pbr

Name:		python-module-%{pypi_name}
Version:	0.5.23
Release:	alt1
Summary:	Python Build Reasonableness
Group:		Development/Python

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/pbr
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

Requires:	python-module-pip

BuildRequires:	python-devel
BuildRequires:	python-module-d2to1 >= 0.2.10
BuildRequires:	python-module-testtools
BuildRequires:	python-module-sphinx >= 1.1.3
BuildRequires:	python-module-objects.inv

%description
PBR is a library that injects some useful and sensible default behaviors
into your setuptools run. It started off life as the chunks of code that
were copied between all of the OpenStack projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active
branches, it seems like a good time to make that code into a proper
re-usable library.

%prep
%setup -q
# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%python_build

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%python_install

# do not include tests due to unmet dependencies
rm -rf %{buildroot}%{python_sitelibdir}/%{pypi_name}/test*

%files
%doc html README.rst LICENSE
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelibdir}/%{pypi_name}

%changelog
* Mon Dec 16 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.23-alt1
- Initial release for Sisyphus (based on Fedora)
