# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
BuildRequires: perl(Config.pm) perl(English.pm) perl(IO/Select.pm) perl(IO/Socket.pm) perl(Time/Local.pm) python-devel
# END SourceDeps(oneline)
Summary: A utility to collect various Linux performance data
Name: collectl
Version: 3.6.5
Release: alt1_1
License: GPLv2+ or Artistic
Group: File tools
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.src.tar.gz
Source1: %{name}.service
Source2: %{name}.sysconfig
URL: http://collectl.sourceforge.net
BuildArch: noarch
Requires: perl(Sys/Syslog.pm) perl(Time/HiRes.pm) perl(Compress/Zlib.pm)
Source44: import.info

%description
A utility to collect Linux performance data


%prep
%setup -q

# rename directory for easier inclusion
mv docs html

# fix EOLs + preserve timestamps
for f in col2tlviz.pl
do
    sed -i.orig 's/\r//g' $f
    touch -r $f.orig $f
done


%build
# nothing to do


%install
# create required directories
mkdir -p        $RPM_BUILD_ROOT%{_unitdir} \
                $RPM_BUILD_ROOT%{_sysconfdir} \
                $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig \
                $RPM_BUILD_ROOT%{_bindir} \
                $RPM_BUILD_ROOT%{_datadir}/%{name}/utils \
                $RPM_BUILD_ROOT%{_mandir}/man1/ \
                $RPM_BUILD_ROOT%{_var}/log/%{name}

# install the files, setting the mode
install -p -m 755  collectl.pl       $RPM_BUILD_ROOT%{_bindir}/collectl
install -p -m 644  *.ph              $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 644  envrules.std      $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 755  col2tlviz.pl      $RPM_BUILD_ROOT%{_datadir}/%{name}/utils
install -p -m 755  client.pl         $RPM_BUILD_ROOT%{_datadir}/%{name}/utils
install -p -m 644  man1/collectl*.1  $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 644  collectl.conf     $RPM_BUILD_ROOT%{_sysconfdir}
install -p -m 644  %{SOURCE1}        $RPM_BUILD_ROOT%{_unitdir}
install -p -m 644  %{SOURCE2}        $RPM_BUILD_ROOT%{_sysconfdir}/sysconfig/%{name}


%files
%doc ARTISTIC COPYING GPL RELEASE-collectl html
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*
%{_var}/log/%{name}/


%changelog
* Wed Nov 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.5-alt1_1
- update to new release by fcimport

* Thu Aug 02 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_2
- update to new release by fcimport

* Wed Jun 20 2012 Igor Vlasenko <viy@altlinux.ru> 3.6.3-alt1_1
- fc import

