%define _unpackaged_files_terminate_build 1
%define angie_user _angie
%define angie_group _angie
%define angie_etc %_sysconfdir/angie
%define angie_spool %_spooldir/angie
%define angie_log %_logdir/angie
%define modpath %_libdir/angie/modules
%def_with debug
%def_with geoip
%def_with image_filter
%def_with perl
%def_with xslt

Name: angie
Version: 1.10.2
Release: alt2

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
%{?_with_geoip:BuildRequires: libGeoIP-devel}
%{?_with_image_filter:BuildRequires: libgd-devel}
%{?_with_xslt:BuildRequires: libxslt-devel}

%description
%summary.

%if_with geoip
%package geoip
Summary: GeoIP module for Angie
Group: System/Servers
Requires: GeoIP-Lite-City GeoIP-Lite-Country
Requires: angie = %EVR

%description geoip
GeoIP module for Angie
%endif

%if_with image_filter
%package image_filter
Summary: image_filter module for Angie
Group: System/Servers
Requires: angie = %EVR

%description image_filter
image_filter module for Angie
%endif

%if_with perl
%package perl
Summary: Perl for Angie
Group: System/Servers
Requires: angie = %EVR

%description perl
Perl for Angie
%endif

%package xslt
Summary: XSLT module for Angie
Group: System/Servers
%def_with xslt
Requires: angie = %EVR

%description xslt
XSLT module for Angie

%prep
%setup -a1
%if_with perl
sed -i auto/lib/perl/make \
  -e 's/INSTALLSITEMAN3DIR=.*/INSTALLDIRS=vendor/' \
  -e 's/nginx/angie/g' \
  #
mv src/http/modules/perl/{nginx,angie}.pm
mv src/http/modules/perl/{nginx,angie}.xs
sed -i 's/nginx/angie/g' \
  src/http/modules/perl/Makefile.PL \
  src/http/modules/perl/angie.pm \
  #
%endif

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
  %{?_with_debug:--with-debug} \
  --with-file-aio \
  --with-http_acme_module `# angie` \
  --with-http_addition_module \
  --with-http_auth_request_module \
  --with-http_dav_module \
  --with-http_flv_module \
  %{?_with_geoip:--with-http_geoip_module=dynamic} \
  --with-http_gunzip_module \
  --with-http_gzip_static_module \
  %{?_with_image_filter:--with-http_image_filter_module=dynamic} \
  --with-http_mp4_module \
  %{?_with_perl:--with-http_perl_module=dynamic} \
  --with-http_random_index_module \
  --with-http_realip_module \
  --with-http_secure_link_module \
  --with-http_slice_module \
  --with-http_ssl_module \
  --with-http_stub_status_module \
  --with-http_sub_module \
  --with-http_v2_module \
  --with-http_v3_module `#angie` \
  %{?_with_xslt:--with-http_xslt_module=dynamic} \
  --with-mail \
  --with-mail_ssl_module \
  --with-stream \
  --with-stream_mqtt_preread_module `#angie` \
  --with-stream_rdp_preread_module `#angie` \
  --with-stream_realip_module `#angie` \
  --with-stream_ssl_module \
  --with-stream_ssl_preread_module `#angie` \
  --with-threads \
  #

%make_build DESTDIR=%buildroot

%install
mkdir -p \
  %buildroot%angie_etc/conf-{enabled,available}.d \
  %buildroot%angie_etc/modules-{enabled,available}.d \
  %buildroot%angie_etc/sites-{enabled,available}.d \
  %buildroot%angie_log \
  %buildroot%angie_spool/tmp/{client,proxy,fastcgi,scgi,uwsgi} \
  %buildroot%_datadir/angie/html \
  %buildroot%_lockdir/angie \
  %buildroot%modpath \
  #

%makeinstall_std

for s in %buildroot/%modpath/*.so; do
  fn=${s##*/}
  module=${fn%%.so}
  module=${module#ngx_}
  module=${module%%_module}
  echo "load_module %modpath/$fn;" >>\
    %buildroot%angie_etc/modules-available.d/$module.conf
done

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
%dir %angie_etc
%dir %angie_etc/http.d
%dir %angie_etc/modules-available.d
%dir %angie_etc/stream.d
%dir %_datadir/angie
%dir %_libdir/angie
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

%if_with geoip
%files geoip
%config(noreplace) %angie_etc/modules-available.d/http_geoip.conf
%modpath/ngx_http_geoip_module.so
%endif

%if_with image_filter
%files image_filter
%config(noreplace) %angie_etc/modules-available.d/http_image_filter.conf
%modpath/ngx_http_image_filter_module.so
%endif

%if_with perl
%files perl
%config(noreplace) %angie_etc/modules-available.d/http_perl.conf
%modpath/ngx_http_perl_module.so
%perl_vendor_archlib/angie.pm
%perl_vendor_autolib/angie
%endif

%files xslt
%config(noreplace) %angie_etc/modules-available.d/http_xslt_filter.conf
%modpath/ngx_http_xslt_filter_module.so

%changelog
* Wed Oct 22 2025 Constantin Sunzow <protvin@altlinux.org> 1.10.2-alt2
- Build with:
  + debug (ALT 56455).
  + geoip (ALT 56453).
  + image_filter (ALT 56452).
  + perl (ALT 56454).
  + xslt (ALT 56450).

* Tue Sep 02 2025 Constantin Sunzow <protvin@altlinux.org> 1.10.2-alt1
- New version.

* Fri Jul 04 2025 Constantin Sunzow <protvin@altlinux.org> 1.10.0-alt1
- New version.

* Tue Jun 17 2025 Constantin Sunzow <protvin@altlinux.org> 1.9.1-alt1
- New version.

* Wed Apr 30 2025 Constantin Sunzow <protvin@altlinux.org> 1.9.0-alt1
- New version.

* Mon Mar 03 2025 Constantin Sunzow <protvin@altlinux.org> 1.8.2-alt1
- New version.

* Fri Jan 10 2025 Constantin Sunzow <protvin@altlinux.org> 1.8.1-alt1
- Initial build.
