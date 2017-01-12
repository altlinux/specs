%define _unpackaged_files_terminate_build 1
%define oname dicttoxml

%def_with python3

Name: python-module-%oname
Version: 1.7.4
Release: alt1
Summary: Converts a Python dictionary or other native data type into a valid XML string
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/dicttoxml/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/quandyfactory/dicttoxml.git
Source0: https://pypi.python.org/packages/74/36/534db111db9e7610a41641a1f6669a964aacaf51858f466de264cc8dcdd9/%{oname}-%{version}.tar.gz
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel rpm-build-python3

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

%package -n python3-module-%oname
Summary: Converts a Python dictionary or other native data type into a valid XML string
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
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
%setup -q -n %{oname}-%{version}

rm -fR dist

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.markdown
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.markdown
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.7.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.8-alt1.git20150106.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.8-alt1.git20150106.1
- NMU: Use buildreq for BR.

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.8-alt1.git20150106
- Initial build for Sisyphus

