%define oname user
Name: python3-module-%oname
Version: 2.7.6
Release: alt1.1
Summary: Hook to allow user-specified customization code to run
License: PSF
Group: Development/Python3
Url: http://www.python.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname.py
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-tools-2to3

%description
As a policy, Python doesn't run user-specified code on startup of
Python programs (interactive sessions execute the script specified in
the PYTHONSTARTUP environment variable if it exists).

However, some programs or sites may find it convenient to allow users
to have a standard customization file, which gets run when a program
requests it.  This module implements such a mechanism.  A program
that wishes to use the mechanism must execute the statement

    import user

The user module looks for a file .pythonrc.py in the user's home
directory and if it can be opened, execfile()s it in its own global
namespace.  Errors during this phase are not caught; that's up to the
program that imports the user module, if it wishes.

The user's .pythonrc.py could conceivably test for sys.version if it
wishes to do different things depending on the Python version.

%prep
install -p -m644 %SOURCE0 .
2to3 -w -n %oname.py

%install
install -d %buildroot%python3_sitelibdir
install -p -m644 %oname.py %buildroot%python3_sitelibdir/

%files
%python3_sitelibdir/*

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.7.6-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Aug 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.7.6-alt1
- Initial build for Sisyphus

