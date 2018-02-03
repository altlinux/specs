%define oname lorem-ipsum-generator
Name: python-module-%oname
Version: 0.3
Release: alt1.svn20090927.1
Summary: Generates random lorem ipsum text
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lorem-ipsum-generator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://lorem-ipsum-generator.googlecode.com/svn/trunk/
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools
BuildPreReq: python-module-pygtk

%py_provides lipsum
Requires: %oname = %EVR
%py_requires gtk.glade

%description
Lorem Ipsum Generator provides a GTK+ graphical user interface, and a
Python module, that generates random "lorem ipsum" text. The Lorem Ipsum
Generator can produce a given quantity of paragraphs or sentences of
"lorem ipsum" text.

%package -n %oname
Summary: Generates random lorem ipsum text
Group: Text tools

%description -n %oname
Lorem Ipsum Generator provides a GTK+ graphical user interface, and a
Python module, that generates random "lorem ipsum" text. The Lorem Ipsum
Generator can produce a given quantity of paragraphs or sentences of
"lorem ipsum" text.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%check
python setup.py test
python src/testlipsum.py

%files
%doc README TODO
%python_sitelibdir/*

%files -n %oname
%_bindir/*
%_desktopdir/*

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3-alt1.svn20090927.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sat Dec 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.svn20090927
- Initial build for Sisyphus

