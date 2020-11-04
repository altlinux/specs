%define _unpackaged_files_terminate_build 1
%define oname pexpect

%def_with check
%def_without doc

Name: python3-module-%oname
Version: 4.8.0
Release: alt1

Summary: Pexpect is a pure Python Expect. It allows easy control of other applications

License: ISC
Group: Development/Python3
Url: https://pypi.python.org/pypi/pexpect

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-ptyprocess

%if_with doc
BuildRequires: python3-module-sphinx
%endif

%if_with check
BuildRequires: /dev/pts
BuildRequires: man-db
BuildRequires: openssl
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch
Obsoletes: %oname < 0.999-alt6

%description
Pexpect is a pure Python module for spawning child applications; controlling
them; and responding to expected patterns in their output. Pexpect works like
Don Libes' Expect. Pexpect allows your script to spawn a child application and
control it as if a human were typing commands.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation

%description docs
This package contains documentation for %oname.

%prep
%setup
# fix some incompatibility
%__subst 's|"time"|"time -p true"|' tests/test_async.py
%__subst 's|"python"|"python3"|' pexpect/replwrap.py

fix_env_python () {
    # change shebang /usr/bin/env python -> /usr/bin/$PYTHON
    PYTHON="$1"
    find -type f -name '*.py' | \
        xargs sed -i \
            "1s|#!/usr/bin/env python[[:space:]]*$|#!/usr/bin/$PYTHON|"

    # change python -> $PYTHON callings
    find tests -type f -name '*.py' | \
        xargs sed -i \
            "s/\(.*pexpect.spawn(\x27\)\(python\)\(\(\x27\| \)\)/\1$PYTHON\3/"

    sed -i \
        "s|self.runfunc(\x27python exit1.py\x27|self.runfunc(\x27$PYTHON exit1.py\x27|" \
        tests/test_run.py

    sed -i "1s|#!/usr/bin/env python[[:space:]]*$|#!/usr/bin/$PYTHON|" \
        tests/fakessh/ssh
}

fix_env_python python3

%if_with doc
%prepare_sphinx3 .
ln -s ../objects.inv doc/
%endif

%build
%python3_build

%install
%python3_install
%if_with doc
export PYTHONPATH=%buildroot%python3_sitelibdir
%make -C doc html SPHINXBUILD=sphinx-build-3
%endif

%check
%if_with check
export LC_ALL="en_US.UTF-8"
py.test3 -v
%endif

%files
%doc LICENSE *.rst
%python3_sitelibdir/pexpect/
%python3_sitelibdir/pexpect-*.egg-info/

%if_with doc
%files docs
%doc doc/_build/html
%doc examples
%endif

%changelog
* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 4.8.0-alt1
- new version 4.8.0 (with rpmrb script)
- temp. disable doc subpackage build (wait for fixes for sphinx)
- remove pexpect provides

* Wed Nov 04 2020 Vitaly Lipatov <lav@altlinux.ru> 4.7.0-alt2
- build python3 separately

* Sat Nov 23 2019 Stanislav Levin <slev@altlinux.org> 4.7.0-alt1
- 4.6 -> 4.7.0.

* Mon Feb 25 2019 Stanislav Levin <slev@altlinux.org> 4.6-alt3
- Fixed testing:
  + increased timeout for test_large_stdout_stream
  + skipped assertion of trailing output (test_interact_escape_None
    and test_interact_exit_unicode)
  + added closing of child in test_spawn_uses_env

* Fri Feb 01 2019 Grigory Ustinov <grenka@altlinux.org> 4.6-alt2
- Fixed FTBFS (Added BR on python-module-pyte) (Closes: #36015).

* Mon Aug 20 2018 Stanislav Levin <slev@altlinux.org> 4.6-alt1
- 4.4 -> 4.6.

* Wed Mar 21 2018 Stanislav Levin <slev@altlinux.org> 4.4-alt1
- 4.2.1 -> 4.4.0

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 4.2.1-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0-alt1.dev.git20150811.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Aug 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.dev.git20150811
- Version 4.0.dev

* Sun Aug 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.3-alt1
- Version 3.3
- Added module for Python 3

* Fri Dec 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0-alt1
- Version 3.0

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.3-alt1.1.1
- Rebuild with Python-2.7

* Thu Nov 12 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.1
- Rebuilt with python 2.6

* Mon Dec 29 2008 Vitaly Lipatov <lav@altlinux.ru> 2.3-alt1
- new version 2.3 (with rpmrb script)
- cleanup spec

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 0.999-alt8.1
- Rebuilt with python-2.5.

* Wed Apr 20 2005 Andrey Orlov <cray@altlinux.ru> 0.999-alt8
- Documentation and examples added

* Sat Jul 03 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt7
- Provide pexpect clause added

* Thu May 20 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt6
- Previous packages are obsoleted

* Tue May 18 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt5
- Conditional operators excluded from spec

* Mon May 10 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt4.d
- Rebuild

* Thu Apr 22 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt3.d
- BuildNoArch clause added

* Tue Apr 13 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt2.d
- Rebuild with new rpm/python macros
- Fix description field omited before

* Mon Mar 29 2004 Andrey Orlov <cray@altlinux.ru> 0.999-alt1.d
- Initial release

