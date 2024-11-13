%define git %nil

Name: pam-mysql
Summary: MySQL authentication for PAM
Version: 1.0.0
Release: alt0.2.b3
License: GPL-2
Group: System/Libraries
Url: https://github.com/NigelCunningham/pam-MySQL

Packager: L.A. Kostis <lakostis@altlinux.ru>

Source: pam_mysql-%version.tar
Source1: %name.conf

Patch0: pam_mysql-alt-conf.patch
Patch1: pam_mysql-fix-dangling-pointer.patch
Patch2: pam_mysql-fix-tests-ub.patch

BuildRequires(pre): libpam-devel meson
BuildRequires: libmariadb-devel zlib-devel libssl-devel cmake ninja-build

%description
This is a module that allows people to login to PAM-aware applications by
authenticating to a MySQL database. Now configurable in terms of which
host the database resides upon and which table and username and password
column to interrogate.

%prep
%setup -q -n pam_mysql-%version
%autopatch -p2
subst "s,@PAM_DIR@,%_pam_modules_dir," meson.build

%build
%meson
%meson_build

%check
%meson_test

%install
%meson_install
install -pD -m600 %SOURCE1 %buildroot%_sysconfdir/%name.conf

%files
%doc AUTHORS COPYING README NEWS examples
%_pam_modules_dir/pam_mysql.so
%attr(600,root,root) %config(noreplace) %_sysconfdir/%name.conf

%changelog
* Wed Nov 13 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.2.b3
- tests: fix UB in password check.

* Thu Aug 15 2024 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.b3
- 1.0.0-beta3.

* Fri Sep 23 2022 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.b2
- 1.0.0-beta2.
- src/configure.c: fix memory allocation error.

* Wed Dec 01 2021 L.A. Kostis <lakostis@altlinux.ru> 1.0.0-alt0.1.b1
- Updated to 1.0.0-beta1.
- Switch to meson.
- Update License.
- Exclude 323 authentication from test (sig11 so beware!).

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
