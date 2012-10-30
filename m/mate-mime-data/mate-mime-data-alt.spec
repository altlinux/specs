# BEGIN SourceDeps(oneline):
BuildRequires: perl(diagnostics.pm)
# END SourceDeps(oneline)
%define _libexecdir %_prefix/libexec
Summary: 		MIME type data files for MATE desktop
Name: 			mate-mime-data
Version: 		1.4.0
Release: 		alt2_1.1
URL: 			http://mate-desktop.org
Source0: 		http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
				# No license attribution, just COPYING.
License: 		GPL+
Group: 			System/Libraries
BuildArch: 		noarch
BuildRequires: 	perl(XML/Parser.pm)
BuildRequires: 	gettext
BuildRequires:  mate-common
BuildRequires:  glib2-devel
BuildRequires:  intltool

# Fedora specific patches
Patch0: gnome-mime-data-2.2.0-openoffice.patch
Patch1: gnome-mime-data-2.2.0-alt-rpminstall.patch
Patch3: gnome-mime-data-2.4.1-default-applications.patch

%description
mate-mime-data provides the file type recognition data files for mate-vfs

%prep
%setup -q
%patch0 -p1 -b .openoffice
%patch1 -p1 -b .rpminstall
%patch3 -p1 -b .default-applications

NOCONFIGURE=1 ./autogen.sh

%build

%configure


make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog NEWS README
%config %{_sysconfdir}/mate-vfs-mime-magic
%{_datadir}/application-registry
%{_datadir}/mime-info/*.keys
%{_datadir}/mime-info/*.mime
%{_datadir}/pkgconfig/*

%changelog
* Wed Oct 24 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.4.0-alt2_1.1
- Build for Sisyphus

* Mon Oct 15 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt2_1
- adapted patches

* Wed Aug 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1_1
- 20120801 mate snapshot

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt2_1
- 20120622 mate snapshot

* Mon Apr 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.2.2-alt1_1
- converted by srpmconvert script

