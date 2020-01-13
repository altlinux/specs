Name: alterator-bro
Version: 0.1.0
Release: alt1

Source: %name-%version.tar

Packager: Paul Wolneykien <manowar@altlinux.org>

Summary: Alterator Backend Request Organ
License: GPLv3+
Group: System/Configuration/Other

BuildPreReq: alterator >= 5.0

Requires: alterator >= 5.1-alt1
Requires: alterator-fbi >= 5.33-alt1
Requires: guile-json

BuildRequires: guile22-devel
BuildRequires: guile-json
BuildRequires: alterator >= 5.0
BuildRequires: alterator-fbi >= 5.33-alt1

%description
If you want to build a brand new UI on the top of the Alterator
platform and JavaScript then alterator-bro is your brother.

%package demo
Summary: Alterator Basic Reflection Organ Demo
Group: System/Configuration/Other
Requires: %name = %version-%release
Requires: nginx

%description demo
The package contains the demo page built with the use of
"bro.js" running under Nginx web server.

%prep
%setup

%build
%make_build

%install
%makeinstall DESTDIR=%buildroot

%files
%_alterator_datadir/design/scripts/bro.js
%_alterator_datadir/ui/bro
%_alterator_libdir/ui/bro

%files demo
%_sysconfdir/nginx/sites-available.d/bro-demo.conf
/var/www/html/bro-demo

%changelog
* Mon Jan 13 2020 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial version.
