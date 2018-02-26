Name:           gnaural
Version:        1.0.20080808
Release:        alt1.qa1
Summary:        A multi-platform programmable binaural-beat generator
Packager:	Sergey Ivanov <seriv@altlinux.ru>

Group:          Sound
License:        GPLv2+
URL:            http://gnaural.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Automatically added by buildreq on Mon Jan 19 2009
BuildRequires: libglade-devel libportaudio2-devel libsndfile-devel
BuildRequires: desktop-file-utils
Requires:       icon-theme-hicolor

%description
Gnaural is a multi-platform programmable binaural-beat generator. It
is actually brainwave entrainment software for creating binaural beats
intended to be used as personal brainwave synchronization software,
for scientific research, or by professionals. Gnaural allows for the
creation of binaural beat tracks specifying different frequencies and
exporting tracks into different audio formats. Gnaural runnings can
also be linked over the internet, allowing synchronous sessions
between many users.

%prep
%setup -q -n %{name}-%{version}


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install INSTALL="install -p" DESTDIR=$RPM_BUILD_ROOT

install -p -dm 755 $RPM_BUILD_ROOT/%{_datadir}/pixmaps
install -p -dm 755 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps

install -p -m 644 pixmaps/%{name}-icon.xpm \
 $RPM_BUILD_ROOT/%{_datadir}/pixmaps
install -p -m 644 pixmaps/%{name}-icon.png \
 $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps

install -p -dm 755 $RPM_BUILD_ROOT/%{_datadir}/applications

sed -i -e 's|^Categories=.*$|Categories=AudioVideo;AudioVideoEditing;|g' \
 -e 's|^Encoding=UTF-8$||g' \
 -e 's|^GenericName=Audio binaural beat editor/generator$||g' \
 -e 's|^Icon=.*$|Icon=%{name}-icon|g' \
 $RPM_BUILD_ROOT/%{_datadir}/gnome/apps/Multimedia/%{name}.desktop

desktop-file-install \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
$RPM_BUILD_ROOT%{_datadir}/gnome/apps/Multimedia/%{name}.desktop

rm -r $RPM_BUILD_ROOT%{_datadir}/gnome


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.glade
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/%{name}-icon.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.xpm
%{_datadir}/icons/hicolor/48x48/apps/%{name}-icon.png


%changelog
* Thu Jan 14 2010 Repocop Q. A. Robot <repocop@altlinux.org> 1.0.20080808-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-gtk-update-icon-cache for gnaural
  * postclean-05-filetriggers for spec file

* Sun Jan 18 2009 Sergey Ivanov <seriv@altlinux.ru> 1.0.20080808-alt1
- first build for Sisyphus

* Mon Jan 05 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-5
- Removed "Application" from .desktop Categories.

* Sun Jan 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-4
- Fixed missing -p for install command.

* Sun Jan 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-3
- Removed fedora as vendor - as per new guidelines.

* Sun Jan 04 2009 Rakesh Pandit <rakesh@fedoraproject.org> 1.0.20080808-2
- Fixed %%version, %%description, timestamp, fixed icon path,
- Removed useless buildrequires, fixed .desktop file installation.

* Sat Dec 06 2008 Rakesh Pandit <rakesh@fedoraproject.org> 1.0-1.20080808
- Initial build.
