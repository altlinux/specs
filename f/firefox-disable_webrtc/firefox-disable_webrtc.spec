# SPEC file for the Firefox Disable WebRTC extension

%define rname	disable_webrtc
%define cid	jid1-5Fs7iTLscUaZBgwr@jetpack

Name:		%firefox_name-%rname
Version:	1.0.23
Release:	alt1

Summary:	Firefox Disable WebRTC extension
Summary(ru_RU.UTF-8):	расширение Disable WebRTC для Firefox

License:	%mpl
Group:		Networking/WWW
URL:		https://addons.mozilla.org/ru/firefox/addon/happy-bonobo-disable-webrtc/
#URL:		https://github.com/ChrisAntaki/disable-webrtc-firefox
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.org>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
Disable WebRTC Firefox extension allows to easily disable WebRTC.
It provides an addon's icon to quickly toggle WebRTC on and off,
if WebRTC is required for a video conference for example.

WebRTC allows websites to get actual IP address from behind VPNs.
This addon fixes that issue and makes VPN usage more effective
by changing browser-wide settings in Firefox.

%description -l ru_RU.UTF-8
Расширение «Disable WebRTC» для Firefox позволяет отключить
поддержку WebRTC в браузере и предоставляет кнопку на панели
инструментов для быстрого включения/выключения WebRTC на случай,
когда WebRTC требуется для приложений типа видеоконференций.

Использование WebRTC даёт возможность сайтам получить реальный
адрес IP пользователя, в т.ч. при работе через VPN. Отключение
поддержки WebRTC в настройках Firefox позволяет избежать этой
утечки информации.

# No %%prep or %%build sections are needed

%install
install -pD -m 644 %SOURCE0 %buildroot%firefox_noarch_extensionsdir/%{cid}.xpi

%files
%firefox_noarch_extensionsdir/%{cid}.xpi

%changelog
* Mon Nov 27 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.0.23-alt1
- Initial build for ALT Linux Sisyphus
