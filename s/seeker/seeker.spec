# TODO: if built as PIE, fails with "read: Bad address"
#global _hardened_build 1

Name:           seeker
Version:        3.0
Release:        alt2
Summary:        Random access disk benchmark utility

Group:          File tools
License:        GPLv2 and CC-BY-SA
URL:            http://www.linuxinsight.com/how_fast_is_your_disk.html
# http://www.linuxinsight.com/how_fast_is_your_disk.html#comment-1583
Source0:        http://smp.if.uj.edu.pl/~baryluk/seeker_baryluk.c
# http://www.linuxinsight.com/how_fast_is_your_disk.html?page=1#comment-971
Source1:        %{name}.LICENSE
# Grabbed with firefox, modified, ran through tidy(1) per CC BY-SA 2.5:
# http://www.linuxinsight.com/about.html
Source2:        %{name}-docs.tar.gz
# https://bugzilla.redhat.com/623667
Patch0:         %{name}-3.0-timeout-blockalign-623667.patch
Source44: import.info

%description
Seeker is a simple utility that reads small pieces of data from a raw
disk device in a random access pattern, and reports the average number
of seeks per second, and calculated random access time of the disk.
The seeker variant included in this package is the multithreaded one
by Witold Baryluk.


%prep
%setup -q -c -T -a 2
install -pm 644 %{SOURCE0} $(basename %{SOURCE0}) # for debuginfo, Patch0
%patch0
cp -p %{SOURCE1} LICENSE


%build
%{__cc} -D_GNU_SOURCE $RPM_OPT_FLAGS $RPM_LD_FLAGS -pthread \
    $(basename %{SOURCE0}) -o seeker


%install
install -Dpm 755 seeker $RPM_BUILD_ROOT%{_sbindir}/seeker


%files
%doc LICENSE how_fast_is_your_disk*
%{_sbindir}/seeker


%changelog
* Tue Feb 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 3.0-alt2
- Build to Sisiphus

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_11
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_10
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_9
- update to new release by fcimport

* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 3.0-alt1_8
- initial fc import

