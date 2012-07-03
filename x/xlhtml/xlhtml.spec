# -*- coding: utf-8 -*-
Name:        xlhtml
Version: 0.5.1
Release: alt2
Summary: A program that converts MS Excel files to useful formats.
Summary(ru_RU.UTF-8): конвертер MS Excel файлов
License: GPL
Group: Office
Url: http://chicago.sourceforge.net/xlhtml/
Source: %name-%version.tgz
Patch0: xlhtml-textoutput-fix.patch

%description
xlhtml generates HTML, XML, csv and tab-delimited versions of MS Excel
spreadsheets. Known to work with XLS files of MS Excel 95, 97 and 2000.

Also included is ppthtml, a utility for converting MS PowerPoint 95/97
presentations to HTML.

%description -l ru_RU.UTF-8
xlhtml создает HTML, XML, csv и tab-delimited файлы из таблиц MS Excel. 
Работает с MS Excel 95, 97 and 2000.

Также включает ppthtml, утилиту для преобразования презентаций MS PowerPoint 95/97
в HTML.


%prep
%setup

%patch0 -p0

%build
%configure
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"
mv ppthtml/README ppthtml/ppt-README
mv ppthtml/THANKS ppthtml/ppt-THANKS
mv ppthtml/ChangeLog ppthtml/ppt-ChangeLog

%install
%__mkdir -p $RPM_BUILD_ROOT/usr/bin
%__mkdir -p $RPM_BUILD_ROOT/usr/share/man/man1

%__install -s -m 755 xlhtml/xlhtml $RPM_BUILD_ROOT/usr/bin
%__install -s -m 755 ppthtml/ppthtml $RPM_BUILD_ROOT/usr/bin
%__install -m 644 xlhtml/xlhtml.1 $RPM_BUILD_ROOT/usr/share/man/man1
%__install -m 644 ppthtml/ppthtml.1 $RPM_BUILD_ROOT/usr/share/man/man1

%files
%doc AUTHORS COPYING xlhtml/README xlhtml/THANKS xlhtml/TODO xlhtml/ChangeLog ppthtml/ppt-README ppthtml/ppt-THANKS ppthtml/ppt-ChangeLog
/usr/bin/xlhtml
/usr/bin/ppthtml
/usr/share/man/man1/xlhtml.1*
/usr/share/man/man1/ppthtml.1*

%changelog
* Mon Jan 03 2005 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt2
- added URL: tag; buildreq is (none)

* Fri Dec 24 2004 Igor Vlasenko <viy@altlinux.ru> 0.5.1-alt1
- added my bugfix patch; first ALT build

* Wed May 15 2002 Vaclav Dvorak <dvorakv@idas.cz>
- first version of RPM spec file
