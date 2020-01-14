%define oname initgroups

Name: python3-module-%oname
Version: 4.0
Release: alt1

Summary: Convenience uid/gid helper function used in Zope2
License: ZPLv2.1
Group: Development/Python3
Url: https://pypi.python.org/pypi/initgroups/

# https://github.com/zopefoundation/initgroups.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
initgroups provides a convenience function to deal with user / group ids
on Unix-style systems.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir/
mv %buildroot%python3_sitelibdir_noarch/* %buildroot%python3_sitelibdir/
%endif

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 4.0-alt1
- Version updated to 4.0
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.14.0-alt1.dev0.git20150618.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.14.0-alt1.dev0.git20150618
- Version 2.14.0.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.1-alt1.dev.git20130313
- Version 2.13.1dev

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

