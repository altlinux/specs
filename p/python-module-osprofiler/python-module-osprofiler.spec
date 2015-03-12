%define sname osprofiler

%def_with python3

Name: python-module-%sname
Version: 0.3.0
Release: alt1
Summary: OpenStack cross-project profiling library
Group: Development/Python
License: ASL 2.0
Url: https://github.com/openstack/%sname
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-pbr >= 0.6
BuildRequires: python-module-d2to1
BuildRequires: python-module-six >= 1.7.0
BuildRequires: python-module-sphinx
BuildRequires: python-module-oslosphinx
BuildRequires: python-module-argparse
BuildRequires: python-module-webob >= 1.2.3

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-pbr >= 0.6
BuildRequires: python3-module-d2to1
BuildRequires: python3-module-six >= 1.7.0
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-oslosphinx
BuildRequires: python3-module-argparse
BuildRequires: python3-module-webob >= 1.2.3

%endif

BuildArch: noarch

%description
OSProfiler is an OpenStack cross-project profiling library.

%if_with python3
%package -n python3-module-%sname
Summary: OpenStack cross-project profiling library
Group: Development/Python3

%description -n python3-module-%sname
OSProfiler is an OpenStack cross-project profiling library.
%endif


%package doc
Summary: Documentation for OpenStack cross-project profiling library
Group: Development/Documentation

%description doc
Documentation for OSProfiler is an OpenStack cross-project profiling library.

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/%sname %buildroot%_bindir/python3-%sname
popd
%endif
%python_install

# Delete tests
rm -fr %buildroot%python_sitelibdir/tests
rm -fr %buildroot%python_sitelibdir/*/tests
rm -fr %buildroot%python3_sitelibdir/tests
rm -fr %buildroot%python3_sitelibdir/*/tests

export PYTHONPATH="$( pwd ):$PYTHONPATH"
pushd doc
sphinx-build -b html -d build/doctrees   source build/html
popd

# Fix hidden-file-or-dir warnings
rm -fr doc/build/html/.buildinfo

%files
%doc AUTHORS ChangeLog LICENSE PKG-INFO README.rst
%python_sitelibdir/*
%_bindir/%sname

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%_bindir/python3-%sname
%endif

%files doc
%doc doc/build/html

%changelog
* Thu Mar 12 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3.0-alt1
- Initial release
