Name: xneurchecker
Version: 0.4
Release: alt5
Summary: LibXNeur commandline tool

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
* Thu Jun 08 2017 Fr. Br. George <george@altlinux.ru> 0.4-alt5
- Rebuild with new libxneur

* Thu Nov 17 2016 Fr. Br. George <george@altlinux.ru> 0.4-alt4
- Rebuild with new libxneur

* Mon Oct 28 2013 Fr. Br. George <george@altlinux.ru> 0.4-alt3
- Rebuild with new libxneur

* Tue Nov 20 2012 Fr. Br. George <george@altlinux.ru> 0.4-alt2
- Build winthout libraru version dependency

* Mon May 23 2011 Fr. Br. George <george@altlinux.ru> 0.4-alt1
- Initial build from scratch

