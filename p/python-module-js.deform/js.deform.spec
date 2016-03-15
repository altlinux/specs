%define oname js.deform

%def_with python3

Name: python-module-%oname
Version: 2.0
Release: alt1.a2.2.git20140519.1
Summary: Fanstatic packaging of deform
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/js.deform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Kotti/js.deform.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname
%py_requires js.jquery js.jquery_form js.jquery_maskedinput
%py_requires js.jquery_maskmoney js.jquery_sortable js.tinymce
%py_requires js.jquery_timepicker_addon js.jqueryui js.modernizr
%py_requires js.typeahead deform shutilwhich

%description
This library packages deform for fanstatic.

%package -n python3-module-%oname
Summary: Fanstatic packaging of deform
Group: Development/Python3
%py3_provides %oname
%py3_requires js.jquery js.jquery_form js.jquery_maskedinput
%py3_requires js.jquery_maskmoney js.jquery_sortable js.tinymce
%py3_requires js.jquery_timepicker_addon js.jqueryui js.modernizr
%py3_requires js.typeahead deform shutilwhich

%description -n python3-module-%oname
This library packages deform for fanstatic.

%prep
%setup

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

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0-alt1.a2.2.git20140519.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a2.2.git20140519
- Initial build for Sisyphus

