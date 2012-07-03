Name: callweaver-sounds
Version: 0.1
Release: alt3

Summary: Sounds for CallWeaver IP PBX 
License: Creative Commons License
Group: System/Servers
Url: http://callweaver.org/
Packager: Eugene Prokopiev <enp@altlinux.ru>

Source0: %name-%version.tar

Requires: callweaver

BuildArch: noarch

%description
Sounds for CallWeaver IP PBX recorded by Melanie Taylor http://www.artistryvo.com/.
Funding for these sounds was provided by Nate Smith.

%prep

%build

%install
tar -xf %SOURCE0
mkdir -p  %buildroot/%_datadir/callweaver/sounds/en
cp -a %name-%version/* %buildroot/%_datadir/callweaver/sounds/en/
mkdir -p %buildroot/%_docdir/%name-%version
mv %buildroot/%_datadir/callweaver/sounds/en/README  %buildroot/%_docdir/%name-%version/

%files
%dir %doc %_docdir/%name-%version
%doc %_docdir/%name-%version/*
%dir %_datadir/callweaver/sounds
%_datadir/callweaver/sounds/*
%dir %_docdir/callweaver-sounds-%version 

%changelog
* Fri May 22 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt3
- apply repocop patch to own docdir subdirectory

* Fri Feb 06 2009 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt2
- fix repocop warning

* Mon Apr 14 2008 Eugene Prokopiev <enp@altlinux.ru> 0.1-alt1
- initial build for Sisyphus

