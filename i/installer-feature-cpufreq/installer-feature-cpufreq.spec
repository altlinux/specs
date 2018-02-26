Name: installer-feature-cpufreq
Version: 0.3
Release: alt1

Summary: Installer hook for cpufreq-simple
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
This package contains installer hook for enabling cpufreq-simple
service.

%package stage3
Summary: Installer stage3 hook or cpufreq-simple
License: GPL
Group: System/Configuration/Other
Requires: cpufreq-simple libshell

%description stage3
This package contains installer stage3 hook for enabling cpufreq-simple
service.

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files stage3
%hookdir/*

%changelog
* Tue Nov 29 2011 Mikhail Efremov <sem@altlinux.org> 0.3-alt1
- Source install2-init-functions.

* Wed Nov 09 2011 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Set 'conservative' as AC off-line governor for non-Intel CPUs.

* Thu Nov 03 2011 Mikhail Efremov <sem@altlinux.org> 0.1-alt1
- Initial build

