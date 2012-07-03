# Spec file for rootsh utility

Name: rootsh
 
Version: 1.5.3
Release: alt1
    
Summary: a logging wrapper for shells

License: %gpl3plus
Group: Shells
URL: http://sourceforge.net/projects/rootsh/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar

Source1: %name.sh
Source2: %name.csh
Source3: %name.sysconfig
Source4: %name.cron
Source5: README.ALT.utf8

Patch0:  %name-1.5.3-create_file_perms.patch

BuildRequires(pre): rpm-build-licenses
AutoReqProv: yes

%define rootsh_group _%name
%define logs_dir     %_var/log/%name
%define conf_file    %_sysconfdir/sysconfig/%name

%description
Rootsh is a wrapper for shells that logs all echoed keystrokes
and terminal output to a file and/or to syslog.
 
It's main purpose is the auditing of users who need a shell with
root privileges. They start rootsh through the sudo mechanism. 

%prep
%setup
%patch0

/bin/mv -f -- COPYING COPYING.orig
/bin/ln -s -- $(relative %_licensedir/GPL-3 %_docdir/%name/COPYING) COPYING

# Fix typo in program version:
%__subst 's#1.5.2#1.5.3#g' configure

%build
%configure
%make_build

%install
%makeinstall

mkdir -p -- %buildroot%_sysconfdir/{profile.d,bashrc.d,sysconfig,cron.daily}
install -m 0755 -- %SOURCE1 %buildroot%_sysconfdir/bashrc.d/%name.sh
install -m 0755 -- %SOURCE2 %buildroot%_sysconfdir/profile.d/%name.csh
install -m 0644 -- %SOURCE3 %buildroot%conf_file
install -m 0755 -- %SOURCE4 %buildroot%_sysconfdir/cron.daily/%name

cp %SOURCE5 README.ALT.utf8

%__subst 's#@@conf_file@@#%{conf_file}#g;s#@@logs_dir@@#%{logs_dir}#g' \
	%buildroot%_sysconfdir/bashrc.d/%name.sh \
	%buildroot%_sysconfdir/profile.d/%name.csh \
	%buildroot%conf_file \
	%buildroot%_sysconfdir/cron.daily/%name

mkdir -p -- %buildroot%logs_dir

%pre
# Add the "_rootsh" user
%_sbindir/groupadd -r -f %rootsh_group 2>/dev/null ||:

%files
%doc AUTHORS README THANKS ChangeLog
%doc README.ALT.utf8
%doc --no-dereference COPYING

%attr(0710,root,%rootsh_group) %_bindir/%name
%attr(01730,root,%rootsh_group) %dir %logs_dir

%_sysconfdir/bashrc.d/%name.sh
%_sysconfdir/profile.d/%name.csh
%_sysconfdir/cron.daily/%name
%conf_file

%_man1dir/%name.*

%changelog
* Wed Mar 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.3-alt1
- Initial build for ALT Linux Sisyphus

* Sun Mar 08 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.5.3-alt0.1
- Initial build

