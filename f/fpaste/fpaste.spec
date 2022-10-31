Name: fpaste
Version: 0.4.3.0
Release: alt1
Summary: A simple tool for pasting info onto the Fedora community paste server
License: GPL-3.0+
Group: Networking/WWW
URL: https://pagure.io/fpaste

Source0: https://pagure.io/fpaste/archive/%{version}/fpaste-%{version}.tar.gz

BuildArch:  noarch

BuildRequires: rpm-build-python3

%description
It is often useful to be able to easily paste text to the Fedora Pastebin at
http://paste.fedoraproject.org and this simple script will do that and return
the resulting URL so that people may examine the output. This can hopefully
help folks who are for some reason stuck without X, working remotely, or any
other reason they may be unable to paste something into the pastebin.  This is
not a general client for paste servers. It will only ever support the paste
server that the Fedora community is running.

%prep
%setup

%install
mkdir -p %buildroot%_bindir
make install BINDIR=%buildroot%_bindir MANDIR=%buildroot%_mandir

%files
%doc README.rst TODO
%_bindir/%name
%_man1dir/%name.1*

%changelog
* Mon Oct 31 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.3.0-alt1
- New version.

* Fri Jan 14 2022 Andrey Cherepanov <cas@altlinux.org> 0.4.2.0-alt2
- Initial build for Sisyphus.

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.4.2.0-alt1_2
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.4.2.0-alt1_1
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.4.1.1-alt2_2
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.4.1.1-alt2_1
- update to new release by fcimport

* Sun Nov 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.1.1-alt1_1
- update to new release by fcimport

* Thu Oct 01 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.1.0-alt1_1
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.0.1-alt1_3
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.4.0.1-alt1_2
- update to new release by fcimport

* Tue Oct 29 2019 Igor Vlasenko <viy@altlinux.ru> 0.4.0.1-alt1_1
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.9.2-alt1_3
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.3.9.2-alt1_2
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.9.2-alt1_1
- update to new release by fcimport

* Sat Jun 23 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.9.1-alt2_3
- rebuild

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.3.9.1-alt1_3
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.9.1-alt1_1
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.3.8.3-alt1_3
- update to new release by fcimport

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.8.3-alt1_1
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.3.8.1-alt1_2
- update to new release by fcimport

* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.8.1-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.3.8.0-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.7.3.3-alt1_1
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.7.3.1-alt1_1
- update to new release by fcimport

* Wed May 14 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.7.2-alt1_1
- update to new release by fcimport

* Fri Feb 21 2014 Igor Vlasenko <viy@altlinux.ru> 0.3.7.1-alt1_11
- update to new release by fcimport

* Thu Aug 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.7.1-alt1_9
- update to new release by fcimport

* Fri Apr 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.7.1-alt1_8
- update to new release by fcimport

* Fri Mar 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.7.1-alt1_6
- update to new release by fcimport

* Fri Feb 08 2013 Igor Vlasenko <viy@altlinux.ru> 0.3.7.1-alt1_5
- update to new release by fcimport

* Mon Dec 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.3.7.1-alt1_4
- initial fc import

