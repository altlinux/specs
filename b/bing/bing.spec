Name: bing
Version: 1.1.3
Release: alt1

Summary: Bing, a point-to-point bandwidth measurement tool (b from Bandwith)
License: BSD
Group: Networking/Other

Url: http://fgouget.free.fr/bing/index-en.shtml
Source: %name-%version.tar.bz2
Patch0: bing.patch
Packager: Michael Shigorin <mike@altlinux.org>

Summary(ru_RU.KOI8-R): Bing - средство измерения производительности сети

# Automatically added by buildreq on Tue Aug 05 2003
BuildRequires: groff-base groff-ps

%description
Bing determines the real (raw, as opposed to available or average)
throughput on a link by measuring ICMP echo requests roundtrip times
for different packet sizes for each end of the link.

%description -l ru_RU.KOI8-R
Bing определяет реальную (а не доступную или среднюю) пропускную способность
канала связи путем измерения времени возвращения эхо-запросов ICMP при
использовании различных размеров пакетов для обоих концов соединения.

%prep
%setup -q
%patch -p0

%build
%make_build

%install
install -pD -m755 bing %buildroot%_bindir/bing
install -pD -m644 unix/bing.8 %buildroot%_man8dir/bing.8

%files
%doc ChangeLog Readme.* bing.ps
%_bindir/bing
%_man8dir/bing*

%changelog
* Fri Nov 17 2006 Michael Shigorin <mike@altlinux.org> 1.1.3-alt1
- added Russian summary charset (was omitted; fixes #5105)
- escaped macro in changelog
- updated Url:

* Mon Aug 25 2003 Egor S. Orlov <oes@altlinux.ru> 1.1.3-alt0.2
- Added russian translation for summary and description

* Tue Aug 05 2003 Egor S. Orlov <oes@altlinux.ru> 1.1.3-alt0.1
- Initial build for ALT
- Added bing.ps to %%doc

