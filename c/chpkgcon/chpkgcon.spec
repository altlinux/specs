%define _unpackaged_files_terminate_build 1

Name: chpkgcon
Version: 0.1.0
Release: alt1

Summary: A tool to alter SELinux security context of a packaged program
License: %gpl2plus
Group: System/Base
Packager: Paul Wolneykien <manowar@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildArch: noarch

%description
The chpkgcon tool tries to alter the SELinux security context of files
and programs releatd to the given RPM file. In particular, it adjusts
the context of files and directories under %_var, /run and %_sysconfdir
owned by the package. It also overrides SELinuxContext= directive in all
systemd(1) service unit files related to the package.

%prep
%setup

%build
%make_build sbindir=%_sbindir datadir=%_datadir mandir=%_mandir \
	    sysconfdir=%_sysconfdir localstatedir=%_var \
	    runstatedir=/run unitdir=%_unitdir

%install
%makeinstall_std sbindir=%_sbindir datadir=%_datadir mandir=%_mandir \
	         sysconfdir=%_sysconfdir localstatedir=%_var \
		 runstatedir=/run unitdir=%_unitdir

%files
%_sbindir/*
%_man8dir/*.8.*
%config(noreplace) %_sysconfdir/*.conf

%changelog
* Wed Sep 09 2026 Paul Wolneykien <manowar@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus.
