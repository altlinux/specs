Name: bing
Version: 1.3.5
Release: alt1

Summary: Bing, a point-to-point bandwidth measurement tool (b from Bandwith)
Summary(ru_RU.UTF-8): Bing - средство измерения производительности сети
Group: Networking/Other
# from bing.8 by nomossa
License: BSD-4-Clause-UC
Url: http://fgouget.free.fr/bing/index-en.shtml

Packager: Michael Shigorin <mike@altlinux.org>

Source: http://fgouget.free.fr/%name/%{name}_src-%version.tar.gz

# Automatically added by buildreq on Tue Aug 05 2003
BuildRequires: groff-base groff-ps

%description
Bing determines the real (raw, as opposed to available or average)
throughput on a link by measuring ICMP echo requests roundtrip times
for different packet sizes for each end of the link.

%description -l ru_RU.UTF-8
Bing определяет реальную (а не доступную или среднюю) пропускную способность
канала связи путем измерения времени возвращения эхо-запросов ICMP при
использовании различных размеров пакетов для обоих концов соединения.

%prep
%setup

%build
%make_build "COPTIM=$RPM_OPT_FLAGS"

%install
install -pD -m755 %name %buildroot%_bindir/%name
install -pD -m644 unix/%name.8 %buildroot%_man8dir/%name.8

%files
%doc ChangeLog Readme.* bing.ps
%_bindir/%name
%_man8dir/%name.8.*

%changelog
* Sat Apr 16 2022 Yuri N. Sedunov <aris@altlinux.org> 1.3.5-alt1
- 1.3.5
- spec converted to UTF-8
- fixed License tag

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.1.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Fri Nov 17 2006 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- added Russian summary charset (was omitted; fixes #5105)
- escaped macro in changelog
- updated Url:

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 1.1.3-alt0.2
- Added russian translation for summary and description

* Tue Aug 05 2003 Egor S. Orlov <oes@altlinux.ru> 1.1.3-alt0.1
- Initial build for ALT
- Added bing.ps to %%doc

