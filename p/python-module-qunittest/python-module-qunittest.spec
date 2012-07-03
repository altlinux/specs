%define version 1.0
%define release alt2
%setup_python_module qunittest

Summary: A GUI unit test runner for Python
Name: %packagename
Version: %version
Release: %release.1
Source0: %modulename-%version.tar.gz
License: GNU General Public License version 2
Group: Development/Python
Prefix: %prefix
Packager: Python Development Team <python at packages.altlinux.org>
Url: http://projects.edgewall.com/qunittest/
BuildArch: noarch

%description
QUnitTest is an easy-to-use GUI framework and application for use with the
Python unit testing framework. It can be used to conveniently execute unit
tests and suites, and then display the results in a useful fashion.

The goal of QUnitTest is to make execution of unit tests and results display
as easy as possible. This allows the programmer to focus on changes and
refactoring while frequently executing her unit tests to track progress.

%prep
%setup  -q -n %modulename-%version

%build
#__subst "s/scripts=\\['scripts\\/qunittest'\\],//" setup.py
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES
rm -f %buildroot%_bindir/qunittest
install -m 0755 scripts/qunittest %buildroot%python_sitelibdir/QUnitTest.py
ln -s %python_sitelibdir/QUnitTest.py %buildroot%_bindir/qunittest

%files -f INSTALLED_FILES
%python_sitelibdir/QUnitTest.py
#_bindir/qunittest

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Mon Nov 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.0-alt1.1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt1.1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-alt1.1
- Rebuilt with python-2.4.

* Wed Oct 13 2004 Ivan Fedorov <ns@altlinux.ru> 1.0-alt1
- Initial build

