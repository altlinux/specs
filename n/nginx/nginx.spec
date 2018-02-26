%define pcre_version 4.5

%def_with perl
%def_with aio
%def_with aio
%def_without syslog
%def_without image_filter
%def_without xslt
%def_without debug
%def_without geoip
%def_enable cache_purge

Name: nginx
Version: 1.2.1
Release: alt1

Summary: Fast HTTP server
License: BSD
Group: System/Servers

Url: http://sysoev.ru/nginx
Source: %url/%name-%version.tar
Source1: %name.conf.in
Source2: %name.init
Source3: %name.logrotate.in
Source5: %name.sysconfig
Source6: default.conf
Source7: cache_purge.tar
Patch0: alt-mime-types.patch
Patch1: nginx-0.8-syslog.patch
Patch2: nginx-perl-vendor.patch

Packager: Denis Smirnov <mithraen@altlinux.ru>

# Automatically added by buildreq on Mon May 07 2007
BuildRequires: libpcre-devel libssl-devel perl-devel zlib-devel

%if_with geoip
BuildRequires: libGeoIP-devel
Requires: GeoIP-Lite-City GeoIP-Lite-Country
%endif

%if_with image_filter
BuildRequires: libgd2-devel
%endif

%if_with xslt
BuildRequires: libxml2-devel libxslt-devel
%endif

%if_with debug
BuildRequires: google-perftools-devel
%endif

Requires(pre): shadow-utils
Requires(post): sed

Provides: webserver

%define nginx_user _nginx
%define nginx_group _nginx
%define nginx_etc %_sysconfdir/%name
%define nginx_spool %_spooldir/%name
%define nginx_log %_logdir/%name

%define configs %buildroot{%_sysconfdir/logrotate.d/%name,%nginx_etc/{%name.conf,sites-available.d/default.conf}}

%description
Fast HTTP server, extremely useful as an Apache frontend

%prep
%setup -a 7
%patch0 -p1
%if_with syslog
%patch1 -p2
%endif
%patch2 -p2

%build
%ifarch i686
	CPU="-mtune=pentiumpro" \
%else # pentium4 athlon
	CPU="-mtune=%_arch" \
%endif
%ifarch i586
	CPU="" \
%endif
%ifnarch %ix86
	CPU="" \
%endif # for x86_64 TODO for amd64/nocona
# FIXME: %%configure?
CFLAGS="%optflags $CPU" ./configure \
	--prefix=/ \
	--conf-path=%nginx_etc/nginx.conf \
	--sbin-path=%_sbindir \
	--error-log-path=%nginx_log/nginx.error.log \
	--http-log-path=%nginx_log/nginx.log \
	--http-client-body-temp-path=%nginx_spool/tmp/client \
	--http-proxy-temp-path=%nginx_spool/tmp/proxy \
	--http-fastcgi-temp-path=%nginx_spool/tmp/fastcgi \
	--http-uwsgi-temp-path=%nginx_spool/tmp/uwsgi \
	--http-scgi-temp-path=%nginx_spool/tmp/scgi \
	--pid-path=%_var/run/nginx.pid \
	--user=%nginx_user \
	--group=%nginx_group \
	--with-http_ssl_module \
	--with-cc-opt="-I %_includedir/pcre/" \
	--with-rtsig_module	\
	--with-select_module    \
	--with-poll_module      \
%if_with aio
	--with-aio_module	\
	--with-file-aio		\
%endif
	--with-mail \
	--with-mail_ssl_module \
	--with-imap \
	--with-imap_ssl_module \
	--with-md5=%_libdir \
	--with-http_ssl_module  \
%if_enabled cache_purge
	--add-module=cache_purge \
%endif
	--with-http_mp4_module \
	--with-http_realip_module \
	--with-http_addition_module \
	--with-http_sub_module \
	--with-http_dav_module \
	--with-http_flv_module \
	--with-http_gzip_static_module \
	--with-http_stub_status_module \
	--with-http_secure_link_module \
%if_with geoip
	--with-http_geoip_module \
%endif
%if_with image_filter
	--with-http_image_filter_module \
%endif
%if_with xslt
	--with-http_xslt_module \
%endif
%if_with debug
	--with-google_perftools_module \
%endif
%if_with perl	
	--with-http_perl_module \
%endif
%if_with syslog
	--with-syslog \
%endif


subst s!%buildroot!!g objs/*.h
%make_build DESTDIR=%buildroot

%install
mkdir -p %buildroot{%nginx_etc,%_sysconfdir/logrotate.d,%_sbindir,%nginx_spool/tmp,%nginx_log}
mkdir -p %buildroot%_spooldir/nginx/tmp/{client,proxy,fastcgi,scgi,uwsgi}
mkdir -p %buildroot%_lockdir/%name
mkdir -p %buildroot%nginx_etc/sites-enabled.d
mkdir -p %buildroot%nginx_etc/sites-available.d
mkdir -p %buildroot%nginx_etc/conf-enabled.d
mkdir -p %buildroot%nginx_etc/conf-available.d

%makeinstall DESTDIR=%buildroot

rm -f %buildroot%nginx_etc/%name.conf
install -pD -m644 %SOURCE1 %buildroot%nginx_etc/%name.conf
install -pD -m755 %SOURCE2 %buildroot%_initdir/%name
install -pD -m644 %SOURCE3 %buildroot%_sysconfdir/logrotate.d/%name
install -pD -m644 %SOURCE5 %buildroot%_sysconfdir/sysconfig/%name
install -pD -m644 %SOURCE6 %buildroot%nginx_etc/sites-available.d/default.conf

subst s!@nginx_user@!%nginx_user!g %configs
subst s!@nginx_etc@!%nginx_etc!g %configs
subst s!@nginx_spool@!%nginx_spool!g %configs
subst s!@nginx_log@!%nginx_log!g %configs

mkdir -p %buildroot%_docdir/%name-%version
cp -a CHANGES CHANGES.ru %buildroot%_docdir/%name-%version/

%if_with uwsgi
install -pD -m644 uwsgi/uwsgi_params %buildroot%nginx_etc/
%endif

rm -rf %buildroot/html/

%files
%_initdir/*
%_sbindir/*
%dir %nginx_etc
%dir %nginx_etc/sites-enabled.d
%dir %nginx_etc/sites-available.d
%dir %nginx_etc/conf-enabled.d
%dir %nginx_etc/conf-available.d

%dir %nginx_etc/sites-available.d/default.conf

# these are private; should also confirm to SPP (#12647)
%attr(0700,root,root) %dir %_lockdir/%name
%attr(1770,root,%nginx_group) %dir %nginx_spool/tmp
%attr(1770,root,%nginx_group) %dir %nginx_spool/tmp/client
%attr(1770,root,%nginx_group) %dir %nginx_spool/tmp/proxy
%attr(1770,root,%nginx_group) %dir %nginx_spool/tmp/fastcgi
%attr(1770,root,%nginx_group) %dir %nginx_spool/tmp/scgi
%attr(1770,root,%nginx_group) %dir %nginx_spool/tmp/uwsgi
%attr(1770,root,%nginx_group) %dir %nginx_spool
%attr(1770,root,%nginx_group) %dir %nginx_log
%config(noreplace) %nginx_etc/mime.types
%config(noreplace) %nginx_etc/nginx.conf
%config(noreplace) %nginx_etc/fastcgi.conf
%config(noreplace) %nginx_etc/scgi_params
%config(noreplace) %nginx_etc/uwsgi_params
%config(noreplace) %nginx_etc/fastcgi_params
%config(noreplace) %_sysconfdir/logrotate.d/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%nginx_etc/*.default
%nginx_etc/koi-win
%nginx_etc/koi-utf
%nginx_etc/win-utf
%_docdir/%name-%version
%if_with perl
%perl_vendor_archlib/nginx.pm
%perl_vendor_autolib/nginx
%endif
%if_with uwsgi
%config(noreplace) %nginx_etc/uwsgi_params
%endif

%pre
%_sbindir/groupadd -r -f %nginx_group ||:
%_sbindir/groupadd -r -f _webserver ||:
%_sbindir/useradd -r -g %nginx_group -G _webserver -d /dev/null -s /dev/null -n %nginx_user \
	2> /dev/null > /dev/null ||:

%post
sed -i 's/\(types_hash_bucket_size[[:space:]]*\)[[:space:]]32[[:space:]]*;[[:space:]]*$/\1 64;/' /etc/nginx/nginx.conf ||:
%post_service %name

%preun
%preun_service %name

%changelog
* Wed Jun 06 2012 Anton Farygin <rider@altlinux.ru> 1.2.1-alt1
- new version

* Wed May 30 2012 Anton Farygin <rider@altlinux.ru> 1.2.0-alt1
- new version (closes: #27215)

* Fri Jan 27 2012 Anton Farygin <rider@altlinux.ru> 1.1.13-alt1
- new version
- decreased starting priority in initscript to 98 (closes: #26466)
- removed old Readme.ALT (closes: #26861)
- fixed duplicated ogg in mime-types (closes: #26863)

* Tue Nov 29 2011 Anton Farygin <rider@altlinux.ru> 1.1.9-alt1
- new version

* Wed Oct 26 2011 Anton Farygin <rider@altlinux.ru> 1.1.6-alt1
- new version

* Mon Oct 17 2011 Alexey Tourbin <at@altlinux.ru> 1.1.5-alt1.1
- rebuilt for perl-5.14

* Sun Oct 09 2011 Anton Farygin <rider@altlinux.ru> 1.1.5-alt1
- new version

* Thu Sep 22 2011 Anton Farygin <rider@altlinux.ru> 1.1.4-alt1
- new version
- enabled http_mp4_module

* Thu Sep 15 2011 Anton Farygin <rider@altlinux.ru> 1.1.3-alt1
- new version

* Fri Sep 09 2011 Anton Farygin <rider@altlinux.ru> 1.1.2-alt1
- new version

* Tue Aug 23 2011 Anton Farygin <rider@altlinux.ru> 1.1.1-alt1
- new version

* Wed Jun 01 2011 Anton Farygin <rider@altlinux.ru> 1.0.4-alt1
- new version

* Fri May 27 2011 Anton Farygin <rider@altlinux.ru> 1.0.3-alt1
- new version

* Wed Apr 13 2011 Anton Farygin <rider@altlinux.ru> 1.0.0-alt2
- add cache_purge module

* Tue Apr 12 2011 Michael Shigorin <mike@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Feb 10 2011 Anton Farygin <rider@altlinux.ru> 0.8.54-alt1
- updated to 0.8.54
- add nginx user to _webserver group (closes: #24938)

* Wed Dec 01 2010 Anton Farygin <rider@altlinux.ru> 0.8.53-alt4
- added patch from 0.9.0 with fix for memory violation in auth_basic

* Tue Nov 30 2010 Anton Farygin <rider@altlinux.ru> 0.8.53-alt3
- fixed build with new perl

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.8.53-alt2.1
- rebuilt with perl 5.12

* Tue Nov 02 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 0.8.53-alt2
- add http_secure_link_module

* Thu Oct 28 2010 Anton Farygin <rider@altlinux.ru> 0.8.53-alt1
- new version

* Mon Oct 04 2010 Anton Farygin <rider@altlinux.ru> 0.8.52-alt1
- new version

* Mon Sep 27 2010 Anton Farygin <rider@altlinux.ru> 0.8.51-alt1
- new version

* Sun Sep 05 2010 Anton Farygin <rider@altlinux.ru> 0.8.50-alt1
- new version

* Fri Aug 20 2010 Anton Farygin <rider@altlinux.ru> 0.8.49-alt1
- new version

* Tue Aug 03 2010 Anton Farygin <rider@altlinux.ru> 0.8.48-alt1
- new version

* Thu Jul 01 2010 Anton Farygin <rider@altlinux.ru> 0.8.43-alt1
- new version
- removed external uswgi module (included to mainstream)
- new uswgi and scgi modules

* Wed May 26 2010 Ivan Fedorov <ns@altlinux.org> 0.8.38-alt1
- new version
- add uswgi module

* Wed Apr 07 2010 Anton Farygin <rider@altlinux.ru> 0.8.35-alt1
- new version
- added (disabled by default) syslogd patch

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 0.8.34-alt1
- new version

* Thu Feb 04 2010 Anton Farygin <rider@altlinux.ru> 0.8.33-alt1
- new version

* Wed Jan 27 2010 Anton Farygin <rider@altlinux.ru> 0.8.32-alt1
- new version
- remove unused patches

* Wed Nov 11 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.24-alt1
- Updated to 0.8.24.

* Tue Oct 06 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.19-alt1
- Updated to 0.8.19:
  + Bugfixes in limit_req;
  + SSL module enforcements (-SSLv2).

* Tue Oct 06 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.18-alt1
- Updated to 0.8.18.
- Move mime.types modification to separate patch.

* Wed Sep 23 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.16-alt1
- Updated to 0.8.16:
  + Bugfixes in resolver code, image module and gzip_vary handling.

* Mon Sep 14 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.15-alt1
- Updated to 0.8.15:
   + Security: a segmentation fault might occur in worker process while
     specially crafted request handling (VU#180065);
   + Bugfix: in file AIO.

* Mon Sep 07 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.14-alt1
- Updated to 0.8.14.

* Sun Sep 06 2009 L.A. Kostis <lakostis@altlinux.ru> 0.8.13-alt1
- NMU:
  + updated to 0.8.13;
  + add new aio module (and enable file aio);
  + add new geoip module (disabled by default);
  + massive update of mime.types database (sync with Apache);
  + nginx.init: get rid of duplicated conftest calls.

* Tue Jul 28 2009 L.A. Kostis <lakostis@altlinux.ru> 0.7.61-alt1
- NMU:
  + updated to 0.7.61.
  + src/event/openssl: fix memory corruption in $ssl_client_cert
    (thanks to Sergey Zhuravlev)

* Wed May 27 2009 L.A. Kostis <lakostis@altlinux.ru> 0.7.59-alt1
- NMU:
  + updated to 0.7.59.
  + fix optimization for x86.
  + add support of building new modules (disabled by default):
    + image_filter
    + xslt.

* Sat May 23 2009 Denis Smirnov <mithraen@altlinux.ru> 0.6.37-alt1.1
- rebuild

* Wed May 20 2009 L.A. Kostis <lakostis@altlinux.ru> 0.6.37-alt1
- NMU:
  + updated to 0.6.37.
  + disable all debug stuff (e.g. perftools support).

* Sat Apr 11 2009 Michael Shigorin <mike@altlinux.org> 0.6.35-alt2
- fixed missing substitution of sites-available.d/default.conf
  (Closes: #19560)

* Sat Feb 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.6.35-alt1
- Bugfix: in shared memory allocations if nginx was built without debugging.
- Bugfixes in an "Expect" request header line support.
- Bugfix: UTF-8 encoding usage in the ngx_http_autoindex_module.

* Sat Feb 07 2009 Denis Smirnov <mithraen@altlinux.ru> 0.6.34-alt2
- update README.ALT
- move default config to /etc/nginx/sites-available.d

* Sat Nov 29 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.34-alt1
- Change: now the EAGAIN error returned by connect() is not considered as
  temporary error.
- Change: now the "gzip_vary" directive turned on issues a "Vary:
  Accept-Encoding" header line for uncompressed responses too.
- Feature: the "expires" directive supports daily time.
- Feature: the "Expect" request header line support.
- Feature: now the "rewrite" directive does a redirect automatically if the
  "https://" protocol is used.
- Bugfix: the "listen" directive parameters such as "backlog", "rcvbuf", etc.
  were not set, if a default server was not the first one.
- Bugfix: the "log_not_found" directive did not work for index files tests.
- Bugfix: now if FastCGI server sends a "Location" header line without status
  line, then nginx uses 302 status code.  Thanks to Maxim Dounin.
- Bugfix: the ngx_http_flv_module did not support several values in a query
  string.
- Bugfix: when a request to a directory was redirected with the slash added,
  nginx dropped a query string from the original request.
- Feature: now nginx returns the 405 status code for POST method requesting a
  static file only if the file exists.
- Bugfix: the resolver did not understand big DNS responses.  Thanks to Zyb.
- Bugfix: in HTTPS mode requests might fail with the "bad write retry" error.
- Bugfix: the ngx_http_charset_module did not understand quoted charset name
  received from backend.
- Bugfix: if the "max_fails=0" parameter was used in upstream with several
  servers, then a worker process exited on a SIGFPE signal.  Thanks to Maxim
  Dounin.
- Bugfix: the $r->header_in() method did not return value of the "Host",
  "User-Agent", and "Connection" request header lines; the bug had appeared
  in 0.6.32.
- Bugfix: a full response was returned for request method HEAD while
  redirection via an "error_page" directive.
- Bugfix: if a directory has search only rights and the first index file was
  absent, then nginx returned the 500 status code.
- Bugfix: of recursive error_page for 500 status code.

* Mon Oct 27 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.32-alt1
- Change: the "none" parameter in the "ssl_session_cache" directive; now this
  is default parameter.  Thanks to Rob Mueller.
- Change: now the 0x00-0x1F, '"' and '\' characters are escaped as \xXX in an
  access_log.  Thanks to Maxim Dounin.
- Change: now nginx allows several "Host" request header line.
- Feature: the "modified" flag in the "expires" directive.
- Feature: the $uid_got and $uid_set variables may be used at any request
  processing stage.
- Feature: the $hostname variable.  Thanks to Andrei Nigmatulin.
- Feature: DESTDIR support.  Thanks to Todd A. Fisher and Andras Voroskoi.
- Bugfix: if sub_filter and SSI were used together, then responses might were
  transferred incorrectly.
- Bugfix: large SSI inclusions might be truncated.
- Bugfix: the "proxy_pass" directive did not work with the HTTPS protocol; the
  bug had appeared in 0.6.9.
- Bugfix: worker processes might not catch reconfiguration and log rotation
  signals.
- Bugfix: a segmentation fault might occur in worker process on Linux, if
  keepalive was enabled.

* Fri Jul 04 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.31-alt1
- Bugfix: nginx did not process FastCGI response if header was at the end of
  FastCGI record; bug appeared in 0.6.2.  Thanks to Sergey Serov.
- Bugfix: a segmentation fault might occur in worker process if a file was
  deleted and the "open_file_cache_errors" directive was off.

* Thu May 08 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.30-alt1
- Update to 0.6.30
- Change: now if an "include" directive pattern does not match any file, then
  nginx does not issue an error.
- Feature: now the time in directives may be
  specified without spaces, for example, "1h50m".
- Bugfix: memory leaks if the "ssl_verify_client" directive was on.  Thanks to
  Chavelle Vincent.
- Bugfix: the "sub_filter" directive might set text to change into output.
- Bugfix: the "error_page" directive did not take into account arguments in
  redirected URI.

* Mon Mar 31 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6.29-alt1
- Update to 0.6.29

* Fri Feb 01 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.35-alt2
- rebuild

* Mon Jan 28 2008 Michael Shigorin <mike@altlinux.org> 0.5.35-alt1.1
- re-added kludge from 0.5.34-alt1.1: the more insightful fix didn't 
  account for the case of i586 (which is our default x86 buildarch)
  while my dirty hack doesnn't account at all, it just has a hammer :)
- so "could not build the types_hash, you should increase types_hash_bucket_size: 32
  error with our default configuration (considerably larger mime.types)
  should go away again

* Sat Jan 26 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.35-alt1
- Change: now the ngx_http_userid_module adds start time microseconds
  to the cookie field contains a pid value.
- Change: now the uname(2) is used on Linux instead of procfs.
  Thanks to Ilya Novikov.
- Feature: the "If-Range" request header line support.
  Thanks to Alexander V. Inyukhin.
- Bugfix: in HTTPS mode requests might fail with the "bad write retry"
  error; bug appeared in 0.5.13.
- Bugfix: the STARTTLS in SMTP mode did not work.
  Thanks to Oleg Motienko.
- Bugfix: large_client_header_buffers did not freed before going to
  keep-alive state.
  Thanks to Olexander Shtepa.
- Bugfix: the "limit_rate" directive did not allow to use full
  throughput, even if limit value was very high.
- Bugfix: the $status variable was equal to 0 if a proxied server
  returned response in HTTP/0.9 version.
- Bugfix: if the "?" character was in a "error_page" directive, then
  it was escaped in a proxied request; bug appeared in 0.5.32.

* Sat Jan 26 2008 Michael Shigorin <mike@altlinux.org> 0.5.34-alt2.2
- replaced ugly kludge introduced by me in 0.5.34-alt1.1
  with an insightful one by Gena Makhomed (#13407)

* Sat Jan 26 2008 Michael Shigorin <mike@altlinux.org> 0.5.34-alt2.1
- added Provides: webserver (#13546)

* Thu Jan 10 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.34-alt2
- rebuild

* Thu Jan 10 2008 Michael Shigorin <mike@altlinux.org> 0.5.34-alt1.1
- got fed up with "could not build the types_hash, you should
  increase types_hash_bucket_size: 32" and did increase the default
  to empirically tested (Linux/i586) value of 64

* Tue Jan 08 2008 Denis Smirnov <mithraen@altlinux.ru> 0.5.34-alt1
- Change: now the full request line instead of URI only is written to
  error_log.
- Feature: the "merge_slashes" directive.
- Feature: the "gzip_vary" directive.
- Feature: the "server_tokens" directive.
- Feature: the "access_log" directive may be used inside the "limit_except" block. 
- Bugfix: if the $server_protocol was used in FastCGI parameters and a
  request line length was near to the "client_header_buffer_size" directive
  value, then nginx issued an alert "fastcgi: the request record is too big".
- Bugfix: if a plain text HTTP/0.9 version request was made to HTTPS server,
  then nginx returned usual response.
- Bugfix: URL double escaping in a redirect of the "msie_refresh"
  directive; bug appeared in 0.5.28.
- Bugfix: a segmentation fault might occur in worker process if
  subrequests were used.
- Bugfix: the big responses may be transferred truncated if SSL and gzip were
 used.
- Bugfix: compatibility with mget.
- Bugfix: nginx did not unescape URI in the "include" SSI command.
- Bugfix: the segmentation fault was occurred on start or while
  reconfiguration if variable was used in the "charset" or
  "source_charset" directives.
- Bugfix: nginx returned the 400 response on requests like
  "GET http://www.domain.com HTTP/1.0". Thanks to James Oakley.
- Bugfix: a segmentation fault occurred in worker process if
  $date_local and $date_gmt were used outside the
  ngx_http_ssi_filter_module.
- Bugfix: a segmentation fault might occur in worker process if debug
  log was enabled. Thanks to Andrei Nigmatulin.
- Bugfix: ngx_http_memcached_module did not set $upstream_response_time.
  Thanks to Maxim Dounin.
- Bugfix: a worker process may got caught in an endless loop, if the
  memcached was used. 

* Sun Jan 06 2008 Michael Shigorin <mike@altlinux.org> 0.5.33-alt2.1
- Fix default nginx.conf:
  + first server_name with wildcards is a fatal error now
  + add two more somewhat unobvious tips on reverse proxying
  + link to http://nginx.net for info/docs

* Sat Dec 01 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.33-alt2
- Auto fix types_hash_bucket_size in config

* Sat Nov 10 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.33-alt1
- Change: now by default the "echo" SSI command uses entity encoding.
- Feature: the "encoding" parameter in the "echo" SSI command.
- Change: mail proxy was split on three modules: pop3, imap and smtp.
- Feature: the "smtp_greeting_delay" and "smtp_client_buffer" directives of the
  ngx_mail_smtp_module.
- Feature: the "server_name" and "valid_referers" directives support regular
  expressions.
- Feature: the "server_name", "map", and "valid_referers" directives support
  the "www.example.*" wildcards.
- Bugfix: sub_filter did not work with empty substitution.
- Bugfix: in sub_filter parsing.
- Bugfix: a worker process may got caught in an endless loop, if the memcached
  was used.
- Bugfix: nginx supported low case only "close" and "keep-alive" values in the
  "Connection" request header line; bug appeared in 0.5.32.
- build --with debug (for more verbose logging)

* Sun Oct 21 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.32-alt1
- Change: now nginx tries to set the "worker_priority", "worker_rlimit_nofile",
  "worker_rlimit_core", and "worker_rlimit_sigpending" without super-user
  privileges.
- Change: now nginx escapes space and "%%" in request to a mail proxy
  authentication server.
- Change: now nginx escapes "%%" in $memcached_key variable.
- Feature: the "add_header Last-Modified ..." directive changes the
  "Last-Modified" response header line.
- Feature: the mail proxy supports AUTHENTICATE in IMAP mode.  Thanks to Maxim
  Dounin.
- Feature: the mail proxy supports STARTTLS in SMTP mode.  Thanks to Maxim
  Dounin.
- Bugfix: nginx did not close directory file on HEAD request if autoindex was
  used.  Thanks to Arkadiusz Patyk.
- Bugfix: the "proxy_hide_header" and "fastcgi_hide_header" directives did not
  hide response header lines whose name was longer than 32 characters.  Thanks
  to Manlio Perillo.
- Bugfix: active connection counter always increased if mail proxy was used.
- Bugfix: if backend returned response header only using non-buffered proxy,
  then nginx closed backend connection on timeout.
- Bugfix: nginx did not support several "Connection" request header lines.
- Bugfix: a charset set by the "charset" directive was not appended to the
  "Content-Type" header set by $r->send_http_header().
- Bugfix: a segmentation fault might occur in worker process if /dev/poll
  method was used.
- Bugfix: a segmentation fault occurred in worker process if invalid address
  was set in the "auth_http" directive.
- Bugfix: now nginx uses default listen backlog value 511 on all platforms
  except FreeBSD.  Thanks to Jiang Hong.
- Bugfix: now Solaris sendfilev() is not used to transfer the client request
  body to FastCGI-server via the unix domain socket.
- Bugfix: if the same host without specified port was used as backend for HTTP
  and HTTPS, then nginx used only one port - 80 or 443.
- Bugfix: the "proxy_ignore_client_abort" and "fastcgi_ignore_client_abort"
  directives did not work; bug appeared in 0.5.13.

* Fri Aug 31 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt4
- rebuild

* Fri Aug 31 2007 Michael Shigorin <mike@altlinux.org> 0.5.31-alt3.1
- properly fixed #7441 (taking into accound ldv@'s objections)
- properly fixed #12655 (ditto)
- readability improvements to initscript
- added /etc/sysconfig/nginx (flexible ulimit setup)

* Fri Aug 31 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt3
- rebuild

* Thu Aug 30 2007 Michael Shigorin <mike@altlinux.org> 0.5.31-alt2.1
- fix back my thinko regarding /var/run/nginx/ directory
- rework upgrade() initscript action (and run it only for package upgrades,
  just do a restart for sysadmin's command) -- should fix #12655

* Thu Aug 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt2
- rebuild

* Thu Aug 30 2007 Michael Shigorin <mike@altlinux.org> 0.5.31-alt1.1
- NMU: moved remnants of directory creation and permissions setup 
  from initscript to specfile (seems like was a band-aid which is
  currently unneeded and non-elegant); see also #12647
- fixed #7441 (service nginx stop would leave children running)

* Fri Aug 17 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.31-alt1
- Feature: named locations.
- Feature: the "proxy_store" and "fastcgi_store" directives.
- Feature: the "proxy_store_access" and "fastcgi_store_access" directives.
- Feature: the $args variable can be set with the "set" directive.
- Feature: the $is_args variable.
- Bugfix: if a client has closed connection to mail proxy then nginx might not
  close connection to backend.
- Bugfix: now nginx escapes space in $memcached_key variable.
- Bugfix: a segmentation fault might occur in worker process when the HTTPS
  protocol was used in the "proxy_pass" directive.
- Bugfix: the perl $$ variable value in ngx_http_perl_module was equal to the
  master process identification number.
- Bugfix: fix building on Solaris/amd64 by Sun Studio 11 and early versions;
  bug appeared in 0.5.29.
- Feature: $nginx_version variable.  Thanks to Nick S. Grechukh.
- Bugfix: if the FastCGI header was split in records, then nginx passed garbage
  in the header to a client.
- Bugfix: Sun Studio compatibility on Solaris/amd64 and Solaris/sparc64.
  Thanks to Jiang Hong and Andrei Nigmatulin.
- Bugfix: of minor potential bugs.  Thanks to Coverity's Scan.
- Security: the "msie_refresh" directive allowed XSS.  Thanks to Maxim Boguk.
- Bugfix: a segmentation fault might occur in worker process if the
  "auth_http_header" directive was used.  Thanks to Maxim Dounin.
- Bugfix: a segmentation fault occurred in worker process if the CRAM-MD5
  authentication method was used, but it was not enabled.
- Bugfix: a segmentation fault might occur in worker process if the eventport
  method was used.
- Bugfix: if remote SSI subrequest was used, then posterior local file
  subrequest might transferred to client in wrong order.
- Bugfix: large SSI inclusions buffered in temporary files were truncated.

* Fri Jul 06 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.26-alt2
- More strict requires for perl-base version

* Fri Jun 22 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.26-alt1
- Remove nginx.perl.fix.patch (added to upstream)
- Drop nginx-0.5.14-gns-catchstderr.patch (added to upstream)
- Bugfix: in SSI parsing.
- Bugfix: nginx could not be built with the --without-http_rewrite_module
  parameter; bug appeared in 0.5.24.
- Security: the "ssl_verify_client" directive did not work if request was made
  using HTTP/0.9.
- Bugfix: a part of response body might be passed uncompressed if gzip was
  used; bug appeared in 0.5.23.

* Wed May 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.22-alt1
- update version to 0.5.22
- fix perl module (#11911)

* Mon May 28 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.20-alt3
- update mime.types (get it from Apache)

* Tue May 08 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.20-alt2
- fix x86_64 building

* Mon May 07 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.20-alt1
- update version to 0.5.20
- remove connection_pool_size option from config file (fix crash on x86_64)
- build with perl support (at@)
- Feature: the "sendfile_max_chunk" directive.
- Feature: the "$http_...", "$sent_http_...", and "$upstream_http_..."
  variables may be changed using the "set" directive.
- Bugfix: a segmentation fault might occur in worker process if the SSI command
  'if expr="$var = /"' was used.
- Bugfix: trailing boundary of multipart range response was transferred
  incorrectly.  Thanks to Evan Miller.

* Mon Apr 30 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.19-alt1
- update version to 0.5.19
- build --with-http_stub_status_module (gns@)
- fix mail proxy building
- Add Symbian sis/sisx files to mime.types (#11459)
- Add hints to config file (#11368)
- Make default config file more useful
- Add README.ALT
- Start more workers in default config (more DoS proof)
- Change: now the $request_time variable has millisecond precision.
- Feature: the $upstream_addr variable.
- Feature: the "proxy_headers_hash_max_size" and
  "proxy_headers_hash_bucket_size" directives.  Thanks to Volodymyr Kostyrko.
- Bugfix: the files more than 2G could not be transferred using sendfile on
  64-bit Linux.
- Feature: the ngx_http_sub_filter_module.
- Feature: the "$upstream_http_..." variables.
- Feature: now the $upstream_status and $upstream_response_time variables keep
  data about all upstreams before X-Accel-Redirect.

* Fri Apr 13 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.17-alt1
- update version to 0.5.17

* Sun Mar 18 2007 Denis Smirnov <mithraen@altlinux.ru> 0.5.14-alt1
- update version to 0.5.14

* Thu Dec 07 2006 Denis Smirnov <mithraen@altlinux.ru> 0.5.0-alt1
- update version to 0.5.0

* Fri Oct 27 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4.11-alt1
- version update

* Fri Oct 20 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4.9-alt2
- rebuild with http_browser_module

* Mon Oct 16 2006 Denis Smirnov <mithraen@altlinux.ru> 0.4.9-alt1
- version update

* Sat Aug 12 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.57-alt1
- version update

* Mon May 08 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.45-alt1
- version update
- authorize by client certifications added

* Mon Apr 17 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.38-alt1
- version update

* Sun Mar 12 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.32-alt1
- version update
- with realip

* Thu Mar 09 2006 Denis Smirnov <mithraen@altlinux.ru> 0.3.30-alt1
- version update;

* Fri Jan 13 2006 LAKostis <lakostis at altlinux.ru> 0.3.19-alt1
- NMU;
- version update;
- x86_64 fixes;
- default config updated;
- init script improvements;
- add logrotate script;
- update patches.

* Sun Nov 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.3.12-alt1
- version update

* Sun Oct 16 2005 Denis Smirnov <mithraen@altlinux.ru> 0.3.2-alt1
- version update
- create directories for temp files (client requests, fastcgi & proxy replies)

* Sat Sep 17 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.45-alt1
- version update

* Fri Aug 19 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.41-alt2
- added two patches (from lakostis@)
- build with optimization flags (from lakostis@)

* Wed Aug 03 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.41-alt1
- version update

* Sun Jul 24 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.40-alt1
- default_charset removed
- charset set reply codepage, source_charset -- source charset :)
- limit_rate supported with proxy and fastcgi
- X-Accel-Limit-Rate header from backend supported
- added: ssi_types
- added: autoindex_exact_size
- added: log_not_found
- added: break
- removed: post_accept_timeout
- build with imap
- many other fixes

* Thu Jun 09 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.35-alt1
- version update

* Sat May 28 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.34-alt1
- 0.1.34
- spec cleanup / macrification (mike@)
- changed "nginx" user/group to "_nginx" (mike@)

* Wed May 18 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.31-alt1
- version update
- some cleanups

* Sun Apr 17 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.28-alt1
- version update

* Sun Mar 27 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.26-alt2
- cleanup

* Sat Mar 26 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.26-alt1
- version update
- add ulimit -n 16384 to initscript

* Mon Mar 21 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.25-alt1
- version update
- cleanup
- tmp moved to /var/spool/nagios/tmp

* Thu Mar 17 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.24-alt1
- version update

* Sun Feb 06 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.17-alt1
- version update

* Sat Jan 29 2005 Denis Smirnov <mithraen@altlinux.ru> 0.1.16-alt1
- version update
- fastcgi support (upstream)

* Fri Dec 24 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1.13-alt1
- version update
- OpenSSL-support builded
- rewrite and pcre support builded
- startup script
- useful default config-file

* Sat Nov 27 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1.10-alt1
- version update

* Tue Oct 12 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1.1-alt1
- first build
