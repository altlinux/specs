%global pypi_name mock
%def_with python3

Name: python-module-%{pypi_name}
Version: 1.0.1
Release: alt1
Summary: A Python Mocking and Patching Library for Testing

Group: Development/Python
License: BSD
Url: https://pypi.python.org/pypi/%{pypi_name}
Packager: Vitaly Kuznetsov <vitty@altlinux.ru>

Source: %name-%version.tar

BuildArch: noarch
BuildRequires: python-devel

%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        A Python Mocking and Patching Library for Testing
Group:		Development/Python
BuildArch:      noarch
BuildRequires:  rpm-build-python3

%description -n python3-module-%{pypi_name}
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

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
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%python_install

%files
%doc docs/ README.txt PKG-INFO LICENSE.txt
%{python_sitelibdir}/*.egg-info
%{python_sitelibdir}/%{pypi_name}.py*

%if_with python3
%files -n python3-module-mock
%doc docs/ README.txt PKG-INFO LICENSE.txt
%{python3_sitelibdir}/*.egg-info
%{python3_sitelibdir}/%{pypi_name}.py*
%{python3_sitelibdir}/__pycache__/%{pypi_name}*
%endif

%changelog
* Fri Aug 29 2014 Lenar Shakirov <snejok@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- 0.8.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt2
- Rebuild with Python-2.7

* Mon Oct 17 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.2-alt1
- 0.7.2

* Mon Mar 14 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt1
- Initial
