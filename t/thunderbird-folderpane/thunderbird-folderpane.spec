%define rname	folderpane
#%set_tbird_ciddir noarch b243fe83-b8a7-47de-855d-21d865243d5d

Name:		%tbird_name-%rname
Version:	0.6.1
Release:	alt5
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
subst 's/maxVersion>11\.0a1/maxVersion>45.*/g' install.rdf
subst 's/maxVersion>2\.5a1/maxVersion>2.40.*/g' install.rdf

%install
%__mkdir_p %buildroot/%ciddir
%__cp -r * %buildroot/%ciddir

%files
%ciddir

%changelog
* Thu Apr 14 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt5
- Adapt for Thunderbird 45.x and Seamonkey 2.40.x

* Tue Nov 05 2013 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt4
- Adapt for Thunderbird 24.x and Seamonkey 2.22.x

* Thu Dec 20 2012 Andrey Cherepanov <cas@altlinux.org> 0.6.1-alt3
- Adapt for Thunderbird 17.0

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
