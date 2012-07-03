%def_enable pam
%def_enable extra
%def_enable captcha
%def_disable hipe

Name: ejabberd
Version: 2.1.10
Release: alt1

Summary: Fault-tolerant distributed Jabber server written in Erlang
License: GPL2
Group: System/Servers
Url: http://www.process-one.net/en/ejabberd/

Requires: erlang >= R11B.5
Requires: jabber-common >= 0.2
Requires: su

BuildRequires(pre): jabber-common >= 0.2
BuildRequires: erlang-devel erlang-otp-devel libcom_err-devel libexpat-devel libssl-devel zlib-devel
%{?_enable_pam:BuildRequires: libpam-devel}

Source: %name-%version-%release.tar

%description
ejabberd is a Free and Open Source distributed fault-tolerant Jabber
server. It writen mostly in Erlang.

The main features of ejabberd is:

* Truly portable
* Distributed
* Fault-tolerance
* Built-in Multi-User Chat service
* Built-in IRC transport
* Built-in Publish-Subscribe service
* Built-in Jabber Users Directory service based on users vCards
* Built-in web-based administration interface
* Built-in HTTP Polling service
* SSL support
* Support for LDAP authentification
* Ability to interface with external components (JIT, MSN-t, Yahoo-t, etc)
* Migration from jabberd14 is possible
* Mostly XMPP-compliant
* Support for JEP-0030 (Service Discovery).
* Support for JEP-0039 (Statistics Gathering).
* Support for xml:lang 

%if_enabled captcha
%package captcha
Summary: captcha script for ejabberd
Group: System/Servers
Requires: %name = %version-%release
Requires: ImageMagick-tools

%description captcha
This package contains a shell script for creating captcha files.
%endif


%if_enabled pam
%package pam
Summary: PAM auth support for jabberd
Group: System/Servers
Requires: %name = %version-%release

%description pam
This package contains a privileged helper employed by %name
to perform PAM authentication of local users as jabber users.

No user-side registration is then possible, and plaintext auth
isn't accepted (basically you want to configure SSL).
%endif

%if_enabled extra
%package extra
Summary: Additional modules for ejabberd
Group: System/Servers
Requires: %name = %version-%release

%description extra
This package contains a set of optional modules that extend ejabberd functionality.
Currently there are: mod_asterisk and mod_rest.
%endif

%prep
%setup

%build
cd src
%configure --enable-odbc %{subst_enable pam} %{subst_enable hipe}
#--enable-user=ejabberd
# SMP-unaware
make

%install
%makeinstall -C src DESTDIR=%buildroot
(cd altlinux && find . -type f |cpio -pumd %buildroot)
grep -A1 -B1 '^%%%%%% ' src/mod_passrecover.erl >mod_passrecover.txt
mkdir -p %buildroot%_localstatedir/ejabberd %buildroot%_logdir/ejabberd \
	%buildroot%_sysconfdir/sysconfig/ %buildroot%_lockdir/ejabberd
mv %buildroot%_sysconfdir/%name/ejabberdctl.cfg %buildroot%_sysconfdir/sysconfig/ejabberd

mkdir -p %buildroot%_datadir/doc
ln -s %name-%version %buildroot%_datadir/doc/%name

%pre
%_sbindir/groupadd -r -f ejabberd &>/dev/null
%_sbindir/useradd -r -g ejabberd  -d %_localstatedir/ejabberd -s /dev/null \
    -c 'ejabberd server' -M -n ejabberd &>/dev/null ||:

%post
%post_service %name
%_jabber_config

%preun
%preun_service %name

%files
%doc COPYING README doc/* examples src/odbc/*.sql mod_passrecover.txt
%_datadir/doc/%name

%dir %_sysconfdir/ejabberd
%config(noreplace) %_sysconfdir/ejabberd/inetrc
%attr(640,root,ejabberd) %config(noreplace) %_sysconfdir/ejabberd/ejabberd.cfg
%attr(0640,root,ejabberd) %config(noreplace) %_sysconfdir/sysconfig/ejabberd
%attr(0640,root,root) %config %_sysconfdir/logrotate.d/ejabberd

%_initdir/ejabberd
%attr(0755,root,ejabberd) %_sbindir/ejabberdctl

%_libdir/ejabberd

%_jabber_server_dir/ejabberd

%_man8dir/*

%dir %_lockdir/%name

%attr(1770,root,ejabberd) %dir %_localstatedir/ejabberd
%attr(1770,root,ejabberd) %dir %_logdir/ejabberd
%attr(1770,root,ejabberd) %dir %_lockdir/ejabberd

%exclude %_sysconfdir/pam.d/ejabberd
%exclude %_libdir/ejabberd/priv/bin/captcha.sh

%if_enabled pam
%exclude %_libdir/ejabberd/ebin/epam.beam
%exclude %_libdir/ejabberd/priv/bin/epam
%endif

%if_enabled extra
%exclude %_libdir/ejabberd/ebin/mod_asterisk.beam
%exclude %_libdir/ejabberd/ebin/mod_rest.beam
%endif

%if_enabled captcha
%files captcha
%attr(4710,root,ejabberd) %_libdir/ejabberd/priv/bin/captcha.sh
%endif

%if_enabled pam
%files pam
%_sysconfdir/pam.d/ejabberd
%_libdir/ejabberd/ebin/epam.beam
%attr(4710,root,ejabberd) %_libdir/ejabberd/priv/bin/epam
%endif

%if_enabled extra
%files extra
%_libdir/ejabberd/ebin/mod_asterisk.beam
%_libdir/ejabberd/ebin/mod_rest.beam
%endif

%changelog
* Sat Mar 31 2012 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.10-alt1
- 2.1.10 (Closes: #26762).

* Thu Nov 17 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.9-alt1
- 2.1.9.

* Mon Jun 06 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.8-alt1
- 2.1.8 (fixes mod_pubsub broken in previous release).

* Fri Jun 03 2011 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.7-alt1
- 2.1.7, fixes CVE-2011-1753 (The vulnerability is caused due to an
  error within the parsing of certain XML input, which can be exploited
  to e.g. cause a high CPU and memory consumption via heavily nested XML
  entities), please update immediately.
- Add PostgreSQL support (pma).

* Thu Dec 16 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.6-alt1
- 2.1.6

* Mon Oct 11 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.5-alt2
[ Mikhail A Pokidko]
- Update modules:
  + mod_statsdx
  + mod_admin_extra
- Fix permissions of captcha.sh
[ Vladimir V. Kamarzin ]
- Update mod_shared_roster_ldap to 0.5.3

* Tue Oct 05 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.5-alt1
- 2.1.5

* Thu Apr 01 2010 Vladimir V. Kamarzin <vvk@altlinux.org> 2.1.3-alt1
[ Mikhail A Pokidko]
- 2.1.3 (Closes: #23264)
- Add some extra modules:
  + mod_asterisk
  + mod_admin_extra
- Remove modules:
  + mod_ctlextra
  + ejabberd_http_bind
  + mod_http_bind
  + mod_http_fileserver
- Disable mod_stats
- Move Extra modules into ejabberd-extra subpackage
- Initscript: add delay at restart
[ Afanasov Dmitry ]
- Fix mod_shared_roster_ldap
[ Vladimir V. Kamarzin ]
- Package captcha script as separate subpackage ejabberd-captcha
- Use /var/lock/ejabberd for ejabberdctl locks

* Fri Apr 10 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.5-alt1
[ Sergey Bolshakov ]
- 2.0.5 release
[ Mikhail A Pokidko]
- Added some extra modules:
  + mod_ctlextra
  + mod_rest
  + mod_stats2file
  + mod_statsdx
  + ejabberd_http_bind
  + mod_http_bind
  + mod_http_fileserver
- Modified default config
[ Vladimir V. Kamarzin ]
- Added dependency on su(1)

* Wed Jan 21 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.3-alt2
[ Michael Shigorin ]
- Added PAM support as a subpackage (enabled by default)

* Mon Jan 19 2009 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.3-alt1
[ Sergey Bolshakov ]
- 2.0.3 release

* Thu Dec 18 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.2-alt2
[ Sergey Bolshakov ]
- Updated to 1734 svn revision of branches/ejabberd-2.0.x

* Mon Oct 06 2008 Vladimir V. Kamarzin <vvk@altlinux.org> 2.0.2-alt1
[ Sergey Bolshakov ]
- 2.0.2 release (Closes: #16093)
- ODBC enabled (Closes: #13598)
- PostgreSQL module added
- Initscript rewritten
- Added /etc/ejabberd/inetrc (Closes: #13618)
[ Vladimir V. Kamarzin ]
- Added mod_shared_roster_ldap with gray_graff patch (Closes: #16485)

* Sun Nov 11 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.4-alt1
- 1.1.4

* Sun Nov 11 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.3-alt3
- newer jabber-config support

* Wed Mar 14 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.3-alt2
- jabber-config support
- added mod_passrecover (#11065)

* Sun Feb 18 2007 Mikhail Yakshin <greycat@altlinux.org> 1.1.3-alt1
- 1.1.3

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.1.1-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Thu Aug 24 2006 Mikhail Yakshin <greycat@altlinux.org> 1.1.1-alt1
- 1.1.1

* Mon Jan 09 2006 Mikhail Yakshin <greycat@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sat Aug 27 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.9.8-alt1
- 0.9.8
- added w3c standards compliance patch

* Wed Apr 20 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.9-alt1
- 0.9
- modified ejabberd init to support 'status' command

* Tue Mar 08 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.7.5-alt2
- fixed #6135 with patch from teo (Sergei Golovan)

* Wed Jan 12 2005 Mikhail Yakshin <greycat@altlinux.ru> 0.7.5-alt1
- 0.7.5

* Sun Aug 22 2004 Mikhail Yakshin <greycat@altlinux.ru> 0.7-alt1
- Initial build for ALT Linux

