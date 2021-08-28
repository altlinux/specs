# BEGIN SourceDeps(oneline):
BuildRequires: libXext-devel libfreetype-devel
# END SourceDeps(oneline)
BuildRequires: zlib-devel
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Arches on which the multilib {sysdefs,types}.h hack is needed:
# (Update libast-wrapper.h when adding archs)

%define multilib_arches %{ix86} ia64 ppc ppc64 s390 s390x x86_64
%define cvs 20080502

Summary:        Library of Assorted Spiffy Things
Name:           libast
Version:        0.7.1
Release:        alt5_0.29.%{cvs}cvs
License:        BSD
URL:            http://www.eterm.org/
# Sources are pulled from cvs:
# $ cvs -z3 -d :pserver:anonymous@anoncvs.enlightenment.org:/var/cvs/e \
#      co -d libast-20080502 -D 20080502 eterm/libast
# $ tar czvf libast-20080502.tar.gz libast-20080502
Source:        libast-%{cvs}.tar.gz
Source1:       libast-wrapper.h
BuildRequires: imlib2-devel libpcre-devel libpcrecpp-devel libXt-devel
BuildRequires: automake autoconf libtool
Source44: import.info

%description
LibAST is the Library of Assorted Spiffy Things.  It contains various
handy routines and drop-in substitutes for some good-but-non-portable
functions.  It currently has a built-in memory tracking subsystem as
well as some debugging aids and other similar tools.

It's not documented yet, mostly because it's not finished.  Hence the
version number that begins with 0.

%package devel
Group: Development/Other
Summary:  Header files, libraries and development documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q -n %{name}-%{cvs}

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

# Fix multiarch stuff
%ifarch %{multilib_arches}
for header in sysdefs types ; do
    mv %{buildroot}%{_includedir}/%{name}/$header.h \
       %{buildroot}%{_includedir}/%{name}/$header-%{_arch}.h
    install -m 0644 -c %{SOURCE1} %{buildroot}%{_includedir}/%{name}/$header.h
    sed -i -e 's/<HEADER>/'$header'/g' %{buildroot}%{_includedir}/%{name}/$header.h
    touch -r ChangeLog %{buildroot}%{_includedir}/%{name}/$header.h
done
sed -i -e '/^LDFLAGS=/d' %{buildroot}%{_bindir}/%{name}-config
touch -r ChangeLog %{buildroot}%{_bindir}/%{name}-config
%endif
# alt #28250
%ifarch %{ix86}
mv %buildroot%_includedir/libast/sysdefs-%{_arch}.h %buildroot%_includedir/libast/sysdefs-i386.h
mv %buildroot%_includedir/libast/types-%{_arch}.h %buildroot%_includedir/libast/types-i386.h
%endif




%files
%doc ChangeLog DESIGN README LICENSE
%{_libdir}/%{name}.so.*

%files devel
%dir %{_includedir}/%{name}
%{_bindir}/%{name}-config
%{_libdir}/%{name}.so
%{_includedir}/%{name}.h
%{_includedir}/%{name}/*.h
%{_datadir}/aclocal/%{name}.m4
%exclude %{_libdir}/*.a

%changelog
* Sat Aug 28 2021 Igor Vlasenko <viy@altlinux.org> 0.7.1-alt5_0.29.20080502cvs
- fixed build with LTO

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.21.20080502cvs
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.19.20080502cvs
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.18.20080502cvs
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.17.20080502cvs
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.15.20080502cvs
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.14.20080502cvs
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.13.20080502cvs
- update to new release by fcimport

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt5_0.12.20080502cvs
- fixed types.h

* Fri Dec 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt4_0.12.20080502cvs
- bugfix (closes: #28250)

* Fri Sep 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt3_0.12.20080502cvs
- fixed build

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_0.12.20080502cvs
- update to new release by fcimport

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_0.11.20080502cvs
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_0.10.20080502cvs
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt2_0.9.20080502cvs
- spec cleanup thanks to ldv@

* Mon Dec 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.7.1-alt1_0.9.20080502cvs
- initial import by fcimport

