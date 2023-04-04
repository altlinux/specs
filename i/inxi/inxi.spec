Name: inxi
Version: 3.3.26
Release: alt1

Summary: A full featured system information script
Summary(ru): Скрипт вывода полной информации об оборудовании и системе

License: GPL-3.0-or-later
Group: Monitoring
URL: https://smxi.org
# Source-url: https://github.com/smxi/inxi/archive/%version/%name-%version-1.tar.gz
Source: %name-%version.tar.gz

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildArch: noarch

Requires: net-tools
Requires: pciutils
Requires: procps
Requires: lm_sensors
Requires: usbutils
Requires: hddtemp
# Recommends: glxinfo

AutoReq: no

%description
Inxi offers a wide range of built-in options, as well as a good number
of extra features which require having the script recommends installed
on the system.

%description -l ru
Inxi позволяет выводить различную информацию об используемом
оборудовании и о работе системы.

%prep
%setup -q
chmod -x %name.changelog
#Disable update option
sed -i "s/B_ALLOW_UPDATE='true'/B_ALLOW_UPDATE='false'/" inxi

%build

%install
install -p -D -m 755 %name %buildroot/%_bindir/%name
install -p -D -m 644 %name.1 %buildroot/%_man1dir/%name.1

%files
%doc %name.changelog
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Tue Apr 04 2023 Leontiy Volodin <lvol@altlinux.org> 3.3.26-alt1
- New version

* Fri Feb 10 2023 Leontiy Volodin <lvol@altlinux.org> 3.3.25-alt1
- New version

* Mon Dec 12 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.24-alt1
- New version

* Tue Nov 01 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.23-alt1
- New version

* Mon Oct 10 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.22-alt1
- New version

* Thu Aug 25 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.21-alt1
- New version

* Fri Jul 29 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.20-alt1
- New version

* Fri Jun 24 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.19-alt1
- New version

* Mon May 30 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.16-alt1
- New version

* Wed Apr 27 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.15-alt1
- New version (3.3.15)

* Mon Mar 28 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.14-alt1
- New version (3.3.14)

* Thu Feb 24 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.13-alt1
- New version (3.3.13)

* Fri Jan 21 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.12-alt1
- New version (3.3.12)

* Mon Jan 10 2022 Leontiy Volodin <lvol@altlinux.org> 3.3.11-alt1
- New version (3.3.11)

* Wed Dec 01 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.09-alt1
- New version (3.3.09)

* Wed Nov 03 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.08-alt1
- New version (3.3.08)

* Sun Oct 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.07-alt1
- New version (3.3.07)

* Tue Aug 17 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.06-alt1
- New version (3.3.06)

* Mon Apr 19 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.04-alt1
- New version (3.3.04)

* Tue Mar 23 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.03-alt1
- New version (3.3.03)

* Tue Feb 09 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.01-alt1
- New version (3.3.01)

* Wed Feb 03 2021 Leontiy Volodin <lvol@altlinux.org> 3.3.00-alt1
- New version (3.3.00)

* Tue Jan 19 2021 Leontiy Volodin <lvol@altlinux.org> 3.2.02.2-alt1
- New version (3.2.02.2)

* Wed Jan 13 2021 Leontiy Volodin <lvol@altlinux.org> 3.2.02-alt1
- New version (3.2.02)

* Sat Dec 19 2020 Leontiy Volodin <lvol@altlinux.org> 3.2.01-alt1
- New version (3.2.01)

* Wed Dec 16 2020 Leontiy Volodin <lvol@altlinux.org> 3.2.00-alt1
- New version (3.2.00)

* Mon Nov 16 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.09-alt1
- New version (3.1.09)

* Mon Oct 19 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.08-alt1
- New version (3.1.08)

* Fri Oct 02 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.07-alt1
- New version (3.1.07)

* Mon Aug 17 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.06-alt1
- New version (3.1.06)

* Mon Jul 27 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.05-alt1
- New version (3.1.05)

* Wed Jul 01 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.04-alt2
- Remove glxinfo from requires

* Tue Jun 30 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.04-alt1
- New version (3.1.04)
- Add glxinfo for graphics info

* Tue Jun 16 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.03-alt1
- New version (3.1.03)

* Thu Jun 04 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.01-alt1
- New version (3.1.01)

* Sat May 09 2020 Leontiy Volodin <lvol@altlinux.org> 3.1.00-alt1
- New version (3.1.00)

* Mon Apr 13 2020 Leontiy Volodin <lvol@altlinux.org> 3.0.38-alt1
- New version (3.0.38)

* Wed Nov 20 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.37-alt1
- New version (3.0.37)

* Thu Aug 15 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.36-alt1
- New version (3.0.36)

* Tue Jul 16 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.35-alt1
- New version (3.0.35)

* Mon May 06 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.34-alt1
- New version (3.0.34)

* Mon Apr 01 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.33-alt1
- New version (3.0.33)

* Tue Feb 12 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.32-alt1
- New version (3.0.32)

* Thu Feb 07 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.31-alt1
- New version (3.0.31)

* Wed Jan 09 2019 Leontiy Volodin <lvol@altlinux.org> 3.0.30-alt1
- New version

* Tue Dec 18 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.29-alt1
- New version

* Fri Dec 07 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.28-alt1
- New version

* Mon Oct 29 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.27-alt1
- New version
- Change project URL

* Wed Oct 03 2018 Leontiy Volodin <lvol@altlinux.org> 3.0.26-alt1
- New version

* Tue Dec 13 2016 Mikhail Kolchin <mvk@altlinux.org> 2.3.5-alt1
- New version

* Fri Sep 16 2016 Mikhail Kolchin <mvk@altlinux.org> 2.3.1-alt1
- New version

* Wed Apr 27 2016 Mikhail Kolchin <mvk@altlinux.org> 2.3.0-alt1
- New version

* Tue Feb 09 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.33-alt1
- New version

* Sun Jan 17 2016 Andrey Cherepanov <cas@altlinux.org> 2.2.32-alt1
- New version

* Tue Nov 24 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.31-alt1
- New version

* Sun Aug 30 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.28-alt1
- New version
- Build from upstream Git repository
- Change project URL

* Thu Jun 25 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.25-alt1.r2604
- New version

* Sat May 23 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.21-alt2
- New version

* Mon Apr 27 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.19-alt2
- Disable autoreq to prevent excess requirements

* Sun Apr 26 2015 Andrey Cherepanov <cas@altlinux.org> 2.2.19-alt1
- Initial build for Sisyphus (thanks Fedora team for the spec)
