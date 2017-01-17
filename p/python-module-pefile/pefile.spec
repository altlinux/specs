%define _unpackaged_files_terminate_build 1
%define svnrev 141

%define oname pefile
Name: python-module-%oname
Version: 2016.3.28
Release: alt1
Summary: Portable Executable reader module
License: MIT
Group: Development/Python
Url: http://code.google.com/p/pefile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://pefile.googlecode.com/svn/trunk
Source0: https://pypi.python.org/packages/92/c0/8589ce9734ffdba258bd3e5acd4afb2e3586c121fe73402f686288b684b0/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
BuildArch: noarch

%description
pefile is a multi-platform Python module to read and work with Portable
Executable (aka PE) files. Most of the information in the PE Header is
accessible, as well as all the sections, section's information and data.

%prep
%setup -q -n %{oname}-%{version}
sed -i 's|\$LastChangedRevision\$|%svnrev|' %oname.py

%build
%python_build

%install
%python_install

%files
%doc README PKG-INFO
%python_sitelibdir/*

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 2016.3.28-alt1
- automated PyPI update

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20140310
- New snapshot

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20121216
- New snapshot

* Fri Jan 27 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20120122
- New snapshot

* Fri Dec 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20110901
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.10-alt1.svn20110505.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20110505
- New snapshot

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20101108
- New snapshot

* Tue Sep 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt1.svn20100817
- Initial build for Sisyphus

