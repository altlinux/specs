Name: ldapexplorertool2
Version: 2.0.1
Release: alt2.svn89

Summary: LDAP Explorer Tool
License: BSD
Group: Databases
Url: http://ldaptool.sf.net

Source0: %name-%version.tar

BuildRequires: gcc-c++ libldap-devel libwxGTK-devel

%description
LDAP Explorer is a multi platform, graphical LDAP tool that enables you to browse, modify and manage LDAP servers

%prep
%setup

%build
%make

%install
mkdir -p %buildroot/%_bindir
%make DESTDIR=%buildroot install

%files
%doc let_userguide.*
%_bindir/%name
%_datadir/%name

%changelog
* Thu Dec 24 2015 Andrey Cherepanov <cas@altlinux.org> 2.0.1-alt2.svn89
- Rebuild with new wx

* Tue Feb 26 2013 Eugene Prokopiev <enp@altlinux.ru> 2.0.1-alt1.svn89
- first build for Sisyphus


