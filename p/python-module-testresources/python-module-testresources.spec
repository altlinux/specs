%global pypi_name testresources
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.2.7
Release:        alt1.1
Summary:        Testresources, a pyunit extension for managing expensive test resources

Group:		Development/Python
License:        ASL 2.0 and BSD and GPLv2+
# file testresources/tests/TestUtil.py is GPLv2+
URL:            https://launchpad.net/testresources
Source0:        %{name}-%{version}.tar
BuildArch:      noarch
 
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-mimeparse python-module-pbr python-module-unittest2 python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-unittest2 rpm-build-python3

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-testtools
#BuildRequires:  python-module-fixtures

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        Testresources, a pyunit extension for managing expensive test resources
Group:		Development/Python
BuildArch:      noarch
#BuildRequires:  rpm-build-python3
#BuildRequires:  python3-module-setuptools
#BuildRequires:  python3-module-testtools
#BuildRequires:  python3-module-fixtures

%description -n python3-module-%{pypi_name}
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%endif

%prep
%setup
# Remove bundled egg-info
rm -rf lib/%{pypi_name}.egg-info

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

# %check
# %{__python} setup.py test


%files
%doc README NEWS doc
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README NEWS doc
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1.1
- NMU: Use buildreq for BR.

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.7-alt1
- First build for ALT (based on Fedora 0.2.7-6.fc21.src)

