%define oname ZPublisherEventsBackport
Name: python-module-%oname
Version: 1.1
Release: alt1
Summary: Backport publication events from Zope 2.12 ZPublisher to Zope 2.10
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ZPublisherEventsBackport/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.monkeypatcher

%py_provides %oname
Requires: python-module-Zope2
%py_requires collective.monkeypatcher

%description
Backport publication events from Zope 2.12 ZPublisher to Zope 2.10.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test

%files
%python_sitelibdir/*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

