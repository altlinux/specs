%define oname elixir
Name:           python-module-%oname
Version:        0.8.0
Release:        alt1.svn20110129.1
Summary:        Declarative Mapper for SQLAlchemy
Group:          Development/Python
License:        MIT
URL:            http://pypi.python.org/pypi/Elixir/
Source:         Elixir-%version.tar.gz
BuildArch:      noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildRequires: python-devel python-module-setuptools

%description
A declarative layer on top of SQLAlchemy. It is a fairly thin wrapper,
which provides the ability to create simple Python classes that map
directly to relational database tables (this pattern is often referred
to as the Active Record design pattern), providing many of the benefits
of traditional databases without losing the convenience of Python
objects.

Elixir is intended to replace the ActiveMapper SQLAlchemy extension, and
the TurboEntity project but does not intend to replace SQLAlchemy's core
features, and instead focuses on providing a simpler syntax for defining
model objects when you do not need the full expressiveness of
SQLAlchemy's manual mapper definitions.

%package tests
Summary: Tests for Elixir
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release

%description tests
A declarative layer on top of SQLAlchemy. It is a fairly thin wrapper,
which provides the ability to create simple Python classes that map
directly to relational database tables (this pattern is often referred
to as the Active Record design pattern), providing many of the benefits
of traditional databases without losing the convenience of Python
objects.

Elixir is intended to replace the ActiveMapper SQLAlchemy extension, and
the TurboEntity project but does not intend to replace SQLAlchemy's core
features, and instead focuses on providing a simpler syntax for defining
model objects when you do not need the full expressiveness of
SQLAlchemy's manual mapper definitions.

This package contains tests for Elixir.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc README AUTHORS CHANGES LICENSE TODO
%python_sitelibdir/*

%files tests
%doc tests

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.8.0-alt1.svn20110129.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.svn20110129
- New snapshot

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1.svn20100902
- Version 0.8.0

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.1-alt1
- Initial build for Sisyphus

