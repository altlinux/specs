%def_without docs
%define _unpackaged_files_terminate_build 1
%define oname cmd2

Name: python3-module-%oname
Version: 0.9.19
Release: alt1

Summary: A toolkit for simple interactive command-line applications

License: MIT
Group: Development/Python3
Url: https://bitbucket.org/catherinedevlin/cmd2

# hg clone https://bitbucket.org/catherinedevlin/cmd2
Source0: https://pypi.python.org/packages/97/80/d5c6efd4a1467865fd25c203fbe3a107f241b09f30cc7f8d9a3e3bef8abd/%{oname}-%{version}.tar.gz

BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3 python3-module-sphinx
BuildRequires: python3-module-wcwidth
BuildRequires: python3-module-attrs
BuildRequires: python3-module-pyperclip
Buildrequires: python3-module-setuptools_scm
Buildrequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-pyparsing python3-module-setuptools time

%description
cmd2, a toolkit for simple interactive command-line applications. A
drop-in enhancement adding features to the Python Standard Library's cmd
module.

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
Group: Development/Python3

%description pickles
cmd2, a toolkit for simple interactive command-line applications. A
drop-in enhancement adding features to the Python Standard Library's cmd
module.

This package contains pickles for cmd2.

%prep
%setup -q -n %{oname}-%{version}
rm -f docs/pycon2010/ui/pycon/pretty.css~

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build_debug

%if_with docs
%make SPHINXBUILD="sphinx-build-3" -C docs html
%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%endif

%install
export PYTHONPATH=%buildroot%python_sitelibdir
%python3_install

%if_with docs
install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/
%endif

for i in $(find %buildroot -name '*~'); do
	rm -f $i
done

%files
%doc LICENSE PKG-INFO docs *.md
%python3_sitelibdir/*
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle
%endif

%if_with docs
%files docs
%doc docs/_build/html docs/pycon2010 example

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Mon Oct 21 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.19-alt1
- Build new version.
- Build without python2.
- Build without docs.

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.6.9-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.6.8-alt1.hg20141208.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.6.8-alt1.hg20141208.1
- NMU: Use buildreq for BR.

* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.8-alt1.hg20141208
- Version 0.6.8

* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.7-alt1
- Version 0.6.7

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.6.4-alt5.1
- Rebuild with Python-3.3

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

