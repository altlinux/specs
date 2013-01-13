%set_verify_elf_method unresolved=strict

Name: gnustep-gsldap
Version: r31303
Release: alt1.svn20100910
Summary: Library which provides an Objective-C interface to access LDAP Servers
License: LGPLv3
Group: Graphical desktop/GNUstep
Url: http://www.gnustep.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.gna.org/svn/gnustep/libs/gsldap/trunk/
Source: %name-%version.tar

BuildPreReq: gcc-objc gnustep-make-devel libgnustep-objc2-devel /proc
BuildPreReq: gnustep-base-devel libldap-devel

%description
gsldap is a library which use open ldap (www.openldap.org) C libraries
to provide an Objective-C interface to access LDAP Servers

%package -n lib%name
Summary: Library which provides an Objective-C interface to access LDAP Servers
Group: System/Libraries

%description -n lib%name
gsldap is a library which use open ldap (www.openldap.org) C libraries
to provide an Objective-C interface to access LDAP Servers

This package contains shared libraries of gsldap.

%package -n lib%name-devel
Summary: Development files of gsldap
Group: Development/Objective-C
Provides: %name-devel = %version-%release
Requires: lib%name = %version-%release

%description -n lib%name-devel
gsldap is a library which use open ldap (www.openldap.org) C libraries
to provide an Objective-C interface to access LDAP Servers

This package contains development files of gsldap.

%prep
%setup

mkdir -p gsldap
for i in *.h; do
	ln -s ../$i gsldap/
done

%build
%make_build \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes \
	AUXILIARY_CPPFLAGS='-O2' \
	CONFIG_SYSTEM_LIBS='-lgnustep-base -lobjc2'
 
%install
%makeinstall_std GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

%files -n lib%name
%doc ChangeLog README
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Sun Jan 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> r31303-alt1.svn20100910
- Initial build for Sisyphus

