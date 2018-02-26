%define build_ver 0.02
%define aspell_ver 0.60
%define src_ver 0.60
Name: aspell-be
Version: %src_ver
Release: alt2

Summary: GNU Aspell Belarusian Word List Package
Summary(be_BY.UTF-8): Слоўнік беларускае мовы для GNU Aspell
Summary(ru_RU.UTF-8): Словарь белорусского языка для GNU Aspell
License: GPL
Group: System/Internationalization
Url: http://aspell.net/

Source: http://mova.linux.by/aspell/aspell6-be-%build_ver.tar.bz2

Requires: aspell >= %aspell_ver
BuildRequires: aspell >= %aspell_ver

%description
GNU Aspell Belarusian Word List Package
%description -l be_BY.UTF-8
Збор слоўнікаў беларускае мовы для GNU Aspell. Пакет утрымлівае
два слоўнікі для праверкі наркамаўскага (be_SU) й новаклясычнага 
(be_BY) правапісаў адпаведна. 
%description -l ru_RU.UTF-8
Словарь белорусского языка для GNU Aspell

%prep
%setup -q -n aspell6-be-%{build_ver}

%build
./configure
%make

%install
%make_install DESTDIR=$RPM_BUILD_ROOT install

%files
%doc README Copyright
%_libdir/aspell/*
%_datadir/*

%changelog
* Mon Jul 19 2004 Vital Khilko <vk@altlinux.ru> 0.60-alt2
- rebuilded for #4441

* Tue May 18 2004 Vital Khilko <vk@altlinux.ru> 0.60-alt1
- new version
- added two dictionaries: be_BY (classic), be_SU (soviet)

* Thu Jan 08 2004 Vital Khilko <vk@altlinux.ru> 0.50.0-alt3
- rebuild with new aspell 0.51.0 

* Mon Oct 20 2003 Vital Khilko <vk@altlinux.ru> 0.50.0-alt2
- fix provides

* Tue Sep 23 2003 Vital Khilko <vk@altlinux.ru> 0.50.0-alt1
- Initial package from Belarusian Language Linux Team
