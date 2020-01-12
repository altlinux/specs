# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libpagemap
Version:        0.0.1 
Release:        alt1_26
Summary:        Pagemap interface library

Group:          System/Libraries
License:        GPLv3+
URL:            https://github.com/pholasek/libpagemap
Source0:        https://github.com/pholasek/%{name}/archive/v%{version}.tar.gz
BuildRequires:  python-devel
Source44: import.info

%description
Package contains library and headers for using kernel pagemap interface

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%setup -q

%build
cd libpagemap-%{version}
make CFLAGS="%{optflags}"
sed -i 1s,python,python2, pagemapdata.py

%install
cd libpagemap-%{version}
make install DESTDIR=%{buildroot}
install -D -p -m 755 pagemapdata.py $RPM_BUILD_ROOT/%{python_sitelibdir_noarch}/pagemapdata.py

%files
%{_bindir}/pgmap
%{_libdir}/libpagemap.so.*
%{python_sitelibdir_noarch}/pagemapdata.py*
%attr(0644,root,root) %{_mandir}/man1/pgmap.1*
%doc libpagemap-%{version}/contrib/
%doc libpagemap-%{version}/README
%doc libpagemap-%{version}/COPYING

%files devel
%{_includedir}/libpagemap.h
%{_libdir}/libpagemap.so

%changelog
* Sun Jan 12 2020 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_26
- fixed build

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_25
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_22
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_20
- update to new release by fcimport

* Wed Sep 21 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_19
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_18
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_15
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_13
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_12
- initial fc import

