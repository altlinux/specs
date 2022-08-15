Name: installer-feature-slideshow
Version: 0.2
Release: alt2

Summary: Prepare slideshow
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

Obsoletes: installer-feature-rm-slideshow < %version
Provides: installer-feature-rm-slideshow = %version-%release

%description
Setup proper localized slideshow or
turn off slideshow in small memory conditions.

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Aug 15 2022 Anton Midyukov <antohami@altlinux.org> 0.2-alt2
- NMU: replace 'egrep' with 'grep -E'

* Mon May 20 2013 Mikhail Efremov <sem@altlinux.org> 0.2-alt1
- Setup proper localized slideshow.
- Rename to installer-feature-slideshow.
- Use slideshow.conf if exists.

* Thu Jul 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build

