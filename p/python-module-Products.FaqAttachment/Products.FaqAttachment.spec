%define oname Products.FaqAttachment
Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20130429
Summary: Attachment support for Products.Faq
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.FaqAttachment/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RedTurtle/Products.FaqAttachment.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.Faq python-module-unittest2
BuildPreReq: python-module-archetypes.schemaextender

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.Faq archetypes.schemaextender

%description
Adding this product to you Plone buildout, and a new attachment field
will be added to every Faq content. You can use this to provide
additional informations to the Faq itself.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20130429
- Initial build for Sisyphus

