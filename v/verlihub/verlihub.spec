%define rel -RC2
%define verlihub_user _verlihub
%define verlihub_group _verlihub
%define verlihub_home %_logdir/%name

Name: verlihub
Version: 0.9.8e
Release: alt1.1

Summary: Direct Connect (p2p) Server

License: GPL
Group: Networking/File transfer
Url: http://www.verlihub-project.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: verlihub-%version%rel.tar

# Automatically added by buildreq on Fri Mar 21 2008
BuildRequires: gcc-c++ glibc-devel libGeoIP-devel libMySQL-devel libpcre-devel zlib-devel

Requires: /usr/bin/mysql

%description
This program let's you have a p2p server for file sharing.

%package -n lib%name-devel
Summary: The files needed for %name development
Summary(ru_RU.KOI8-R): Файлы, требующиеся для разработки приложений с использованием %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
The lib%name-devel package contains the necessary include files
for developing applications with %name

%package -n lib%name
Summary: The library files needed for %name
Group: Networking/File transfer

%description -n lib%name
The lib%name package contains the necessary library for %name

%prep
%setup -n %name

%build
export PTHREAD_LIBS=-lpthread
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

install -d -m1775 %buildroot%_var/run/%name
install -d -m1775 %buildroot%_var/log/%name

install -d %buildroot%_sysconfdir/%name/plugins
install -d %buildroot%_sysconfdir/%name/scripts
ln -s ../../..%_libdir/libplug_pi.so.0.0.0 %buildroot%_sysconfdir/%name/plugins

%pre
/usr/sbin/groupadd -r -f %verlihub_group ||:
/usr/sbin/useradd -g %verlihub_group -c 'The verlihub Daemon' \
       -d %verlihub_home -s /dev/null -r %verlihub_user >/dev/null 2>&1 ||:

%files
%doc AUTHORS README* ChangeLog TODO
%dir %attr(0750,root,%verlihub_group) %_sysconfdir/%name
%dir %attr(0750,root,%verlihub_group) %_sysconfdir/%name/plugins
%dir %attr(0750,root,%verlihub_group) %_sysconfdir/%name/scripts
%dir %attr(1775,root,%verlihub_group) %_var/run/%name
%dir %attr(1775,root,%verlihub_group) %_var/log/%name
%_sysconfdir/%name/plugins/*
%_bindir/verlihub
%_bindir/vh_*
%_datadir/%name/

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/verlihub_config
%_libdir/*.so
%_includedir/%name/

%changelog
* Wed Nov 10 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.8e-alt1.1
- Rebuilt for soname set-versions

* Wed Jun 03 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.8e-alt1
- 0.9.8e

* Tue Dec 09 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.8d-alt4
- Remove obsolete %%post_ldconfig/%%postun_ldconfig calls

* Mon Oct 27 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 0.9.8d-alt3
- Fix build with gcc4.3 (patch from debian)

* Wed Jul 09 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 0.9.8d-alt2
- Merge older vvk's and thresh's builds with sisyphus version:
  + vh_install.in: default port changed to 4111
  + vh_runhub.in: fixed log/pid placement
  + Add pseudouser creation at %%pre stage
  + Package directory for config files
  + Package directories for logs and pidfile
  + Add README.ALT
- Apply db_charset.patch http://dc.hovel.ru/mysql41
- Add dependency on /usr/bin/mysql

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 0.9.8d-alt1
- initial build for ALT Linux Sisyphus

* Sun Nov 19 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9.9-alt0.CVS20061119
- Moved package to GIT:
  + upstream branch contains CVS from upstream
  + master branch contains patched source and all other stuff to build RPM.
- Merged patches:
  + verlihub-0.9.8c-include.patch
  + verlihub-0.9.8c-vh_install.patch
  + verlihub-0.9.8c-vh_runhub.patch
  + verlihub-0.9.8c-timeyear.patch
- Not merged:
  + verlihub-0.9.8c-gcc4.patch (merged upstream already).
- CVS from 20061119.

* Sun Jun 18 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9.8c-alt3.rc2
- gcc4 patch.

* Sun Jan 22 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.9.8c-alt2.rc2
- added time patch.

* Fri Dec 16 2005 Vladimir V Kamarzin <vvk@altlinux.ru> 0.9.8c-alt1.rc2
- Initial build for Sisyphus
