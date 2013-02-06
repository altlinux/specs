Name: omniORBpy
Version: 4.2.0
Release: alt1.svn20130111
Summary: Python bindings for CORBA object request broker (omniORB)
License: LGPLv2.1+
Group: Networking/Remote access
Url: http://sourceforge.net/projects/omniorb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel gcc-c++ libssl-devel libomniORB-devel
BuildPreReq: libomniORB-idl

%description
omniORBpy is a CORBA object request broker for Python.

%package -n python-module-%name
Summary: Python bindings for CORBA object request broker (omniORB)
Group: Development/Python
Conflicts: python-module-pyorbit

%description -n python-module-%name
omniORBpy is a CORBA object request broker for Python.

%package -n python-module-%name-devel
Summary: Development files of omniORBpy
Group: Development/Python
BuildArch: noarch
Requires: python-module-%name = %version-%release
Requires: libomniORB-devel libomniORB-idl

%description -n python-module-%name-devel
omniORBpy is a CORBA object request broker for Python.

This package contains development files of omniORBpy.

%package -n python-module-%name-docs
Summary: Documentation and examples for omniORBpy
Group: Development/Documentation
BuildArch: noarch

%description -n python-module-%name-docs
omniORBpy is a CORBA object request broker for Python.

This package contains development documentation and examples for
omniORBpy.

%prep
%setup

%build
%autoreconf
sed -i 's|\(get_python_lib\)(0|\1(1|' configure
%configure \
	--with-omniorb=%prefix \
	--with-openssl=%prefix
%make_build

%install
%makeinstall_std

%files -n python-module-%name
%doc README* update.log ReleaseNotes.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/omniidl_be/__init__.py*

%files -n python-module-%name-devel
%_includedir/*

%files -n python-module-%name-docs
%doc doc/*.pdf doc/omniORBpy examples

%changelog
* Wed Feb 06 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1.svn20130111
- New snapshot

* Fri Sep 14 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.2.0-alt1.svn20120816
- Version 4.2.0

* Fri Aug 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt2
- Added explicit conflict with python-module-pyorbit

* Thu Aug 23 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6-alt1
- Initial build for Sisyphus

