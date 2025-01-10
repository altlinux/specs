%define _unpackaged_files_terminate_build 1
%define angie_user _angie
%define angie_group _angie
%define angie_etc %_sysconfdir/angie
%define angie_spool %_spooldir/angie
%define angie_log %_logdir/angie
%define modpath %_libdir/angie/modules

Name: angie
Version: 1.8.1
Release: alt1

Summary: Efficient, powerful and scalable reverse proxy and web server
License: BSD-2-Clause
Group: System/Servers
Url: https://angie.software
VCS: https://git.angie.software/web-server/angie.git

Source: %name-%version.tar
# from upstream
Source1: %name-dist-%version.tar

Provides: webserver

BuildRequires(pre): rpm-macros-systemd
BuildRequires: libpcre2-devel
BuildRequires: LibreSSL-devel
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: zlib-devel

%description
%summary.

%prep
%setup -a1

# https://en.angie.software/angie/docs/installation/sourcebuild/#paths
%build
./configure \
  --prefix=/ \
  --group=%angie_user \
  --user=%angie_user \
  --with-cc-opt="-I../libressl/build/include" \
  --with-ld-opt="-L../libressl/build/lib" \
  --conf-path=%angie_etc/angie.conf \
  --error-log-path=%angie_log/errors.log \
  --http-client-body-temp-path=%angie_spool/tmp/client \
  --http-fastcgi-temp-path=%angie_spool/tmp/fastcgi \
  --http-log-path=%angie_log/access.log \
  --http-scgi-temp-path=%angie_spool/tmp/scgi \
  --http-uwsgi-temp-path=%angie_spool/tmp/uwsgi \
  --lock-path=%_var/run/angie.lock \
  --modules-path=%modpath \
  --pid-path=%_var/run/angie.pid \
  --sbin-path=%_sbindir/angie \
  --with-file-aio \
  --with-http_acme_module `# angie` \
  --with-http_addition_module \
  --with-http_auth_request_module \
  --with-http_dav_module \
  --with-http_flv_module \
  --with-http_gunzip_module \
  --with-http_gzip_static_module \
  --with-http_mp4_module \
  --with-http_random_index_module \
  --with-http_realip_module \
  --with-http_secure_link_module \
  --with-http_slice_module \
  --with-http_ssl_module \
  --with-http_stub_status_module \
  --with-http_sub_module \
  --with-http_v2_module \
  --with-http_v3_module `#angie` \
  --with-mail \
  --with-mail_ssl_module \
  --with-stream \
  --with-stream_mqtt_preread_module `#angie` \
  --with-stream_rdp_preread_module `#angie` \
  --with-stream_realip_module `#angie` \
  --with-stream_ssl_module \
  --with-stream_ssl_preread_module `#angie` \
  --with-threads \
%nil

%make_build DESTDIR=%buildroot

%install
mkdir -p \
  %buildroot%angie_etc/conf-{enabled,available}.d \
  %buildroot%angie_etc/sites-{enabled,available}.d \
  %buildroot%angie_log \
  %buildroot%angie_spool/tmp/{client,proxy,fastcgi,scgi,uwsgi} \
  %buildroot%_datadir/angie/html \
  %buildroot%_lockdir/angie \
  %buildroot%modpath \
%nil

%makeinstall_std

install -Dpm 644 man/angie.8 -t %buildroot%_man8dir
install -Dpm 644 dist/angie.conf -t %buildroot%_sysconfdir/angie
install -Dpm 644 dist/angie.service -t %buildroot%_unitdir

install -Dpm 644 dist/default.conf \
  -t %buildroot%_sysconfdir/angie/http.d

install -Dpm 644 dist/example.conf \
  -t %buildroot%_sysconfdir/angie/stream.d
install -Dpm 644 dist/angie.logrotate \
  -t %buildroot%_sysconfdir/logrotate.d/angie

mv %buildroot/html/{50x.html,index.html} \
   %buildroot%_datadir/angie/html

%pre
%_sbindir/groupadd -r -f %angie_group ||:
%_sbindir/groupadd -r -f _webserver ||:
%_sbindir/useradd -r \
  -g %angie_group -G _webserver -d /dev/null -s /dev/null -n %angie_user \
  2> /dev/null > /dev/null ||:

%preun
%systemd_preun angie.service

%postun
%systemd_postun angie.service

%files
%doc README.rst
%config(noreplace) %angie_etc/angie.conf
%config(noreplace) %angie_etc/fastcgi.conf
%config(noreplace) %angie_etc/fastcgi_params
%config(noreplace) %angie_etc/http.d/default.conf
%config(noreplace) %angie_etc/mime.types
%config(noreplace) %angie_etc/prometheus_all.conf
%config(noreplace) %angie_etc/scgi_params
%config(noreplace) %angie_etc/uwsgi_params
%config(noreplace) %_sysconfdir/logrotate.d/angie
%dir %attr(0700,root,root) %_lockdir/angie
%dir %attr(1770,root,%angie_group) %angie_log
%dir %attr(1770,root,%angie_group) %angie_spool
%dir %attr(1770,root,%angie_group) %angie_spool/tmp
%dir %attr(1770,root,%angie_group) %angie_spool/tmp/client
%dir %attr(1770,root,%angie_group) %angie_spool/tmp/fastcgi
%dir %attr(1770,root,%angie_group) %angie_spool/tmp/proxy
%dir %attr(1770,root,%angie_group) %angie_spool/tmp/scgi
%dir %attr(1770,root,%angie_group) %angie_spool/tmp/uwsgi
%dir %modpath
%angie_etc/angie.conf.default
%angie_etc/fastcgi.conf.default
%angie_etc/fastcgi_params.default
%angie_etc/koi-utf
%angie_etc/koi-win
%angie_etc/mime.types.default
%angie_etc/prometheus_all.conf.default
%angie_etc/scgi_params.default
%angie_etc/stream.d/example.conf
%angie_etc/uwsgi_params.default
%angie_etc/win-utf
%_datadir/angie/html
%_man8dir/angie.8.xz
%_sbindir/angie
%_unitdir/angie.service

%changelog
* Fri Jan 10 2025 Constantin Sunzow <protvin@altlinux.org> 1.8.1-alt1
- Initial build.
