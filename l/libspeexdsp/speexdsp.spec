# BEGIN SourceDeps(oneline):
BuildRequires: pkgconfig(fftw3f)
# END SourceDeps(oneline)
%add_optflags %optflags_shared
%define oldname speexdsp
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libspeexdsp
Version:        1.2
%global rc_ver  rc3
Release:        alt3_0.12.%{rc_ver}
Summary:        A voice compression format (DSP)

Group:          System/Libraries
License:        BSD
URL:            http://www.speex.org/
Source0:        http://downloads.xiph.org/releases/speex/%{oldname}-%{version}%{rc_ver}.tar.gz
# a patch to speex (774c87d) was done usptream to fix this issue but it seems it
# hasn't been replicated in speexdsp. Issue seen in at least pjproject
# upstream ML thread http://lists.xiph.org/pipermail/speex-dev/2014-May/008488.html
Patch0:         speexdsp-fixbuilds-774c87d.patch

BuildRequires: libtool-common autoconf-common automake-common
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts: libspeex <= 1.2-0.21.rc1
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
Summary: 	Development package for %{oldname}
Group: 		Development/Other
Requires: 	%{name} = %{version}-%{release}
# speexdsp was split from speex in 1.2rc2. As speexdsp does not depend on
# speex, a versioned conflict is required.
Conflicts: libspeex-devel <= 1.2-0.21.rc1
Provides: speexdsp-devel = %{version}-%{release}
Conflicts: libspeex-devel < 1.2-alt0.6

%description devel
Speex is a patent-free compression format designed especially for
speech. This package contains development files for %{oldname}

This is the DSP package, see the speex package for the codec part.


%prep
%setup -q -n %{oldname}-%{version}%{rc_ver}
%patch0 -p1 -b .inc

%build
autoreconf -vif
%configure \
	--disable-neon \
	--disable-static

%make_build V=1

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete

%files
%doc AUTHORS COPYING TODO ChangeLog README NEWS doc/manual.pdf
%doc %{_docdir}/speexdsp/manual.pdf
%{_libdir}/libspeexdsp.so.*

%files devel
%{_includedir}/speex
%{_libdir}/pkgconfig/speexdsp.pc
%{_libdir}/libspeexdsp.so

%changelog
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

