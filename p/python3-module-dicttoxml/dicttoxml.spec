%define _unpackaged_files_terminate_build 1
%define oname dicttoxml

Name: python3-module-%oname
Version: 1.7.4
Release: alt2
Summary: Converts a Python dictionary or other native data type into a valid XML string
License: GPLv2
Group: Development/Python3
Url: https://pypi.python.org/pypi/dicttoxml/

# https://github.com/quandyfactory/dicttoxml.git
Source0: https://pypi.python.org/packages/74/36/534db111db9e7610a41641a1f6669a964aacaf51858f466de264cc8dcdd9/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

%description
Converts a Python dictionary or other native data type into a valid XML
string.

Supports item (int, float, long, bool, str, unicode, datetime, none) and
collection (list, set, tuple and dict, as well as iterable and dict-like
objects) data types, with arbitrary nesting for the collections. Items
with a datetime type are converted to ISO format strings. Items with a
none type become empty XML elements.

The root object passed into the dicttoxml method can be any of the
supported data types.

%prep
%setup -n %{oname}-%{version}

rm -fR dist

%build
%python3_build

%install
%python3_install

%files
%doc *.markdown
%python3_sitelibdir/*

%changelog
* Wed Jul 28 2021 Grigory Ustinov <grenka@altlinux.org> 1.7.4-alt2
- Drop python2 support.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.8-alt1.git20150106.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.8-alt1.git20150106.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.8-alt1.git20150106
- Initial build for Sisyphus

