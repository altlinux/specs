%define oname WebDAV

Name: python3-module-%oname
Version: 0.4.2
Release: alt3

Summary: This library provides a WebDAV client
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/Python_WebDAV_Library/
BuildArch: noarch

Source: %name-%version.tar
Patch0: port-on-python3.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python-tools-2to3


%description
This library provides a WebDAV client including ACP and searching
support.

%package -n python3-module-webdav
Summary: webdav submodule
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-webdav
This library provides a WebDAV client including ACP and searching
support.

%prep
%setup
%patch -p2

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%files
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/webdav

%files -n python3-module-webdav
%python3_sitelibdir/webdav


%changelog
* Mon Jan 13 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.4.2-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt2
- Moved webdav into separate package

* Sun Oct 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Initial build for Sisyphus

