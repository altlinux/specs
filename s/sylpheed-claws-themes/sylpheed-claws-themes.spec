%define		_name		sylpheed
%define		branch		claws
%define		comp		themes
Name:		%_name-%branch-%comp 
Version:	20040929
Release:	alt1

Summary:	Themes for %_name-%branch.
License: 	GPL
Group: 		Networking/Mail	

Url:		http://sylpheed-claws.sourceforge.net/themes.php
BuildArch: 	noarch

Source:		%_name-iconset-%version.tar.gz

PreReq: 	%_name-%branch

%description
Themes for %_name-%branch.

%prep
%setup -q -n %_name-iconset-%version

%build

%install
%__mkdir_p %buildroot%_datadir/%_name-%branch/%comp
%__cp -a * %buildroot%_datadir/%_name-%branch/%comp
%__rm -f %buildroot%_datadir/%_name-%branch/%comp/README

%files
%doc	README
%_datadir/%_name-%branch/%comp/*

%changelog
* Thu Sep 30 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 20040929-alt1
-  new iconset.

* Mon Jul 05 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 20040525-alt2
-  spec changes (PreReq, 10x to vserge).

* Tue Jun 29 2004 Alex Gorbachenko (agent_007) <algor@altlinux.ru> 20040525-alt1
-  initial build.


