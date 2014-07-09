# BEGIN SourceDeps(oneline):
BuildRequires: gcc-c++ libalsa-devel zlib-devel
# END SourceDeps(oneline)
%define fedora 21
Name:           milkytracker
Version:        0.90.85
Release:        alt2_8
Summary:        Module tracker software for creating music

Group:          Sound
License:        GPLv3+
URL:            http://www.milkytracker.net/
Source0:        http://milkytracker.org/files/%{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         milkytracker-0.90.85-use-system-library.patch
Patch1:         milkytracker-0.90.85-use-system-library-pregenerated.patch
Patch2:         milkytracker-0.90.85-integer-types.patch
Patch3:         milkytracker-0.90.85-gzfile-type.patch

BuildRequires:  libSDL-devel
BuildRequires:  desktop-file-utils
BuildRequires:  zziplib-devel
BuildRequires:  libjack-devel
Source44: import.info


%description
MilkyTracker is an application for creating music in the .MOD and .XM formats.
Its goal is to be free replacement for the popular Fasttracker II software.

%prep
%setup -q
find . -regex '.*\.\(cpp\|h\|inl\)' -print0 | xargs -0 chmod 644

%patch0 -p1 -b .debug
%patch1 -p1 -b .debug
%patch2 -p1 -b .debug
%patch3 -p1 -b .debug

# Explicitly remove source files
rm -rf src/compression/zlib/
rm -rf src/compression/zziplib/generic/

# timestamp: touch files to remove autotool call
touch -r configure aclocal.m4 Makefile.in config.h.in

%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

# copy the icon
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p resources/pictures/carton.png %{buildroot}%{_datadir}/pixmaps/milkytracker.png

# copy the desktop file
desktop-file-install \
%if 0%{?fedora} && 0%{?fedora} < 19
  --vendor fedora \
%endif
  --dir=%{buildroot}%{_datadir}/applications/ %{SOURCE1}


%files
%doc AUTHORS COPYING NEWS README
%{_bindir}/milkytracker
%if 0%{?fedora} && 0%{?fedora} < 19
%{_datadir}/applications/fedora-%{name}.desktop
%else
%{_datadir}/applications/%{name}.desktop
%endif
%{_datadir}/pixmaps/milkytracker.png

%changelog
* Wed Jul 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt2_8
- moved to Sisyphus by mike@ request

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt1_8
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt1_7
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.90.85-alt1_6
- initial fc import

