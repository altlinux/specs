%define git 4f76d51

Name: pam-mysql
Summary: MySQL authentication for PAM
Version: 0.8.1
Release: alt0.1.g%git

Packager: L.A. Kostis <lakostis@altlinux.ru>
Url: https://github.com/NigelCunningham/pam-MySQL
Source: pam_mysql-%version.tar
Source1: %name.conf
License: GPL2
Group: System/Libraries

BuildRequires(pre): libpam-devel
BuildRequires: gcc-c++ libmysqlclient21-devel libstdc++-devel zlib-devel libssl-devel

%description
This is a module that allows people to login to PAM-aware applications by
authenticating to a MySQL database. Now configurable in terms of which
host the database resides upon and which table and username and password
column to interrogate.

%prep
%setup -q -n pam_mysql-%version

%build
%autoreconf
%configure --with-pam-mods-dir=%_pam_modules_dir --with-openssl

%make

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%_sysconfdir
install -p -m600 %SOURCE1 %buildroot%_sysconfdir/

%files
%doc ChangeLog AUTHORS COPYING README NEWS
%_pam_modules_dir/pam_mysql.so
%attr(600,root,root) %config(noreplace) %_sysconfdir/%name.conf

%changelog
* Tue Sep 24 2019 L.A. Kostis <lakostis@altlinux.ru> 0.8.1-alt0.1.g4f76d51
- Updated to v0.8.1-30-g4f76d51.

* Thu Nov 24 2011 L.A. Kostis <lakostis@altlinux.ru> 0.7-alt11.RC1
- Retake package.

* Wed May 02 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.7-alt10.RC1
- 0.7RC1.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.7-alt9.pre3.3.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Feb 09 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7-alt9.pre3.3
- Rebuild with new libMySQL.

* Mon Feb 06 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.7-alt9.pre3.1
- Added libssl-devel to buildrequires.

* Fri Dec 16 2005 Pavlov Konstantin <thresh@altlinux.ru> 0.7-alt9.pre3
- New version.

* Thu Feb 05 2004 Igor Muratov <migor@altlinux.ru> 0.5-alt1
- First build for ALT.

* Mon Feb 17 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- fix buildrequires & requires

* Sun Feb 02 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.5-2mdk
- rebuild

* Wed Dec 04 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.5-1mdk
- from Terry Froy <tez@spilsby.net> :
	- Initial spec
