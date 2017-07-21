# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-macros-fedora-compat
BuildRequires: /usr/bin/pkg-config pkgconfig(glade-sharp-2.0) pkgconfig(glib-sharp-2.0) pkgconfig(gtk-sharp-2.0)
# END SourceDeps(oneline)
#this is to prevent empty debuginfo failur
%global debug_package %{nil}

Name:           monobristol
Version:        0.60.3.1
Release:        alt3
Summary:        GUI launcher for Bristol in Mono
Packager: Ilya Mashkin <oddity@altlinux.ru>
Group:          Sound
License:        GPL+
URL:            http://www.dacr.hu/monobristol/
Source:         http://www.dacr.hu/monobristol/%{name}-%{version}.tar.gz
# No upstrem bugtracker. Patch emailed upstream 20120626
# The patch removes shebang from the top and removes .png extension from icon key
Patch1:         %{name}-0.60.3-desktop.patch
Requires:       bristol
Requires:       mono4-core
Requires:       icon-theme-hicolor

#BuildRequires:  libgtk-sharp2-devel
BuildRequires:  mono4-devel /proc
BuildRequires:  desktop-file-utils

##ExclusiveArch:  #{mono_arches}
Source44: import.info


%description
monoBristol is very simple Gui for Bristol Synthesiser.
Bristol is an emulation package for a number of different 'classic' 
synthesizers including additive and subtractive and a few organs.

%prep
%setup -q
%patch1 -p1

sed -i "s#gmcs#mcs#g" configure*
sed -i "s#gmcs#mcs#g" Makefile.in
sed -i "s#gmcs#mcs#g" monoBristol.make


%build
%configure
# not parallel safe
make

%install
#removal of buildroot is no longer necassary, except for EPEL5
make install DESTDIR=%{buildroot}

# install the AppData file
%__mkdir_p %{buildroot}%{_datadir}/appdata
cp monoBristol.appdata.xml %{buildroot}%{_datadir}/appdata/

#install the icon
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

desktop-file-install    \
    --dir %{buildroot}%{_datadir}/applications \
     monoBristol.desktop

%files
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/monoBristol.desktop
%{_libdir}/%{name}/
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/appdata/monoBristol.appdata.xml

%changelog
* Sat Jul 22 2017 Ilya Mashkin <oddity@altlinux.ru> 0.60.3.1-alt3
- rebuild

* Sat Mar 07 2015 Ilya Mashkin <oddity@altlinux.ru> 0.60.3.1-alt2
- Build for Sisyphus

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.60.3.1-alt1_4
- update to new release by fcimport

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 0.60.3.1-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.60.3-alt1_10
- initial fc import

