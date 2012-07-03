# Spec file for pcal utility

Name: pcal

Version: 4.11.0
Release: alt1
    
Summary: PostScript calendar generation program
Summary(ru_RU.UTF-8): программа для создания календарей в формате PostScript

License: %artistic_license
Group: Text tools
URL: http://pcal.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2

AutoReqProv:   yes
BuildRequires: rpm-build-licenses

%description
Pcal is a calendar-generation program which produce nice-looking
PostScript output.

Pcal  is usually used to generate monthly-format  (one month per
page) calendars  with optional embedded text and  images to mark
special events (e.g. holidays, birthdays, etc). It can also
generate yearly-format (one year per page) calendars.

%description -l ru_RU.UTF-8
Pcal - программа для создания календарей в готовом для печати
виде в формате PostScript.

Pcal  обычно используется для создания календарей на месяц, с
опциональными вставками текста и картинок  для отметки особых
событий (праздников,  дней рождения и т.п.).  Также она может
использоваться для создания календарей на весь год.

%prep
%setup

%build
%make_build

%install
mkdir -p -- %buildroot%_bindir
mkdir -p -- %buildroot%_man1dir
install -m0755 -- exec/pcal %buildroot%_bindir
install doc/pcal.man %buildroot%_man1dir/%name.1


%files
%doc doc/ReadMe.txt html scripts examples
%_bindir/%name
%_man1dir/%{name}*

%changelog
* Sat Feb 23 2008 Nikolay A. Fetisov <naf@altlinux.ru> 4.11.0-alt1
- Initial build for ALT Linux Sisyphus

* Mon Feb 18 2008 Nikolay A. Fetisov <naf@altlinux.ru> 4.11.0-alt0.1
- Initial build

