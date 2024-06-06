%define _unpackaged_files_terminate_build 1
%define oname icinga2_usersyncd

Name: icinga2-usersyncd
Version: 0.1.0
Release: alt1

Group: Monitoring
Summary: A daemon to synchronize ApiUser entries with Host agents on an Icinga 2 instance
Url: http://git.altlinux.org/people/manowar/packages/icinga2-usersyncd.git
License: GPLv2+

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(setuptools) python3(wheel) python3(pytest)

Requires: python3-module-%name = %version-%release

%description
A daemon to synchronize ApiUser entries with Host agents on an
Icinga 2 instance.

%package -n python3-module-%name
Group: Development/Python3
Summary: Python module for a daemon to synchronize ApiUser entries with Host agents on an Icinga 2 instance
# For a proper events.subscribe():
Requires: python3-module-icinga2apic >= 0.7.5-alt3

%description -n python3-module-%name
Python module for a daemon to synchronize ApiUser entries with Host
agents on an Icinga 2 instance.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

mkdir -p %buildroot%_sysconfdir/icinga2/conf.d
mv -v %buildroot%python3_sitelibdir_noarch/%oname/%name.conf \
      %buildroot%_sysconfdir/icinga2/conf.d/%name.conf

mkdir -p %buildroot%_sysconfdir/sysconfig
mv -v %buildroot%python3_sitelibdir_noarch/%oname/%name.sysconfig \
      %buildroot%_sysconfdir/sysconfig/%name

mkdir -p %buildroot%_man1dir
mv -v %buildroot%python3_sitelibdir_noarch/%oname/%name.1 \
      %buildroot%_man1dir/%name.1

mkdir -p %buildroot%_unitdir
mv -v %buildroot%python3_sitelibdir_noarch/%oname/%name.service \
      %buildroot%_unitdir/%name.service

#check
#pyproject_run_pytest

%files
%_bindir/%name
%config(noreplace) %_sysconfdir/icinga2/conf.d/%name.conf
%config(noreplace) %_sysconfdir/sysconfig/%name
%_man1dir/%name.1.*
%_unitdir/%name.service

%files -n python3-module-%name
%python3_sitelibdir_noarch/%oname
%python3_sitelibdir_noarch/%oname-%version.dist-info

%changelog
* Sat Mar 30 2024 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
