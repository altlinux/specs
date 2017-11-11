%define _altdata_dir	%_datadir/alterator 

Name:			alterator-pve
Version:		0.1
Release:		alt4

ExclusiveArch:		x86_64

Source:			%name-%version.tar

Summary:		Alterator module fo PVE Cluster
License:		GPL
Group:			System/Configuration/Other

BuildRequires(pre): 	alterator
Requires:		alterator
Requires:		alterator-sh-functions
Requires:		pve-cluster
Requires:		pve-manager
Requires:		libshell
Requires:		/usr/bin/ssh-keygen

%description
%summary

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_altdata_dir/applications/*
%_altdata_dir/ui/*/
%_alterator_backend3dir/*

%changelog
* Fri Nov 10 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt4
- fix local ip resolving checking

* Tue Nov 07 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt3
- start cluster without manual network settings

* Thu Mar 02 2017 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt2
- fix: added missing runtime dependency.

* Mon Nov 21 2016 Vladimir D. Seleznev <vseleznv@altlinux.org> 0.1-alt1
- Initial release

