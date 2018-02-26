%define rname	folderpane
#%set_tbird_ciddir noarch b243fe83-b8a7-47de-855d-21d865243d5d

Name:		%tbird_name-%rname
Version:	0.6.1
Release:	alt2
Summary:	The FolderPane extension for Thunderbird

License:	GPL
Group:		Networking/Mail
URL:		http://www.chuonthis.com/extensions/

Source0:	%rname.xpi

BuildArch:	noarch

BuildRequires(pre):	rpm-build-thunderbird
BuildRequires:		unzip

%description
Allows for customization of the folder pane. 
Accounts can be rearranged and the startup folder can be chosen.

%prep
%setup -c

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir

%files
%ciddir

%changelog
* Sun Feb 26 2012 Alexey Gladkov <legion@altlinux.ru> 0.6.1-alt2
- Rebuilt with thunderbird (10.0.2)

* Sat Aug 06 2011 Alexey Gladkov <legion@altlinux.ru> 0.6.1-alt1
- New version (0.6.1).

* Wed Feb 02 2011 Radik Usupov <radik@altlinux.org> 0.6-alt1
- New version
  + Updated for Thunderbird 3.0 final.
  + Updated install.rdf for Shredder (Thunderbird 3.2a).
  + Refactored the in-line javascript in folderpane.xul into a separate folderpane.js file.
  + Fix for overriding the TB 3.0 folderpane sort algorithm.
  + Patch by Ben Lerner 

* Mon Apr 23 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt5
- Rebuild with new thunderbird (2.0.0.0)

* Wed Mar 14 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt4
- Fix archive packaging bug.

* Sat Mar 10 2007 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt3
- Rebuild with new thunderbird (2.0)

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt2
- Rebuild with new thunderbird (1.5.0.8)

* Mon Aug 21 2006 Alexey Gladkov <legion@altlinux.ru> 0.0.5-alt1
- first build for ALT Linux.
