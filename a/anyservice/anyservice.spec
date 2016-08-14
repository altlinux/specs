Name: anyservice
Version: 0.2
Release: alt1

Summary: Anyservice - scripts for making systemd like service from any programs

License: MIT
Group: System/Base
Url: http://wiki.etersoft.ru/Anyservice

Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

BuildArch: noarch
BuildPreReq: rpm-build-compat

%description
Anyservice - scripts for making systemd like service from any programs

%prep
%setup

%build

%install
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/etc/systemd-lite/
mkdir -p %buildroot/var/run/anyservice/
mkdir -p %buildroot/var/log/anyservice/

cp example.service %buildroot/etc/systemd-lite/
cp %name.sh %buildroot/%_bindir/%name

%check
#check that port listening

%pre
%files
%dir /etc/systemd-lite/
%config(noreplace) /etc/systemd-lite/*.service
%attr(755,root,root) %_bindir/%name

%dir /var/run/anyservice/
%dir /var/log/anyservice/

%changelog
* Mon Aug 15 2016 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- anyservice.sh: some refactoring
- anyservice.sh: use .off file if exists
- anyservice.sh: add support for EnviromentFile and Environment fields

* Fri Aug 12 2016 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt4
- build for ALT Linux Sisyphus

* Thu May 12 2016 Danil Mikhailov <danil@altlinux.org> 0.1-alt3
- added example, put into right folder

* Mon Apr 25 2016 Danil Mikhailov <danil@altlinux.org> 0.1-alt2
- building version

* Mon Apr 25 2016 Danil Mikhailov <danil@altlinux.org> 0.1-alt1
- initial package version

