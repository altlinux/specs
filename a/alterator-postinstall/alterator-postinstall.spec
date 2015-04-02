
Name:    alterator-postinstall
Version: 0.1
Release: alt3

Source:  %name-%version.tar

Summary: alterator module for postinstall script installer
License: GPL
Group:   System/Configuration/Other
URL:     https://github.com/sergelogvinov/alterator-postinstall.git

BuildArch: noarch
Requires: alterator >= 4.17-alt1
Requires: curl

BuildPreReq: alterator >= 4.17-alt1

%description
alterator module for postinstall script installer

%prep
%setup

%build
%make_build

%install
%makeinstall
mkdir -p %buildroot%_sysconfdir/firsttime.d
touch %buildroot%_sysconfdir/firsttime.d/99-z-auto_postinstall_script.sh
touch %buildroot%_sysconfdir/firsttime.d/99-zz-auto_postinstall_run.sh
mkdir -p %buildroot%_datadir/install2/postinstall.d
touch %buildroot%_datadir/install2/postinstall.d/99-z-auto_postinstall_script.sh
touch %buildroot%_datadir/install2/postinstall.d/99-zz-auto_postinstall_run.sh

%files
%_datadir/alterator/ui/*/
%_alterator_backend3dir/*
# generated scripts should be removed on package uninstall
%ghost %_sysconfdir/firsttime.d/99-z-auto_postinstall_script.sh
%ghost %_sysconfdir/firsttime.d/99-zz-auto_postinstall_run.sh
%ghost %_datadir/install2/postinstall.d/99-z-auto_postinstall_script.sh
%ghost %_datadir/install2/postinstall.d/99-zz-auto_postinstall_run.sh

%changelog
* Thu Apr 02 2015 Andrey Cherepanov <cas@altlinux.org> 0.1-alt3
- Rewrite backend to simplify usage
- Remove generated scripts on package uninstall

* Thu Mar 26 2015 Andrey Cherepanov <cas@altlinux.org> 0.1-alt2
- Spec cleanup, add project URL

* Thu Sep 05 2013 Logvinov Sergey <serge.logvinov@gmail.com> 0.1-alt1
- Initial release

