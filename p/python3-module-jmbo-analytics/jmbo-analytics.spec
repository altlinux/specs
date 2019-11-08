%define _unpackaged_files_terminate_build 1
%define oname jmbo-analytics

Name: python3-module-%oname
Version: 0.2.2
Release: alt2

Summary: Jmbo analytics app
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/jmbo-analytics/
# https://github.com/praekelt/jmbo-analytics.git
BuildArch: noarch

Source0: https://pypi.python.org/packages/3f/02/3ed82c068b9ff75ab03419389ebc8cd91e0cf4699b7f2e0738dcf6b64e0c/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3

%add_python3_req_skip django.core.urlresolvers


%description
panomena-analytics
http://unomena.com

%prep
%setup -q -n %{oname}-%{version}

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Fri Nov 08 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.2.2-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.2.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20120507.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20120507
- Initial build for Sisyphus

