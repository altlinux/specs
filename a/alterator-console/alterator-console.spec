Name: 	 alterator-console
Version: 0.1
Release: alt1

Packager: Andrey Cherepanov <cas@altlinux.org>

Summary: Alterator module for emulate console
License: GPL
Group: 	 System/Configuration/Other
Url: 	 http://wiki.sisyphus.ru/Alterator

Source:  %name-%version.tar

BuildArch: noarch

Requires: alterator >= 4.10-alt6
Requires: alterator-sh-functions >= 0.3-alt1
Requires: alterator-l10n >= 2.0-alt1

BuildPreReq: alterator >= 4.10-alt6

%description
Alterator module for emulate console. It allows to run any shell command
and to return result. It also allow to upload file to an server.

%prep
%setup -q

%build
%make_build

%install
%makeinstall

%files
%_alterator_backend3dir/*
%_alterator_datadir/applications/*
%_alterator_datadir/ui/*/*

%changelog
* Fri Dec 20 2013 Andrey Cherepanov <cas@altlinux.org> 0.1-alt1
- Initial release
