Name:		autoswap
Version:	0.10
Release:	alt1

License:	GPLv3
Group:		System/Configuration/Hardware
BuildArch:	noarch
Source:		%version/%name-%version.tar
Summary:	Automatically search and connect swap partitions
Summary(ru_RU.UTF-8): Автоматичекий поиск и подключение swap разделов

%description
Automatically search and connect swap partitions

%description -l ru_RU.UTF8
 Автоматичекий поиск и подключение swap разделов

%prep
%setup
%__subst s\\'$version'\\"%version"\\ %name.service

%install
install -Dm 755 %name         %buildroot%_bindir/%name
install -Dm 755 %name.init    %buildroot%_initdir/%name
install -pDm 644 %name.service %buildroot%_unitdir/%name.service

%files
%_unitdir/%name.service
%_initdir/%name
%_bindir/%name

%changelog
* Sun Mar 16 2025 Hihin Ruslan <ruslandh@altlinux.ru> 0.10-alt1
- Init build to Sisyphus


