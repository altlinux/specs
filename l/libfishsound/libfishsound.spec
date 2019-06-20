# BEGIN SourceDeps(oneline):
#BuildRequires: /usr/bin/valgrind
# END SourceDeps(oneline)
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           libfishsound
Version:        1.0.0
Release:        alt4_14.1
Summary:        Simple programming interface for Xiph.Org codecs

Group:          System/Libraries
License:        BSD
URL:            http://www.xiph.org/fishsound/
Source0:        http://downloads.xiph.org/releases/libfishsound/libfishsound-%{version}.tar.gz

# also pulled in by speex-devel
BuildRequires:  libflac++-devel libflac-devel
BuildRequires:  libspeex-devel libvorbis-devel liboggz-devel libsndfile-devel
BuildRequires:  doxygen
Source44: import.info

%description
libfishsound provides a simple programming interface for decoding and
encoding audio data using Xiph.Org codecs (FLAC, Speex and Vorbis).

libfishsound by itself is designed to handle raw codec streams from a
lower level layer such as UDP datagrams. When these codecs are used in
files, they are commonly encapsulated in Ogg to produce Ogg FLAC, Speex
and Ogg Vorbis files.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}
Requires:       pkg-config

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation
# note: intentionally not noarch; contains a target-specific Makefile
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch

%description    doc
The %{name}-doc package contains the documentation for %{name}.

%package        tools
Summary:        Sample programs bundled with %{name}
Group:          Sound
Requires:       %{name} = %{version}-%{release}

%description    tools
The %{name}-tools package contains sample programs that use %{name}.
The source code for these are included in %{name}-doc.


%prep
%setup -q
# These dependencies should not be exported
# http://github.com/kfish/libfishsound/issues/#issue/1
sed -i '/^Requires:.*/d' fishsound.pc.in


%build
%configure --disable-static
# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build


%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# overriding docdir does not work
mv $RPM_BUILD_ROOT%{_datadir}/doc/%{name} \
   other-docs
# remove Latex docs, they do not provide hyperlinks and
# thus are less usable than the HTML docs
rm -rf other-docs/latex

# move the examples we want
mkdir -p $RPM_BUILD_ROOT%{_bindir}
(cd src/examples/ && \
  mv .libs/* $RPM_BUILD_ROOT%{_bindir} &&
  make clean && rm -rf .deps .libs Makefile.*)
mv src/examples .


%files
%doc AUTHORS COPYING README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/fishsound.pc

%files doc
%doc examples other-docs/*

%files tools
%{_bindir}/*


%changelog
* Thu Jun 20 2019 Michael Shigorin <mike@altlinux.org> 1.0.0-alt4_14.1
- E2K: avoid valgrind

* Wed Nov 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt4_14
- set doc to noarch

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_12
- update to new release by fcimport

* Mon Feb 15 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_10
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_9
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_8
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_7
- update to new release by fcimport

* Mon Apr 22 2013 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.0-alt3_6.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * arch-dep-package-consists-of-usr-share for libfishsound-doc

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_6
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt3_5.1
- applied repocop patches

* Sun Sep 09 2012 Fr. Br. George <george@altlinux.ru> 1.0.0-alt2_5.1
- Rebuild with liboggz 1.1.1

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_5
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_4
- update to new release by fcimport

* Fri Dec 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt2_3
- spec cleanup thanks to ldv@

* Sat Dec 17 2011 Igor Vlasenko <viy@altlinux.ru> 1.0.0-alt1_3
- initial import by fcimport

