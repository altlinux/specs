%define base_name apt-conf
%define distro t6
%define Distro t6 branch

Name: %base_name-%distro
Version: 6.0.0
Release: alt1

Summary: A set of apt configuration files for %distribution %Distro
License: GPL
Group: System/Configuration/Packaging

Source: %name-%version.tar.bz2

Provides: %base_name = %version-%release, %_sysconfdir/apt/pkgpriorities
Conflicts: apt <= 0:0.5.15cnc6-alt14, apt-conf-sisyphus
%{expand:%%global o_list apt-conf < 0:4.0 %(for n in Castle Compact Junior Master Spring centaurus desktop hpc junior master office-server platform5 school server terminal; do echo -n "apt-conf-$n "; done)}
%{?o_list:Conflicts: %o_list}

%description
This package contains default apt configuration for %distribution %Distro.

%prep
%setup

%build
%make_build REPOSITORIES="t6"

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
* Mon Jul 16 2012 Motsyo Gennadi <drool@altlinux.ru> 6.0.0-alt1
- create config for t6 branch from apt-conf-branch
