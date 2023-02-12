%define _unpackaged_files_terminate_build 1
%define oname cmd2

%def_with docs
%def_with check

Name: python3-module-%oname
Version: 2.4.3
Release: alt1

Summary: A toolkit for simple interactive command-line applications

License: MIT
Group: Development/Python3
Url: https://pypi.org/project/cmd2/

# https://github.com/python-cmd2/cmd2
Source0: %oname-%version.tar.gz
Source1: cmd2.watch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
Buildrequires: python3-module-setuptools_scm

%if_with docs
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx
Buildrequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-wcwidth
BuildRequires: python3-module-attrs
Buildrequires: python3-module-colorama
BuildRequires: python3-module-pyperclip
%endif

%if_with check
BuildRequires: pytest3
BuildRequires: python3-module-pytest-mock
BuildRequires: python3-module-pytest-cov
%endif

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
%setup -n %oname-%version

%if_with docs
%prepare_sphinx3 .
ln -s ../objects.inv docs/
%endif

%build
%python3_build_debug

%if_with docs
# temporary install to avoid circular dependency
%__python3 setup.py install --skip-build --root=_build --force
export PYTHONPATH=$PWD/_build/%python3_sitelibdir

sphinx-build-3 -b html docs build/html
sphinx-build-3 -b pickle docs build/pickle

# remove the sphinx-build leftovers
rm -rf build/html/.{doctrees,buildinfo}
rm -rf build/pickles/.{doctrees,buildinfo}
%endif

%install
%python3_install

%if_with docs
install -d %buildroot%python3_sitelibdir/%oname
cp -fR build/pickle %buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=$PWD/_build/%python3_sitelibdir
pytest3

%files
%doc LICENSE PKG-INFO *.md
%python3_sitelibdir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info
%if_with docs
%exclude %python3_sitelibdir/%oname/pickle

%files docs
%doc build/html docs/examples

%files pickles
%dir %python3_sitelibdir/%oname
%python3_sitelibdir/%oname/pickle
%endif

%changelog
* Sat Feb 11 2023 Grigory Ustinov <grenka@altlinux.org> 2.4.3-alt1
- Automatically updated to 2.4.3.

* Wed Aug 03 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.2-alt1
- Automatically updated to 2.4.2.

* Mon May 16 2022 Grigory Ustinov <grenka@altlinux.org> 2.4.1-alt1
- Automatically updated to 2.4.1.

* Tue Nov 30 2021 Grigory Ustinov <grenka@altlinux.org> 2.3.3-alt1
- Automatically updated to 2.3.3.

* Tue Sep 21 2021 Grigory Ustinov <grenka@altlinux.org> 2.2.0-alt1
- Automatically updated to 2.2.0.

* Wed Jul 07 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.2-alt1
- Automatically updated to 2.1.2.

* Fri Jun 18 2021 Grigory Ustinov <grenka@altlinux.org> 2.1.1-alt1
- Automatically updated to 2.1.1.

* Mon Feb 22 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.0-alt1
- Automatically updated to 1.5.0.

* Wed Nov 18 2020 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Automatically updated to 1.4.0.

* Fri Oct 02 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.11-alt1
- Automatically updated to 1.3.11.

* Mon Sep 21 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.10-alt1
- Automatically updated to 1.3.10.

* Wed Sep 09 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.9-alt1
- Automatically updated to 1.3.9.

* Sun Aug 30 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.8-alt1
- Automatically updated to 1.3.8.

* Wed Aug 26 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.5-alt1
- Automatically updated to 1.3.5.

* Mon Aug 24 2020 Grigory Ustinov <grenka@altlinux.org> 1.3.4-alt1
- Automatically updated to 1.3.4.

* Fri Jul 31 2020 Grigory Ustinov <grenka@altlinux.org> 1.2.1-alt1
- Automatically updated to 1.2.1.

* Wed May 20 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.2-alt1
- Automatically updated to 1.0.2.

* Mon Mar 23 2020 Grigory Ustinov <grenka@altlinux.org> 1.0.1-alt1
- Automatically updated to 1.0.1.

* Thu Feb 27 2020 Grigory Ustinov <grenka@altlinux.org> 0.10.1-alt1
- Automatically updated to 0.10.1.

* Wed Dec 11 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.22-alt1
- Build new version.

* Mon Dec 09 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.21-alt1
- Build new version.

* Fri Nov 15 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.20-alt1
- Build new version.

* Fri Nov 08 2019 Grigory Ustinov <grenka@altlinux.org> 0.9.19-alt2
- Cleanup spec.
- Build with docs.
- Enable check.

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

