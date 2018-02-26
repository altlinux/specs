Name: datefudge
Version: 1.12 
Release: alt2 

Summary: This program implements a cheap way to fake a Linux program into believing that the clock is set to Something Else.
Summary (ru_RU.UTF-8): Программа реализующая простой способ заставить Linux-программу получать отличающиеся от реальных системное время и дату.  
License: GPLv2
Group: Development/Other
Url: http://ftp.debian.org/debian/pool/main/d/datefudge 
Source: datefudge_1.12.tar.bz2
Patch: datefudge_1.12.patch.bz2

%description
I use this program to find corner cases like "will this program behave
itself on a leap day" or "does this code handle expiry of an SSL
certificate correctly". Manually setting the system clock isn't an
option in many cases, especially on multiuser systems.

This program is not a complete solution. It is not meant to be.
Specifically, it does not touch the times in *stat() results. As a
consequence, programs like "make" will be confused.

%description -l ru_RU.UTF-8
Эта программа предназначена для тестирования случаев изменения поведения программы в
заданный момент времени. Она позволит получить ответ на вопросы подобные:  
"Как будет вести себя приложение в определенный день?" или "Правильно ли обрабатывается
ситуация устаревания SSL сертификатов?". Во многих случаях ручной перевод часов невозможен,
особенно на многопользовательских системах.

Это не полное решение задачи. время, сообщаемое функцией *stat() не изменяется.
Поэтому подобные make программы могут вести себя странно.

%prep 
%setup 
%patch -p1

%build 
%make

%install
%makeinstall DESTDIR=$RPM_BUILD_ROOT

%files 
%doc README COPYING
%_mandir/man1/datefudge.1*
%_bindir/datefudge
%_libdir/datefudge.so

%changelog
* Mon Jul 05 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.12-alt2
- Spec fixed

* Wed Apr 14 2004 Vyacheslav Dikonov <slava@altlinux.ru> 1.12-alt1
- ALTLinux build
