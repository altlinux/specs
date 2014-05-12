Name: altquire
Version: 0.1
Release: alt2

Summary: a TUI frontend for dc3dd
License: GPLv2+
Group: File tools

Url: http://altlinux.org/rescue
Source: %name-%version.tar
Packager: Michael Shigorin <mike@altlinux.org>

BuildArch: noarch
Requires: lsblk forensic-scripts

Summary(ru_RU.UTF-8): текстовый интерфейс к dc3dd

%define aqdir %_exec_prefix/libexec/%name

%description
Text-mode frontend for the usual forensic operations.
Please note that this release features Russian strings.

%description -l ru_RU.UTF-8
Текстовый интерфейс для обычных следственных действий,
поддерживает русский язык.

%prep
%setup

%build
sed -i "s,PROGRAMPATH='.',PROGRAMPATH='%aqdir'," %name

%install
install -pDm755 %name %buildroot%_sbindir/%name
mkdir -p %buildroot%aqdir
cp -a *.sh %buildroot%aqdir/

%files
%_sbindir/*
%aqdir

%changelog
* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt2
- made noarch

* Mon May 12 2014 Michael Shigorin <mike@altlinux.org> 0.1-alt1
- initial release of scripts by Maxim Suhanov

