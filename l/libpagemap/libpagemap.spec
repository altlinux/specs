# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:           libpagemap
Version:        0.0.1 
Release:        alt1_14
Summary:        Pagemap interface library

Group:          System/Libraries
License:        GPLv3+
URL:            https://fedorahosted.org/libpagemap/
Source0:        https://fedorahosted.org/released/libpagemap/%{name}-%{version}.tar.gz
BuildRequires:  python-devel
Source44: import.info

%description
Package contains library and headers for using kernel pagemap interface

%package        devel
Summary:        Development files for %{name}
Group:          Development/C
Requires:       %{name} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%setup -q

%build
make CFLAGS="%{optflags} -std=c99" %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
install -D -p -m 755 pagemapdata.py $RPM_BUILD_ROOT/%{python_sitelibdir_noarch}/pagemapdata.py

%files
%{_bindir}/pgmap
%{_libdir}/libpagemap.so.*
%{python_sitelibdir_noarch}/pagemapdata.py*
%attr(0644,root,root) %{_mandir}/man1/pgmap.1*
%doc contrib/
%doc README
%doc COPYING

%files devel
%{_includedir}/libpagemap.h
%{_libdir}/libpagemap.so

%changelog
* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_14
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_13
- update to new release by fcimport

* Thu Apr 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.0.1-alt1_12
- initial fc import

