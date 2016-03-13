%define version 3.3.2
%define release alt1
%setup_python_module em
%define pname empy

%def_with python3

Name: %{packagename}
Version: %{version}
Release: alt1.1
License: LGPL
Source0: http://www.alcyone.com/software/%pname/%pname-latest.tar.gz
Url: http://www.alcyone.com/software/empy
Summary: A templating system for Python
Group: Development/Python
BuildArch: noarch
Packager: Fr. Br. George <george@altlinux.ru>

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel
%endif

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

%package -n python3-module-%modulename
Summary: A templating system for Python
Group: Development/Python3

%description -n python3-module-%modulename
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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --optimize=2 --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc doc
%doc sample* test.sh

%if_with python3
%files -n python3-module-%modulename
%doc doc
%doc sample* test.sh
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.3.2-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3.2-alt1
- Version 3.3.2
- Added module for Python 3

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3-alt1.1.1.1
- Rebuild with Python-2.7

* Tue Nov 17 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1.1.1
- Rebuilt with python 2.6

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 3.3-alt1.1
- Rebuilt with python-2.5.

* Mon Nov 21 2005 Fr. Br. George <george@altlinux.ru> 3.3-alt1
- Initial ALT build

