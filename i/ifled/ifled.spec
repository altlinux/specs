Name:		ifled
Version:	0.6
Release:	alt2
Group:		Monitoring
License:	GPL
Summary:	Keyboard LED interface activity indicator
Summary(ru_RU.KOI8-R): Индикатор активности интерфейсов лампочками клавиатуры
URL:		http://www.sudac.org/~napolium/linux/
Source0:	%name-%version.tar.gz
Source1:	%name.init
Source2:	%name.sysconfig
Source3:	%name.README.ALT

%description
InterfaceLED is a program that uses the keybord LEDs to monitor various
things about a specified interface. For example if a network card is sending
or receiveing data.

%description -l ru_RU.KOI8-R
InterfaceLED --- программа, использующая лампочки клавиатуры для мониторинга
различных событий для указанного интерфейса. Например, приёма или передачи данных.

%prep
%setup -q

%build
%make clean
%make_build

%install
%__mkdir_p %buildroot%_sbindir
install %name %buildroot%_sbindir
%__mkdir_p %buildroot%_initdir/
%__mkdir_p %buildroot%_sysconfdir/sysconfig/
install %SOURCE1 %buildroot%_initdir/%name
install %SOURCE2 %buildroot%_sysconfdir/sysconfig/%name
%__cp %SOURCE3 README.ALT

%post
%post_service %name

%preun
%preun_service %name

%files
%_sbindir/%name
%_initdir/%name
%config(noreplace) %_sysconfdir/sysconfig/%name
%doc ChangeLog README README.ALT

%changelog
* Mon May 31 2004 Denis Ovsienko <pilot@altlinux.ru> 0.6-alt2
- cleaned up initscript and spec
- ifled service is off by default
- README.ALT

* Mon Apr 07 2003 Denis Ovsienko <pilot@altlinux.ru> 0.6-alt1.0
- initial ALTLinux Sisyphus build

