%define version 1.5.2
%define release alt1.hg20131227
%define oname PasteDeploy

%def_with python3

%setup_python_module %oname

Name: %packagename
Version:%version
Release: alt1.hg20131227.1.1
Epoch: 1

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

# Automatically added by buildreq on Fri Jan 29 2016 (-bi)
# optimized out: python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-genshi python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base python3-module-Pygments python3-module-babel python3-module-cssselect python3-module-docutils python3-module-genshi python3-module-jinja2 python3-module-pytz python3-module-setuptools python3-module-snowballstemmer
BuildRequires: python-module-alabaster python-module-docutils python-module-html5lib python3-module-html5lib python3-module-sphinx rpm-build-python3 time

#BuildRequires: python-module-setuptools
#BuildPreReq: python-module-sphinx python-module-Pygments
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildRequires: python3-devel python3-module-distribute
#BuildPreReq: python3-module-sphinx python3-module-Pygments
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.5.2-alt1.hg20131227.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 29 2016 Mikhail Efremov <sem@altlinux.org> 1:1.5.2-alt1.hg20131227.1
- NMU: Use buildreq for BR.

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.2-alt1.hg20131227
- Version 1.5.2

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.5.1-alt1.hg20120916.1
- Rebuild with Python-3.3

* Sat Sep 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.5.1-alt1.hg20120916
- New snapshot

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

