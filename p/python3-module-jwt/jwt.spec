%define _unpackaged_files_terminate_build 1
%define oname jwt

Name: python3-module-%oname
Version: 2.6.0
Release: alt1
Summary: JSON Web Token implementation in Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/PyJWT/

# https://github.com/progrium/pyjwt.gi
Source0: https://files.pythonhosted.org/packages/75/65/db64904a7f23e12dbf0565b53de01db04d848a497c6c9b87e102f74c9304/PyJWT-2.6.0.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
A Python implementation of JSON Web Token draft 01.

%prep
%setup -n PyJWT-%{version}

%build
export LC_ALL=en_US.UTF-8
%python3_build

%install
export LC_ALL=en_US.UTF-8
%python3_install

%files
%doc AUTHORS* *.md
%python3_sitelibdir/*

%changelog
* Tue Jan 24 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.6.0-alt1
- 2.6.0 released

* Thu Jul 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.4.0-alt1
- 2.4.0 released

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.3.0-alt1
- 2.3.0 released

* Mon Oct 04 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.1.0-alt1
- 2.1.0 released

* Tue Aug 03 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.1-alt2
- Drop python2 support.

* Fri Nov 29 2019 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.7.1-alt1
- 1.7.1 released

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20150118
- Version 0.4.1

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20140922
- Initial build for Sisyphus

