Name:           targetcli
Version:        2.1.fb49
Release:        alt2

Summary:        An administration shell for storage targets

License:        ASL 2.0
Group:          System/Libraries
URL:            https://github.com/open-iscsi/targetcli-fb

Source:         %name-%version.tar

BuildArch:      noarch

Requires: target-restore
Requires: python3-module-%name = %EVR

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools

%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.

%package -n python3-module-%name
Summary:        An administration shell for storage targets
Group:          Development/Python3

%description -n python3-module-%name
An administration shell for storage targets


%prep
%setup

sed -i "s/__version__ = .*/__version__ = '%version'/g" \
	%name/__init__.py

%build
%python3_build_debug
bzip2 --stdout targetcli.8 > targetcli.8.bz2

%install
%python3_install

mkdir -p %buildroot%_man8dir/
install -m 644 targetcli.8.bz2 %buildroot%_man8dir/

%files
%_bindir/targetcli
%doc COPYING README.md
%_man8dir/targetcli.8.*

%files -n python3-module-%name
%python3_sitelibdir/*


%changelog
* Fri Feb 07 2020 Vitaly Lipatov <lav@altlinux.ru> 2.1.fb49-alt2
- use python3 only (drop python2 module)

* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 2.1.fb49-alt1
- 2.1.fb49
- switch to python3

* Sun Jan 31 2016 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb35-alt2
- Man pages packaging fixed

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb35-alt1
- First build for ALT (based on Fedora 2.1.fb35-2.fc21.src)

