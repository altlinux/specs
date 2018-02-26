Name: livecd-hostname
Version: 0.4
Release: alt1

Summary: Try to fetch and setup machine hostname
License: %gpl2only
Group: System/Configuration/Other

Source0: %name-%version.tar

Packager: Andriy Stepanov <stanv@altlinux.ru>

BuildRequires: rpm-build-licenses
BuildArch: noarch
PreReq: service chkconfig

Requires: libshell iproute2

Requires(post): chkconfig
Requires(preun): chkconfig

%description
%summary

%prep
%setup -c

%install
mkdir -p %buildroot%_initdir/
install -pD -m0755 %name-%version/%name %buildroot%_initdir/%name

%post
/sbin/chkconfig --add %name ||:

%preun
if [ $1 = 0 ]; then
    /sbin/chkconfig --del %name
fi

%files 
%_initdir/%name


%changelog
* Mon May 25 2009 Andriy Stepanov <stanv@altlinux.ru> 0.4-alt1
- Rebuild with new Version

* Wed Apr 01 2009 Andriy Stepanov <stanv@altlinux.ru> 0.3-alt1
- Rebuild with new Version

* Tue Mar 31 2009 Andriy Stepanov <stanv@altlinux.ru> 0.2-alt1
- Rebuild with new Version

* Thu Mar 26 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt2
- downgrade boot sequence

* Mon Mar 23 2009 Andriy Stepanov <stanv@altlinux.ru> 0.1-alt1
- first build
