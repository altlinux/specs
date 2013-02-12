%define soname 0.0.0
%define _monodir /usr/lib/mono

Name: mod_mono
Version: 1.9
Release: alt1.1

Summary: A module to deploy an ASP.NET application on Apache2 with Mono
License: GPL
Group: System/Servers

Url: http://www.mono-project.com
Packager: Mono Maintainers Team <mono@packages.altlinux.org>

# http://go-mono.com/sources/mod_mono/%name-%version.tar.gz
Source0: %name-%version.tar
Source1: %name.apache.conf
Source2: monodemo.apache.conf
Source3: mono.conf
Source4: mono.load
Source5: monodemo.apache2.conf
Source6: monodemo.mods.start
Source7: mono.start

Patch0: %name-%version-%release.patch

BuildRequires(pre): apache2-devel > 2.2.22-alt15
BuildRequires: apache-devel

%description
This package provides mod_mono, a package that allows Apache to
serve ASP.NET pages by proxying the requests to a slightly
modified version of our XSP server, called mod-mono-server, that
is installed along with XSP.

%package -n apache-%name
Summary: A module to deploy an ASP.NET application on Apache1 with Mono
Group: System/Servers
Requires: apache-base
Conflicts: %apache2_name-%name

%description -n apache-%name
This package provides mod_mono, a package that allows Apache to
serve ASP.NET pages by proxying the requests to a slightly
modified version of our XSP server, called mod-mono-server, that
is installed along with XSP.

%package -n apache-monodemo
Summary: apache1-related mono demonstration application configs
Group: System/Servers
Requires: apache-%name, xsp-samples

%description -n apache-monodemo
%summary

%package -n %apache2_name-%name
Summary: A module to deploy an ASP.NET application on Apache2 with Mono
Group: System/Servers
Requires: %apache2_name-base > 2.2.22-alt15
Requires: %apache2_name-mmn = %apache2_mmn
Requires: %apache2_libaprutil_name >= %apache2_libaprutil_evr
Conflicts: apache-%name

%description -n %apache2_name-%name
This package provides mod_mono, a package that allows Apache to
serve ASP.NET pages by proxying the requests to a slightly
modified version of our XSP server, called mod-mono-server, that
is installed along with XSP.

%package -n %apache2_name-monodemo
Summary: %apache2_name-related mono demonstration application configs
Group: System/Servers
Requires: %apache2_name-%name > 1.9-alt1
Requires: xsp-samples

%description -n %apache2_name-monodemo
%summary

%package doc
Summary: Documentation for %name module (readme and manpage)
Group: Documentation

%description doc
%summary

%prep
%setup
%patch0 -p1

%build
%autoreconf
# 1. Build module for apache1.
%configure \
	--with-apxs=%_sbindir/apxs \
	--with-mono-default-config-dir=%_sysconfdir/mono/mod-mono-applications \
	--disable-static \
	--with-gnu-ld
%make_build
cp src/.libs/mod_mono.so.%soname mod_mono.so.%soname-1.3

%make clean

# 2. Build module for apache2.
%configure \
	--with-apxs=%apache2_apxs \
	--with-apr-config=%_bindir/apr-1-config \
	--with-mono-default-config-dir=%_sysconfdir/mono/mod-mono-applications \
	--disable-static \
	--with-gnu-ld \
	CFLAGS="$CFLAGS -I%_includedir/apu-1" \
	LDFLAGS="-lapr-1"
%make_build
cp src/.libs/mod_mono.so.%soname mod_mono.so.%soname-2

%install

# crate dirs
install -dm1770 %buildroot%_localstatedir/%name
install -dm1770 %buildroot%_var/run/%name

# install apache1 module
install -pDm0644 mod_mono.so.%soname-1.3 %buildroot/%apache_moduledir/%name.so.%soname
pushd %buildroot/%apache_moduledir
ln -s %name.so.%soname %name.so
popd

# install apache2 module
install -pDm0644 mod_mono.so.%soname-2 %buildroot/%apache2_moduledir/%name.so.%soname
pushd  %buildroot/%apache2_moduledir
ln -s %name.so.%soname %name.so
popd

# apache1 configs
install -pDm0644 %SOURCE1 %buildroot%apache_modconfdir/%name.conf
install -pDm0644 %SOURCE2 %buildroot%apache_modconfdir/monodemo.conf

# apache2 configs
install -pDm0644 %SOURCE3 %buildroot%apache2_mods_available/mono.conf
install -pDm0644 %SOURCE4 %buildroot%apache2_mods_available/mono.load
install -pDm0644 %SOURCE5 %buildroot%apache2_addonconfdir/A.monodemo.conf
install -pDm0644 %SOURCE6 %buildroot%apache2_mods_start/110-monodemo.conf
install -pDm0644 %SOURCE7 %buildroot%apache2_mods_start/100-mono.conf

# manpage
install -pDm0644 man/mod_mono.8 %buildroot%_man8dir/%name.8

# for %%ghost
mkdir -p %buildroot%apache2_mods_enabled/
touch %buildroot%apache2_mods_enabled/mono.conf
touch %buildroot%apache2_mods_enabled/mono.load

%post -n apache-%name
%_initdir/httpd condrestart

%postun -n apache-%name
%_initdir/httpd condrestart

%files -n apache-%name
%config(noreplace) %apache_modconfdir/%name.conf
%apache_moduledir/%name.so*
%dir %attr(1770,root,%apache_group) %_localstatedir/%name
%dir %attr(1770,root,%apache_group) %_var/run/%name

%files -n %apache2_name-%name
%config(noreplace) %apache2_mods_available/mono.*
%config(noreplace) %apache2_mods_start/100-mono.conf
%ghost %apache2_mods_enabled/mono.*
%apache2_moduledir/%name.so*
%dir %attr(1770,root,%apache2_group) %_localstatedir/%name
%dir %attr(1770,root,%apache2_group) %_var/run/%name

%files -n apache-monodemo
%config(noreplace) %apache_modconfdir/monodemo.conf

%files -n %apache2_name-monodemo
%config(noreplace) %apache2_addonconfdir/A.monodemo.conf
%config(noreplace) %apache2_mods_start/110-monodemo.conf

%files doc
%_man8dir/%name.*
%doc README NEWS ChangeLog AUTHORS

%changelog
* Sat Feb 09 2013 Aleksey Avdeev <solo@altlinux.ru> 1.9-alt1.1
- Rebuild with apache2-2.2.22-alt16 (fix unmets)
- Add %%apache2_mods_start/100-mono.conf file for auto loading module
- Add %%ghost for %%apache2_mods_enabled/*.{load,conf}

* Wed Apr 23 2008 Vladimir V Kamarzin <vvk@altlinux.ru> 1.9-alt1
- 1.9
- Apply upstream patch for fix mod_mono compilation for apache 1.3
  https://bugzilla.novell.com/show_bug.cgi?id=374272

* Wed Dec 19 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.6-alt1
- 1.2.6

* Tue Aug 21 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.4-alt2
- Fixed apache2-mod_mono postun script

* Thu Aug 09 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed May 30 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.1-alt4
- Fixed default path to mod-mono-server

* Mon Apr 16 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.1-alt3
- Change module activation way accordind to new apache2 scheme
- Fix permissions of %%_var/run/%%name in apache2 subpackage
- Move monodemo-related configs to separate packages
- Move module enabling/disabling to monodemo subpackage.
- Enable mod_mono after apache2-%name package installation, disable it before
  final uninstall

* Tue Mar 13 2007 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.1-alt2
- Update buildrequires:
  + use libapr1-devel libaprutil1-devel instead of libapr-devel libaprutil-devel
- Update configure options of apache2 module:
  + Use apr-1-config instead of apr-config
  + Use %%_includedir/apu-1 instead of %%_includedir/apu
  + Link with -lapr-1
- Don't touch source by sed, modify code instead
- Switch to use .gear-tags

* Fri Dec 01 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.2.1-alt1
- 1.2.1
- Removed mod_mono-1.1.18-alt-configure.in-patch:
  + inegrated into source tree of master-branch
  + don't delete test -x call, use test -n instead

* Wed Nov 08 2006 Vladimir V Kamarzin <vvk@altlinux.ru> 1.1.18-alt1
- 1.1.18
- Build module for Apache1 and Apache2 instead of Apache2-only, separate
  packages
  + apache-%name
  + apache2-%name
  + %name-doc
- Added mod_mono-1.1.18-alt-configure.in-patch - don't check existance of
  MonoApplicationsConfigDir at build-time
- Fix default path to mod-mono-server
- Move socket file from /tmp to %%_var/run/%%name/
- Move wapdir from /tmp to %%_localstatedir/%%name/
- Condrestart apache after installing module
- Use full url in Source
- Set Packager to mono@packages
- Added sample apache-configs
- Removed README.ALT

* Wed Nov 23 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.10-alt1
- Update to release

* Sat Oct 08 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.1.9.2-alt1
- update to release

* Sun May 22 2005 Evgeny Sinelnikov <sin@altlinux.ru> 1.0.9-alt1
- release

* Sun Sep 26 2004 Pavel S. Mironchik <tibor@altlinux.ru> 1.0-alt1
- Rebuilded for ALTlinux
