%define version 1.7.5
%define release alt1.hg20120208
%define oname PasteScript

%def_with python3

%setup_python_module %oname

Name: %packagename
Version:%version
Release: %release
Serial: 1

Summary: A pluggable command-line frontend

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://pythonpaste.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://bitbucket.org/ianb/pastescript
Source: %modulename-%version.tar

Conflicts: python-module-paste.script
Obsoletes: python-module-paste.script
%py_provides %oname

BuildRequires: python-module-PasteDeploy
BuildPreReq: python-module-sphinx python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-PasteDeploy
BuildPreReq: python3-module-sphinx python3-module-Pygments
BuildPreReq: python-tools-2to3
%endif

%description
A pluggable command-line frontend, including commands to setup
package file layouts.

%if_with python3
%package -n python3-module-%oname
Summary: A pluggable command-line frontend (Python 3)
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip new

%description -n python3-module-%oname
A pluggable command-line frontend, including commands to setup
package file layouts.
%endif

%prep
%setup -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%if_with python3
pushd ../python3
sed -i 's|%_bindir/env python|%_bindir/env python3|' \
	tests/test_logging_config.py scripts/paster
for i in scripts/paster $(find ./ -name '*.py'); do
	2to3 -w -n $i
done
%python3_build
popd
%endif

%python_build
./regen-docs

%install
%if_with python3
pushd ../python3
%python3_install
mv %buildroot%_bindir/paster %buildroot%_bindir/paster3
popd
%endif
%python_install

%files
%doc docs/_build/*
%python_sitelibdir/paste/script
%python_sitelibdir/%modulename-*
%_bindir/paster
%exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%_bindir/paster3
%python3_sitelibdir/paste/script
%python3_sitelibdir/%modulename-*
%endif

%changelog
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.5-alt1.hg20120208
- New snapshot
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.5-alt1.hg20111107
- Version 1.7.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.7.4-alt1.hg20110427.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.4-alt1.hg20110427.1
- Added %%py_provides PasteScript

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.4-alt1.hg20110427
- New snapshot

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.4-alt1.hg20101117
- New snapshot
- Change upstream repository from svn to hg

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.svn20090922.2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.svn20090922.1
- Version 1.7.4

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 1.7.3-alt1
- Initial build for ALT Linux


