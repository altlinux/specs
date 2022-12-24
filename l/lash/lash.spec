Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install gcc-c++ python3-devel texinfo
# END SourceDeps(oneline)
Summary(ru_RU.UTF-8): Менеджер сессий для сервера JACK
Group: System/Libraries
%add_optflags %optflags_shared
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Summary:      LASH Audio Session Handler
Name:         lash
Version:      0.5.4
Release:      alt1_49
License:      GPLv2+
URL:          http://www.nongnu.org/lash/
Source0:      http://download.savannah.gnu.org/releases/lash/lash-%{version}.tar.gz
Source1:      %{name}-panel.desktop
Patch0:       lash-0.5.3-no-static-lib.patch
# Fix DSO-linking failure
# Upstream bugtracker is closed for some reason. Sent via email:
Patch1:       lash-linking.patch
# Fix build against gcc-4.7
Patch2:       lash-gcc47.patch
# Modernize texi2html arguments for texi2html-5.0
Patch3:       lash-Modernize-texi2html-arguments.patch

BuildRequires: libalsa-devel
BuildRequires: desktop-file-utils
BuildRequires: gcc
BuildRequires: gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel 
BuildRequires: libjack-devel
BuildRequires: libxml2-devel
BuildRequires: readline-devel
BuildRequires: swig
BuildRequires: texi2html
BuildRequires: chrpath
BuildRequires: libuuid-devel

Requires:      liblash = %{?epoch:%epoch:}%{version}-%{release}
Source44: import.info


%description
LASH is a session management system for JACK and ALSA audio applications on
GNU/Linux. It allows you to save and restore audio sessions consisting of
multiple interconneced applications, restoring program state (i.e. loaded
patches) and the connections between them.

%package -n liblash-devel
Group: Development/Other
Summary:      Development files for LASH
Requires:     liblash = %{?epoch:%epoch:}%{version}-%{release}
Provides: lash-devel = %EVR

%description -n liblash-devel
Development files for the LASH library.

%package        -n liblash
Group: System/Libraries
Summary:        Shared libraries for using %{name}

%description    -n liblash
The %{name}-libs package contains lash shared libraries.

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .linking
%patch2 -p1 -b .gcc47
%patch3 -p1 -b .texi2html

# Hack to build against newer swig
%if 0%{?rhel} && 0%{?rhel} <= 7
sed -i 's|1.3.31|2.0.0|g' configure*
%else
sed -i 's|1.3.31|4.0.0|g' configure*
%endif

%build
CFLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE" %configure --disable-static --disable-serv-inst
%make_build


%install
mkdir -p %{buildroot}%{_sysconfdir}
%makeinstall_std
rm -f %{buildroot}%{_infodir}/dir
rm -f %{buildroot}%{_libdir}/liblash.la

# Move icons to the right place
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/16x16/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/24x24/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/96x96/apps
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
mv %{buildroot}%{_datadir}/lash/icons/lash_16px.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_24px.png %{buildroot}%{_datadir}/icons/hicolor/24x24/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_48px.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash_96px.png %{buildroot}%{_datadir}/icons/hicolor/96x96/apps/lash.png
mv %{buildroot}%{_datadir}/lash/icons/lash.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/lash.svg

# Remove rpath
chrpath --delete %{buildroot}%{_bindir}/lash_control
chrpath --delete %{buildroot}%{_bindir}/lash_simple_client
chrpath --delete %{buildroot}%{_bindir}/lashd
chrpath --delete %{buildroot}%{_bindir}/lash_synth
chrpath --delete %{buildroot}%{_bindir}/lash_panel
chrpath --delete %{buildroot}%{_bindir}/lash_save_button

# Move the dtd file to our Fedora Friendly place
mkdir -p %{buildroot}%{_datadir}/xml/lash/dtds
mv %{buildroot}%{_datadir}/lash/dtds/lash-project-1.0.dtd %{buildroot}%{_datadir}/xml/lash/dtds

# This directory is empty!
rm -rf %{buildroot}%{_datadir}/lash

# install the desktop entry
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                         \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Work around the newer texi2html which is behaving somehow else
if [ ! -d docs/lash-manual-html-split/lash-manual/ ]; then
  mkdir -p docs/lash-manual-html-split/lash-manual/
  cp -p docs/lash-manual-html-split/*.html docs/lash-manual-html-split/lash-manual/
fi



%files
%doc AUTHORS ChangeLog NEWS README docs/lash-manual-html-split/lash-manual icons/lash.xcf
%doc --no-dereference COPYING
%{_bindir}/lash*
%{_datadir}/icons/hicolor/16x16/apps/lash.png
%{_datadir}/icons/hicolor/24x24/apps/lash.png
%{_datadir}/icons/hicolor/48x48/apps/lash.png
%{_datadir}/icons/hicolor/96x96/apps/lash.png
%{_datadir}/icons/hicolor/scalable/apps/lash.svg
%{_datadir}/xml/lash
%{_datadir}/applications/lash-panel.desktop

%files -n liblash-devel
%{_libdir}/liblash.so
%{_includedir}/lash-1.0
%{_libdir}/pkgconfig/lash*

%files -n liblash
%{_libdir}/liblash.so.1
%{_libdir}/liblash.so.1.*

%changelog
* Sat Dec 24 2022 Igor Vlasenko <viy@altlinux.org> 1:0.5.4-alt1_49
- update to new release by fcimport

* Mon Apr 04 2022 Igor Vlasenko <viy@altlinux.org> 1:0.5.4-alt1_47
- fix build

* Tue Nov 24 2020 Igor Vlasenko <viy@altlinux.ru> 1:0.5.4-alt1_43
- updated buildrequires

* Wed Sep 18 2019 Igor Vlasenko <viy@altlinux.ru> 1:0.5.4-alt1_40
- update to new release by fcimport

* Sun Dec 30 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.5.4-alt1_35
- rebuild with readline7

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 1:0.5.4-alt1_34
- update to new release by fcimport

* Wed Nov 22 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.5.4-alt1_32
- picked up from orphaned
- reverted to last stable version 0.5.4

* Thu Feb 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.7
- Fixed build

* Thu May 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.0-alt0.20090725.6
- restored python-module-lash - required by other packages

* Mon Feb 25 2013 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.6.0-alt0.20090725.5
- fixed build on arm

* Fri Jun 08 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.4
- Fixed build

* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.0-alt0.20090725.3.1.1
- Rebuild with Python-2.7

* Sat Nov 06 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.3.1
- Rebuilt for soname set-versions

* Wed Mar 24 2010 Timur Batyrshin <erthad@altlinux.org> 0.6.0-alt0.20090725.3
- python support removed

* Wed Nov 25 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.0-alt0.20090725.2
- Rebuilt with python 2.6

* Tue Aug 04 2009 Timur Batyrshin <erthad@altlinux.org> 0.6.0-alt0.20090725.1
- Initial build for sisyphus
