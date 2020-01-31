Name:       libpagemap
Version:    0.0.1 
Release:    alt2

Summary:    Pagemap interface library
License:    GPLv3+
Group:      System/Libraries
URL:        https://github.com/pholasek/libpagemap

Source0:    https://github.com/pholasek/%{name}/archive/v%{version}.tar.gz
Source44:   import.info

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3


%description
Package contains library and headers for using kernel pagemap interface

%package devel
Summary: Development files for %{name}
Group: Development/Other
Requires: %{name} = %{version}-%{release}

%description devel
Development files for %{name}.

%prep
%setup -q

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%add_optflags %optflags_shared

cd libpagemap-%{version}
make CFLAGS="%{optflags}"
sed -i 1s,python,python3, pagemapdata.py

%install
cd libpagemap-%{version}
make install DESTDIR=%{buildroot}
install -D -p -m 755 pagemapdata.py $RPM_BUILD_ROOT/%{python3_sitelibdir_noarch}/pagemapdata.py

%files
%{_bindir}/pgmap
%{_libdir}/libpagemap.so.*
%{python3_sitelibdir_noarch}/pagemapdata.py*
%attr(0644,root,root) %{_mandir}/man1/pgmap.1*
%doc libpagemap-%{version}/contrib/
%doc libpagemap-%{version}/README
%doc libpagemap-%{version}/COPYING

%files devel
%{_includedir}/libpagemap.h
%{_libdir}/libpagemap.so


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.0.1-alt2
- Porting on Python3.

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

