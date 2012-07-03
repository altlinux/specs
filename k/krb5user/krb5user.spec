Name: krb5user
Version: 0.1.2
Release: alt2.3

Summary: User helper library for MIT Kerberos

License: %gpl2plus
URL: http://tartarus.ru/
Group: System/Libraries
Packager: Evgeny Sinelnikov <sin@altlinux.ru>

Source: %name-%version.tar

%setup_python_subpackage %name

# Automatically added by buildreq on Tue Oct 07 2008
BuildRequires: boost-python-devel gcc-c++ libkrb5-devel scons
BuildRequires: libcom_err-devel libkrb5-devel scons

BuildRequires: boost-devel >= 1.39.0

BuildRequires(pre): rpm-build-licenses

%description
User helper library for MIT Kerberos.

%package -n lib%name
Summary: User helper library for MIT Kerberos
Group: System/Libraries

%description -n lib%name
User helper library for MIT Kerberos

%package -n lib%name-devel
Summary: Headers for developing with MIT Kerberos user helper library
Group: System/Libraries

%description -n lib%name-devel
Headers for developing with MIT Kerberos user helper library

%package -n %packagename
Summary: Python binding for MIT Kerberos user helper library
Group: Development/Python
%setup_std_python_package_deps

%description -n %packagename
Python binding for MIT Kerberos user helper library

%prep
%setup -q

%build
scons

%install
scons install --install-sandbox=%buildroot --libdir=%_libdir

%files -n lib%name
%_libdir/lib*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/lib*.so
%_libdir/pkgconfig/*

%files -n %packagename
%python_sitelibdir/*

%changelog
* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.2
- Rebuilt with Boost 1.48.0

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.2-alt2.1.3.1
- Rebuild with Python-2.7

* Sat Jul 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.1.3
- Rebuilt with Boost 1.47.0

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.1.2
- Rebuilt with Boost 1.46.1

* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 0.1.2-alt2.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt2.1
- Rebuilt with python 2.6

* Fri Jul 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.2-alt2
- Rebuild with boost-1.39.0

* Tue Apr 21 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.2-alt1
- Clean code for krb5 internal FQDN lookup

* Tue Mar 03 2009 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.1-alt1
- Fixed long delay due backward resolving with hostname like FQDN
- Removed obsolete macroses %post*_ldconfig

* Tue Nov 11 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt4
- Fixed install for x86_64

* Wed Oct 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt3
- Fixed bug with check for fqdn from gethostname() if getaddrinfo() failed

* Wed Oct 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt2
- Added krb5user_set_ccname() to python binding

* Wed Oct 22 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.1.0-alt1
- Using gethostname() if getaddrinfo() failed for default hostname
- Added krb5user_set_ccname() for change credential cache

* Tue Oct 07 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.3-alt1
- Added kinit_password_*() functions
- Added python bindings

* Fri Sep 26 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.2-alt1
- Fixed build scripts
- Added pkgconfig

* Thu Sep 25 2008 Evgeny Sinelnikov <sin@altlinux.ru> 0.0.1-alt1
- Initial first build

