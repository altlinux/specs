%define _unpackaged_files_terminate_build 1
%define oname multienum

Name: python3-module-%oname
Version: 0.2.4
Release: alt2

Summary: Enumerator type supporting multiple equivalent names
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/multienum/
BuildArch: noarch

# https://github.com/sorreltree/multienum.git
Source0: https://pypi.python.org/packages/9d/89/95b37cffa32113a49506ba38821aa6ca53829861c92e01d89d7a5c14ee53/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose

%py3_provides %oname


%description
An enumeration type supporting multiple equivalent names.

%prep
%setup -q -n %{oname}-%{version}


%build
%python3_build_debug

%install
%python3_install
install -p -m644 %oname.py %buildroot%python3_sitelibdir/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.4-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.2.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt1.b.git20150202.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.b.git20150202
- Initial build for Sisyphus

