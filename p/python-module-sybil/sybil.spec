%define _unpackaged_files_terminate_build 1

%def_with python3

%define  oname sybil

Name:    python-module-%oname
Version: 1.0.9
Release: alt2

Summary:  Automated testing for the examples in your documentation.
License: MIT
Group:   Development/Python
URL:     https://github.com/cjw296/sybil

BuildArch: noarch

BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(nose.core)
BuildRequires: python2.7(pytest)
BuildRequires: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3(nose.core)
BuildRequires: python3(pytest)
%endif

# https://github.com/cjw296/sybil.git
Source:  %oname-%version.tar

Patch: %oname-%version-%release.patch
Patch1: %oname-1.0.7-alt-docs.patch


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
%patch -p1
%patch1 -p1

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

PYTHONPATH=$(pwd) NAME=%oname VERSION=%version %make -C docs html SPHINXBUILD=sphinx-build
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
* Sun Jan 13 2019 Ivan A. Melnikov <iv@altlinux.org> 1.0.9-alt2
- Update tests to fix FTBFS.

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.9-alt1.qa1
- NMU: applied repocop patch

* Thu Aug 30 2018 Stanislav Levin <slev@altlinux.org> 1.0.9-alt1
- 1.0.7 -> 1.0.9.

* Thu Jun 07 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt2
- Fixed documentation build.

* Thu Mar 01 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.7-alt1
- Updated to upstream version 1.0.7.

* Wed Aug 23 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.5-alt1
- Initial build for ALT.
