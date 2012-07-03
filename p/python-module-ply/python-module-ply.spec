%define oname ply

%def_with python3

Name: python-module-%oname
Version: 3.4
Release: alt1

Summary: lex and yacc python implementation

License: LGPL
Group: Development/Python
Url: http://www.dabeaz.com/ply/

Source: http://www.dabeaz.com/ply/%oname-%version.tar.bz2

BuildArch: noarch

# Automatically added by buildreq on Fri Mar 24 2006
BuildRequires: python-devel python-modules python-modules-compiler python-modules-encodings
BuildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
PLY is a 100%% Python implementation of the common parsing tools lex
and yacc.

%if_with python3
%package -n python3-module-%oname
Summary: lex and yacc python 3 implementation
Group: Development/Python3

%description -n python3-module-%oname
PLY is a 100%% Python implementation of the common parsing tools lex
and yacc.
%endif

%prep
%setup -q -n %oname-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%find_lang %name

%files -f %name.lang
#%_bindir/*
%doc CHANGES README TODO doc/*.html example/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES README TODO doc/*.html
%python3_sitelibdir/*
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt1
- Version 3.4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.3-alt1.1
- Rebuild with Python-2.7

* Sat Nov 27 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1
- Version 3.3

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Sat Jul 05 2008 Vitaly Lipatov <lav@altlinux.ru> 2.5-alt1
- new version 2.5 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)
- fix summary (s/lyx/lex)

* Fri Mar 24 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6-alt0.1
- initial build for ALT Linux Sisyphus

