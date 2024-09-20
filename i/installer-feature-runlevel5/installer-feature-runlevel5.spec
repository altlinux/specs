Name: installer-feature-runlevel5
Version: 0.2
Release: alt1

Summary: Provide a system with graphical boot
License: GPL-2.0-or-later
Group: System/Configuration/Other

Source: %name-%version.tar

BuildArch: noarch

%description
%summary.

%package stage2
Summary: Provide a system with graphical boot
Group: System/Configuration/Other

%description stage2
%summary.

%prep
%setup -q

%install
%makeinstall

%files stage2
%_datadir/install2/postinstall.d/*

%changelog
* Fri Sep 20 2024 Anton Midyukov <antohami@altlinux.org> 0.2-alt1
- 90-runlevel5.sh: adapt to modern conditions
- cleanup spec

* Thu Sep 18 2008 Vladislav Zavjalov <slazav@altlinux.org> 0.1-alt2
- remove Requires: portmap > 1:4.0-alt2

* Wed Apr 23 2008 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
