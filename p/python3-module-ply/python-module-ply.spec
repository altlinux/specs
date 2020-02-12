%define _unpackaged_files_terminate_build 1
%define oname ply

%def_with check

Name: python3-module-%oname
Version: 3.11
Release: alt2

Summary: lex and yacc python implementation
License: BSD
Group: Development/Python3
Url: http://www.dabeaz.com/ply/
BuildArch: noarch

# Source-url: https://pypi.io/packages/source/p/%oname/%oname-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools


%description
PLY is a 100%% Python implementation of the common parsing tools lex
and yacc.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
pushd test
%__python3 testlex.py -v
%__python3 testyacc.py -v
popd

%files
%doc CHANGES doc/*.html
%python3_sitelibdir/*


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 3.11-alt2
- Build for python2 disabled.

* Sun Jun 30 2019 Vitaly Lipatov <lav@altlinux.ru> 3.11-alt1
- new version 3.11 (with rpmrb script)

* Fri Jun 15 2018 Stanislav Levin <slev@altlinux.org> 3.9-alt2
- Fix python3 package
- Enable tests

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

