Name: mosobrtv
Summary: View Moscow educational television
Summary(ru_RU.UTF-8): Просмотр Московского образовательного ТВ
Group: Education
License: MIT
Version: 1
Release: alt1
Url: https://git.osmesh.ru/MOS/mosobrtv
Source0: %{name}-%{version}.tar
BuildArch: noarch

Requires: %{_bindir}/xdg-open

%description
View Moscow educational television

%description -l ru_RU.UTF-8
Просмотр Московского образовательного ТВ

%files
%{_datadir}/applications/mosobrtv.desktop
%dir %{_datadir}/mosobrtv
%{_datadir}/mosobrtv/mosobrtv.m3u8
%{_datadir}/icons/hicolor/scalable/apps/mosobrtv.svg

#----------------------------------------------------------------

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/applications
install -m0644 mosobrtv.desktop %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/mosobrtv
install -m0644 mosobrtv.m3u8 %{buildroot}%{_datadir}/mosobrtv
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -m0644 mosobrtv.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps

%changelog
* Thu Sep 01 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 1-alt1
- Initial build

