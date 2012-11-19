Name: xneurchecker
Version: 0.4
Release: alt2
Summary: LibXNeur commandline ool

License: GPL
Group: Office
Url: http://xneur.ru/

Source: %name-%version.tar.bz2

# Automatically added by buildreq on Sun May 22 2011
# optimized out: fontconfig libaspell-devel libdbus-glib libgdk-pixbuf libpcre-devel pkg-config
BuildRequires: libxneur-devel

%description
%summary

%prep
%setup
sed -i 's/ = 0.12.0//' configure.in

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%doc AUTHORS ChangeLog NEWS README TODO
%_bindir/*

%changelog
* Tue Nov 20 2012 Fr. Br. George <george@altlinux.ru> 0.4-alt2
- Build winthout libraru version dependency

* Mon May 23 2011 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Initial build from scratch

