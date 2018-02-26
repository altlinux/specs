%define oname egenix-mx-base

%def_without python3

Name: python-module-%oname
Version: 3.2.4
Release: alt1

Summary: eGenix.com mx Base Distribution
License: eGenix.com Public License Agreement
Group: Development/Python

Packager: Python Development Team <python@packages.altlinux.org>

Source: %name-%version.tar

Url: http://www.egenix.com/products/python/mxBase/

Obsoletes: egenix-mx-base < 2.0.3-alt8
Provides: egenix-mx-base  = %version-%release

%setup_python_module %oname
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python-tools-2to3
%endif

%description
The eGenix mx Extension Series are a collection of Python extensions
written in ANSI C and Python which provide a large spectrum of useful
additions to everyday Python programming.

The Base Distribution includes the Open Source subpackages of the
series and is needed by all other add-on packages of the series:

  mxDateTime - Date/Time Library for Python
  mxTextTools - Fast Text Parsing and Processing Tools for Python
  mxProxy - Object Access Control for Python
  mxBeeBase - On-disk B+Tree Based Database Kit for Python
  mxURL - Flexible URL Data-Type for Python
  mxUID - Fast Universal Identifiers for Python
  mxStack - Fast and Memory-Efficient Stack Type for Python
  mxQueue - Fast and Memory-Efficient Queue Type for Python
  mxTools - Fast Everyday Helpers for Python

%if_with python3
%package -n python3-module-%oname
Summary: eGenix.com mx Base Distribution (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
The eGenix mx Extension Series are a collection of Python 3 extensions
written in ANSI C and Python 3 which provide a large spectrum of useful
additions to everyday Python 3 programming.

The Base Distribution includes the Open Source subpackages of the
series and is needed by all other add-on packages of the series:

  mxDateTime - Date/Time Library for Python 3
  mxTextTools - Fast Text Parsing and Processing Tools for Python 3
  mxProxy - Object Access Control for Python 3
  mxBeeBase - On-disk B+Tree Based Database Kit for Python 3
  mxURL - Flexible URL Data-Type for Python 3
  mxUID - Fast Universal Identifiers for Python 3
  mxStack - Fast and Memory-Efficient Stack Type for Python 3
  mxQueue - Fast and Memory-Efficient Queue Type for Python 3
  mxTools - Fast Everyday Helpers for Python 3
%endif

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%if_with python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
%python3_build
popd
%endif
%python_build_debug

%install
%python_install

find %buildroot/%python_sitelibdir/mx/ -type d -name Doc -print0 | xargs -r0 rm -rf --
find %buildroot/%python_sitelibdir/mx/ -type f -name 'test*.py' -delete
rm -f %buildroot/%python_sitelibdir/mx/{BeeBase/showBeeDict.py,Misc/FileLock.py,Proxy/mxProxy/weakreftest.py,Stack/stackbench.py,Queue/queuebench.py}

%if_with python3
pushd ../python3
%python3_install
popd
find %buildroot/%python3_sitelibdir/mx/ -type d -name Doc -print0 | xargs -r0 rm -rf --
find %buildroot/%python3_sitelibdir/mx/ -type f -name 'test*.py' -delete
rm -f %buildroot/%python3_sitelibdir/mx/{BeeBase/showBeeDict.py,Misc/FileLock.py,Proxy/mxProxy/weakreftest.py,Stack/stackbench.py,Queue/queuebench.py}
%endif

%files
%python_sitelibdir/mx/
%python_sitelibdir/*.egg-info
%doc COPYRIGHT LICENSE README

%if_with python3
%files -n python3-module-%oname
%doc COPYRIGHT LICENSE README
%python3_sitelibdir/*
%endif

%changelog
* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt1
- Version 3.2.4

* Wed Apr 18 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt2
- Fixed build

* Thu Apr 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt1
- Version 3.2.3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.1.3-alt2.1
- Rebuild with Python-2.7

* Sun Mar 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt2
- Rebuilt for debuginfo

* Thu Jul 29 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.3-alt1
- Version 3.1.3

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.2-alt1.1
- Rebuilt with python 2.6

* Mon Jul 27 2009 Andrey Rahmatullin <wrar@altlinux.ru> 3.1.2-alt1
- 3.1.2
- spec cleanup

* Mon Jan 28 2008 Grigory Batalov <bga@altlinux.ru> 2.0.6-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 2.0.6-alt2
- Skip whrandom module requirement.

* Tue Jan 11 2005 Andrey Orlov <cray@altlinux.ru> 2.0.6-alt1
- New Version
- Package provide egenix-mx-base with version now (#5765)

* Sat Jul 10 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt11
- Typo error in spec fixed

* Sat Jul 03 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt10
- Provides egenix-mx-base added

* Thu May 20 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt9
- Previous package obsoleted

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt8
- Conditional packaging operators excluded from spec;

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt7.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt6.d
- Some unusable files excluded (because of invalid dependences, preliminary
  fix);
- Docs moved into %_datadir/doc;
- Requirements of python2.3(Constants) excluded;

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt5.d
- REbuild with new macros

* Wed Apr 14 2004 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt4.d
- Fix new python policy compatibility

* Mon Dec 01 2003 Andrey Orlov <cray@altlinux.ru> 2.0.3-alt3
- Try Rebuild With Py23

* Mon Nov 18 2002 AEN <aen@altlinux.ru> 2.0.3-alt2
- rebuild in new environment

* Fri Mar 29 2002 Maxim Dzumanenko <mvd@altlinux.ru> 2.0.3-alt1
- first version

