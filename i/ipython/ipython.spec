%define _unpackaged_files_terminate_build 1

%define oname ipython

%def_without doc

Name: ipython
Version: 5.5.0
Release: alt6

%setup_python_module IPython

Summary: An enhanced interactive Python shell
License: BSD
Group: Development/Python

Url: https://ipython.org
BuildArch: noarch

# https://github.com/ipython/ipython.git
Source: %name-%version.tar
Patch1: %name-%version-alt-docs.patch

%add_findreq_skiplist %python_sitelibdir/IPython/utils/eventful.py
%add_findreq_skiplist %python3_sitelibdir/IPython/utils/eventful.py

BuildRequires: python-module-setuptools
BuildRequires: python-module-zmq
BuildRequires: python-module-tornado python-modules-sqlite3
BuildRequires: python-module-jsonschema python-module-traitlets
BuildRequires: python-module-pexpect python-module-pickleshare
BuildRequires: python-module-simplegeneric 
BuildRequires: python2.7(pathlib2)
BuildRequires: python2.7(prompt_toolkit)
BuildRequires: python2.7(nose.tools)
BuildRequires: python-module-testpath
%if_with doc
BuildRequires: python-module-sphinx-devel python-module-matplotlib-sphinxext python-module-numpydoc
BuildRequires: python2.7(sphinx_rtd_theme) graphviz
%endif

Requires: python-module-%oname

%description
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

Main features:
* Comprehensive object introspection.
* Input history, persistent across sessions.
* Caching of output results during a session with automatically generated
  references.
* Readline based name completion.
* Extensible system of 'magic' commands for controlling the environment and
  performing many tasks related either to IPython or the operating system.
* Configuration system with easy switching between different setups (simpler
  than changing $$PYTHONSTARTUP environment variables every time).
* Session logging and reloading.
* Extensible syntax processing for special purpose situations.
* Access to the system shell with user-extensible alias system.
* Easily embeddable in other Python programs.
* Integrated access to the pdb debugger and the Python profiler.

%package doc
Summary: IPython documentation
Group: Development/Python

%description doc
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

This package contains IPython documentation (html and PDF formats).

%package examples
Summary: IPython examples
Group: Development/Python

%description examples
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

This package contains examples for IPython.

%package -n python-module-%oname
Summary: An enhanced interactive Python shell
Group: Development/Python

%add_python_req_skip Gnuplot Numeric bzrlib foolscap nose setuptools twisted msvcrt oct2py rpy2 System builtins clr
%py_requires jsonschema traitlets pexpect simplegeneric
%py_requires pathlib2
# fake due exaile
%py_provides IPython
# fake due BALL
%py_provides ipykernel

%description -n python-module-%oname
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

This package contains modules for Python-2.

%package -n python-module-%oname-tests
Summary: An enhanced interactive Python shell
Group: Development/Python

%description -n python-module-%oname-tests
IPython provides a replacement for the interactive Python interpreter with
extra functionality.

This package contains tests for Python-2.

%prep
%setup
%patch1 -p1

%if_with doc
%prepare_sphinx docs
ln -s ../objects.inv docs/source/
%endif

%build
#python_build

%install
mkdir -p %buildroot
#python_install
#rm %buildroot%_bindir/iptest

%if_with doc
install -d %buildroot%_docdir/%name
cp docs/source/*.txt %buildroot%_docdir/%name/

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs html PYTHON=python
cp -R docs/build/html/* examples %buildroot%_docdir/%name/
%endif

%files
#%doc COPYING.rst
#%doc README.rst
#%_bindir/*
#%_man1dir/*
%if_with doc
%dir %_docdir/%name
%_docdir/%name/*.txt
%endif

%files -n python-module-%oname
#%python_sitelibdir/IPython/
#%python_sitelibdir/*.egg-info
#%exclude %python_sitelibdir/IPython/*/tests

#%files -n python-module-%oname-tests
#%python_sitelibdir/IPython/*/tests

%if_with doc
%files doc
%_docdir/%name
%exclude %_docdir/%name/*.txt
%exclude %_docdir/%name/examples
#_docdir/%name/manual/

%files examples
%dir %_docdir/%name
%_docdir/%name/examples
%endif

%changelog
* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 5.5.0-alt6
- last (fake) build before remove (wait for rebuild BALL and exaile)

* Mon Sep 14 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 5.5.0-alt5
- Rebuilt without python-3.
- Moved python modules into separate packages.

* Thu Feb 06 2020 Stanislav Levin <slev@altlinux.org> 5.5.0-alt4
- Fixed FTBFS.

* Fri May 11 2018 Andrey Bychkov <mrdrew@altlinux.org> 5.5.0-alt3
- rebuild with python3.6

* Wed Mar 28 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 5.5.0-alt2
- Updated build and runtime dependencies.

* Fri Nov 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 5.5.0-alt1
- Updated to upstream version 5.5.0.

* Tue Oct 03 2017 Michael Shigorin <mike@altlinux.org> 4.0.0-alt6
- introduced doc knob (on by default)

* Fri Aug 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt5
- Applied upstream patches to fix test failures.

* Wed Aug 02 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.0.0-alt4
- Fixed build.

* Mon Apr 11 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1.1
- (NMU) rebuild with rpm-build-python3-0.1.10 (for new-style python3(*) reqs)
  and with python3-3.5 (for byte-compilation).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Mar  2 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.0-alt3
- .spec: fail if the maintainer's intentions are not fulfilled
  (because the sources or the build environment have changed since the
  spec was written): rm/cp without -f

* Sun Aug 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2
- %_bindir/ipython33 -> %_bindir/ipython3

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.1-alt1
- Version 3.2.1

* Wed Apr 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.0-alt1
- Version 3.1.0

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.1-alt1
- Version 2.4.1

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.1-alt1
- Version 2.3.1

* Thu Aug 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.0-alt1
- Version 2.2.0

* Sun Jul 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.0-alt1
- Version 2.1.0

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 0.13.1-alt1
- Version 0.13.1 (rel)

* Tue Jul 03 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.13-alt2
- Version 0.13 (rel)

* Fri Jun 01 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13-alt1.git20120601
- Version 0.13 (dev)
- Added package for Python 3

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.10-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.10-alt1.1
- Rebuilt with python 2.6

* Tue Aug 11 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.10-alt1
- 0.10

* Sun Mar 29 2009 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt2
- fix default indent bindings (vsu@)

* Thu Feb 19 2008 Andrey Rahmatullin <wrar@altlinux.ru> 0.9.1-alt1
- 0.9.1
- disable strict python requires detection, update skipped dependencies list
- package docs and examples separately

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.7.1.fix1-alt1.1
- Rebuilt with python-2.5.

* Sun Mar 05 2006 Leonid Shalupov <shalupov@altlinux.ru> 0.7.1.fix1-alt1
- 0.7.1.fix1
- stripped requires of runtime-detected frameworks: tk gtk qt wx (#7140)

* Thu Jun 16 2005 Leonid Shalupov <shalupov@altlinux.ru> 0.6.15-alt1
- 0.6.15

* Sat Feb 19 2005 Leonid Shalupov <shalupov@altlinux.ru> 0.6.11-alt1
- Initial build
