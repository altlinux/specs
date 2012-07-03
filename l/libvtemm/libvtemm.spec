# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# %name or %version is ahead of its definition. Predefining for rpm 4.0 compatibility.
%define name libvtemm
%define version 0.25.0
%global api 1.2
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           libvtemm
Version:        0.25.0
Release:        alt3_3

Summary:        C++ interface for VTE (a GTK2 terminal emulator widget)

Group:          System/Libraries
# library is LGPLv3+, examples are GPLv3+.
License:        LGPLv3+ and GPLv3+
URL:            http://gtkmm.org
Source0:        http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{release_version}/%{name}-%{version}.tar.bz2

BuildRequires:  libglibmm-devel >= 2.22.0
BuildRequires:  libpangomm-devel >= 2.24.0
BuildRequires:  libgtkmm2-devel >= 2.19.2
BuildRequires:  libvte-devel >= 0.26.0
Source44: import.info

%description
libvtemm provides a C++ interface to the VTE library.

%package        devel
Summary:        Headers for developing programs that will use %{name}
Group:          Development/C
Requires:       libvtemm = %{version}-%{release}

%description devel
This package contains the static libraries and header files needed for
developing libvtemm applications.

%package        docs
Summary:        Documentation for %{name}, includes full API docs
Group:          Documentation
Requires:       libgtkmm2-doc

%description    docs
This package contains the full API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING COPYING.lesser NEWS README
%doc old_news_and_changelogs/ChangeLog* old_news_and_changelogs/NEWS*
%{_libdir}/*.so.*

%files devel
# examples
%doc %{_datadir}/%{name}-%{api}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/%{name}-%{api}
%{_libdir}/pkgconfig/*.pc

%files docs
%doc %{_docdir}/%{name}-%{api}
%doc %{_datadir}/devhelp/

%changelog
* Tue Jun 12 2012 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt3_3
- fixed build

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt2_3
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt2_2
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 0.25.0-alt1_2
- initial import by fcimport

