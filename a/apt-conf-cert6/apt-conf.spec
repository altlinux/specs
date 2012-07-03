%define base_name apt-conf
%define distro cert6
%define Distro Certified 6

Name: %base_name-%distro
Version: 6.0
Release: alt1

Summary: A set of apt configuration files for %distribution %Distro
License: GPL
Group: System/Configuration/Packaging
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>

Source: %name-%version.tar

Provides: %base_name = %version-%release, %_sysconfdir/apt/pkgpriorities
PreReq: coreutils
Conflicts: apt <= 0:0.5.15cnc6-alt14
%{expand:%%global o_list apt-conf < 0:4.0 %(for n in Castle Compact Junior Master Spring branch desktop hpc junior master office-server school server sisyphus terminal platform5 mithraen etersoft; do echo -n "apt-conf-$n "; done)}
%{?o_list:Conflicts: %o_list}

%description
This package contains default apt configuration for %distribution %Distro.

%prep
%setup

%build
%make_build REPOSITORIES='cert6'

%install
%makeinstall

%triggerpostun -- apt < 0.3.19cnc51-alt3 %{?o_list:%o_list}
f=%_sysconfdir/apt/sources.list
if [ ! -f "$f" ]; then
	if [ -f "$f".rpmsave ]; then
		cp -pf "$f".rpmsave "$f"
	elif [ -f "$f".rpmnew ]; then
		cp -pf "$f".rpmnew "$f"
	fi
fi

%files
%config(noreplace) %_sysconfdir/apt

%changelog
* Wed Oct 20 2010 Vitaly Kuznetsov <vitty@altlinux.ru> 6.0-alt1
- cert6
