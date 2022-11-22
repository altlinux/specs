%filter_from_requires /^python3(_common)/d 
%filter_from_requires /^xfce4-session/d
%filter_from_requires /^\/sbin\/poweroff/d
%filter_from_requires /^\/sbin\/reboot/d

Name:           epoptes
Version:        22.01
Release:        alt1

Summary:        Computer lab management tool
Summary(ru_RU.UTF-8): Инструмент управления компьютерным классом
License:        GPLv3
Group:          Networking/Remote access
Url:            http://www.epoptes.org

# Source0-url: https://github.com/epoptes/%name/archive/refs/tags/v%version.tar.gz
Source0:         %name-%version.tar

Source1:       %name-server.service
Source2:       %name-client.service

BuildRequires: rpm-build-python3
BuildRequires: python3-module-distutils-extra
BuildRequires: intltool

BuildArch:     noarch

Requires: python3-module-pygobject3-pygtkcompat 
Requires: twisted-core-tools
Requires: cert-sh-functions
Requires: python3-module-service_identity
Requires: python3-module-hamcrest

%description
Epoptes is an open source computer lab management and monitoring tool.
It allows for screen broadcasting and monitoring, remote command execution, message sending, imposing restrictions
like screen locking or sound muting the clients and much more!
Visit http://epoptes.org for more information.

%description -l ru_RU.UTF-8
Epoptes - это инструмент управления и мониторинга компьютерных классов с открытым исходным кодом.
Он позволяет транслировать и контролировать экран, удаленно выполнять команды, отправлять сообщения,
накладывать ограничения. Например, блокировку экрана или отключение звука у клиентов и многое другое!
Посетите сайт http://epoptes.org для получения дополнительной информации.

%package client
Summary:       Epoptes client
Summary(ru_RU.UTF-8): Клиент Epoptes
Group:         Networking/Remote access
BuildArch:     noarch

%description client
This is a client part of Epoptes Computer lab management tool

%description -l ru_RU.UTF-8
Клиентская часть инструмента управления компьютерным классом.

%prep
%setup -q -n %name-%version 

sed -i -e 's,/etc/default/epoptes,/etc/epoptes.conf,g' debian/epoptes.postinst
sed -i -e 's,/etc/default/epoptes,/etc/epoptes.conf,g' epoptes/common/config.py
sed -i -e 's,/etc/default/epoptes-client,/etc/epoptes-client.conf,g' epoptes-client/epoptes-client

sed -i -e 's|/etc/default/locale|/etc/locale.conf|g' epoptes-client/epoptes-client

sed -i -e 's,/etc/epoptes/server.key,/var/lib/ssl/private/epoptes.key,g' debian/epoptes.postinst
sed -i -e 's,/etc/epoptes/server.key,/var/lib/ssl/private/epoptes.key,g' debian/epoptes.postrm
sed -i -e 's,/etc/epoptes/server.key,/var/lib/ssl/private/epoptes.key,g' twisted/plugins/epoptesd.py

sed -i -e 's,/etc/epoptes/server.crt,/var/lib/ssl/certs/epoptes.cert,g' debian/epoptes.postinst
sed -i -e 's,/etc/epoptes/server.crt,/var/lib/ssl/certs/epoptes.cert,g' debian/epoptes.postrm
sed -i -e 's,/etc/epoptes/server.crt,/var/lib/ssl/certs/epoptes.cert,g' epoptes/common/config.py
sed -i -e 's,/etc/epoptes/server.crt,/var/lib/ssl/certs/epoptes.cert,g' twisted/plugins/epoptesd.py
sed -i -e 's,/etc/epoptes/server.crt,/var/lib/ssl/certs/epoptes.cert,g' data/040-epoptes-certificate
sed -i -e 's,/etc/epoptes/server.crt,/var/lib/ssl/certs/epoptes.cert,g' epoptes-client/epoptes-client

%build
#nothing to build here

%install
%__python3 setup.py install --root=%buildroot --prefix=%_prefix
%find_lang %name

install -pD -m644 %SOURCE1 %buildroot%_unitdir/%name-server.service
install -pD -m644 %SOURCE2 %buildroot%_unitdir/%name-client.service
rm -f %buildroot/%_docdir/%name/README.md 
install -pD -m644 %_builddir/%name-%version/debian/epoptes.default %buildroot%_sysconfdir/%name.conf
install -pD -m644 %_builddir/%name-%version/debian/epoptes-client.default %buildroot%_sysconfdir/%name-client.conf

%pre
getent group epoptes >/dev/null || groupadd -f -r epoptes

%files -f %name.lang
%doc README.md
%config(noreplace) %_sysconfdir/%name.conf
%_unitdir/%name-server.service
%_bindir/%name
%_datadir/%name/
%_datadir/ltsp/
%python3_sitelibdir_noarch/%name/
%python3_sitelibdir_noarch/twisted/
%python3_sitelibdir_noarch/%{name}-%{version}*.egg-info
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.svg
%_man1dir/*.1*

%files client
%config(noreplace) %_sysconfdir/%name-client.conf
%_sysconfdir/xdg/autostart/%name-client.desktop
%_unitdir/%name-client.service
%_sbindir/%name-client
%_datadir/%name-client/
%_man8dir/*.8*

%changelog
* Tue Nov 22 2022 Evgeniy Kukhtinov <neurofreak@altlinux.org> 22.01-alt1
- Initial build 
