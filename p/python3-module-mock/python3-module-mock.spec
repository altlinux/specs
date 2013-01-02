%define modulename mock

Name: python3-module-mock
Version: 0.8.0
Release: alt1
Summary: A Python mock object library

Group: Development/Python
License: Apache License 2.0
Url: http://code.google.com/p/mock/

Source: %modulename-%version.tar

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires:  python3-devel

%description
Mock is a Python module that provides a core Mock class. It is intended to
reduce the need for creating a host of trivial stubs throughout your test suite.
After performing an action, you can make assertions about which methods /
attributes were used and arguments they were called with. You can also specify
return values and set needed attributes in the normal way.

%prep
%setup -q -n %{modulename}-%{version}

%build
%python3_build

%install
%python3_install

%files
%doc docs/ README.txt PKG-INFO LICENSE.txt
%{python3_sitelibdir_noarch}/*.egg-info
%{python3_sitelibdir_noarch}/%{modulename}.py*
%{python3_sitelibdir_noarch}/__pycache__/%{modulename}*

%changelog
* Wed Jan 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt1
- 0.8.0
