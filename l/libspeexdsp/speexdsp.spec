# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(fftw3f)
# END SourceDeps(oneline)
Group: System/Libraries
%add_optflags %optflags_shared
%define oldname speexdsp
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libspeexdsp
Version:        1.2.1
Release:        alt1_5
Summary:        A voice compression format (DSP)

License:        BSD-3-Clause
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{oldname}-%{version}.tar.gz

BuildRequires:  gcc
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts:      libspeex <= 1.2-0.21.rc1
Source44: import.info
Provides: speexdsp = %{version}-%{release}
Conflicts: libspeex < 1.2-alt0.6

%description
Speex is a patent-free compression format designed especially for
speech. It is specialized for voice communications at low bit-rates in
the 2-45 kbps range. Possible applications include Voice over IP
(VoIP), Internet audio streaming, audio books, and archiving of speech
data (e.g. voice mail).

This is the DSP package, see the speex package for the codec part.

%package devel
Group: Development/Other
Summary: 	Development package for %{oldname}
Requires: 	%{name} = %{version}-%{release}
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts:      libspeex-devel <= 1.2-0.21.rc1
Provides: speexdsp-devel = %{version}-%{release}
Conflicts: libspeex-devel < 1.2-alt0.6

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{oldname}

This is the DSP package, see the speex package for the codec part.


%prep
%setup -n %{oldname}-%{version} -q


%build
%configure \
%ifarch aarch64 %e2k
	--disable-neon \
%endif
	--disable-static

%make_build

%install
%makeinstall_std

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete




%files
%doc --no-dereference COPYING
%doc AUTHORS TODO ChangeLog README NEWS doc/manual.pdf
%doc %{_docdir}/speexdsp/manual.pdf
%{_libdir}/libspeexdsp.so.1*

%files devel
%{_includedir}/speex/
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so

%changelog
* Tue Aug 29 2023 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_5
- update to new release by fcimport

* Tue Aug 02 2022 Igor Vlasenko <viy@altlinux.org> 1.2.1-alt1_2
- update to new release by fcimport

* Tue Jul 27 2021 Igor Vlasenko <viy@altlinux.org> 1.2.0-alt1_3
- e2k support imported

* Tue Jul 27 2021 Michael Shigorin <mike@altlinux.org> 1.2.0-alt1_1.2
- built for sisyphus

* Tue Jul 27 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.2.0-alt1_1.1
- fixed build for Elbrus

* Thu Jun 25 2020 Igor Vlasenko <viy@altlinux.ru> 1.2.0-alt1_1
- update to new release by fcimport

* Tue Jan 08 2019 Michael Shigorin <mike@altlinux.org> 1.2-alt3_0.12.rc3
- disable neon unconditionally, we don't do it on armh either
  (which might be just wrong by now)

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.12.rc3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.10.rc3
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.9.rc3
- update to new release by fcimport

* Sat Nov 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt2_0.7.rc3
- added conflict with old speex

* Mon Nov 09 2015 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1_0.7.rc3
- new version

