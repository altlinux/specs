%define _unpackaged_files_terminate_build 1
%define oname whois

%def_disable check

Name: python3-module-%oname
Version: 0.6.4
Release: alt2

Summary: Whois querying and parsing of domain registration information
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-whois
BuildArch: noarch

Source0: https://pypi.python.org/packages/4e/7d/dafe428145b6e712d12442abef54167e530ba54bf7ae6cf9e654233eabfb/python-%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-pytest

%py3_provides %oname


%description
Whois querying and parsing of domain registration information.

Goal:
* Create a simple importable Python module which will produce parsed
  WHOIS data for a given domain.
* Able to extract data for all the popular TLDs (com, org, net, ...)
* Query a WHOIS server directly instead of going through an intermediate
  web service like many others do.
* Works with Python 2.4+ and no external dependencies

%prep
%setup -q -n python-%{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test -v

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Nov 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.6.4-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4-alt1.1
- NMU: Use buildreq for BR.

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

