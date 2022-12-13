%define _unpackaged_files_terminate_build 1
%define pypi_name pdb-clone

Name: %pypi_name
Version: 1.10.2
Release: alt1
License: GPL-2.0
Summary: A clone of pdb, fast and with the remote debugging and attach features
Group: Development/Python
Url: https://pypi.org/project/pdb-clone/
VCS: https://github.com/corpusops/pdbclone

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

# gdb provides python(gdb) on %_datadir/gdb/python, but it's for internal usage
# only, for example:
# (gdb) python import gdb; print (gdb.__file__)
# /usr/share/gdb/python/gdb/__init__.py
#
# pdb-clone provides module for gdb, that is called from gdb
# (gdb) python import pdb_clone.bootstrappdb_gdb
%add_python3_req_skip gdb

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

%package -n python3-module-%pypi_name
Summary: Module for %name
Group: Development/Python
# wellknown PyPI name
%py3_provides %pypi_name
Provides: python3-module-pdb_clone = %EVR

%description -n python3-module-%pypi_name
%summary

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%files
%doc pdb-clone.wiki/*
%_bindir/pdb-attach
%_bindir/pdb-clone

%files -n python3-module-%pypi_name
%python3_sitelibdir/pdb_clone/
%python3_sitelibdir/%{pyproject_distinfo %pypi_name}/

%changelog
* Mon Dec 12 2022 Stanislav Levin <slev@altlinux.org> 1.10.2-alt1
- 1.10.1 -> 1.10.2.
- Stopped build Python2 package.

* Thu Oct 04 2018 Fr. Br. George <george@altlinux.ru> 1.10.1-alt2
- Remove python*(gdb) dependency

* Thu Sep 20 2018 Fr. Br. George <george@altlinux.ru> 1.10.1-alt1
- Autobuild version bump to 1.10.1

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

