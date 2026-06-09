Name:     swap_cleaner
Version:  0.1.2
Release:  alt2

Summary:  swap cleaner at shutdown
License:  GPL-2.0-or-later
Group:    Other
URL:      https://altlinux.space/ivkco/ivk-supplement

BuildArch: noarch

Source:   %name-%version.tar

%description
This script clean swap area(s) prior system shutdown or manualy.

%prep
%setup

%build

%install
install -D -m0744 sbin/swap_cleaner %buildroot%_sbindir/swap_cleaner
install -D -m0644 unit/swap_cleaner.service \
        %buildroot%_unitdir/swap_cleaner.service

%files
%doc README.md swap_cleaner.conf.sample
%_unitdir/swap_cleaner.service
%_sbindir/swap_cleaner

%changelog
* Tue Jun 09 2026 Anton Midyukov <antohami@altlinux.org> 0.1.2-alt2
- sbin/swap_cleaner: fix for multiple swap partitions support (Closes: 59483).
- Fix URL.

* Fri May 22 2026 Anton Midyukov <antohami@altlinux.org> 0.1.2-alt1
- Fix bug in case of swapfile (size of file evaluation).

* Mon May 18 2026 Anton Midyukov <antohami@altlinux.org> 0.1.1-alt1
- Initial build.
