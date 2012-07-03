%define rname	lightning-ru
%define cid	langpack-ru@lightning.mozilla.org
%define ciddir	%tbird_noarch_extensionsdir/%cid

Name:		thunderbird-%rname
Version:	1.0
Release:	alt2
Serial: 1
Summary:	Russian (RU) Language Pack for Lightning
Packager:	Radik Usupov <radik@altlinux.org>

BuildArch: noarch

License:	GPL
Group:		Networking/Mail
URL:		http://www.mozilla.org/projects/calendar/lightning/

Source0:	lightning-ru-%version.xpi

BuildRequires(pre):	rpm-build-thunderbird 
BuildRequires:		unzip

%description
The Mozilla Lightning in Russian.

%install
%__mkdir_p %buildroot/%ciddir
unzip -qq -d %buildroot/%ciddir %SOURCE0
subst 's/8\.\*\.\*/12.*/' %buildroot/%ciddir/install.rdf

%files
%ciddir

%changelog
* Thu Jun 21 2012 Andrey Cherepanov <cas@altlinux.org> 1:1.0-alt2
- Apapt for new version of Thunderbird

* Mon Feb 20 2012 Radik Usupov <radik@altlinux.org> 1:1.0-alt1
- New version (1.0)
- Drop old folders

* Sat Aug 27 2011 Radik Usupov <radik@altlinux.org> 1.0b5pre-alt2
- Rebuild from new version TB

* Mon Aug 01 2011 Radik Usupov <radik@altlinux.org> 1.0b5pre-alt1
- New version (1.0b5pre)

* Tue Feb 08 2011 Radik Usupov <radik@altlinux.org> 1.0b3pre-alt1
- Initial build (Closes: 24993)

