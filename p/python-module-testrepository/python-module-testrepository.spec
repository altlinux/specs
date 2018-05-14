%global pypi_name testrepository

Name:           python-module-%{pypi_name}
Version:        0.0.20
Release:        alt2

Summary:        A repository of test results
Group:          Development/Python
License:        ASL 2.0
URL:            https://launchpad.net/testrepository
BuildArch:      noarch

Source0:        %{name}-%{version}.tar

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-numpy python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-mimeparse python-module-pbr 
BuildRequires: python-module-unittest2 python-module-fixtures
BuildRequires: python-module-subunit python-module-testtools
BuildRequires: python-module-extras

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-mimeparse
BuildPreReq: python3-module-pbr python3-module-unittest2
BuildPreReq: python3-module-fixtures python3-module-subunit
BuildPreReq: python3-module-testtools python3-module-extras

%description
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%package -n python3-module-%{pypi_name}
Summary:        A repository of test results
Group:		Development/Python
BuildArch:      noarch

%description -n python3-module-%{pypi_name}
Provides a database of test results which can be used to
support easy developer workflows, supporting functionality
like isolating failing tests. Testrepository is compatible
with any test suite that can output subunit. This includes any
TAP test suite and any pyunit compatible test suite.

%prep
%setup
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
pushd ../python3
%python3_install
mv %{buildroot}%{_bindir}/testr %{buildroot}%{_bindir}/python3-testr
popd

%python_install

%files
%doc README.txt Apache-2.0
%{_bindir}/testr
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-module-%{pypi_name}
%doc README.txt Apache-2.0
%{_bindir}/python3-testr
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.0.20-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.20-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

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

