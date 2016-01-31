Name:           targetcli
License:        ASL 2.0
Group:          System/Libraries
Summary:        An administration shell for storage targets
Version:        2.1.fb35
Release:        alt2
URL:            https://fedorahosted.org/targetcli-fb/
Source:         %{name}-%{version}.tar
BuildArch:      noarch
BuildRequires:  python-devel python-module-setuptools
Requires:       python-module-rtslib >= 2.1.fb41, python-module-configshell, python-module-ethtool


%description
An administration shell for configuring iSCSI, FCoE, and other
SCSI targets, using the TCM/LIO kernel target subsystem. FCoE
users will also need to install and use fcoe-utils.


%prep
%setup

%build
%python_build
bzip2 --stdout targetcli.8 > targetcli.8.bz2

%install
%python_install
mkdir -p %{buildroot}%{_sysconfdir}/target/backup
mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 targetcli.8.bz2 %{buildroot}%{_mandir}/man8/

%files
%{python_sitelibdir}/*
%{_bindir}/targetcli
%dir %{_sysconfdir}/target
%dir %{_sysconfdir}/target/backup
%doc COPYING README.md
%{_mandir}/man8/targetcli.8.*

%changelog
* Sun Jan 31 2016 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb35-alt2
- Man pages packaging fixed

* Thu Jul 31 2014 Lenar Shakirov <snejok@altlinux.ru> 2.1.fb35-alt1
- First build for ALT (based on Fedora 2.1.fb35-2.fc21.src)

