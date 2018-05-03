Name: pdb-clone
Version: 1.10
Release: alt1.1.1
License: GPL
Summary: A clone of pdb, fast and with the remote debugging and attach features
Source: %name.%version.tar.gz
Group: Development/Python
Url: https://pypi.python.org/pypi/pdb-clone
%setup_python_module %name

BuildRequires(pre): rpm-build-python3
# XXX
%add_python3_req_skip gdb

# Automatically added by buildreq on Wed Apr 22 2015
# optimized out: libcloog-isl4 python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-modules-unittest python-test python3-dev python3-test

%description
Implement the most recent Python 3 features of pdb, as defined in the
Python 3 pdb documentation. The pdb command line interface remains
unchanged except for the new detach and thread pdb commands.

Improve significantly pdb performance. With breakpoints, pdb-clone runs
just below the speed of the interpreter while pdb runs 10 to 100 times
slower than the interpreter, see Performances.

Extend pdb with remote debugging. A remote debugging session may be
started when the program stops at a pdb.set_trace_remote() hard-coded
breakpoint, or at any time and multiple times by attaching to the
process main thread. See RemoteDebugging

Fix pdb long standing bugs entered in the Python issue tracker, see the
News.

Add a bdb comprehensive test suite (more than 70 tests) and run both pdb
and bdb test suites.

%package -n %packagename
Summary: Module for %name, %summary
Group: Development/Python
%description -n %packagename
%summary

%package -n python3-module-%name
Summary: Module for %name
Group: Development/Python
%description -n python3-module-%name
%summary

%prep
%setup
# Hack in coding
sed -i '/#!/i# coding: latin1' lib/pdb_clone/pdb.py

%build
%python_build
python3 setup.py clean
%python3_build

%ifarch %ix86
ln -s lib.linux-i686-%_python_version build/lib.linux-%_arch-%_python_version
ln -s lib.linux-i686-%_python3_version build/lib.linux-%_arch-%_python3_version
%endif

%install
%python_install
%python3_install

%check
PYTHONPATH=`pwd`/build/lib.linux-%_arch-%_python_version python setup.py check
PYTHONPATH=`pwd`/build/lib.linux-%_arch-%_python_version python setup.py test
PYTHONPATH=`pwd`/build/lib.linux-%_arch-%_python3_version python3 setup.py check
# TODO some tests failed here
PYTHONPATH=`pwd`/build/lib.linux-%_arch-%_python3_version python3 setup.py test

%files
%_bindir/*

%files -n %packagename
%python_sitelibdir/*

%files -n python3-module-%name
%python3_sitelibdir/*

%changelog
* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.10-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.10-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.10-alt1
- Autobuild version bump to 1.10
- Provide python3 package

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Wed Apr 22 2015 Fr. Br. George <george@altlinux.ru> 1.9.1-alt1
- Initial build for ALT

