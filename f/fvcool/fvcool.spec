%define origname FVCool104

Name: fvcool
Version: 1.04
Release: alt3

Summary: CPU cooling software for AMD's Athlon/Duron

License: BSD like
Group: System/Configuration/Hardware
Url: http://www.nt.phys.kyushu-u.ac.jp/shimizu/

Source: %origname.tar.bz2
Source1: %name-rc
Patch: fvcool-1.04-alt-hack-configure.patch

# Automatically added by buildreq on Mon May 24 2004
#BuildRequires: hostinfo libdb4.2-devel

# Do not use with kernel version before 2.4.26-alt1
Requires: kernel >= 2.4.26

%description
CPU cooling software for AMD's Athlon/Duron

%prep
%setup -n %origname
%patch

%build
autoreconf -fisv
%configure
%make

%install
install -D -m644 %name $RPM_BUILD_ROOT/usr/sbin/%name
install -D -m755 %SOURCE1 %buildroot%_initdir/%name

%post
%post_service %name

%preun
%preun_service %name

%files
%doc ReadMe* CopyRight
%attr(0755, root, wheel) /usr/sbin/%name
%_initdir/%name

%changelog
* Wed Mar 03 2010 Igor Vlasenko <viy@altlinux.ru> 1.04-alt3
- resurrected from orphaned

* Sun Jan 23 2005 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt2
- add init.d script (bug #5926), thanks viy@

* Sun Nov 07 2004 Vitaly Lipatov <lav@altlinux.ru> 1.04-alt1
- new version

* Mon May 24 2004 Vitaly Lipatov <lav@altlinux.ru> 1.03-alt1
- first build for Sisyphus
