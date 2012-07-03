%define oname ordereddict
Name: python-module-%oname
Version: 1.1
Release: alt1.1
Summary: A drop-in substitute for Py2.7's new collections.OrderedDict
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/ordereddict/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-%version.tar.gz

BuildPreReq: python-devel
BuildArch: noarch

%description
Drop-in substitute for Py2.7's new collections.OrderedDict. The recipe
has big-oh performance that matches regular dictionaries (amortized O(1)
insertion/deletion/lookup and O(n)
iteration/repr/copy/equality_testing).

%prep
%setup

%build
%python_build

%install
%python_install

%files
%python_sitelibdir/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt1.1
- Rebuild with Python-2.7

* Tue Sep 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

