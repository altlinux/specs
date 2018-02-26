Name:		kontakter
Version:	0.2
Release:	alt1

Summary:	Contact manager - client side
License:	GPLv3+
Group:		Office
URL:		http://giowisys.com/
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source:		Kontakter_v%{version}_src.tar.bz2
Patch:		%{name}.diff

BuildRequires:	gcc-c++, make, libqt4-devel

%description
Kontakter is an easy to use address book with advance search
functionality and a very intuitive user interface. The contacts
are stored in a SQLITE database and can be synchronized over
the network with a central database provided by kontakter's server.
(This feature will be available in the next version)

Features:
* intuitive GUI
* cross-platform (Windows, Mac OS X, GNU/Linux)
* export/import contacts in the vCard format (.vcf)
* export contacts to PDF
* print function
* export/import SQLITE databases with all your contacts
* up to 6 custom fields
* synchronize your contacts with a central database over the network
  (in the next version)

%package	server
Summary:	Contact manager - server side
Group:		Office

%description	server
Contact manager - server side

%prep
%setup -q -n Kontakter
%patch -p 0

%build
pushd src/client
qmake-qt4
make
popd
pushd src/server
qmake-qt4
make
popd

%install
# client
%__install -D -m0755 src/client/client %{buildroot}%{_bindir}/%{name}
%__install -D -m0644 src/installers/deb/usr/share/applications/kontakter.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%__install -D -m0644 src/installers/deb/usr/share/pixmaps/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
# server
%__install -D -m0755 src/server/server %{buildroot}%{_bindir}/%{name}-server
%__install -D -m0644 src/installers/deb/usr/share/applications/kontakter-server.desktop %{buildroot}%{_datadir}/applications/%{name}-server.desktop
%__install -D -m0644 src/installers/deb/usr/share/pixmaps/%{name}-server.xpm %{buildroot}%{_datadir}/pixmaps/%{name}-server.xpm

%files
%doc AUTHORS.txt CHANGELOG.txt COPYING.txt LICENSE.txt README.txt TODO.txt
%_bindir/%name
%_desktopdir/%name.desktop
%_pixmapsdir/%name.xpm

%files	server
%_bindir/%{name}-server
%_desktopdir/%{name}-server.desktop
%_pixmapsdir/%{name}-server.xpm

%changelog
* Mon Feb 07 2011 Andrey Cherepanov <cas@altlinux.org> 0.2-alt1
- Initial build in Sisyphus


