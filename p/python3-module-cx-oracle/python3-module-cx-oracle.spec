%define        _unpackaged_files_terminate_build 1
%define        pypiname cx-oracle
%define        modname cx_Oracle
%define        distname cx_Oracle
%def_disable   check
%def_enable    doc

Name:          python3-module-%pypiname
Version:       8.3.0.7
Release:       alt0.git6766bca
Summary:       Python interface to Oracle Database now superseded by python-oracledb
License:       BSD-3-Clause
Group:         Development/Python3
Url:           https://oracle.github.io/python-cx_Oracle/
Vcs:           https://github.com/oracle/python-cx_Oracle.git

Source:        %name-%version.tar
Patch:         %name-%EVR.patch
BuildRequires(pre): rpm-build-pyproject
BuildRequires: libodpic-devel
BuildRequires: python3(wheel)
%{?!_disable_doc:BuildRequires: python3-module-sphinx-sphinx-build-symlink}
%if_enabled check
BuildRequires: python3(pytest)
%endif

%description
cx_Oracle has a major new release under a new name and homepage python-oracledb.

The source code has moved to github.com/oracle/python-oracledb.

New projects should install python-oracledb instead of cx_Oracle. Critical
patches and binary packages for new Python releases may continue to be made in
the cx_Oracle namespace for a limited time, subject to demand.

cx_Oracle is a Python extension module that enables access to Oracle Database.
It conforms to the Python database API 2.0 specification with a considerable
number of additions and a couple of exclusions. See the homepage for a feature
list.

cx_Oracle 8.3 was tested with Python versions 3.6 through 3.10. You can use
cx_Oracle with Oracle 11.2, 12c, 18c, 19c and 21c client libraries. Oracle's
standard client-server version interoperability allows connection to both older
and newer databases. For example Oracle 19c client libraries can connect to
Oracle Database 11.2. Older versions of cx_Oracle may work with older versions
of Python.


%prep
%setup
%autopatch -p1

%build
export ODPIC_LIB_DIR=%_libdir/
export ODPIC_INC_DIR=%_includedir/
%pyproject_build
%{?!_disable_doc:%make -C doc html SPHINXBUILD=sphinx-build-3}

%install
%pyproject_install

%check
# NOTE: cx_Oracle.DatabaseError: DPI-1047: Cannot locate a 64-bit Oracle Client library: "libclntsh.so
%pyproject_run_pytest
%pyproject_run_unittest

%files
%doc *.md
%_defaultdocdir/%modname
%{?!_disable_doc:%doc doc/build/html/*}
%python3_sitelibdir/%{distname}*.so
%python3_sitelibdir/%{modname}*/METADATA

%changelog
* Wed Jan 31 2024 Pavel Skrylev <majioa@altlinux.org> 8.3.0.7-alt0.git6766bca
- Initial build v8.3.0p7 for Sisyphus.
