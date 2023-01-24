Name: python3-module-hass-frontend
Version: 20230110.0
Release: alt1

Summary: Home automation platform -- frontend
License: Apache-2.0
Group: System/Servers
Url: https://www.home-assistant.io/

Source0: hass-frontend-%version.tar

BuildArch: noarch
BuildRequires: rpm-build-python3 python3-module-setuptools

%description
Home Assistant is a home automation platform running on Python 3.
It is able to track and control all devices at home and offer a platform
for automating control.
This package contains frontend part of Home Assistant.

%install
mkdir -p %buildroot%python3_sitelibdir/
tar xf %SOURCE0 -C %buildroot%python3_sitelibdir/

%files
%python3_sitelibdir/hass_frontend
%python3_sitelibdir/home_assistant_frontend-*-info

%changelog
* Mon Jan 23 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 20230110.0-alt1
- 20230110.0

* Wed Nov 09 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20221108.0-alt1
- 20221108.0

* Wed Sep 14 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20220907.2-alt1
- 20220907.2

* Wed Jul 20 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20220707.1-alt1
- 20220707.1

* Fri Jul 15 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20220706.0-alt1
- 20220706.0

* Tue May 17 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20220504.1-alt1
- 20220504.1

* Tue Mar 29 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20220301.2-alt1
- 20220301.2

* Thu Feb 10 2022 Sergey Bolshakov <sbolshakov@altlinux.ru> 20220203.0-alt1
- 20220203.0

* Tue Oct 12 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20211007.1-alt1
- 20211007.1

* Thu Oct 07 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20211006.0-alt1
- 20211006.0

* Fri Aug 06 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210804.0-alt1
- 20210804.0

* Mon Jun 21 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210603.0-alt1
- 20210603.0

* Tue Apr 13 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210407.3-alt1
- 20210407.3

* Fri Apr 09 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210407.2-alt1
- 20210407.2

* Tue Mar 16 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210302.6-alt1
- 20210302.6

* Fri Feb 19 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20210127.7-alt1
- 20210127.7

* Fri Jan 29 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201229.1-alt1
- 20201229.1

* Mon Nov 23 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201111.2-alt1
- 20201111.2

* Mon Nov 02 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201021.4-alt1
- 20201021.4

* Fri Oct 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20201001.2-alt1
- 20201001.2

* Wed Sep 30 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200918.2-alt1
- 20200918.2

* Tue Sep 22 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200918.0-alt1
- 20200918.0

* Tue Aug 18 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200811.0-alt1
- 20200811.0

* Tue Jul 21 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200702.1-alt1
- 20200702.1

* Tue Jul 07 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200702.0-alt1
- 20200702.0

* Wed Mar 04 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200220.5-alt1
- 20200220.5

* Wed Feb 12 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200130.2-alt1
- 20200130.2

* Mon Jan 20 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200108.2-alt1
- 20200108.2

* Thu Jan 16 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20200108.0-alt1
- 20200108.0

* Tue Jan 14 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 20191204.1-alt1
- initial
