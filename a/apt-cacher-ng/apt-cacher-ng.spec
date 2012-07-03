Name: apt-cacher-ng
Version: 0.3.8
Release: alt1.1

Summary: Caching HTTP download proxy for software packages

License: Public domain
Group: Development/Other
Url: http://www.unix-ag.uni-kl.de/~bloch/acng/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://ftp.debian.org/debian/pool/main/a/apt-cacher-ng/%{name}_%version.orig.tar.gz
Patch: apt-cacher-ng-0.3.8-alt-gcc4.6.patch

# Automatically added by buildreq on Sat Apr 18 2009
BuildRequires: boost-devel bzlib-devel gcc-c++ libfuse-devel zlib-devel

%description
Apt-Cacher NG is a caching HTTP download proxy for software packages,
primarily for Debian/Ubuntu clients. It's partially based on concepts
of Apt-Cacher but is rewritten with a main focus on performance and low
resource usage.

%prep
%setup -q
%patch -p2

%build
%make all

%install
mkdir -p %buildroot%_sbindir %buildroot%_libdir/%name %buildroot%_mandir/man8/
mkdir -p %buildroot%_sysconfdir/%name/ %buildroot%_sysconfdir/xinetd.d
install apt-cacher-ng %buildroot%_sbindir/%name
install acngfs %buildroot%_sbindir/%name
install in.acng expire-caller.pl distkill.pl %buildroot%_libdir/%name/
install -m644 doc/man/*.8 %buildroot%_mandir/man8/
cp -a conf/{*mirror*,*.html,*.css} %buildroot%_libdir/%name/
cp -a conf/*.conf %buildroot%_sysconfdir/%name/
cd %buildroot%_sysconfdir/%name/ && cp -s ../..%_libdir/%name/{*mirror*,*.html,*.css} . && cd -
mkdir -p %buildroot/var/log/%name/

cat <<EOF > %buildroot%_sysconfdir/xinetd.d/%name
# default: off
# description: The %name server.
service %name
{
	disable		= yes
	socket_type	= stream
	protocol	= tcp
	wait		= no
	user		= root
	nice		= 10
	rlimit_as	= 16M
	server		= %_sbindir/in.acng
	only_from	= 127.0.0.1
	server_args = -c %_sysconfdir/%name
}
EOF

%files
%doc COPYING README TODO
%_sysconfdir/%name/
%_sysconfdir/xinetd.d/%name
%_sbindir/%name
%_libdir/%name/
%_mandir/man8/*
/var/log/%name/

%changelog
* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.8-alt1.1
- Fixed build

* Sat Apr 18 2009 Vitaly Lipatov <lav@altlinux.ru> 0.3.8-alt1
- initial build for ALT Linux Sisyphus

