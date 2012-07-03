# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: gcc-c++ rpm-macros-fedora-compat
# END SourceDeps(oneline)
%add_optflags %optflags_shared
Name:      liborigin
Version:   20080225
Release:   alt1_6
Summary:   Library for reading OriginLab OPJ project files

License:   GPLv2
Group:     Sciences/Other
URL:       http://sourceforge.net/projects/%{name}/

Source:    http://belnet.dl.sourceforge.net/sourceforge/liborigin/%{name}-%{version}.tar.gz
# Include <cstddef> into tree.hh
Patch0:    %{name}-%{version}-gcc.patch


BuildRequires: ctest cmake
Source44: import.info

%description
A library for reading OriginLab OPJ project files.

%package devel
Summary:  Header files, libraries and development documentation for %{name}
Group:    Development/C
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.

%prep
%setup -q
%patch0 -p1

%build

# fix for hardcoded path of %{_libdir}
%ifarch x86_64 sparc64 ppc64 amd64 s390x
%{__sed} -i "s|install(TARGETS origin DESTINATION lib)|install(TARGETS origin DESTINATION lib64)|" CMakeLists.txt
%endif

%{fedora_cmake}

%{__make} VERBOSE=1 %{?_smp_mflags}

%install
%{__make} INSTALL="install -p" DESTDIR=%{buildroot} install

install -d  %{buildroot}%{_includedir}/%{name}/
install -pm 644 OPJFile.h tree.hh %{buildroot}%{_includedir}/%{name}/

#W: spurious-executable-perm 
chmod 0644 ws4.opj

%files
%doc COPYING README ws4.opj import.qs
%{_bindir}/opj2dat
%{_libdir}/%{name}.so.0*

%files devel
%{_includedir}/%{name}/
%{_libdir}/%{name}.so

%changelog
* Sun Dec 18 2011 Igor Vlasenko <viy@altlinux.ru> 20080225-alt1_6
- initial import by fcimport

* Thu May 08 2008 Yury Aliaev <mutabor@altlinux.ru> 20080225-alt1
- v.20080225
- added man page from Debian

* Thu May 31 2007 Yury Aliaev <mutabor@altlinux.ru> 20070529-alt1
- v.20070529

* Sun May 06 2007 Yury Aliaev <mutabor@altlinux.ru> 20070115-alt2.1
- dummy release due to Sisyphus robots' stupidity and some responsible person
insanity. Actually nothing is changed since previous release.

* Tue Apr 17 2007 Yury Aliaev <mutabor@altlinux.ru> 20070115-alt2
- fixed build for 64 bit architectures

* Fri Feb 16 2007 Yury Aliaev <mutabor@altlinux.ru> 20070115-alt1
- v.20070115

* Wed Jul 19 2006 Yury Aliaev <mutabor@altlinux.ru> 20060616-alt1
- v.20060616

* Sat Jun 10 2006 Yury Aliaev <mutabor@altlinux.ru> 20060607-alt1
- v.20060607

* Sat Jun 3 2006 Yury Aliaev <mutabor@altlinux.ru> 20060529-alt1
- v.20060529

* Mon May 29 2006 Yury Aliaev <mutabor@altlinux.ru> 20060517-alt2
- Ooops! Previous built always leaded to segfaults. Now fixed.

* Wed May 24 2006 Yury Aliaev <mutabor@altlinux.ru> 20060517-alt1
- First build for Sisyphus.
