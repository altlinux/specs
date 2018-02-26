Summary: Display the HTTP headers returned by webservers
Name: furl
Version: 2.1
Release: alt1
License: GPL
Group: Networking/WWW
URL: http://www.gumbynet.org.uk/software/furl.html
Packager: Mikhail Pokidko <pma@altlinux.org>
Source: %name-%version.tar.gz


%description
A small utility designed to display the HTTP headers returned by web-servers
in response to client requests.

%prep
%setup -q

%build
%configure
%make

%install
#makeinstall
%make_install DESTDIR="%buildroot" install

%files
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%_bindir/*


%changelog
* Tue Jul 18 2006 Mikhail Pokidko <pma@altlinux.ru> 2.1-alt1
- Initial build
