# Created by pyp2rpm-1.0.1
%global pypi_name testrepository
%def_with python3

Name:           python-module-%{pypi_name}
Version:        0.0.20
Release:        alt1.1
Summary:        A repository of test results
Group:          Development/Python

License:        ASL 2.0
URL:            https://launchpad.net/testrepository
Source0:        %{name}-%{version}.tar
BuildArch:      noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-numpy python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-mimeparse python-module-pbr python-module-unittest2 python3-module-html5lib python3-module-mimeparse python3-module-pbr python3-module-unittest2 rpm-build-python3

#BuildRequires:  python-devel
#BuildRequires:  python-module-setuptools
#BuildRequires:  python-module-fixtures
#buildRequires:  python-module-python-subunit
#BuildRequires:  python-module-testtools
#BuildRequires:  python-module-extras

Requires:       python-module-fixtures
Requires:       python-module-python-subunit
Requires:       python-module-testtools
Requires:       python-module-extras

%description
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%if_with python3
%package -n python3-module-%{pypi_name}
Summary:        A repository of test results
Group:		Development/Python
BuildArch:      noarch
#BuildRequires:  rpm-build-python3
#BuildRequires:  python3-module-setuptools
#BuildRequires:  python3-module-fixtures
#buildRequires:  python3-module-python-subunit
#BuildRequires:  python3-module-testtools
#BuildRequires:  python3-module-extras

Requires:       python3-module-fixtures
Requires:       python3-module-python-subunit
Requires:       python3-module-testtools
Requires:       python3-module-extras

%description -n python3-module-%{pypi_name}
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%endif

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

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
mv %{buildroot}%{_bindir}/testr %{buildroot}%{_bindir}/python3-testr
popd
%endif

%python_install

%files
%doc README.txt Apache-2.0
%{_bindir}/testr
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%if_with python3
%files -n python3-module-%{pypi_name}
%doc README.txt Apache-2.0
%{_bindir}/python3-testr
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.0.20-alt1.1
- NMU: Use buildreq for BR.

* Tue Aug 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.20-alt1
- Version 0.0.20

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt3
- Enable python3

* Mon Aug 18 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt2
- BuildReq: python-module-subunit -> python-module-python-subunit

* Sat Aug 16 2014 Lenar Shakirov <snejok@altlinux.ru> 0.0.18-alt1
- First build for ALT (based on Fedora 0.0.18-1.fc21.src)

