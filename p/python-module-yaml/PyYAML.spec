%define project PyYAML

%def_with python3

Name: python-module-yaml
Version: 3.10
Release: alt2

Summary: PyYAML, a YAML parser and emitter for Python
License: MIT/X Consortium
Group: Development/Python
Url: http://pyyaml.org/
#BuildArch: noarch

Source: %project-%version.tar

BuildRequires: python-devel libyaml-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
YAML is a data serialization format designed for human readability
and interaction with scripting languages.

PyYAML is a YAML parser and emitter for the Python programming
language.  PyYAML features a complete YAML 1.1 parser, Unicode
support, and relatively sensible error messages.

%if_with python3
%package -n python3-module-yaml
Summary: PyYAML, a YAML parser and emitter for Python3
Group: Development/Python3

%description -n python3-module-yaml
YAML is a data serialization format designed for human readability
and interaction with scripting languages.

PyYAML is a YAML parser and emitter for the Python3 programming
language.  PyYAML features a complete YAML 1.1 parser, Unicode
support, and relatively sensible error messages.
%endif

%prep
%setup -n %project-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing

%python_build build_ext
%if_with python3
pushd ../python3
%python3_build build_ext
popd
%endif

%install
%python_install --record=INSTALLED_FILES
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc CHANGES README
%dir %python_sitelibdir/yaml
#python_sitelibdir/*

%if_with python3
%files -n python3-module-yaml
%python3_sitelibdir/*
%endif

%changelog
* Sat Apr 07 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt2
- Dont' rename _yaml.*.so -> _yaml.so

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.10-alt1
- Version 3.10
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.05-alt2.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.05-alt2.1
- Rebuilt with python 2.6

* Sun Jul 20 2008 Alexander Myltsev <avm@altlinux.ru> 3.05-alt2
- Fix #16285 (package lost directory).
- Pull a minor bugfix from SVN (a single dot is not a valid float).

* Fri Nov 16 2007 Alex V. Myltsev <avm@altlinux.ru> 3.05-alt1
- Initial build for Sisyphus.

