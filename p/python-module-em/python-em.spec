%define version 3.3
%define release alt1
%setup_python_module em
%define pname empy

Name: %{packagename}
Version: %{version}
Release: %{release}.1.1.1
License: LGPL
Source0: http://www.alcyone.com/software/%pname/%pname-latest.tar.gz
Url: http://www.alcyone.com/software/empy
Summary: A templating system for Python
Group: Development/Python
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

%description
EmPy is a system for embedding Python expressions and statements
in template text; it takes an EmPy source file, processes it, and
produces output.  This is accomplished via expansions, which are
special signals to the EmPy system and are set off by a special
prefix (by default the at sign, '@').  EmPy can expand arbitrary
Python expressions and statements in this way, as well as a
variety of special forms.  Textual data not explicitly delimited
in this way is sent unaffected to the output, allowing Python to
be used in effect as a markup language.  Also supported are "hook"
callbacks, recording and playback via diversions, and dynamic,
chainable filters.  The system is highly configurable via command
line options and embedded commands

#----------------------------------------------------------------------
# Prepare, Building & Install
#----------------------------------------------------------------------
%prep
%setup -n %pname-%version
#*%patch1 -p1

%build
%python_build

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%files -f INSTALLED_FILES
%doc doc
%doc sample* test.sh

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3-alt1.1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.3-alt1.1
- Rebuilt with python-2.5.

* Mon Nov 21 2005 Fr. Br. George <george@altlinux.ru> 3.3-alt1
- Initial ALT build

