%define mpiimpl openmpi
%define mpidir %_libdir/%mpiimpl

Name: srp
Summary: The Secure Remote Password protocol
Version: 2.1.2
Release: alt6
Group: Networking/Other
License: MIT
URL: http://srp.stanford.edu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://srp.stanford.edu/source/srp-2.1.2.tar.gz

Conflicts: telnet-server

BuildPreReq: %mpiimpl-devel libssl-devel
BuildPreReq: libpam0-devel libgnutls-devel libgnutls-openssl-devel zlib-devel
BuildPreReq: libncurses-devel cracklib-devel

%description
The Secure Remote Password protocol is the core technology behind the Stanford
SRP Authentication Project. The Project is an Open Source initiative that
integrates secure password authentication into new and existing networked
applications.

The Project's primary purpose is to improve password security by making strong
password authentication technology a standard part of deployed real-world
systems. This is accomplished by making this technology an easy-to-use,
hassle-free alternative to weak and vulnerable legacy password authentication
schemes. SRP makes these objectives possible because it offers a unique
combination of password security, user convenience, and freedom from restrictive
licenses.

%package profile
Summary: Profile settings for Secure Remote Password protocol
Group: Networking/Other
BuildArch: noarch
Requires: %name = %version-%release

%description profile
The Secure Remote Password protocol is the core technology behind the Stanford
SRP Authentication Project. The Project is an Open Source initiative that
integrates secure password authentication into new and existing networked
applications.

This package contains profile settings for SRP.

%package doc
Summary: Documentation for Secure Remote Password protocol
Group: Documentation
BuildArch: noarch

%description doc
The Secure Remote Password protocol is the core technology behind the Stanford
SRP Authentication Project. The Project is an Open Source initiative that
integrates secure password authentication into new and existing networked
applications.

This package contains documentation for SRP.

%package -n lib%name-devel
Summary: Static development files for Secure Remote Password protocol
Group: Development/C

%description -n lib%name-devel
The Secure Remote Password protocol is the core technology behind the Stanford
SRP Authentication Project. The Project is an Open Source initiative that
integrates secure password authentication into new and existing networked
applications.

This package contains static development files for SRP.

%prep
%setup

%build
mpi-selector --set %mpiimpl
source %mpidir/bin/mpivars.sh

%add_optflags -I%mpidir/include -DOPENSSL -DOPENSSL_ENGINE
export LIBS=-lcrypto
%configure \
	--bindir=%_libdir/%name/bin \
	--with-openssl=%prefix \
	--with-mpi=%mpidir/lib \
	--with-pam \
	--with-zlib \
	--with-engine \
	--enable-tls \
	--enable-loginf \
	--enable-glob
%make_build

%install
%makeinstall_std

mv %buildroot%_bindir/* %buildroot%_libdir/%name/bin/

%ifarch x86_64
mv %buildroot%_libexecdir/* %buildroot%_libdir/
%endif

install -d %buildroot%_sysconfdir/xinetd.d
cat <<EOF>%buildroot%_sysconfdir/xinetd.d/telnetd
# default: off
# description: A SRP telnet server

service telnet
{
	socket_type = stream
	protocol  = tcp
	user = root
	wait = no
	server = /usr/sbin/telnetd
	server_args = -h -a valid
	disable = yes
}
EOF

install -d %buildroot%_sysconfdir/profile.d
cat <<EOF>%buildroot%_sysconfdir/profile.d/%name.sh
export PATH=%_libdir/%name/bin:$PATH
EOF

%files
%doc CHANGES README README.NIS
%_libdir/%name
%_libdir/security/*
%_sbindir/*
%_sysconfdir/xinetd.d/*

%files profile
%_sysconfdir/profile.d/*

%files -n lib%name-devel
%_libdir/*.a
%_includedir/*

%files doc
%doc docs

%changelog
* Mon Jun 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt6
- Rebuilt with OpenMPI 1.6

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt5
- Rebuilt with cracklib 2.8.13-alt3

* Tue Mar 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt4
- Rebuilt for debuginfo

* Mon Nov 15 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt3
- Fixed for gcc 4.5.1

* Mon Oct 04 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt2
- Rebuilt with openssl10

* Wed Jul 08 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.2-alt1
- Initial build for Sisyphus

