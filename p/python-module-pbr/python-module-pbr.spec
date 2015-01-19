%global pypi_name pbr

%def_with python3

Name:		python-module-%{pypi_name}
Version:	0.10.7
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
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires:	python3-devel
BuildRequires:	python3-module-d2to1
BuildRequires:	python3-module-testtools
%endif

%description
PBR is a library that injects some useful and sensible default behaviors
into your setuptools run. It started off life as the chunks of code that
were copied between all of the OpenStack projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active
branches, it seems like a good time to make that code into a proper
re-usable library.

%package -n python3-module-%pypi_name
Summary:	Python Build Reasonableness
Group:		Development/Python3
Requires:	python3-module-pip

%description -n python3-module-%pypi_name
PBR is a library that injects some useful and sensible default behaviors
into your setuptools run. It started off life as the chunks of code that
were copied between all of the OpenStack projects. Around the time that
OpenStack hit 18 different projects each with at least 3 active
branches, it seems like a good time to make that code into a proper
re-usable library.

%prep
%setup
# Remove the requirements file so that pbr hooks don't add it
# to distutils requiers_dist config
rm -rf {test-,}requirements.txt

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%if_with python3
pushd ../python3
%python3_install
popd
rm -rf %{buildroot}%{python3_sitelibdir}/%{pypi_name}/test*
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

# do not include tests due to unmet dependencies
rm -rf %{buildroot}%{python_sitelibdir}/%{pypi_name}/test*

%files
%doc html README.rst LICENSE
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelibdir}/%{pypi_name}

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst LICENSE
%_bindir/*.py3
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%{python3_sitelibdir}/%{pypi_name}
%endif

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.7-alt1
- Version 0.10.7

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Version 0.10.0 (ALT #30192)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.23-alt1.1
- Added module for Python 3

* Mon Dec 16 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.23-alt1
- Initial release for Sisyphus (based on Fedora)
