%define version 1.5.1
%define release alt1.hg20120315
%define oname PasteDeploy

%def_with python3

%setup_python_module %oname

Name: %packagename
Version:%version
Release: %release
Serial: 1

Summary: Load, configure, and compose WSGI applications and servers

License: MIT/X11
Group: Development/Python
BuildArch: noarch
Url: http://pythonpaste.org
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone http://bitbucket.org/ianb/pastedeploy
Source: %modulename-%version.tar

Conflicts: python-module.paste.deploy
Obsoletes: python-module.paste.deploy
%py_provides %oname

BuildRequires: python-module-setuptools
BuildPreReq: python-module-sphinx python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-sphinx python3-module-Pygments
%endif

%description
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files. Paste Script provides commands to serve applications based on
this configuration file.

%if_with python3
%package -n python3-module-%oname
Summary: Load, configure, and compose WSGI applications and servers (Python 3)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This tool provides code to load WSGI applications and servers from
URIs; these URIs can refer to Python Eggs for INI-style configuration
files. Paste Script provides commands to serve applications based on
this configuration file.
%endif

%prep
%setup -n %modulename-%version
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

./regen-docs

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc docs/_build/*
%python_sitelibdir/paste/deploy
%python_sitelibdir/%modulename-*
#exclude %python_sitelibdir/tests

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/paste/deploy
%python3_sitelibdir/%modulename-*
%endif

%changelog
* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.1-alt1.hg20120315
- New snapshot
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.1-alt1.hg20110815
- Version 1.5.1

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.3.4-alt1.hg20101028.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.4-alt1.hg20101028.1
- Added %%py_provides PasteDeploy

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.3.4-alt1.hg20101028
- New snapshot

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.svn20090714.2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.4-alt1.svn20090714.1
- Version 1.3.4

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 1.3.3-alt1
- Initial build for ALT Linux

