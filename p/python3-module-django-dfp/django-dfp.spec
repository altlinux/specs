%define _unpackaged_files_terminate_build 1
%define oname django-dfp

Name: python3-module-%oname
Version: 0.4.1
Release: alt2

Summary: DFP implementation for Django
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/django-dfp/
BuildArch: noarch

# https://github.com/praekelt/django-dfp.git
Source0: https://pypi.python.org/packages/e5/7b/dcce10c6192402aed8e0907b1f5e8b69d007066768d9c45085c9ce95f8cf/%{oname}-%{version}.tar.gz
Patch0: porting-on-python3.patch

BuildRequires(pre): rpm-build-python3


%description
App that provides tags to fetch Google DFP ads.

%prep
%setup -q -n %{oname}-%{version}
%patch -p2

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Wed Dec 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.1-alt2
- porting on python3

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.2-alt1.git20140721.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.git20140721
- Initial build for Sisyphus

