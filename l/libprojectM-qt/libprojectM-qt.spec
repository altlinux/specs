# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:		libprojectM-qt
Version:	2.0.1
Release:	alt2_5
Summary:	The Qt frontend to the projectM visualization plugin
Group:		Sound
License:	GPLv2+
URL:		http://projectm.sourceforge.net/
Source0:	http://downloads.sourceforge.net/projectm/%{name}-%{version}.tar.bz2
BuildRequires:	ctest cmake qt4-devel libprojectM-devel = %{version}
Source44: import.info

%description
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.

%package	devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	libprojectM-qt = %{version}-%{release}

%description	devel
projectM-qt is a GUI designed to enhance the projectM user and preset writer
experience.  It provides a way to browse, search, rate presets and setup
preset playlists for projectM-jack and projectM-pulseaudio.
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%{fedora_cmake} -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir} .
make %{?_smp_mflags} VERBOSE=1


%install
make install DESTDIR=$RPM_BUILD_ROOT


%files
%{_libdir}/*.so.*
%{_datadir}/pixmaps/prjm16-transparent.svg

%files devel
%doc ReadMe
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed May 09 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_5
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_4
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt2_3
- spec cleanup thanks to ldv@

* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 2.0.1-alt1_3
- initial import by fcimport

