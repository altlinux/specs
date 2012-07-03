Name: phpldapadmin
Version: 1.1.0.6
Release: alt2

Summary: Handle the adminstration of LDAP server over the web
Summary(ru_RU.UTF8): Управление LDAP сервером через web
License: GPL
Group: Networking/WWW
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

Url: http://phpldapadmin.sourceforge.net
Source: http://prdownloads.sourceforge.net/phpldapadmin/%name-%version.tar.gz
Source1: %name-ru.po
Patch1: %name-convert_to_ascii.patch

Requires: mod_php5 php5-ldap

BuildArch: noarch

%define pla_home %_var/www/html/%name

%description
%name -  is a web-based LDAP client. It provides easy, anywhere-accessible,
multi-language administration for your LDAP server. Its hierarchical tree-viewer
and advanced search functionality make it intuitive to browse and administer 
your LDAP directory. Since it is a web application, this LDAP browser works on 
many platforms, making your LDAP server easily manageable from any location. 
%name - is the perfect LDAP browser for the LDAP professional and novice alike.
Its user base consists mostly of LDAP administration professionals.

%description -l ru_RU.UTF8
%name - доступный через сеть клиент LDAP. Он предоставляет простую, доступную, многоязычную 
среду для администрирования вашего сервера LDAP. Его иерархическое дерево просмотра и 
функциональные возможности ускоренного поиска делают его интуитивно понятным, чтобы 
просматривать и управлять вашим каталогом LDAP.
%name - совершенный браузер LDAP для профессионала LDAP и новичков.
Его пользователи состят главным образом из профессионалов в администрировании LDAP.

После установки откорректируйте config.php согласно вашим настройкам.

%prep
%setup -q -n %name-%version
%__cp -f %SOURCE1 locale/ru_RU/LC_MESSAGES/messages.po
%patch1 -p0

%build
# Compile locales by hand.
for f in $(ls locale/*/*/*.po); do
    msgfmt -v -o "$(dirname $f)/messages.mo" "$f"
done

%install
%__mkdir_p %buildroot%pla_home
%__mkdir_p %buildroot%pla_home/config
%__rm INSTALL LICENSE
%__mv config/config.php.example config/config.php
%__cp -aRf index.php %buildroot%pla_home/index.php
%__cp -aRf config/config.php %buildroot%pla_home/config/config.php
%__cp -aRf htdocs %buildroot%pla_home/htdocs
%__cp -aRf lib %buildroot%pla_home/lib
%__cp -aRf locale %buildroot%pla_home/locale
%__cp -aRf templates %buildroot%pla_home/templates
%__cp -aRf tools %buildroot%pla_home/tools
%__ln_s %_defaultdocdir/%name-%version %buildroot%pla_home/doc
%__cat << EOF > %buildroot%pla_home/.htaccess
Options -Indexes
Order Deny,Allow
Deny from all
Allow from localhost
EOF


%files
%pla_home/ 
%doc doc/*
%attr(0640,root,apache) %config(noreplace) %verify(not size mtime md5) %pla_home/config/config.php
%attr(0640,root,apache) %config(noreplace) %pla_home/.htaccess

%changelog
* Sat Sep 24 2011 Alexey Tourbin <at@altlinux.ru> 1.1.0.6-alt2
- removed set_strip_method macro

* Sat Jan 10 2009 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0.6-alt1
- Update to 1.1.0.6
- Update SOURCE1 from http://launchpadlibrarian.net
- Add patch for fix convert to ascii #18450 (thanks erthad@)

* Sat Nov 29 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0.5-alt2
- Add SOURCE1 for fix #18022
- Convert spec to UTF8

* Tue Feb 19 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.1.0.5-alt1
- Update to 1.1.0.5
- Change requires from php to php5

* Mon Jan 16 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.8-alt0
- Update to 0.9.8

* Fri Nov 25 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.7.2-alt0
- Update to 0.9.7.2

* Tue Oct 25 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.7.1-alt1
- Update to 0.9.7.1-rc3

* Fri Jun 03 2005 Slava Dubrovskiy <dubrsl@altlinux.ru> 0.9.6c-alt1
- 0.9.6c
- Some spec cleanup
- Added Russian summary & description

* Fri Jan 23 2004 Michael Shigorin <mike@altlinux.ru> 0.9.3-alt1
- built for ALT Linux
