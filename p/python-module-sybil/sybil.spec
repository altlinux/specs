%define  oname sybil
%def_with python3

Name:    python-module-%oname
Version: 1.0.5
Release: alt1

Summary:  Automated testing for the examples in your documentation.
License: MIT
Group:   Development/Python
URL:     https://github.com/cjw296/sybil

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(nose.core)
BuildRequires: python-module-sphinx-devel python2.7(pkginfo)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(nose.core)
%endif

# https://github.com/cjw296/sybil.git
Source:  %oname-%version.tar.gz

%description
Automated testing for the examples in your documentation.

%if_with python3
%package -n python3-module-%oname
Group: Development/Python3
Summary:        Automated testing for the examples in your documentation.

%description -n python3-module-%oname
Automated testing for the examples in your documentation.
%endif

%prep
%setup -n %oname-%version

%if_with python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

PYTHONPATH=$(pwd) %make -C docs html SPHINXBUILD=sphinx-build
mv docs/_build/html ./
rm -rf docs/_build

%check
PYTHONPATH=$(pwd) py.test

%if_with python3
pushd ../python3
PYTHONPATH=$(pwd) py.test3
popd
%endif

%files
%doc README.rst docs html
%python_sitelibdir/%oname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%oname
%doc README.rst docs html
%python3_sitelibdir/%oname/
%python3_sitelibdir/*.egg-info
%endif

%changelog
* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.
