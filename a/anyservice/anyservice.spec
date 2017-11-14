Name: anyservice
Version: 0.8
Release: alt1

Summary: Anyservice - scripts for making systemd like service from any programs

License: MIT
Group: System/Base
Url: http://wiki.etersoft.ru/Anyservice

# Source-git: https://github.com/Etersoft/anyservice.git
Source: %name-%version.tar

Packager: Danil Mikhailov <danil@altlinux.org>

BuildArch: noarch
BuildPreReq: rpm-build-compat

Requires: eepm >= 1.9.7

%description
Anyservice - scripts for making systemd like service from any programs

%prep
%setup

%build

%install
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/etc/%name/
mkdir -p %buildroot/var/run/%name/
mkdir -p %buildroot/var/log/%name/

cp example.service %buildroot/etc/%name/example.service.off
cp %name.sh %buildroot/%_bindir/%name

%check
#check that port listening

%pre
%files
%dir /etc/%name/
%config(noreplace) /etc/%name/*.service.off
%attr(755,root,root) %_bindir/%name

%dir /var/run/%name/
%dir /var/log/%name/

%changelog
* Tue Nov 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.8-alt1
- add support for /etc/systemd/system place for service files

* Tue Oct 24 2017 Vitaly Lipatov <lav@altlinux.ru> 0.7-alt1
- anyservice.sh: fix tabs
- add sleep to fix restart issue (eterbug #11688)

* Thu Oct 13 2016 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- replace $MYMONIT with monit (add monit to requires)

* Fri Sep 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.5-alt1
- implement reload (supports ExecReload too)
- more correct options handling
- add --quiet support for list

* Tue Aug 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt2
- fix EnvironmentFile using

* Tue Aug 23 2016 Vitaly Lipatov <lav@altlinux.ru> 0.4-alt1
- fix logdir and drop obsoleted DEFAULTLOGDIR
- fix Environment, set TMPDIR and HOME

* Tue Aug 16 2016 Vitaly Lipatov <lav@altlinux.ru> 0.3-alt1
- big refactoring
- realize checkd and isautostarted
- add prefix for monit
- put example.service disabled by default
- improve monit status checking
- Caution: use /etc/anyservice as anyservice dir

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

