%def_with python3

%global oname ddt

Name: python-module-ddt
Version: 1.1.1
Release: alt1
Summary: A Python library to multiply test cases
Group: Development/Python
License: MIT
Url: https://github.com/txels/ddt

# https://github.com/txels/ddt.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires: rpm-build-python
BuildRequires: python-module-setuptools
BuildRequires: python-module-nose python-module-json
BuildRequires: python-module-six >= 1.4.0
BuildRequires: python-module-mock
BuildRequires: python-module-yaml

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-nose
BuildRequires: python3-module-six >= 1.4.0
BuildRequires: python3-module-mock
BuildRequires: python3-module-yaml
%endif

%description
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.

%if_with python3
%package -n python3-module-%oname
Summary: Data-Driven/Decorated Tests
Group: Development/Python

%description -n python3-module-%oname
DDT (Data-Driven Tests) allows you to multiply one test case by running it with
different test data, and make it appear as multiple test cases.  It is used in
combination with other testing frameworks like unittest and nose.
%endif

%prep
%setup

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
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
nosetests-%__python_version
%if_with python3
nosetests-%__python3_version
%endif

%files
%doc README.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.1-alt1
- Updated to upstream version 1.1.1.

* Mon Nov 14 2016 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- Initial build for ALT (based on CentOS 1.0.1-2.el7.src)
