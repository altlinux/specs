%define _unpackaged_files_terminate_build 1
%define oname whois
%define pypi_name python-whois

%def_with check

Name: python3-module-%pypi_name
Version: 0.9.4
Release: alt1

Summary: Whois querying and parsing of domain registration information
License: MIT
Group: Development/Python3
Url: https://pypi.org/project/python-whois
BuildArch: noarch

Provides: python3-module-%oname = %EVR
Obsoletes: python3-module-%oname < %EVR

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-dateutil
%endif

%description
Whois querying and parsing of domain registration information.

Goal:
* Create a simple importable Python module which will produce parsed
  WHOIS data for a given domain.
* Able to extract data for all the popular TLDs (com, org, net, ...)
* Query a WHOIS server directly instead of going through an intermediate
  web service like many others do.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
# disable online tests
%pyproject_run_pytest -v -k "\
not test_ipv4 \
and not test_ipv6 \
and not test-il_parse \
and not test_choose_server \
and not test_simple_ascii_domain \
and not test_simple_unicode_domain"

%files
%doc README.*
%python3_sitelibdir/%oname
%python3_sitelibdir/python_whois-%version.dist-info


%changelog
* Wed May 22 2024 Anton Vyatkin <toni@altlinux.org> 0.9.4-alt1
- new version 0.9.4
- rename package to use PyPI name

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

