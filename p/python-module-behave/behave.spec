%define oname behave

%def_with python3

Name: python-module-%oname
Version: 1.2.5
Release: alt1.a1.git20141018.1.1.1
Summary: behave is behaviour-driven development, Python style
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/behave/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/behave/behave.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-parse python-module-parse_type
BuildPreReq: python-module-six python-module-nose
BuildPreReq: python-module-mock python-module-hamcrest
BuildPreReq: python-module-argparse python-module-tox
BuildPreReq: python-module-coverage python-module-jsonschema
BuildPreReq: python-module-simplejson python-module-ordereddict
BuildPreReq: python-module-sphinx-devel python-module-Pygments-tests
BuildPreReq: python-module-sphinxcontrib-cheeseshop
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-parse python3-module-parse_type
BuildPreReq: python3-module-six python3-module-nose
BuildPreReq: python3-module-mock python3-module-hamcrest
BuildPreReq: python3-module-argparse python3-module-tox
BuildPreReq: python3-module-coverage python3-module-jsonschema
BuildPreReq: python3-module-simplejson
%endif

%py_provides %oname
Requires: %oname-common = %EVR
%py_requires json parse parse_type simplejson ordereddict
%add_python_req_skip gherkin

%description
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

%package -n %oname-common
Summary: Common files for Python 2 & 3 modules
Group: Development/Python

%description -n %oname-common
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains common files for Python 2 & 3 modules.

%package -n python3-module-%oname
Summary: behave is behaviour-driven development, Python style
Group: Development/Python3
%py3_provides %oname
Requires: %oname-common = %EVR
%py3_requires json parse parse_type simplejson
%add_python3_req_skip gherkin
%add_python3_req_skip gherkin.formatter
%add_python3_req_skip gherkin.tag_expression

%description -n python3-module-%oname
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Behavior-driven development (or BDD) is an agile software development
technique that encourages collaboration between developers, QA and
non-technical or business participants in a software project.

behave uses tests written in a natural language style, backed up by
Python code.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

install -d %buildroot%_sysconfdir
cp -fR etc/* %buildroot%_sysconfdir/

%make -C docs pickle
%make -C docs html

cp -fR build/docs/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst *features
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc build/docs/html/*

%files -n %oname-common
%_sysconfdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst *features
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Sat Feb 03 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1.1
- (NMU) Fix Requires to gherkin

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.2.5-alt1.a1.git20141018.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.2.5-alt1.a1.git20141018.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.5-alt1.a1.git20141018
- Initial build for Sisyphus

