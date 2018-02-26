# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(check)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Summary: A pipeline manipulation library
Name: libpipeline
Version: 1.2.0
Release: alt3_2
License: GPLv3+
Group: Development/C
URL: http://libpipeline.nongnu.org/
Source0: http://download.savannah.gnu.org/releases/libpipeline/%{name}-%{version}.tar.gz
BuildRequires: libtool
Provides: bundled(gnulib)
Source44: import.info

%description
libpipeline is a C library for setting up and running pipelines of
processes, without needing to involve shell command-line parsing which is
often error-prone and insecure.  This alleviates programmers of the need to
laboriously construct pipelines using lower-level primitives such as fork(2)
and execve(2).

%package devel
Summary: Header files and libraries for pipeline manipulation library
Group: Development/C
Requires: libpipeline = %{version}-%{release}

%description devel
libpipeline-devel contains the header files and libraries needed
to develop programs that use libpipeline library.

%prep
%setup -q

%build
./configure --libdir=%{_libdir}
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix} \
             INSTALL='install -p'
rm $RPM_BUILD_ROOT/%{_libdir}/libpipeline.la

%files
%doc COPYING README ChangeLog NEWS
%{_libdir}/libpipeline.so.*

%files devel
%{_libdir}/libpipeline.so
%{_includedir}/*.h
%{_mandir}/man3/*
%{_libdir}/pkgconfig/libpipeline.pc

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt3_2
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_2
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt2_1
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- initial import by fcimport

