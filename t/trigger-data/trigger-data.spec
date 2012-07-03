Name: trigger-data
Version: 0.5.2
Release: alt2
Summary: Data package for trigger
URL: http://sourceforge.net/projects/trigger-rally/
License: GPL
Group: Games/Sports
Requires: trigger
Packager: Ilya Mashkin <oddity@altlinux.ru>

BuildArch: noarch
Source0: trigger-%version-data.tar.bz2

%description
Data package for trigger

%prep
%setup -q -n trigger-%{version}-data

%build

%install
%__mkdir_p %buildroot%_gamesdatadir/trigger
%__mv events maps plugins sounds textures vehicles %buildroot%_gamesdatadir/trigger/
%__install -D -pm 644 trigger.config.defs %buildroot%_gamesdatadir/trigger/

%files
%_gamesdatadir/trigger

%changelog
* Sun Jan 11 2009 Ilya Mashkin <oddity@altlinux.ru> 0.5.2-alt2
- fix url

* Sat Feb 18 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Thu Mar 31 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.5.1c-alt1
- Initial build.
