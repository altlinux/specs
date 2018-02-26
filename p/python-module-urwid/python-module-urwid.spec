%define rname urwid
Name: python-module-urwid
Version: 0.9.9
Release: alt1.1.1.1

Summary: Urwid is a console user interface library for Python.
#Summary(ru_RU.UTF8): Urwid - библиотека для написания консольных интерфейсов на Python
License: LGPL
Group: Development/Python
Url: http://excess.org/urwid

Packager: Alexey Morsov <swi@altlinux.ru>
Source: %name-%version.tar

Buildrequires: python-modules-curses python-module-setuptools
Requires: python-modules-curses

%description
Urwid is a console user interface library for Python. Urwid is released 
under the GNU Lesser General Public License and it includes many features 
useful for text console application developers:

 * Fluid interface resizing (xterm window resizing / fbset on Linux console)
 * Web application display mode using Apache and CGI [ Live Demo ]
 * Support for UTF-8, simple 8-bit and CJK encodings
 * Multiple text alignment and wrapping modes built-in
 * Ability create user-defined text layout classes
 * Simple markup for setting text attributes
 * Powerful list box that handles scrolling between different widget types
 * List box contents may be managed with a user-defined class
 * Flexible edit box for editing many different types of text
 * Buttons, check boxes and radio boxes
 * Customizable layout for all widgets
 * Easy interface for creating HTML screen shots 

#description -l ru_RU.UTF8

%prep
%setup

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%install
%python_build_install --optimize=2 --record=INSTALLED_FILES


%files -f INSTALLED_FILES
%python_sitelibdir/%rname/
%python_sitelibdir/%rname-%version-py*.egg-info/

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.9-alt1.1.1
- Rebuild with Python-2.7

* Wed Mar 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.9-alt1.1
- Rebuilt for debuginfo

* Sat Jan 23 2010 Alexey Morsov <swi@altlinux.ru> 0.9.9-alt1
- new version

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8.4-alt2
- Rebuilt with python 2.6

* Wed Jun 17 2009 Alexey Morsov <swi@altlinux.ru> 0.9.8.4-alt1
- new version

* Thu Dec 13 2007 Alexey Morsov <swi@altlinux.ru> 0.9.8.1-alt1
- initial build

