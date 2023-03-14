# error in help2man
%def_disable manpages

Name: linstor-client
Summary: Linstor Client
Version: 1.17.0
Release: alt1
Group: Development/Python3
License: GPLv3
URL: https://github.com/LINBIT/linstor-client
Source: http://www.linbit.com/downloads/linstor/linstor-client-%version.tar.gz
BuildArch: noarch
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-linstor >= 1.4.1
%{?_enable_manpages:BuildRequires: help2man xsltproc docbook-style-xsl}

%description
User space client to ease DRBD9 resource management.
Linstor, developed by LINBIT, is a software that manages DRBD replicated LVM/ZFS volumes
across a group of machines. It maintains DRBD configuration on the participating machines.
It creates/deletes the backing LVM/ZFS volumes.
It automatically places the backing LVM/ZFS volumes among the participating machines.

%prep
%setup -n %name-%version

%build
%if_enabled manpages
python3 setup.py build_man
%endif
%python3_build

%install
%python3_install

%files
%doc README.md
%_bindir/*
%python3_sitelibdir/*
%_sysconfdir/bash_completion.d/*
%if_enabled manpages
%_man8dir/*
%endif

%changelog
* Tue Mar 14 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.17.0-alt1
- 1.17.0

* Tue Dec 13 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.16.0-alt1
- 1.16.0

* Mon Oct 31 2022 Andrew A. Vasilyev <andy@altlinux.org> 1.15.1-alt1
- 1.15.1

* Thu Nov 11 2021 Alexey Shabalin <shaba@altlinux.org> 1.10.2-alt1
- 1.10.2

* Sun Nov 15 2020 Alexey Shabalin <shaba@altlinux.org> 1.4.1-alt1
- 1.4.1

* Sat Jun 29 2019 Alexey Shabalin <shaba@altlinux.org> 1.1.2-alt1
- Initial build for ALT
