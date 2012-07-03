Name: livecd-encfs
Version: 1.0
Release: alt3

Summary: Mount volumes with encrypted user home directories
License: GPL
Group: System/Configuration/Other

Packager: Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1

Source0: %name.tar

BuildArch: noarch
PreReq: service chkconfig

%description
Mount volumes with encrypted user home directories and add corresponding
paths to the /etc/security/pam_encfs.conf

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 %name/%name %buildroot%_initdir/%name

%files 
%_initdir/%name

%changelog
* Wed Sep 22 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt3
- Add chkconfig support.

* Tue Sep 22 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt2
- Mount filesystems in the asynchronous mode by default.

* Sun Sep 21 2009 Paul Wolneykien <manowar@altlinux.ru> 1.0-alt1
- Initial build for ALT Linux
