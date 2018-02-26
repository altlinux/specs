%define oname cmd2

%def_with python3

Version: 0.6.4
Release: alt5
%setup_python_module %oname

Name: python-module-%oname
Summary: A toolkit for simple interactive command-line applications
# hg clone http://hg.assembla.com/python-cmd2 cmd2
Source: %name-%version.tar
License: MIT
Group: Development/Python
Url: http://www.assembla.com/wiki/show/python-cmd2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

BuildArch: noarch
BuildPreReq: python-devel python-module-distribute
BuildPreReq: python-module-pyparsing python-module-sphinx-devel
#py_requires setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-distribute
BuildPreReq: python3-module-pyparsing
%endif

%description
cmd2, a toolkit for simple interactive command-line applications. A
drop-in enhancement adding features to the Python Standard Library's cmd
module.

%if_with python3
%package -n python3-module-%oname
Summary: A toolkit for simple interactive command-line applications (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
cmd2, a toolkit for simple interactive command-line applications. A
drop-in enhancement adding features to the Python Standard Library's cmd
module.
%endif

%package docs
Summary: Documentation and examples for cmd2
Group: Development/Documentation

%description docs
cmd2, a toolkit for simple interactive command-line applications. A
drop-in enhancement adding features to the Python Standard Library's cmd
module.

This package contains documentation and examples for cmd2.

%package pickles
Summary: Pickles for cmd2
Group: Development/Python

%description pickles
cmd2, a toolkit for simple interactive command-line applications. A
drop-in enhancement adding features to the Python Standard Library's cmd
module.

This package contains pickles for cmd2.

%prep
%setup
rm -f docs/pycon2010/ui/pycon/pretty.css~
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug
%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%make -C docs html
%make -C docs pickle

%install
export PYTHONPATH=%buildroot%python_sitelibdir
%python_install develop
%if_with python3
pushd ../python3
%python3_install
popd
%endif

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

for i in $(find %buildroot -name '*~'); do
	rm -f $i
done

%files
%doc README.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/site.py*
%exclude %python_sitelibdir/%oname/pickle

%files docs
%doc docs/_build/html docs/pycon2010 example

%files pickles
%dir %python_sitelibdir/%oname
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc README.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri May 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt5
- Added module for Python 3

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt4
- Avoid conflict with python-module-distribute

* Sat Nov 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt3
- Removed all backup files

* Fri Nov 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2
- Fixed backup-file-in-package (repocop)

* Wed Nov 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for ALT Linux Sisyphus (ALT #26387)

