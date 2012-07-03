Name: wgetpaste
Version: 2.18
Release: alt2

Summary: wgetpaste is a special bash-script that simplifies publication of text files at various pastebin services
Summary(ru_RU.UTF-8): wgetpaste - это скрипт, упрощающий публикацию различных текстовых файлов на pastebin-сервисах

License: Public Domain
Group: Networking/WWW
Url: http://wgetpaste.zlin.dk/
BuildArch: noarch

Packager: Anton Chernyshov <ach@altlinux.org>
Source0: %name-%version.tar.bz2
Source1: %name.example
Source2: zlin.conf

Requires: wget bash sed coreutils

# Automatically added by buildreq on Wed Oct 20 2010 (-bi)
BuildRequires: xclip

%description
wgetpaste - simple script, that publics text-file given as argument on a 
pastebin service. When successful, it returns link pointing to web-page with
published file, to terminal.

%description -l ru_RU.UTF-8
wgetpaste - скрипт, публикующий указанный ему в качестве аргумента 
текстовый файл на pastebin сервисе. В случае успеха он возвращает в консоль
ссылку на web-страницу, содержащую опубликованный файл.

%prep
%setup

%install
%__install -D %name %buildroot/%_bindir/%name
%__install -D %{SOURCE1}  %buildroot/%_sysconfdir/%name.conf
%__install -D %{SOURCE2}  %buildroot/%_sysconfdir/%name.d/zlin.conf

%files
%_sysconfdir/*
%_bindir/*
%doc _wgetpaste

%changelog
* Thu Nov 4 2010 2010 Anton Chernyshov <ach@altlinux.org> 2.18-alt2
  + fix package license
  + add runtime dependencies
  + fix changelog according to distrubution rules

* Tue Nov 2 2010 Anton Chernyshov <ach@altlinux.org> 2.18-alt1.1
  + fix spec bug

* Sun Oct 10 2010 Anton Chernyshov <ach@altlinux.org> 2.18-alt1
  + create a spec file, test it according to Sisyphus requirements and 
    initial build
