Name:            netactview
Version:         0.6.4
Release:         alt1
Summary:         Graphical network connections viewer for Linux

Group:           Networking/Other
License:         GPLv2+
URL:             http://netactview.sourceforge.net/
Source0:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:          missing-call-to-setgroups.patch
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  gnome-vfs-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgtop2-devel
BuildRequires:  perl-XML-Parser

%description
Netactview is a graphical network connections viewer for Linux, similar
in functionality with Netstat. It includes features like process
information, host name retrieval, automatic refresh and sorting. It has
a fully featured GTK 2 graphical interface.

%prep
%setup -q
#patch0 -p1

%build
%configure
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%doc README COPYING AUTHORS NEWS ChangeLog
%_bindir/%name
%_datadir/%name
%_pixmapsdir/%name.png
%_desktopdir/%name.desktop
%_man1dir/%name.1*

%changelog
* Mon Jul 11 2016 Andrey Cherepanov <cas@altlinux.org> 0.6.4-alt1
- Initial build in Sisyphus

