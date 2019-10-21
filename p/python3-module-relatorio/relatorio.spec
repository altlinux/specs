%define _unpackaged_files_terminate_build 1
%define oname relatorio

%def_without check

Name: python3-module-%oname
Version: 0.9.0
Release: alt1

Summary: A templating library able to output odt and pdf files
License: GPL
Group: Development/Python3
Url: https://pypi.python.org/pypi/relatorio/

Source0: https://pypi.python.org/packages/18/de/18b3e8d004e43f86884c5c6148d4b15b86d07a267f45835c684deb2a4c06/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools

%py_provides %oname

%description
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
A templating library which provides a way to easily output all kind of
different files (odt, ods, png, svg, ...). Adding support for more
filetype is easy: you just have to create a plugin for this.

relatorio also provides a report repository allowing you to link python
objects and report together, find reports by mimetypes/name/python
objects.

This package contains tests for %oname.

%prep
%setup -q -n %{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%if_with check
%check
python3 setup.py test
%endif

%files
%doc AUTHORS CHANGES LICENSE README examples/
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Oct 18 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.9.0-alt1
- Version updated to 0.9.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.6.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.4-alt1
- automated PyPI update

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt3
- Fixed build

* Tue Oct 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt2
- Moved tests into separate package

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus

