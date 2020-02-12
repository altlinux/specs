%define _unpackaged_files_terminate_build 1
%define oname pkgconfig

Name: python3-module-%oname
Version: 1.2.2
Release: alt2

Summary: Interface Python with pkg-config
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pkgconfig/
BuildArch: noarch

# https://github.com/matze/pkgconfig.git
Source0: https://pypi.python.org/packages/9d/ba/80910bbed2b4e646a6adab4474d2e506744c260c7002a0e6b41ef8750d8d/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
pkgconfig is a Python module to interface with the pkg-config command
line tool and supports Python 2.6+.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3 -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.2.2-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20141212.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20141212
- Initial build for Sisyphus

