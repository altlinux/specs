%define oname repoze.who-friendlyform

Name:           python3-module-%oname
Version:        1.0.8
Release:        alt6

Summary:        Collection of repoze.who friendly form plugins
Group:          Development/Python3
License:        BSD-derived
URL:            http://pypi.python.org/pypi/repoze.who-friendlyform/

Source:         %oname-%version.tar.gz

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python-tools-2to3 gif2png

%py3_requires repoze.who zope.interface webob
%py3_provides repoze.who.plugins.friendlyform


%description
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

%package docs
Summary: Documentation for repoze.who-friendlyform
Group: Development/Documentation
BuildArch: noarch

%description docs
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

This package contains documentation for repoze.who-friendlyform.

%package pickles
Summary: Pickles for repoze.who-friendlyform
Group: Development/Python3

%description pickles
repoze.who-friendlyform is a repoze.who plugin which provides a
collection of developer-friendly form plugins, although for the time
being such a collection has only one item.

This package contains pickles for repoze.who-friendlyform.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile
sed -i 's|implements(|# implements(|' repoze/who/plugins/friendlyform.py

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build

export PYTHONPATH=$PWD
pushd docs/source/_static
gif2png logo_hi.gif
popd
%make -C docs html

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
    %buildroot%python3_sitelibdir/
%endif

install -d %buildroot%python3_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%files
%doc *.txt PKG-INFO tests.py CONTRIBUTORS
%python3_sitelibdir/repoze.who_friendlyform*
%python3_sitelibdir/repoze/who/plugins/*
%exclude %python3_sitelibdir/*.pth

%files docs
#doc docs/build/latex/*.pdf
%doc docs/build/html

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle


%changelog
* Thu Dec 12 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.8-alt6
- build for python2 disabled

* Fri Feb 09 2018 Stanislav Levin <slev@altlinux.org> 1.0.8-alt5.1.1.1.1
- (NMU) Fix Provides of python3 module

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt5.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.8-alt5.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.8-alt5.1
- NMU: Use buildreq for BR.

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt5
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.8-alt4.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt4
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt3
- Set as archdep package

* Tue Apr 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt2
- Rebuilt with python-module-sphinx-devel

* Tue Nov 23 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.8-alt1
- Version 1.0.8

* Thu Jul 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.6-alt1
- Initial build for Sisyphus

