Name: ccd2iso
Version: 0.3
Release: alt1

Summary:  CloneCD image to ISO image file converter
Summary (ru_RU.UTF-8): Программа для преобразования образов CloneCD в ISO
License: GPL
Group: Archiving/Cd burning
Url: http://sourceforge.net/projects/ccd2iso/
Source0: ccd2iso-0.3.tar.gz 

%description
ccd2iso is a tool to convert CloneCD disk images (.ccd) to the ISO format.

%description -l ru_RU.UTF-8
ccd2iso - средство преобразования образов диска CloneCD (.ccd) в формат ISO.

%prep
%setup -q 

%build
%configure
%make

%install
%__install -d -m755 $RPM_BUILD_ROOT%_bindir
%__install -pD -m755 src/ccd2iso $RPM_BUILD_ROOT%_bindir

%files
%_bindir/*
%doc README

%changelog
* Fri Feb 02 2007 Vyacheslav Dikonov <slava@altlinux.ru> 0.3-alt1
- ALTLinux build
