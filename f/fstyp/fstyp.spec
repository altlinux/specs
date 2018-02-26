Name: fstyp
Version: 0.1
Release: alt7

Summary: filesystem type identifier
Summary(ru_RU.KOI8-R): автоопределение типа файловой системы

License: GPL
Group: System/Kernel and hardware

Url: http://mkp.net/fstyp/
Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: %name-%version.tar

Patch1: %name-file.patch

%description
A Linux version of the fstyp command found in most commercial
Unices.  fstyp can be used to heuristically detect which
filesystem type a block device contains.

%description -l ru_RU.KOI8-R
Linux-версия команды fstyp, имеющейся во многих коммерческих
UNIX-системах. fstyp может эвристическими методами определить
тип файловой системы, находящейся на блочном устройстве.

%prep
%setup -q
%patch1 -p1

%build
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*
%_man8dir/*
%doc AUTHORS ChangeLog COPYING

%changelog
* Sun Oct 24 2010 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt7
- rebuild

* Wed Nov 19 2008 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt6
- cleanup spec

* Thu May 27 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt5
- russian manpage moved to man-pages-ru

* Wed Mar 10 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt4
- libdb4.0 req deleted

* Mon Jan 05 2004 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt3
- russian manpage installing

* Thu Nov 06 2003 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt2
- russian manpage added

* Tue Oct 21 2003 Denis Smirnov <mithraen@altlinux.ru> 0.1-alt1
- package created
