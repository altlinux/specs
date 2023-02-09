Name: sympa
Version: 6.2.71
Release: alt0.2.b1

%def_without authorcheck
%define ngxconfdir %_sysconfdir/nginx/sites-available.d
%define _exec_prefix %_libexecdir/%name
%define _var_prefix %_localstatedir/%name
%define static_content %_datadir/sympa/static_content
%define s_user %name
%define s_group %name

# Unbundling helper macro
# 1st arg is the path to dir bundling files (from)
# 2nd arg is the path to dir containing original files (with)
%global unbundle_from_with() \
  bundled_dir="%1" \
  bundled_files="$(find "${bundled_dir}" -maxdepth 1 -type f -printf '%f\\n')" \
  original_dir="%2" \
  for file in ${bundled_files} \
  do \
    if [ -f "${original_dir}/${file}" ] \
    then \
      rm -f "${bundled_dir}/${file}" \
      ln -s "${original_dir}/${file}" "${bundled_dir}/${file}" \
    fi \
  done

# Bundled Fonts
%global unbundle_fontawesome       1
%global unbundle_raleway           1
#
%global unbundle_foundation_icons  0

# Not available ?
%global unbundle_foundation        0
# Not available ?
%global unbundle_html5shiv         0
# Not available ?
%global unbundle_jquery            1
# Available version is too old
%global unbundle_jquery_migrate    0
# Not available
%global unbundle_jquery_minicolors 0
#
%global unbundle_jquery_ui         0
# Only available for Fedora
%global unbundle_jqplot            0
#
%global unbundle_respond           0

# Licenses
# Sympa itself is GPLv2+.
# Possibly bundled fonts are :
# - fontawesome-fonts :      OFL
# - fontawesome-fonts-web:   OFL and MIT
# - impallari-raleway-fonts: OFL
# - foundation-icons-fonts:  MIT
# Possibly bundled javascripts are :
# - js-html5shiv:            MIT or GPLv2
# - javascript-jquery-jqplot:        MIT or GPLv2
# - javascript-jquery:               MIT
# - js-respond:              MIT
# - javascript-jquery-ui:            MIT
# - js-foundation:           MIT
# - javascript-jquery-migrate:       MIT
# - javascript-jquery-minicolors:    MIT
%global licenses_bundled     %nil
# MIT
%if ! %unbundle_foundation_icons || ! %unbundle_foundation || ! %unbundle_jquery || ! %unbundle_jquery_migrate || ! %unbundle_jquery_minicolors || ! %unbundle_jquery_ui || ! %unbundle_respond
%global licenses_bundled %licenses_bundled and MIT
%endif
# MIT or GPLv2
%if ! %unbundle_html5shiv || ! %unbundle_jqplot
%global licenses_bundled %licenses_bundled and (MIT or GPLv2)
%endif

Summary: Powerful multilingual List Manager
Summary(fr): Gestionnaire de listes électroniques
Summary(ja): 高機能で多言語対応のメーリングリスト管理ソフトウェア
# The License: tag depends on bundled code for a given distro/release
License: GPLv2+%licenses_bundled
Group: System/Servers
Url: http://www.sympa.org
Source0: https://github.com/sympa-community/sympa/releases/download/%version%{?pre_rel}/%name-%version%{?pre_rel}.tar

Source101: sympa-httpd24-spawn_fcgi.conf
Source102: sympa-lighttpd.conf
Source103: sympa-nginx-spawn_fcgi.conf
Source106: sympa-rsyslog.conf
Source107: sympa-logrotate.conf
Source113: sympa-systemd-README.RPM.md
Source114: aliases.sympa.sendmail
Source115: aliases.sympa.postfix
Source129: sympa.service.d-dependencies.conf
Source130: sympa-sysconfig

Source200: apache2.mods-start
Source201: apache2.sites-start
Source202: apache2.ports-start


# Add path to MHonArc::UTF8 so that sympa setup won't miss it
Patch5: sympa-2.6.70-sympa-mhonarc.patch
# RPM specific customization of site defaults
Patch13: sympa-6.2.57b.1-confdef.patch
# ALT fhs specifics
Patch20: sympa-6.2.70-conf-alt-fhs.patch

# install & check
BuildRequires: perl-devel perl-ldap
BuildRequires: perl(Archive/Zip.pm)
BuildRequires: perl(CGI/Cookie.pm)
BuildRequires: perl(CGI/Fast.pm)
BuildRequires: perl(CGI/Util.pm)
BuildRequires: perl(Class/Singleton.pm)
BuildRequires: perl(Data/Password.pm)
BuildRequires: perl(DateTime.pm)
BuildRequires: perl(DateTime/Format/Mail.pm)
BuildRequires: perl(DBD/SQLite.pm)
BuildRequires: perl(DBI.pm)
BuildRequires: perl(Encode.pm)
BuildRequires: perl(Encode/MIME/Header.pm)
BuildRequires: perl(FCGI.pm)
BuildRequires: perl(File/Copy/Recursive.pm)
BuildRequires: perl(File/NFSLock.pm)
BuildRequires: perl(HTML/Entities.pm)
BuildRequires: perl(HTML/FormatText.pm)
BuildRequires: perl(HTML/Parser.pm)
BuildRequires: perl(HTML/StripScripts/Parser.pm)
BuildRequires: perl(HTML/TreeBuilder.pm)
BuildRequires: perl(HTTP/Request.pm)
BuildRequires: perl(IO/Scalar.pm)
BuildRequires: perl(IO/Socket/IP.pm)
BuildRequires: perl(IO/Socket/SSL.pm)
BuildRequires: perl(Locale/Messages.pm)
BuildRequires: perl(LWP/Protocol/https.pm)
BuildRequires: perl(LWP/UserAgent.pm)
BuildRequires: perl(Mail/Address.pm)
BuildRequires: perl(MIME/Charset.pm)
BuildRequires: perl(MIME/EncWords.pm)
BuildRequires: perl(MIME/Entity.pm)
BuildRequires: perl(MIME/Head.pm)
BuildRequires: perl(MIME/Lite/HTML.pm)
BuildRequires: perl(MIME/Parser.pm)
BuildRequires: perl(MIME/Tools.pm)
BuildRequires: perl(Net/CIDR.pm)
BuildRequires: perl(SOAP/Lite.pm)
BuildRequires: perl(SOAP/Transport/HTTP.pm)
BuildRequires: perl(Template.pm)
BuildRequires: perl(Term/ProgressBar.pm)
BuildRequires: perl(Test/Compile.pm)
BuildRequires: perl(Test/Net/LDAP.pm)
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Text/LineFold.pm)
BuildRequires: perl(Unicode/GCString.pm)
BuildRequires: perl(Unicode/Normalize.pm)
BuildRequires: perl(Unicode/UTF8.pm)
BuildRequires: perl(URI.pm)
BuildRequires: perl(URI/Escape.pm)
BuildRequires: perl(XML/LibXML.pm)

%if %{with authorcheck}
BuildRequires: perl(Test/Fixme.pm)
BuildRequires: perl(Test/Perl/Critic.pm)
BuildRequires: perl(Test/Pod/Coverage.pm)
BuildRequires: perl(Test/Pod/Spelling/CommonMistakes.pm)
%endif

Requires(pre): shadow-utils

Requires: smtpdaemon
Requires: mhonarc
Requires: logrotate
Requires: perl(DBD/mysql.pm)
Requires: perl(FCGI.pm)

# Optional CPAN packages
Requires: perl(AuthCAS.pm)
Requires: perl(Clone.pm)
Requires: perl(Crypt/CipherSaber.pm)
Requires: perl(Crypt/Eksblowfish.pm)
Requires: perl(Crypt/OpenSSL/X509.pm)
Requires: perl(Crypt/SMIME.pm)
Requires: perl(Data/Password.pm)
Requires: perl(DateTime/TimeZone.pm)
Requires: perl(DBD/CSV.pm)
Requires: perl(Encode/Locale.pm)
# Recommended for handling Japanese vendor codepages.
Requires: perl(Encode/EUCJPASCII.pm)
# Handling several Chinese standards.
Requires: perl(Encode/HanExtra.pm)
Requires: perl(IO/Socket/IP.pm)
Requires: perl(IO/Socket/SSL.pm)
Requires: perl(List/Util/XS.pm)
Requires: perl(LWP/Protocol/https.pm)
Requires: perl(Mail/DKIM/Verifier.pm)
Requires: perl(Net/DNS.pm)
Requires: perl(Net/SMTP.pm)
Requires: perl(Unicode/Normalize.pm)
Requires: perl(Unicode/UTF8.pm)
# On disk attachments compression
Requires: perl(Archive/Zip/SimpleZip.pm)

BuildRequires(pre): rpm-macros-webserver-common rpm-macros-apache2 rpm-macros-javascript

%add_perl_lib_path %_datadir/%name/lib
%filter_from_provides /perl(Conf\.pm)/d
%filter_from_requires /perl(Conf\.pm)/d;/\/usr\/share\/fonts\-font\-awesome.*/d;\/usr\/share\/javascript.*/d

%description
Sympa is scalable and highly customizable mailing list manager. It
can cope with big lists (200,000 subscribers) and comes with a
complete (user and admin) Web interface. It is internationalized,
and supports the us, fr, de, es, it, fi, and chinese locales. A
scripting language allows you to extend the behavior of commands.
Sympa can be linked to an LDAP directory or an RDBMS to create
dynamic mailing lists. Sympa provides S/MIME-based authentication
and encryption.

%description -l ja
Sympa はスケーラブルで高いカスタマイズ性を持つメーリングリスト管理
ソフトウェアです。巨大なリスト (登録者数 200,000) にも適用でき、完
全な (一般ユーザ用および管理者用) ウェブインタフェースをそなえてい
ます。国際化されており、多数の言語に対応します。内蔵のスクリプティ
ング言語でコマンドの動作を拡張できます。Sympa はまた、LDAP ディレ
クトリや RDBMS と連携して動的なメーリングリストを作成できます。ま
た、S/MIME に基づく認証や暗号化もできます。

%package web
Group: System/Servers
Summary: WWW and SOAP Sympa services
Requires: %name = %EVR, %name-static-content = %EVR
Provides: ww%name = %EVR

%description web
WWW and SOAP Sympa services.

%package web-multiwatch
Group: System/Servers
Summary: WWW and SOAP Sympa services (multiwatch-version)
Requires: %name-web = %EVR, multiwatch
BuildArch: noarch

%description web-multiwatch
WWW and SOAP Sympa services (multiwatch version).

%package apache2
Group: System/Servers
Summary: Sympa with Apache2 HTTP Server
Summary(fr): Sympa avec Serveur HTTP Apache2
Summary(ja): SympaのApache2 HTTP Server対応
Requires: %name-web = %EVR
Requires: apache2
BuildArch: noarch
Conflicts: %name-lighttpd, %name-nginx

%description apache2
Apache HTTP Server support for Sympa.

%description apache2 -l ja
Sympa の Apache HTTP Server 対応。

%package lighttpd
Group: System/Servers
Summary: Sympa with lighttpd
Summary(fr): Sympa avec lighttpd
Summary(ja): Sympaのlighttpd対応
Requires: %name-web = %EVR
BuildArch: noarch
Requires: lighttpd
Conflicts: %name-apache2, %name-nginx

%description lighttpd
lighttpd support for Sympa.

%description lighttpd -l ja
Sympa の lighttpd 対応。

%package nginx
Group: System/Servers
Summary: Sympa with nginx
Summary(fr): Sympa avec nginx
Summary(ja): Sympaのnginx対応
Requires: %name-web = %EVR
BuildArch: noarch
Requires: nginx spawn-fcgi
Conflicts: %name-apache2, %name-lighttpd

%description nginx
nginx support for Sympa.

%description nginx -l ja
Sympa の nginx 対応。

%package devel-doc
Group: System/Servers
Summary: Sympa devel doc
Requires: %name = %EVR

%description devel-doc
Sympa documentation for developers.

%package static-content
Group: System/Servers
Summary: Sympa static web content
# Bundled fonts
%if %unbundle_fontawesome
BuildRequires: fonts-font-awesome >= 4.3.0
Requires: fonts-font-awesome >= 4.3.0
%else
Provides: bundled(fonts-font-awesome) = 4.3.0
%endif
%if %unbundle_raleway
BuildRequires: fonts-otf-impallari-raleway >= 3.0
Requires: fonts-otf-impallari-raleway >= 3.0
%else
Provides: bundled(fonts-otf-impallari-raleway) = 3.0
%endif
%if %unbundle_foundation_icons
BuildRequires: fonts-otf-foundation-icons >= 3.0
Requires: fonts-otf-foundation-icons >= 3.0
%else
Provides: bundled(fonts-otf-foundation-icons) = 3.0
%endif
# Bundled javascript libs
# foundation
%if %unbundle_foundation
BuildRequires: javascript-foundation6 >= 6.4.2
Requires: javascript-foundation6 >= 6.4.2
%else
Provides: bundled(javascript-foundation) = 6.4.2
# Bundled in bundled js-foundation
Provides: bundled(javascript-what-input) = 4.2.0
%endif
# html5shiv
%if %unbundle_html5shiv
BuildRequires: javascript-html5shiv >= 3.7.2
Requires: javascript-html5shiv >= 3.7.2
%else
Provides: bundled(javascript-html5shiv) = 3.7.2
%endif
# jquery
%if %unbundle_jquery
BuildRequires: javascript-jquery >= 3.5.0
Requires: javascript-jquery >= 3.5.0
%else
Provides bundled(javascript-jquery) = 3.6.0
%endif
# jquery-migrate
%if %unbundle_jquery_migrate
BuildRequires: xstatic-jquery-migrate-common >= 1.4.1
Requires: xstatic-jquery-migrate-common >= 1.4.1
%else
Provides: bundled(javascript-jquery-migrate) = 1.4.1
%endif
# jquery-minicolors
%if %unbundle_jquery_minicolors
BuildRequires: javascript-jquery-minicolors >= 2.3.1
Requires: javascript-jquery-minicolors >= 2.3.1
%else
Provides: bundled(javascript-jquery-minicolors) = 2.3.1
%endif
# jquery-ui
%if %unbundle_jquery_ui
BuildRequires: javascript-jquery-ui >= 1.12.1
Requires: javascript-jquery-ui >= 1.12.1
%else
Provides: bundled(javascript-jquery-ui) = 1.12.1
%endif
# jqplot
%if %unbundle_jqplot
BuildRequires: javascript-jquery-jqplot >= 1.0.8
Requires: javascript-jquery-jqplot >= 1.0.8
%else
Provides: bundled(javascript-jquery-jqplot) = 1.0.8
%endif
# respond
%if %unbundle_respond
BuildRequires: javascript-respond >= 1.4.2
Requires: javascript-respond >= 1.4.2
%else
Provides: bundled(javascript-respond) = 1.4.2
%endif
BuildArch: noarch

%description static-content
Sympa static web content.

%prep
%setup -q -n %name-%version
%patch5 -p1 -b .mhonarc
%patch13 -p0 -b .confdef
%patch20 -p1 -b .alt-fhs

%build
%autoreconf

# Give install "-p" preserving mtime to prevent unexpected update of CSS.
%configure \
    --enable-fhs \
    --prefix=%_prefix \
    --bindir=%_exec_prefix \
    --docdir=%_docdir/%name \
    --libexecdir=%_libexecdir/sympa \
    --sysconfdir=%_sysconfdir/sympa \
    --with-cgidir=%_exec_prefix \
    --with-confdir=%_sysconfdir/sympa \
    --without-initdir \
    --with-unitsdir=%_unitdir \
    --with-piddir=%_runtimedir/sympa \
    --with-smrshdir=%_sysconfdir/smrsh \
    --with-aliases_file=%_localstatedir/sympa/sympa_aliases \
    --with-perl=%_bindir/perl \
    --with-staticdir=%static_content \
    --with-cssdir=%_localstatedir/sympa/css \
    --with-picturesdir=%_localstatedir/sympa/pictures \
    --with-localedir=%_datadir/locale \
    INSTALL_DATA='install -c -p -m 644'
%make_build

# cancel workaround in Makefile getting previous version.
rm -f previous_sympa_version

pushd po/sympa; rm -f stamp-po; make; popd
pushd po/web_help; rm -f stamp-po; make; popd

%install
%make install DESTDIR=%buildroot

%find_lang --with-man --output=%name.lang %name
%find_lang --output=web_help.lang --all-name web_help

# Unbundle fonts from static_content/fonts
# font-awesome
%if %unbundle_fontawesome
%unbundle_from_with %buildroot%static_content/fonts/font-awesome/fonts %_datadir/fonts-font-awesome/fonts
%unbundle_from_with %buildroot%static_content/fonts/font-awesome/css %_datadir/fonts-font-awesome/css
%endif

# Raleway
%if %unbundle_raleway
rm -f %buildroot%static_content/fonts/Raleway/OFL.txt
%unbundle_from_with %buildroot%static_content/fonts/Raleway %_datadir/fonts/otf/impallari-raleway
%endif

# foundation-icons
%if %unbundle_foundation_icons
rm -f %buildroot%_datadir/fonts/foundation-icons/preview.html
rm -f %buildroot%_datadir/fonts/foundation-icons/foundation-icons.{eot,svg,woff}
rm -rf %buildroot%_datadir/fonts/foundation-icons/svgs
%unbundle_from_with %buildroot%static_content/fonts/foundation-icons %_datadir/fonts/foundation-icons
%endif

# Unbundle javascript libraries from static_content/js
# FIXME : foundation (Foundation for Sites 6, with float grid support)
%if %unbundle_foundation
%unbundle_from_with %buildroot%static_content/js/foundation/js %_datadir/javascript/foundation/js
%unbundle_from_with %buildroot%static_content/js/foundation/css %_datadir/javascript/foundation/css
# what-input.js
%unbundle_from_with %buildroot%static_content/js/foundation/js/vendor %_datadir/javascript
%endif

# html5shiv
%if %unbundle_html5shiv
%unbundle_from_with %buildroot%static_content/js/html5shiv %_datadir/javascript
%endif

# jquery
%if %unbundle_jquery
%unbundle_from_with %buildroot%static_content/js %_jquerydir
%endif

# FIXME : jquery-migrate
%if %unbundle_jquery_migrate
%unbundle_from_with %buildroot%static_content/js %_datadir/javascript/jquery_migrate
%endif

# FIXME : jquery-minicolors
%if %unbundle_jquery_minicolors
%unbundle_from_with %buildroot%static_content/js/jquery-minicolors %_datadir/javascript/jquery-minicolors
%endif

# jquery-ui
%if %unbundle_jquery_ui
%unbundle_from_with %buildroot%static_content/js/jquery-ui %_datadir/javascript/jquery-ui
# FIXME: Unbundle theme (smoothness ?)
#unbundle_from_with %static_content/js/jquery-ui/images %_datadir/javascript/jquery-ui/themes/smoothness/images
%endif

# jqplot
%if %unbundle_jqplot
%unbundle_from_with %buildroot%static_content/js/jqplot %_datadir/javascript/jquery-jqplot
%endif

# respond
%if %unbundle_respond
%unbundle_from_with %buildroot%static_content/js/respondjs %_datadir/javascript
%endif

# Save version info.
mv %buildroot%_sysconfdir/%name/data_structure.version \
    %buildroot%_sysconfdir/%name/data_structure.current_version
touch %buildroot%_sysconfdir/%name/data_structure.version

# Copy *httpd config files.
install -d %buildroot%apache2_mods_start
install -d %buildroot%apache2_sites_available
install -d %buildroot%apache2_sites_start
install -d %buildroot%apache2_ports_start
# FIXME! should be a better way!
install -p -m644 %SOURCE200 %buildroot%apache2_mods_start/%name.conf
install -p -m644 %SOURCE201 %buildroot%apache2_sites_start/%name.conf
install -p -m644 %SOURCE202 %buildroot%apache2_ports_start/%name.conf
sed -e 's|@DATADIR@|%_var_prefix|g;s|@STATIC_CONTENT@|%static_content|g' \
	%SOURCE101 > %buildroot%apache2_sites_available/%name.conf

# install lighttpd
install -pD -m644 /dev/null %buildroot%_sysconfdir/lighttpd/conf.d/%name.conf
sed -e 's|@CODEDIR@|%_exec_prefix|g;s|@STATIC_CONTENT@|%static_content|g;s|@DATADIR@|%_var_prefix|g' \
	%SOURCE102 %buildroot%_sysconfdir/lighttpd/conf.d/%name.conf

# Install the nginx configuration file.
install -pD -m644 /dev/null %buildroot%ngxconfdir/%name.conf
sed -e 's|@CODEDIR@|%_exec_prefix|g;s|@STATIC_CONTENT@|%static_content|g;s|@DATADIR@|%_var_prefix|g' \
	%SOURCE103 > %buildroot%ngxconfdir/%name.conf

# Copy init scripts or unit files for nginx/spawn-fcgi etc.
install -m 0644 service/wwsympa-spawn-fcgi.service \
    %buildroot%_unitdir/wwsympa.service
install -m 0644 service/sympasoap-spawn-fcgi.service \
    %buildroot%_unitdir/sympasoap.service
mkdir -p %buildroot%_tmpfilesdir
install -m 0644 service/sympa-tmpfiles.conf \
    %buildroot%_tmpfilesdir/%name.conf
mkdir -p %buildroot%_sysconfdir/systemd/system/sympa.service.d
install -m 0644 %SOURCE129 \
    %buildroot%_sysconfdir/systemd/system/sympa.service.d/dependencies.conf

# multiwatch variant
install -m 0644 service/wwsympa-multiwatch.service \
    %buildroot%_unitdir/
install -m 0644 service/wwsympa-multiwatch.socket \
    %buildroot%_unitdir/wwsympa.socket
install -m 0644 service/sympasoap-multiwatch.service \
    %buildroot%_unitdir/
install -m 0644 service/sympasoap-multiwatch.socket \
    %buildroot%_unitdir/sympasoap.socket

# Copy system config file.
mkdir -p %buildroot%_sysconfdir/sysconfig
install -m 0644 %SOURCE130 %buildroot%_sysconfdir/sysconfig/%name

# Copy docs.
mv %buildroot%_docdir/%name __doc
cp -p AUTHORS.md CONTRIBUTING.md NEWS.md README.md __doc/
cp -p %SOURCE113 __doc/README.RPM.md
ln -s %_sysconfdir/%name/README \
    %buildroot/%_datadir/%name/default/README

# Copy robot aliases.
install -m 0644 %SOURCE114 %SOURCE115 %buildroot%_sysconfdir/%name/
touch %buildroot%_sysconfdir/%name/aliases.sympa.sendmail.db
touch %buildroot%_sysconfdir/%name/aliases.sympa.postfix.db

# Copy rsyslog config
mkdir -p %buildroot%_sysconfdir/rsyslog.d
install -m 0644 %SOURCE106 %buildroot%_sysconfdir/rsyslog.d/%name.conf

# Create logrotate item
mkdir -p %buildroot%_sysconfdir/logrotate.d
install -m 0644 %SOURCE107 %buildroot%_sysconfdir/logrotate.d/%name

# Create configuration override structure
for conffile in \
    auth.conf charset.conf crawlers_detection.conf create_list.conf \
    edit_list.conf nrcpt_by_domain.conf topics.conf \
    mime.types sympa.wsdl ;
    do cp -a %buildroot%_datadir/%name/default/$conffile \
        %buildroot%_sysconfdir/%name/;
done

# Create directory for S/MIME user certificates
mkdir -p %buildroot%_var_prefix/X509-user-certs

touch %buildroot%_var_prefix/{sympa_aliases,sympa_aliases.db}

%check
make check
%if %{with authorcheck}
make authorcheck || true
%endif

%pre
# Create "sympa" group if it does not exist
getent group %s_group >/dev/null || /usr/sbin/groupadd -r %s_group

# Create "sympa" user if it does not exist
getent passwd sympa >/dev/null || \
  /usr/sbin/useradd -r -g %s_group \
      -d %_var_prefix \
      -c "System User for Sympa" \
      -s "/sbin/nologin" \
      %s_user
exit 0

%post
# register service
%post_service %name

# create cookie
function create_cookie {
    cook=`mktemp`
    perl -ne 'chomp $_; print $1 if /^cookie\s+(\S.*)/' \
        %_sysconfdir/%name/%name.conf > $cook
    if [ '!' -s $cook ]; then
        if [ -e %_sysconfdir/%name/cookies.history ]; then
            cp -p %_sysconfdir/%name/cookies.history $cook
        else
            dd if=/dev/urandom bs=2048 count=1 2>/dev/null | md5sum | \
            cut -d" " -f1 > $cook
        fi
        perl -i -pe '/^#cookie\s/ and $_ = "cookie ".`cat '$cook'`."\n"' \
            %_sysconfdir/%name/%name.conf
    fi
    rm -f $cook
}

# create config at first time.
function create_config {
    ## create site configurations
    if [ '!' -e %_sysconfdir/%name/data_structure.version ]; then
        cat %_sysconfdir/%name/data_structure.current_version > \
            %_sysconfdir/%name/data_structure.version
    fi
}

function upgrade_data_structure {
    # Stop sympa if it is running
    if systemctl is-active %name > /dev/null 2>&1; then
        /usr/bin/systemctl stop %name > /dev/null 2>&1
        ACTIVE="yes"
    fi
    # Upgrade
    rm -f %_sysconfdir/%name/%name.conf.bin > /dev/null 2>&1
    if %_sbindir/sympa.pl --upgrade > /dev/null 2>&1; then
        # Start sympa if it was running previously
        if [ "$ACTIVE" == "yes" ]; then
            /usr/bin/systemctl start %name > /dev/null 2>&1
        fi
    else
        echo ============================================================
        echo Notice: Failed upgrading data structure.  See logfile.
        echo Sympa is stopped.
        echo ============================================================
    fi
}

# Install
if [ $1 -eq 1 ]; then
    create_cookie
    create_config
    echo ============================================================
    echo Sympa had been installed successfully.  If you installed
    echo Sympa at first time, please read:
    echo %_docdir/%name-%version/README.RPM.md
    echo ============================================================
fi

# Update
if [ $1 -gt 1 ]; then
    upgrade_data_structure
fi

%preun
%preun_service %name

%post web
# register service
%post_service wwsympa
%post_service sympasoap

%preun web
%preun_service wwsympa
%preun_service sympasoap

%files -f %name.lang -f web_help.lang
%doc __doc/* COPYING
%dir %attr(2771,root,%s_group) %_sysconfdir/%name/
%_sysconfdir/%name/README
%config(noreplace) %attr(0640,%s_user,%s_group) %_sysconfdir/%name/%name.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/auth.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/charset.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/crawlers_detection.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/create_list.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/edit_list.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/nrcpt_by_domain.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/topics.conf
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/mime.types
%config(noreplace,missingok) %attr(-,%s_user,%s_group) %_sysconfdir/%name/sympa.wsdl
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/create_list_templates
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/tasks
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/scenari
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/mail_tt2
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/web_tt2
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/custom_actions
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/custom_conditions
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/data_sources
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/families
%dir %attr(-,%s_user,%s_group) %_sysconfdir/%name/search_filters
%attr(0640,%s_user,%s_group) %config(missingok) %_sysconfdir/%name/data_structure.current_version
%attr(0640,%s_user,%s_group) %ghost %config(noreplace,missingok) %verify(not md5 mtime size) %_sysconfdir/%name/data_structure.version
%config(noreplace) %attr(0664,root,%s_group) %_sysconfdir/%name/aliases.sympa.sendmail
%config(noreplace) %attr(0664,root,%s_group) %_sysconfdir/%name/aliases.sympa.sendmail.db
%config(noreplace) %attr(0664,root,%s_group) %_sysconfdir/%name/aliases.sympa.postfix
%config(noreplace) %attr(0664,root,%s_group) %_sysconfdir/%name/aliases.sympa.postfix.db
%_sysconfdir/smrsh
%config(noreplace) %_sysconfdir/rsyslog.d/*
%config(noreplace) %_sysconfdir/logrotate.d/sympa
%_sbindir/*
%dir %_exec_prefix
%attr(4711,%s_user,%s_group) %_exec_prefix/bouncequeue
%attr(4711,%s_user,%s_group) %_exec_prefix/familyqueue
%attr(4711,%s_user,%s_group) %_exec_prefix/queue
%attr(4711,root,%s_group) %_exec_prefix/sympa_newaliases-wrapper
%attr(0751,%s_user,%s_group) %_var_prefix/
%attr(0644,%s_user,%s_group) %ghost %config(noreplace,missingok) %verify(not md5 mtime size) %_var_prefix/sympa_aliases
%attr(0644,root,%s_group) %ghost %config(noreplace,missingok) %verify(not md5 mtime size) %_var_prefix/sympa_aliases.db
%attr(-,%s_user,%s_group) %_var/spool/%name/
%_datadir/%name/
%exclude %static_content
%_man1dir/*
%_man5dir/*
%_man8dir/*
%_unitdir/sympa.service
%_unitdir/sympa-outgoing.service
%_unitdir/sympa-archive.service
%_unitdir/sympa-bounce.service
%_unitdir/sympa-task.service
%_tmpfilesdir/%name.conf
%ghost %attr(0751,%s_user,%s_group) %_runtimedir/%name/
%dir %_sysconfdir/systemd/system/sympa.service.d/
%config(noreplace) %_sysconfdir/systemd/system/sympa.service.d/*
%config(noreplace) %_sysconfdir/sysconfig/sympa

%files web
%_exec_prefix/sympa_soap_server.fcgi
%attr(6711,%s_user,%s_group) %_exec_prefix/sympa_soap_server-wrapper.fcgi
%_exec_prefix/wwsympa.fcgi
%attr(6711,%s_user,%s_group) %_exec_prefix/wwsympa-wrapper.fcgi
%_unitdir/wwsympa.service
%_unitdir/sympasoap.service

%files web-multiwatch
%_unitdir/wwsympa-multiwatch.service
%_unitdir/sympasoap-multiwatch.service
%_unitdir/wwsympa.socket
%_unitdir/sympasoap.socket

%files apache2
%config(noreplace) %apache2_mods_start/%name.conf
%config(noreplace) %apache2_sites_available/%name.conf
%config(noreplace) %apache2_sites_start/%name.conf
%config(noreplace) %apache2_ports_start/%name.conf

%files lighttpd
%config(noreplace) %_sysconfdir/lighttpd/conf.d/%name.conf

%files nginx
%config(noreplace) %ngxconfdir/%name.conf

%files devel-doc
%_man3dir/*

%files static-content
%static_content

%changelog
* Thu Feb 09 2023 L.A. Kostis <lakostis@altlinux.ru> 6.2.71-alt0.2.b1
- nginx: added param for vhosts setup.
- .spec: fix typo in data_structure init.

* Thu Jan 26 2023 L.A. Kostis <lakostis@altlinux.ru> 6.2.71-alt0.1.b1
- Updated to 6.2.71b.1.

* Thu Dec 15 2022 L.A. Kostis <lakostis@altlinux.ru> 6.2.70-alt0.1
- Updated to 6.2.70.
- Update patches.
- Added systemd socket activation services with multiwatch.

* Mon Jan 31 2022 L.A. Kostis <lakostis@altlinux.ru> 6.2.68-alt0.1
- Updated to 6.2.68.

* Fri Nov 26 2021 L.A. Kostis <lakostis@altlinux.ru> 6.2.67-alt0.1.b2
- Updated to 6.2.67b.2
- Req: added perl-Archive-Zip-SimpleZip (see upstream issue #1235)

* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 6.2.66-alt0.3
- Fix unowned dirs.

* Wed Nov 10 2021 L.A. Kostis <lakostis@altlinux.ru> 6.2.66-alt0.2
- Unbundle jquery.
- Split static-content into subpackage.
- Rename wwwsympa->web.

* Mon Nov 08 2021 L.A. Kostis <lakostis@altlinux.ru> 6.2.66-alt0.1
- Rebuild for ALTLinux.

* Tue Oct 05 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.66-1
- Update to 6.2.66

* Thu Jul 15 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.64-1
- Update to 6.2.64
- Fix jquery-ui unbundling
- Add 2 upstream patches

* Tue Apr 27 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.62-1
- Update to 6.2.62
  - Fixes CVE-2020-26880 (RHBZ#1886232 - RHBZ#1886233)
- Unbundle jquery-ui
- Unbundle jquery on EL8

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 6.2.60-2.1
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Wed Feb 17 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.60-2
- Prepare for jquery-ui retirement in F34
- Remove conditionals for F31

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.60-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 04 2021 Xavier Bachelot <xavier@bachelot.org> 6.2.60-1
- Update to 6.2.60
  - Fixes CVE-2020-29668 (RHBZ#1906576)

* Sat Nov 07 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.58-2
- Add BR: perl-Test-Net-LDAP
- Remove all of EL6 thus sysvinit support

* Tue Oct 20 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.58-1
- Update to 6.2.58

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.56-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.56-2
- Prepare for some js packages retirement in Fedora

* Sun May 24 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.56-1
- Update to 6.2.56 (Fixes CVE-2020-10936)
- Fix typo in url and also socket location in lighttpd configuration (RHBZ#1812325)

* Mon Mar 02 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.54-1
- Update to 6.2.54 (Fixes CVE-2020-9369).

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.52-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Xavier Bachelot <xavier@bachelot.org> 6.2.52-2
- Add upstream patches to fix 2 scenario failures.

* Fri Dec 27 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.52-1
- Update to 6.2.52.

* Sun Dec 22 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.50-1
- Update to 6.2.50.
- Re-enable Crypt::OpenSSL::X509 for EL8.

* Fri Nov 29 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-3
- Add patch to fix compile executables test on F32.
- Add dependency on Socket6 and IO::Socket::IP
  (or alternatively Socket6 and IO::Socket::INET6 on EL6).
- Add patch to fix ldap 2 level query.
- Re-enable Crypt::SMIME for EL8.
- Re-enable all web subpackages for EL8.

* Wed Oct 16 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-2
- Don't require optional perl modules unavailable on EL8.
- Disable httpd and lighttpd support for EL8 until missing bits are available.
- Change sympa localstatedir owner/group to sympa:sympa. Fixes RHBZ#1761455.

* Mon Sep 30 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.48-1
- Update to 6.2.48.

* Mon Sep 23 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.46-1
- Update to 6.2.46.
- Unbundle foundation-icons font.
- Add dependency on LWP::Protocol::https (RHBZ#1753111).
- Don't unbundle js-respond on EL8 (yet).

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.2.44-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jul 18 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-3
- Don't build for ix86 on EL6.
- Re-order some parts of spec for better readability.
- Use bcond_with macro instead of custom macros.

* Mon Jul 15 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-2
- Don't package OChangeLog and ONEWS. Saves 5MB.
- Move developers documentation to devel-doc sub-package.
- Compute an accurate License: tag.

* Wed Jun 26 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.44-1
- Update to 6.2.44.

* Mon Jun 10 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.43-0.2.b.2
- Update to 6.2.43 beta 2.

* Thu May 23 2019 IKEDA Soji <ikeda@conversion.co.jp> 6.2.43-0.1.b.1
- Update to 6.2.43 beta 1.
- Move sympa.conf-dist to doc.

* Thu Mar 21 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.42-1
- Update to 6.2.42.

* Sun Mar 10 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.41-0.2.b.2
- Update to 6.2.41 beta 2.

* Sun Feb 03 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.41-0.1.b.1
- Update to 6.2.41 beta 1.

* Mon Jan 28 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.40-2
- Unbundle jqplot on F29+.
- Use versioned Requires and BuildRequires for unbundled fonts and libs.

* Sat Jan 19 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.40-1
- Update to 6.2.40.

* Fri Jan 11 2019 Xavier Bachelot <xavier@bachelot.org> 6.2.38-2
- Fix fontawesome, jquery-ui and jquery-migrate unbundling on EL7.
- Fix wwsympa/sympasoap not being restarted on update.

* Fri Dec 21 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.38-1
- Update to 6.2.38.

* Sat Dec 08 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.3.b.3
- Update to 6.2.37 beta 3.

* Sat Nov 03 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.2.b.2
- Update to 6.2.37 beta 2.

* Sun Oct 07 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.37-0.1.b.1
- Update to 6.2.37 beta 1.

* Sun Sep 23 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.36-1
- Update to 6.2.36.

* Sun Aug 26 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.35-0.1.b.1
- Update to 6.2.35b.1.
- For sympa-httpd with Fedora & EL7: Use mod_proxy_fcgi instead of mod_fcgid.

* Sun Aug 26 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.34-2
- Issue #36: Init scripts for wwsympa/sympasoap were broken.

* Thu Jul 05 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.34-1
- Update to 6.2.34.

* Fri Jun 29 2018 IKEDA Soji <ikeda@conversion.co.jp> 6.2.33-0.2.b.2
- Update to 6.2.33 beta 2.
  Upstream #170 WWSympa: Switch to Foundation 6
  Upstream #220 static_content directory structure
  Upstream #336 Starting a test framework

* Wed Apr 25 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.32-2
- Add missing Requires on EL6 and EL7.

* Thu Apr 19 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.32-1
- Update to 6.2.32 (Security release).
  See https://sympa-community.github.io/security/2018-001.html

* Mon Mar 26 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.30-1
- Update to 6.2.30.

* Thu Mar 22 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.28-1
- Update to 6.2.28.

* Tue Mar 20 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.26-1
- Update to 6.2.26.
- Fix scriptlet.

* Tue Mar 13 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.3.b.3
- Update to 6.2.25 beta 3.
- Add Requires on optional Crypt::Eksblowfish.

* Mon Mar 05 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.2.b.2
- Update to 6.2.25 beta 2.
- Move static_content to an FHS compliant location.

* Tue Feb 13 2018 Xavier Bachelot <xavier@bachelot.org> 6.2.25-0.1.b.1
- Update to 6.2.25 beta 1.
- Remove useless and bogus directories creation for conf override.
- Own the now properly created css and pictures directories.
  Subsequently the above directory doesn't need to be writable anymore.
- Unbundle Raleway font.
- Simplify sysvinit/systemd in configure.

* Tue Dec 26 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.24-2
- Ensure newaliases works out of the box.

* Thu Dec 21 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.24-1
- Update to 6.2.24.

* Thu Dec 14 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.4.b.3
- Update to 6.2.23 beta 3.

* Tue Dec 12 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.4.b.2
- Unbundle jquery (Fedora only).

* Thu Nov 30 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.3.b.2
- Update to 6.2.23 beta 2.

* Wed Nov 22 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.2.b.1
- Specify all build dependencies. Fixes test suite failure on F25/F26.

* Mon Nov 20 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.23-0.1.b.1
- Update to 6.2.23 beta 1.
- Drop upstream patches.
- Add missing BuildRequires:.
- Remove duplicate Requires:.
- Fix License: to acknowledge for bundled javascript libraries.
- Track more bundled javascript libraries.

* Wed Nov 08 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-4
- Run autoreconf for jquery patch.

* Wed Oct 25 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-3
- Fix scriplet bug in upgrade_data_structure.
- Unbundle font-awesome.

* Fri Oct 20 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-2
- Add patches from upstream sympa-6.2 branch.

* Tue Oct 03 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.22-1
- Update to 6.2.22.

* Thu Sep 14 2017 Xavier Bachelot <xavier@bachelot.org> 6.2.19-0.2.b.2
- Rework spec to better comply with Fedora packaging guidelines.

* Sat Aug 19 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.19b.1-1
- Added --bindir to install sympa_smtpc under libexecdir.

* Sun Jun 25 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.18-1
- Updated.

* Thu Jun 15 2017 IKEDA Soji <ikeda@conversion.co.jp> 6.2.17b.2-1
- Updated README.RPM.md.

* Sun Aug 07 2016 IKEDA Soji <ikeda@conversion.co.jp> 6.2.17-1
- Typos in el6-README.RPM.
- Added a build dependency perl(Test::Harness).
- Added a dependency perl(Unicode::Normalize).
- Added a definition parameter %%{do_autoreconf}.

* Sat Jun 18 2016 IKEDA Soji <ikeda@conversion.co.jp> 6.2.16-1
- Adopted adjustment to Fedora by Xavier Bachelot <xavier@bachelot.org>.
- Avoiding use of buildroot macro in build section.
- Simplified configure option.
- Added patch14 to disable service by default.
- Added unit customization file source129.

* Thu Feb 26 2015 IKEDA Soji <ikeda@conversion.co.jp> 6.2-1
- New minor release sympa-6.2.
