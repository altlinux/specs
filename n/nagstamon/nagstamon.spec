# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python rpm-build-python3
BuildRequires: /usr/bin/desktop-file-install python-devel python3-devel
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           nagstamon
Version:        2.0.1
Release:        alt5
Summary:        Nagios status monitor for the desktop
License:        GPLv2
Group:          Monitoring
Url:            http://nagstamon.ifw-dresden.de/
Source:         http://sourceforge.net/projects/nagstamon/files/nagstamon/nagstamon%%200.9.9/Nagstamon-%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-module-PyQt5-devel
BuildRequires:  python3-module-setuptools
BuildRequires:  python3-module-sip
Requires:       python3-module-BeautifulSoup4
Requires:       python3-module-psutil
Requires:	python3-module-sip
Requires:	python3-module-requests
BuildArch:      noarch
Source44: import.info

%description
Nagstamon is a Nagios status monitor which takes place in systray or on desktop
(GNOME, KDE, Windows) as floating statusbar to inform you in realtime about the
status of your Nagios and derivatives monitored network. It allows to connect
to multiple Nagios, Icinga, Opsview, Op5, Check_MK/Multisite and Centreon
servers.

%prep
%setup -q -n Nagstamon

%build
python3 setup.py build

%install
python3 setup.py install \
    --root=%{buildroot} \
    --install-lib=%{python3_sitelibdir_noarch}

#chmod +x %{buildroot}/%{python_sitelibdir_noarch}/Nagstamon/Server/Multisite.py
mv %{buildroot}/%{_bindir}/nagstamon.py %{buildroot}/%{_bindir}/nagstamon
#i18n ru_RU
install -D -m 644 Nagstamon/QUI/all.qm %{buildroot}/%{python3_sitelibdir_noarch}/Nagstamon/translate/ru_RU.qm


# desktop stuff
mkdir -p %{buildroot}%{_datadir}/{applications,pixmaps}
install -m 644 Nagstamon/resources/nagstamon.svg \
    %{buildroot}%{_datadir}/pixmaps/nagstamon.svg
install -m 644 Nagstamon/resources/nagstamon.desktop \
    %{buildroot}/%{_datadir}/applications/nagstamon.desktop

desktop-file-install \
  --dir=%{buildroot}%{_datadir}/applications \
  %{buildroot}/%{_datadir}/applications/nagstamon.desktop

%files
%doc ChangeLog COPYRIGHT LICENSE
%{_datadir}/pixmaps/nagstamon.svg
%{_datadir}/applications/nagstamon.desktop
%{python3_sitelibdir_noarch}/Nagstamon
%{python3_sitelibdir_noarch}/Nagstamon/translate/*.qm
%{_bindir}/nagstamon
%{_mandir}/man1/nagstamon.1*
%{python3_sitelibdir_noarch}/%{name}-%{version}-py%{__python3_version}.egg-info


%changelog
* Wed Mar 01 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt5
- More strings translated

* Thu Feb 02 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt4
- rudimentary translation to Russian

* Tue Jan 31 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt3
- Fixed version of requests

* Tue Jan 31 2017 Denis Medvedev <nbr@altlinux.org> 2.0.1-alt2
- fixed dependencies

* Tue Jan 31 2017 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_1
- converted for ALT Linux by srpmconvert tools

* Fri Sep 30 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_2
- update to new release by fcimport

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_1
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_3
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_2
- update to new release by fcimport

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.11-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_3
- update to new release by fcimport

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.10-alt1_2
- update to new release by fcimport

* Fri Jul 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_9
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1_7
- initial fc import

