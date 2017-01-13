%define _unpackaged_files_terminate_build 1
%define oname ply

%def_with python3

Name: python-module-%oname
Version: 3.9
Release: alt1

Summary: lex and yacc python implementation

License: LGPL
Group: Development/Python
Url: http://www.dabeaz.com/ply/

Source0: https://pypi.python.org/packages/a8/4d/487e12d0478ee0cbb15d6fe9b8916e98fe4e2fce4cc65e4de309209c0b24/%{oname}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base
BuildRequires: python-module-setuptools python3-module-setuptools rpm-build-python3 time

#BuildPreReq: python-module-distribute
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python-tools-2to3
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
%setup -q -n %{oname}-%{version}
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc CHANGES doc/*.html example/
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES doc/*.html
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 3.9-alt1
- automated PyPI update

* Fri Apr 22 2016 Vitaly Lipatov <lav@altlinux.ru> 3.8-alt1
- new version 3.8 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.6-alt1.1
- NMU: Use buildreq for BR.

* Sun Jan 03 2016 Vitaly Lipatov <lav@altlinux.ru> 3.6-alt1
- new version 3.6 (with rpmrb script)

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4-alt2
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 3.4-alt1.1
- Rebuild with Python-3.3

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

