# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define rver	0.42-6
%define ver	%(echo %rver|tr '-' '.')
%define rel	13
%add_optflags -fcommon

Summary:	Real-time patchable audio and multimedia processor
Name:		pd
Version:	%{ver}
Release:	alt5_%{rel}
License:	BSD
Group:		Sciences/Other
URL:		http://www.puredata.org
Source0:	https://downloads.sourceforge.net/pure-data/%{name}-%{rver}.src.tar.gz
Patch0:		pd-0.42-6-tcl86.patch
Patch1:		pd-0.42-6-big_endian.patch
Patch2:		pd-0.42-6-fix_strncpy_usage.patch
#Patch3:		pd-0.42-6-hurd.patch
Patch4:		pd-0.42-6-nostrip.patch
Patch5:		pd-0.42-6-linking.patch
BuildRequires:	tcl >= 8.5
BuildRequires:	pkgconfig(tcl) >= 8.5
BuildRequires:	tk >= 8.5
BuildRequires:	pkgconfig(tk) >= 8.5
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(alsa)
#BuildRequires:	fftw3-devel
BuildRequires:	libportaudio2-devel
Requires:	tcl >= 8.5
Requires:	tk >= 8.5
# PD expects quite a few files from the docs to be present for various
# things to work, so there's really no point in separating them out
# - AdamW 2008/12
Obsoletes:	%{name}-doc < %{version}-%{release}
Source44: import.info

%description
Pd gives you a canvas for patching together modules that analyze, process,
and synthesize sounds, together with a rich palette of real-time control  
and I/O possibilities.  Similar to Max (Cycling74) and JMAX (IRCAM).  A   
related software package named Gem extends Pd's capabilities to include   
graphical rendering.

%package devel
Summary:	Development files for Pure Data
Group:		Development/Other

%description devel
Development files for Pure Data.

%prep
%setup -q -n %{name}-%{rver}
%patch0 -p1 -b .tcl86
%patch1 -p1 -b .big_endian
%patch2 -p1 -b .strncopy
#patch3 -p1 -b .hurd
%patch4 -p1 -b .nostrip
%patch5 -p1 -b .linking

sed -i -e 's|doc/|share/%{name}/doc/|g' src/s_main.c src/u_main.tk
sed -i -e 's|\(^set help_top_directory\).*|\1 %{_datadir}/%{name}/doc|' src/u_main.tk

%ifarch %e2k
sed -i 's,-O6,-O%_optlevel,' src/configure*
%endif

%build
pushd src
autoconf
export CPPFLAGS="%{optflags}"
%configure \
	--enable-jack \
	--enable-alsa \
	--enable-fftw \
	--enable-portaudio \
	--enable-portmidi

subst "s|-ljack|$(pkg-config --libs jack)|" makefile
%make_build LDFLAGS=""
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_includedir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}

install -m 755 bin/pd %{buildroot}/%{_bindir}
install bin/pdsend bin/pdreceive %{buildroot}/%{_bindir}
install bin/pd-gui bin/pd-watchdog %{buildroot}/%{_bindir}
install bin/pd.tk %{buildroot}/%{_bindir}

install src/*.h %{buildroot}/%{_includedir}/%{name}
cp -pr doc/ %{buildroot}%{_datadir}/%{name}
#%cp -pr extra %%{buildroot}/%%{_libdir}/%%{name}/pd

install -m 644 man/*.1 %{buildroot}/%{_mandir}/man1

%files
%doc README.txt LICENSE.txt
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}


%changelog
* Sat Nov 25 2023 Igor Vlasenko <viy@altlinux.org> 0.42.6-alt5_13
- update

* Tue Nov 02 2021 Igor Vlasenko <viy@altlinux.org> 0.42.6-alt5_12
- restored e2k fix

* Fri Dec 11 2020 Igor Vlasenko <viy@altlinux.ru> 0.42.6-alt4_12
- fixed build with gcc10

* Tue Sep 08 2020 Igor Vlasenko <viy@altlinux.ru> 0.42.6-alt3_12
- update by mgaimport

* Fri Oct 04 2019 Michael Shigorin <mike@altlinux.org> 0.42.6-alt3_10
- E2K: avoid superfluous optimization level

* Fri Mar 08 2019 Igor Vlasenko <viy@altlinux.ru> 0.42.6-alt2_10
- to Sisyphus as alibaubio 0.4.9 dep

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 0.42.6-alt1_10
- update by mgaimport

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.42.6-alt1_9
- new version

* Wed Dec 30 2009 Timur Batyrshin <erthad@altlinux.org> 0.42.5-alt0.svn12837.0.M51.1
- backport to M51

* Sat Dec 19 2009 Timur Batyrshin <erthad@altlinux.org> 0.42.5-alt0.svn12837.1
- svn12837

* Mon Oct 26 2009 Timur Batyrshin <erthad@altlinux.org> 0.42.5-alt0.svn12677.1
- svn12677
- merged with svn tree

* Mon Oct 12 2009 Timur Batyrshin <erthad@altlinux.org> 0.42.5-alt0.svn12520.1
- added menu link, icon and mime typeinfo
- removed *.c, *.o from install tree
- applied patches: 
  * initbang/closebang (new object)
  * fixed some minor bugs and made several minor ui improvements

* Sun Oct 04 2009 Timur Batyrshin <erthad@altlinux.org> 0.42.5-alt0.svn12520.0.1
- 0.42.5.svn12520

* Thu May 28 2009 Timur Batyrshin <erthad@altlinux.org> 0.41.4-alt1
- initial build for sisyphus

