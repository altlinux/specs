Name: gav-themes
Version: 0.7.3
Release: alt1
Summary: Themes collection for gav
Group: Games/Sports 
License: GPL
Source0: %name-%version.tar.gz
Requires: gav
BuildArch: noarch
%description
Themes collection for GPL Arcade Volleyball game

%prep

%build

%install
%__mkdir -p $RPM_BUILD_ROOT%_gamesdatadir/gav/
tar -zxvf %SOURCE0 -C $RPM_BUILD_ROOT%_gamesdatadir/gav/

%files 
%_gamesdatadir/gav/themes/*


%changelog
* Thu Apr 01 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.7.3-alt1
- first build

