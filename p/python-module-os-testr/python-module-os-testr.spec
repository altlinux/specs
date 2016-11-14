%def_with python3

%define pypi_name os-testr

Name: python-module-os-testr
Version: 0.6.0
Release: alt1
Summary: A testr wrapper to provide functionality for OpenStack projects
Group: Development/Python
License: ASL 2.0
Url: http://git.openstack.org/cgit/openstack/%pypi_name
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar
BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires: python-module-pbr
BuildRequires: python-module-setuptools

Requires: python-module-pbr
Requires: python-module-babel
Requires: python-module-testrepository
Requires: python-module-subunit
Requires: python-module-testtools
Requires: python-module-setuptools

%description
ostestr is a testr wrapper that uses subunit-trace for output and builds
some helpful extra functionality around testr.

%if_with python3
%package -n python3-module-%pypi_name
Summary: A testr wrapper to provide functionality for OpenStack projects
Group: Development/Python
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-pbr
BuildRequires: python3-module-setuptools

Requires: python3-module-pbr
Requires: python3-module-babel
Requires: python3-module-testrepository
Requires: python3-module-subunit
Requires: python3-module-testtools
Requires: python3-module-setuptools

%description -n python3-module-%pypi_name
ostestr is a testr wrapper that uses subunit-trace for output and builds
some helpful extra functionality around testr.
%endif

%package doc
Summary: Documentation for ostestr module
Group: Development/Documentation
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx

%description doc
Documentation for ostestr module

%prep
%setup

rm -f test-requirements.txt requirements.txt

%if_with python3
rm -rf ../python3
cp -a . ../python3
find ../python3/ -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees source build/html
popd
# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/generate-subunit %buildroot%_bindir/python3-generate-subunit
mv %buildroot%_bindir/ostestr %buildroot%_bindir/python3-ostestr
mv %buildroot%_bindir/subunit-trace %buildroot%_bindir/python3-subunit-trace
mv %buildroot%_bindir/subunit2html %buildroot%_bindir/python3-subunit2html
popd
%endif
%python_install

%files
%doc README.rst
%_bindir/generate-subunit
%_bindir/ostestr
%_bindir/subunit-trace
%_bindir/subunit2html
%python_sitelibdir/os_testr
%python_sitelibdir/os_testr-*.egg-info

%if_with python3
%files -n python3-module-%pypi_name
%doc README.rst
%_bindir/python3-generate-subunit
%_bindir/python3-ostestr
%_bindir/python3-subunit-trace
%_bindir/python3-subunit2html
%python3_sitelibdir/os_testr
%python3_sitelibdir/os_testr-*.egg-info
%endif

%files doc
%doc doc/build/html

%changelog
* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 0.6.0-alt1
- Initial build for ALT (based on CentOS 0.6.0-1.el7.src)

