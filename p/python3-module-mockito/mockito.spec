%define _unpackaged_files_terminate_build 1

%define oname mockito

Name: python3-module-%oname
Version: 0.7.1
Release: alt2

Summary: Spying framework
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/mockito/
BuildArch: noarch

Source0: https://pypi.python.org/packages/a8/20/ee40b6b6c6ee28b0358c677822c784ba51715f0369873b8e3acc50ea417a/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose
BuildRequires: python-tools-2to3

%py3_provides %oname


%description
Mockito is a spying framework based on Java library with the same name.

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc AUTHORS *.rst
%python3_sitelibdir/*


%changelog
* Mon Feb 10 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.7.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.7.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.2-alt1
- Initial build for Sisyphus

