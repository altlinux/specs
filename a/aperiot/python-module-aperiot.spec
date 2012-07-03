Name: aperiot
Version: 0.2
Release: alt1

%setup_python_module %name

Summary: A grammar description language and a parser generator for Python
Source: %name-%version.tar.gz
License: BSD
Group: Development/Python
Url: http://sites.google.com/site/aperiotparsergenerator/
Requires: %packagename = %version
Buildarch: noarch

# Automatically added by buildreq on Mon Jan 23 2012
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-email
BuildRequires: python-module-distribute python-module-libutilitaspy

%description
Aperiot is a grammar description language and a parser generator for
Python. Its purpose is to provide the means to describe a language's
grammar and automatically generate a Python parser to recognize and
process text written in that language. It is intended to be used mainly
for programming and modelling languages.

``Aperio'' is a Latin word meaning ``to uncover,'' ``to unearth.''
A parser is, after all, a tool that uncovers the structure of text.

%package -n %packagename
Group: Development/Python
Summary: Python module for %name
%description -n %packagename
Python module for %name, %summary

%prep
%setup

%build
%python_build

%install
export PYTHONPATH=build/lib
%python_install

%files
%doc *txt
%_bindir/*

%files -n %packagename
%python_sitelibdir/aperiot*

%changelog
* Mon Jan 23 2012 Fr. Br. George <george@altlinux.ru> 0.2-alt1
- Autobuild version bump to 0.2
- No documentation included, what a ptiy :(
- Buildreq updated

* Wed Jul 27 2011 Fr. Br. George <george@altlinux.ru> 0.1.2-alt2
- Clean up spec
- New upstream URL

* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.1
- Rebuilt with python 2.6

* Sun Jun 08 2008 Fr. Br. George <george@altlinux.ru> 0.1.2-alt1
Initial build from scratch

