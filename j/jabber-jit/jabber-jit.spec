%define dname jabberd-jit
%define username _jabber_jit

Name: jabber-jit

Version: 1.2.1
Release: alt0.2

Summary: Jabber ICQ Transport

Group: System/Servers
License: %gpl2plus
URL: http://omever.ya.ru/
#SVN URL: svn://ns1.mytlt.ru/jit/
Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: jit-%version.tar
Source1: %name.xml
Source2: %name.logrotate
Source3: %name.init
Source4: %name.adapter

Patch1:  %name-1.1.5-no-thanks-we-have-logrotate.patch
Patch2:  %name-1.2.1-alt-headers_fix.patch

Obsoletes: ejabberd-jit
#Requires(post): jabber-common
Requires(post): rpm-macros-jabber

BuildRequires(pre): rpm-build-licenses jabber-common
# Automatically added by buildreq on Fri Dec 12 2008
BuildRequires: gcc-c++ libmhash-devel

%description
Jabber ICQ Transport is a Jabber component which provides interoperability
between ICQ and Jabber IM systems. JIT is based on a special fast jabberd
core with pthreads.

%prep
%setup -q -n jit-%version
%patch1 -p1
%patch2 -p0

pushd jit/jit
../../makeversion.sh
popd

%build
%__subst '/^COMMON_CFLAGS/ s|-I%_includedir ||' platform-settings
%__subst 's|^OUT_FILE=.*|OUT_FILE=jabber-jit|' platform-settings
%__subst '/^COMMON_CFLAGS/ s|-g ||' platform-settings
%__subst '/^CONFIG_FILE/ s|jabber.xml|jabber-jit.xml|' platform-settings

%configure
%make_build

%install
mkdir -p %buildroot%_sbindir \
    %buildroot%_libdir/%name \
    %buildroot%_sysconfdir/%name \
    %buildroot%_spooldir/%name \
    %buildroot%_initdir \
    %buildroot%_docdir/%name-%version \
    %buildroot%_sysconfdir/logrotate.d

/bin/install jabberd/jabberd-jit %buildroot%_sbindir/jabber-jit
/bin/install jit/jit.so %buildroot%_libdir/%name
/bin/install xdb_file/xdb_file.so %buildroot%_libdir/%name

/bin/install {README,AUTHORS} %buildroot%_docdir/%name-%version
/bin/install -m644 LICENSE %buildroot%_docdir/%name-%version
/bin/install doc/FAQ %buildroot%_docdir/%name-%version
/bin/install jit/{INSTALL,*.example} %buildroot%_docdir/%name-%version
/bin/install -m644 ChangeLog %buildroot%_docdir/%name-%version

/bin/install -m640 %SOURCE1 %buildroot%_sysconfdir/%name/%name.xml
/bin/install -m644 %SOURCE2 %buildroot%_sysconfdir/logrotate.d/%name
/bin/install -m755 %SOURCE3 %buildroot%_initdir/%name
/bin/install -pD -m0755 %SOURCE4 %buildroot%_jabber_component_dir/%name

%__subst 's#@libdir@#%_libdir/%{name}#g' %buildroot%_initdir/%name \
			%buildroot%_sysconfdir/%name/%name.xml
%__subst 's#@configfile@#%_sysconfdir/%name/%name.xml#g' %buildroot%_jabber_component_dir/%name


%pre
%_sbindir/groupadd -r -f %username 2>/dev/null ||:
%_sbindir/useradd -r -g %username -c 'jabber transport' -d %_datadir/%name \
 -s /dev/null %username 2>/dev/null ||:

%post
%_jabber_config
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%name
%_libdir/%name
%config(noreplace) %attr(0640,root,%username) %_sysconfdir/%name/%name.xml
%dir %attr(1770,root,%username) %_spooldir/%name
%_initdir/%name
%_docdir/%name-%version
%_sysconfdir/logrotate.d/%name
%_jabber_component_dir/%name

%changelog
* Tue May 26 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.1-alt0.2
- Fix build with GCC 4.4

* Wed Feb 04 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.1-alt0.1
- Pre-1.2.1 version from SVN trunk
  * Fix for ICQ protocol changes
- Add LSB header into init script

* Fri Dec 12 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.2.0-alt1
- New version 1.2.0
- Revives from orphaned
- Fix file permissions (Closes: #13296)
- Fix pathes in config files (Closes: #12558)
- Fix init script (Closes: #12557)

* Tue Mar 11 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.1.7-alt1.svn7.1
- Build with patches from om@mytlt.ru

* Tue Mar 27 2007 Mikhail Pokidko <pma@altlinux.ru> 1.1.7-alt1
- New version.
- ALT Linux Jabber Policy packaging.

* Tue Dec 13 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.6-alt5
- Updated scripts and configuration to match changes in jabberd 1.4.4

* Wed Jul 27 2005 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.6-alt4
- Patch by Sergey Golovan to add browse/disco capabilities [Patch7]

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.6-alt3.1
- Rebuilt with libstdc++.so.6.

* Thu Oct 14 2004 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.6-alt3
- Use jabber-conftool in scripts

* Wed Dec 31 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.6-alt2
- Bring C++ code to the standard in order to compile with g++ 3.3 [Patch6]

* Thu Jul 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.6-alt1
- New version
- Patch4 updated
- Updated the init script for start_daemon/stop_daemon

* Sun Mar 23 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.5-alt1
- new version

- Patch0: avoid an unnecessary ICQ auth request when Jabber user authorizes
  an ICQ user's s10n
- Patch1 removed (gone upstream)
- Patch2 updated
- Patch4 updated
- Patch5: don't adorn logfile names with date
- Added logrotate config
  
* Tue Feb 18 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.4-alt1
- 1.1.4
- Patch0 removed (gone upstream)
- Patch2 updated and enhanced

* Sat Feb 08 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.3-alt1
- 1.1.3
- Updated Patch4 to also strip off illicit name attribute from s10n
- Updated default config
- More stuff in the documents

* Fri Feb 07 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt3
- Patch4: get rid of origfrom hack attribute

* Thu Feb 06 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt2
- Patch3: experimental patch to get rid of the /registered resource
- Fixed lockfile name in the init script

* Tue Jan 28 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt1
- Added init script

* Fri Jan 24 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt0.2
- Patch2: Clean vCards DESC from IP address info and ego-boosting
  
* Fri Jan 17 2003 Mikhail Zabaluev <mhz@altlinux.ru> 1.1.2-alt0.1
- Initial pre-release (no good init script as of yet)
  

