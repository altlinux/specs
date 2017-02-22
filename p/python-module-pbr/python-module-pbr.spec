%global pypi_name pbr

%def_with doc
%def_with python3

Name:		python-module-%pypi_name
Version:	1.8.1
Release:	alt1.1.1.1
Summary:	Python Build Reasonableness
Group:		Development/Python

License:	ASL 2.0
URL:		http://pypi.python.org/pypi/pbr
Source0:	%name-%version.tar.gz
BuildArch:	noarch


# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-cryptography python-module-cssselect python-module-enum34 python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pyasn1 python-module-pytz python-module-serial python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-alabaster python-module-d2to1 python-module-docutils python-module-html5lib python-module-mimeparse python-module-pbr python-module-unittest2 python3-module-d2to1 python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-unittest2 rpm-build-python3 time

#BuildRequires:	python-devel
#BuildRequires:	python-module-d2to1 >= 0.2.10
#BuildRequires:	python-module-testtools
#BuildRequires:	python-module-sphinx >= 1.1.3
#BuildRequires:	python-module-objects.inv
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires:	python3-devel
#BuildRequires:	python3-module-d2to1
#BuildRequires:	python3-module-testtools
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

%package -n python3-module-%pypi_name-tests
Summary: Tests for PBR library (Python 3)
Group: Development/Python3
Requires: python3-module-%pypi_name = %version-%release

%description -n python3-module-%pypi_name-tests
Tests for PBR library (Python 3)

%package tests
Summary: Tests for PBR library
Group: Development/Python
Requires: %name = %version-%release

%description tests
Tests for PBR library

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
export SKIP_PIP_INSTALL=1
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%if_with doc
# generate html docs
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc README.rst LICENSE
%if_with doc
%doc html
%endif
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/%pypi_name-*.egg-info
%python_sitelibdir/%pypi_name
%exclude %python_sitelibdir/%pypi_name/tests

%files tests
%python_sitelibdir/%pypi_name/tests


%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst LICENSE
%_bindir/*.py3
%python3_sitelibdir/%pypi_name-*.egg-info
%python3_sitelibdir/%pypi_name
%exclude %python3_sitelibdir/%pypi_name/tests

%files -n python3-module-%pypi_name-tests
%python3_sitelibdir/%pypi_name/tests

%endif

%changelog
* Sat Jan 14 2017 Michael Shigorin <mike@altlinux.org> 1.8.1-alt1.1.1.1
- BOOTSTRAP: introduce doc knob (avoid sphinx)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.8.1-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jan 27 2016 Mikhail Efremov <sem@altlinux.org> 1.8.1-alt1.1
- NMU: Use buildreq for BR.

* Tue Oct 27 2015 Alexey Shabalin <shaba@altlinux.ru> 1.8.1-alt1
- 1.8.1
- add tests subpackage

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.7-alt1
- Version 0.10.7

* Wed Aug 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10.0-alt1
- Version 0.10.0 (ALT #30192)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.23-alt1.1
- Added module for Python 3

* Mon Dec 16 2013 Pavel Shilovsky <piastry@altlinux.org> 0.5.23-alt1
- Initial release for Sisyphus (based on Fedora)
