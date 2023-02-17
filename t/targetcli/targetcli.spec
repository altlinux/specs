%define _unpackaged_files_terminate_build 1

Name: targetcli
Version: 2.1.54
Release: alt1
Epoch: 1

Summary: An administration shell for storage targets

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/open-iscsi/targetcli-fb

Source: %name-%version.tar

BuildArch: noarch

Requires: target-restore
Requires: python3-module-%name = %EVR

BuildRequires(pre): rpm-build-python3
# build backend and its deps
BuildRequires: python3(setuptools)
BuildRequires: python3(wheel)

%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.

%package -n python3-module-%name
Summary: An administration shell for storage targets
Group: Development/Python3

%description -n python3-module-%name
An administration shell for storage targets

%prep
%setup

sed -i "s/__version__ = .*/__version__ = '%version'/g" \
	%name/__init__.py

%build
%pyproject_build
bzip2 --stdout targetcli.8 > targetcli.8.bz2

%install
%pyproject_install

mkdir -p %buildroot%_man8dir/
install -m 644 targetcli.8.bz2 %buildroot%_man8dir/

# systemd unit
mkdir -p %buildroot%_unitdir/
install -m 644 systemd/* %buildroot%_unitdir/

%files
%_bindir/targetcli
%_bindir/targetclid
%doc COPYING README.md
%_man8dir/targetcli.8.*
%_unitdir/targetclid.*

%files -n python3-module-%name
%python3_sitelibdir/%name/
%python3_sitelibdir/%{pyproject_distinfo targetcli-fb}/

%changelog
* Wed Feb 15 2023 Stanislav Levin <slev@altlinux.org> 1:2.1.54-alt1
- 2.1.fb49 -> 2.1.54.

* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.fb49-alt2
- use python3 only (drop python2 module)

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 2.1.fb49-alt1
- 2.1.fb49
- switch to python3

* Sun Jan 31 2016 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb35-alt2
- Man pages packaging fixed

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb35-alt1
- First build for ALT (based on Fedora 2.1.fb35-2.fc21.src)

