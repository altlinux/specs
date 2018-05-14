%global pypi_name testresources

Name:           python-module-%{pypi_name}
Version:        0.2.7
Release:        alt2
Summary:        Testresources, a pyunit extension for managing expensive test resources

Group:		Development/Python
License:        ASL 2.0 and BSD and GPLv2+
# file testresources/tests/TestUtil.py is GPLv2+
URL:            https://launchpad.net/testresources
Source0:        %{name}-%{version}.tar
BuildArch:      noarch
 
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-cffi python-module-cryptography python-module-enum34 python-module-pyasn1 python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-unittest python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-setuptools
BuildRequires: python-module-mimeparse python-module-pbr
BuildRequires: python-module-testtools python-module-fixtures
BuildRequires: python-module-unittest2

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-html5lib python3-module-mimeparse
BuildPreReq: python3-module-pbr python3-module-unittest2
BuildPreReq: python3-module-testtools python3-module-fixtures


%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%package -n python3-module-%{pypi_name}
Summary:        Testresources, a pyunit extension for managing expensive test resources
Group:		Development/Python
BuildArch:      noarch

%description -n python3-module-%{pypi_name}
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%prep
%setup
# Remove bundled egg-info
rm -rf lib/%{pypi_name}.egg-info

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
%{__python} setup.py test

%files
%doc README NEWS doc
%{python_sitelibdir}/%{pypi_name}
%{python_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-module-%{pypi_name}
%doc README NEWS doc
%{python3_sitelibdir}/%{pypi_name}
%{python3_sitelibdir}/%{pypi_name}-%{version}-py?.?.egg-info


%changelog
* Mon May 14 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.2.7-alt2
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.7-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.7-alt1.1
- NMU: Use buildreq for BR.

* Mon Jul 21 2014 Lenar Shakirov <snejok@altlinux.ru> 0.2.7-alt1
- First build for ALT (based on Fedora 0.2.7-6.fc21.src)

