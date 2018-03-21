%define oname sphinxcontrib-websupport
%def_with python3
%def_disable check

Name:           python-module-%oname
Version:        1.0.1
Release:        alt2%ubt
Summary:        Sphinx API for Web Apps
License:        BSD
Group:          Development/Python
BuildArch:      noarch
URL:            http://sphinx-doc.org/

# https://github.com/sphinx-doc/sphinxcontrib-websupport.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-ubt
BuildRequires: python-dev python-module-docutils python-module-jinja2 python-module-mock python-module-pytest
BuildRequires: python-module-setuptools python-module-six python-module-sphinx python2.7(sqlalchemy)
BuildRequires: python-module-whoosh python-module-xapian
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-docutils python3-module-jinja2 python3-module-mock python3-module-pytest
BuildRequires: python3-module-setuptools python3-module-six python3-module-sphinx python3(sqlalchemy)
BuildRequires: python3-module-whoosh python3-module-xapian
%endif

%description
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.

%if_with python3
%package -n python3-module-%oname
Summary: Sphinx API for Web Apps
Group: Development/Python3

%description -n python3-module-%oname
sphinxcontrib-websupport provides a Python API to easily integrate Sphinx
documentation into your Web application.
%endif

%prep
%setup

%if_with python3
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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
py.test tests/

%if_with python3
pushd ../python3
py.test3 tests/
popd
%endif

%files
%doc LICENSE README.rst
%python_sitelibdir/sphinxcontrib/websupport
%python_sitelibdir/sphinxcontrib_websupport-%{version}*-py?.?-*.pth
%python_sitelibdir/sphinxcontrib_websupport-%{version}*-py?.?.egg-info

%if_with python3
%files -n python3-module-%oname
%doc LICENSE README.rst
%python3_sitelibdir/sphinxcontrib/websupport
%python3_sitelibdir/sphinxcontrib_websupport-%{version}*-py?.?-*.pth
%python3_sitelibdir/sphinxcontrib_websupport-%{version}*-py?.?.egg-info
%endif

%changelog
* Wed Mar 21 2018 Stanislav Levin <slev@altlinux.org> 1.0.1-alt2%ubt
- Rebuild with new setuptools to fix namespace package

* Thu Oct 12 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.1-alt1
- Initial build for ALT.

* Wed Oct 11 2017 Troy Dawson <tdawson@redhat.com> - 1.0.1-3
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 30 2017 Javier Peña <jpena@redhat.com> - 1.0.1-1
- Initial package.
