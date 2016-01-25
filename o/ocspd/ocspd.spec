%define ocspduser _ocspd
%define ocspd_root %_localstatedir/%name


Name: ocspd
Version: 3.1.1
Release: alt3.git20150326

Summary: OCSP Responder
Group: System/Servers
License: License: %asl
Url: https://pki.openca.org/projects/ocspd/
Packager: Vladimir Didenko <cow@altlinux.ru>

Source0: %name-%version.tar
Source1: %name.init
Source2: %name.service
Source3: %name.sysconf
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-licenses
BuildRequires: libpki-devel
BuildRequires: libmysqlclient-devel
BuildRequires: zlib-devel

%description
The OpenCA OCSPD project is aimed to develop a robust and easy-to-install
OCSP daemon. The server is developed as a stand-alone application and can
be integrated into many different PKI solutions as it does not depend on
specific database scheme. Furthermore it can be used as a responder for
multiple CAs.

The OCSP Responder is an rfc2560 compliant OCSPD responder. The purpose
of such a server is to provide an on-line tool to verify the status of a
certificate (such as Mozilla/Firefox/Netscape7).

%prep
%setup -n %name-%version
%patch0 -p1

%build
cp src/global-vars.in src/global-vars
%autoreconf
%configure --with-ocspd-user=%{ocspduser} --with-ocspd-group=%{ocspduser}
%make

%install
%makeinstall_std

install -m755 -pd %buildroot%{_initdir}
rm -f %buildroot%{_sysconfdir}/init.d/*
install -pD -m755 %SOURCE1 %buildroot%_initdir/%name
install -p -D -m 644 %SOURCE2 %buildroot%_unitdir/%name.service
install -p -D -m 644 %SOURCE3 %buildroot%_sysconfdir/sysconfig/%name
install -m755 -pd %buildroot%_sysconfdir/%name/ca-samples.d
mv %buildroot%_sysconfdir/%name/ca.d/* %buildroot%_sysconfdir/%name/ca-samples.d

%pre
%_sbindir/groupadd -r -f %ocspduser ||:
/usr/sbin/useradd -r -g %ocspduser -d /dev/null -s /dev/null -c 'OCSPD user' %ocspduser >/dev/null 2>&1 ||:

%post
%post_service %name

%preun
%preun_service %name

%files
%doc AUTHORS COPYING ChangeLog INSTALL README NEWS
%config(noreplace) %_sysconfdir/%name/pki/token.d/*.xml
%config(noreplace) %_sysconfdir/%name/%name.xml
%config(noreplace) %_sysconfdir/sysconfig/%name
%_sysconfdir/%name/ca.d/
%_sysconfdir/%name/ca-samples.d/*.xml
%_bindir/%name-genreq.sh
%exclude %_bindir/test.sh
%exclude %_pkgconfigdir/openca-ocspd.pc
%_sbindir/%name
%_initdir/%name
%systemd_unitdir/%name.service
%_man3dir/*.3.*

%changelog
* Mon Jan 25 2016 Vladimir Didenko <cow@altlinux.ru> 3.1.1-alt3.git20150326
- new version

* Thu Jul 9 2015 Vladimir Didenko <cow@altlinux.ru> 3.1.1-alt2.1
- pack doc files

* Thu Jul 9 2015 Vladimir Didenko <cow@altlinux.ru> 3.1.1-alt2
- Add reload command to service file

* Mon Jul 6 2015 Vladimir Didenko <cow@altlinux.ru> 3.1.1-alt1
- Initial build
