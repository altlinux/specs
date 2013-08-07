%define oname sphinx

Name: python3-module-%oname-sphinx-build-symlink
Version: 0.1
Release: alt1

Summary: sphinx-build symlink for python3 sphinx
License: BSD
Group: Development/Python
Url: http://sphinx.pocoo.org/
Conflicts: python-module-sphinx

BuildArch: noarch

%description
Sphinx is a tool that makes it easy to create intelligent and beautiful
documentation for Python projects (or other documents consisting of
multiple reStructuredText sources)

This package contains a sphinx-build symlink for python3 sphinx

%prep

%build

%install
install -d %buildroot%_bindir
ln -s py3_sphinx-build %buildroot%_bindir/sphinx-build

%files
%_bindir/*

%changelog
* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- initial build

