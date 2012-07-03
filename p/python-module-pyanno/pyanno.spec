%define oname pyanno
Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20120109
Summary: Package for curating data annotation efforts
License: BSD
Group: Development/Python
Url: https://github.com/enthought/uchicago-pyanno
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/enthought/uchicago-pyanno.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-sphinx-devel

%description
pyAnno 2.0 is a Python library for the analysis and
diagnostic testing of annotation and curation
efforts. pyAnno implements statistical models for
inferring from categorical data annotated by multiple
annotators

    * annotator accuracies and biases,
    * gold standard categories of items,
    * prevalence of categories in population, and
    * population distribution of annotator accuracies
      and biases.

%package tests
Summary: Tests for pyAnno
Group: Development/Python
Requires: %name = %version-%release

%description tests
pyAnno 2.0 is a Python library for the analysis and
diagnostic testing of annotation and curation
efforts. pyAnno implements statistical models for
inferring from categorical data annotated by multiple
annotators

    * annotator accuracies and biases,
    * gold standard categories of items,
    * prevalence of categories in population, and
    * population distribution of annotator accuracies
      and biases.

This package contains tests for pyAnno.

%package pickles
Summary: Pickles for pyAnno
Group: Development/Python

%description pickles
pyAnno 2.0 is a Python library for the analysis and
diagnostic testing of annotation and curation
efforts. pyAnno implements statistical models for
inferring from categorical data annotated by multiple
annotators

    * annotator accuracies and biases,
    * gold standard categories of items,
    * prevalence of categories in population, and
    * population distribution of annotator accuracies
      and biases.

This package contains pickles for pyAnno.

%package docs
Summary: Documentation for pyAnno
Group: Development/Documentation

%description docs
pyAnno 2.0 is a Python library for the analysis and
diagnostic testing of annotation and curation
efforts. pyAnno implements statistical models for
inferring from categorical data annotated by multiple
annotators

    * annotator accuracies and biases,
    * gold standard categories of items,
    * prevalence of categories in population, and
    * population distribution of annotator accuracies
      and biases.

This package contains documentation for pyAnno.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source

%build
%python_build_debug

%install
%python_install

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

cp -fR ../pyanno-docs/pickle %buildroot%python_sitelibdir/%oname

%files
%doc LICENSE.txt README
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/test
%exclude %python_sitelibdir/%oname/pickle

%files tests
%python_sitelibdir/%oname/test

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc ../pyanno-docs/html data

%changelog
* Thu Jan 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20120109
- Version 2.0.1

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.git20111123
- Initial build for Sisyphus

