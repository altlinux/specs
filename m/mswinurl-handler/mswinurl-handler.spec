Name: mswinurl-handler
Version: 0.01
Release: alt1
Summary: Windows URL file (x-mswinurl) MIME handler
Summary(ru_RU.UTF-8): Обработчик Windows URL файлов (x-mswinurl)
License: GPLv3
Group: Networking/Other
URL: http://www.altlinux.org
Packager: Alexei Mezin <alexvm@altlinux.org>
Vendor: ALT Linux Team

Source: %name-%version.tar.gz

BuildRequires: desktop-file-utils
Requires: filesystem icon-theme-hicolor xdg-utils
BuildArch: noarch

%description
MIME type x-mswinurl (Windows URL files) handler which opens URL with xdg-open

%description -l ru_RU.UTF-8
Обработчик MIME-типа x-mswinurl (файлы Windows URL), который открывает ссылки через xdg-open

%prep
%setup

%build

%install
install -D -m0755 %name.sh  %buildroot/%_bindir/%name.sh
desktop-file-install --dir=%buildroot/%_desktopdir %name.desktop


%check
desktop-file-validate %{buildroot}/%{_desktopdir}/*.desktop

%files
%_bindir/*
%_desktopdir/*

%changelog
* Wed Sep 16 2026 Alexei Mezin <alexvm@altlinux.org> 0.01-alt1
- Initial build

