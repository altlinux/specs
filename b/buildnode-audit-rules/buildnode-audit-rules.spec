%define _unpackaged_files_terminate_build 1

Name: 	  buildnode-audit-rules
Version:  0.1.1
Release:  alt1

Summary:  Manage audit rules for logging package build processes
License:  GPLv3
Group:    Monitoring
Url: 	  http://git.altlinux.org/people/nbr/packages/buildnode-audit-rules.git

Source:   %name-%version.tar

BuildArch: noarch
BuildRequires: libaudit-devel bats /proc help2man

%description
Contains system startup scripts that manage special auditd(8) rules
to monitor package build processes. The scripts construct the
necessary rules based on the system architecture and given
configuration files, inserting them into the kernel using
auditctl(8). The resulting configuration is then verified.

%prep
%setup

%build
%make_build

%install
%makeinstall_std sbindir=%_sbindir \
		 sysconfdir=%_sysconfdir \
		 unitdir=%_unitdir \
		 initdir=%_initdir \
		 man1dir=%_man1dir

%check
%make_build check DEBUG=1

%files
%config(noreplace) %_sysconfdir/audit/%name.conf
%_sbindir/%name
%_unitdir/%name.service
%_initdir/%name
%_man1dir/%name.1.*

%changelog
* Thu Jan 19 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.1-alt1
- Fixed error in case when the audit rule list is empty.
- Strongly require auditd.service.
- Added SysV-init script.

* Wed Jan 18 2023 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
