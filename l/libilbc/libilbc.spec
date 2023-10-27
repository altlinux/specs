# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define major 2
%define libname libilbc%{major}
%define libnamedev libilbc-devel

Summary:	Internet Low Bitrate Codec (iLBC) library
Name:		libilbc
Epoch:		1
Version:	2.0.2
Release:	alt1_8.2
License:	BSD-style
Group:		System/Libraries
URL:		https://github.com/TimothyGu/libilbc
Source0:	https://github.com/TimothyGu/libilbc/releases/download/v%{version}/libilbc-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
Source44: import.info
Patch33: libilbc-2.0.2-added-mipseb-and-ppc64le.patch

%description
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%package -n	%{libname}
Summary:	Internet Low Bitrate Codec (iLBC) library
Group:          System/Libraries

%description -n	%{libname}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%package -n %{libnamedev}
Summary:	Development and header files for the iLBC library
Group:		Development/C
Requires:	%{libname} = %{epoch}:%{version}-%{release}
#Provides:	ilbc-devel = %{epoch}:%{version}-%{release}
#Provides:	%{name}-devel = %{epoch}:%{version}-%{release}
#Conflicts:	libilbc2-devel < 1.0.0

%description -n %{libnamedev}
iLBC (internet Low Bitrate Codec) is a FREE speech codec suitable for robust
voice communication over IP. The codec is designed for narrow band speech and
results in a payload bit rate of 13.33 kbit/s with an encoding frame length of
30 ms and 15.20 kbps with an encoding length of 20 ms. The iLBC codec enables
graceful speech quality degradation in the case of lost frames, which occurs in
connection with lost or delayed IP packets.

%prep

%setup -q -n libilbc-%{version}
%ifarch %e2k
sed -i "s/__aarch64__/__e2k__/" typedefs.h
%else
%patch33 -p1
%endif

%build
autoreconf -fi
%configure \
    --disable-static
%make_build

%install
%makeinstall_std

# symlinks for compatibility
ln -s ilbc.h %{buildroot}%{_includedir}/iLBC_decode.h
ln -s ilbc.h %{buildroot}%{_includedir}/iLBC_define.h
ln -s ilbc.h %{buildroot}%{_includedir}/iLBC_encode.h

# we don't want these
rm -f %{buildroot}%{_libdir}/*.*a
rm -rf %{buildroot}%{_datadir}/doc/libilbc

%files -n %{libname}
%doc COPYING README* NEWS*
%{_libdir}/libilbc.so.%{major}*

%files -n %{libnamedev}
%{_includedir}/*.h
%{_libdir}/libilbc.so
%{_libdir}/pkgconfig/libilbc.pc


%changelog
* Fri Oct 27 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1:2.0.2-alt1_8.2
- NMU: fixed FTBFS on LoongArch

* Sat Jan 08 2022 Michael Shigorin <mike@altlinux.org> 1:2.0.2-alt1_8.1
- E2K: ftbfs workaround (ilyakurdyukov@)

* Sun Dec 05 2021 Igor Vlasenko <viy@altlinux.org> 1:2.0.2-alt1_8
- new version

* Fri Jan 25 2013 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt7
- fix libilbc-devel: non-strict dependency on libilbc

* Wed May 25 2011 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt6
- rebuild

* Sun Oct 10 2010 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt5
- auto rebuild

* Sat Nov 15 2008 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt4
- remove post_ldconfig/pre_ldconfig
- cleanup spec
- move static library to separate package

* Wed Jan 24 2007 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt3
- Cleanup spec

* Sun Mar 19 2006 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt2
- fixed build with --as-needed

* Sat May 07 2005 Denis Smirnov <mithraen@altlinux.ru> 0.6-alt1
- build

* Sat May 07 2005 Motsyo Gennadi <drool_linux@pisem.net> 0.6-alt1.drool
- build for ALT Linux

* Sun Mar 13 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.6-1mdk
- 0.6 (final rfc3951)
- use the %%mkrel macro
- new S1 and S2

* Sun Sep 26 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.5-1mdk
- initial mandrake package
