# Spec file for lcal utility

Name: lcal

Version: 2.1.0
Release: alt1
    
Summary: PostScript lunar calendar generation program
Summary(ru_RU.UTF-8): программа для создания календарей фаз Луны в формате PostScript

License: %artistic_license
Group: Text tools
URL: http://pcal.sourceforge.net/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2

AutoReqProv:   yes
BuildRequires: rpm-build-licenses

%description
Lcal  is a program which  generates full-year PostScript lunar
(moon phase) calendars in a 2-page format, a compressed 1-page
format, or an ''odd-days-only'' 1-page format.

%description -l ru_RU.UTF-8
Lcal - программа для создания годовых календарей фаз Луны в 
готовом для печати виде в формате PostScript.

%prep
%setup

%build
%make_build

%install
mkdir -p -- %buildroot%_bindir
mkdir -p -- %buildroot%_man1dir
install -m0755 -- lcal %buildroot%_bindir
install lcal.man %buildroot%_man1dir/%name.1


%files
%doc ReadMe.txt
%_bindir/%name
%_man1dir/%{name}*

%changelog
* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.0-alt1
- Initial build for ALT Linux Sisyphus

* Tue Feb 26 2008 Nikolay A. Fetisov <naf@altlinux.ru> 2.1.0-alt0.1
- Initial build

