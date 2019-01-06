Name: lstorrent
Version: 0.0.1
Release: alt1
License: GPL2+
Group: File tools
Summary: allow to view files in *.torrent file from command line
Url: http://code.google.com/p/lstorrent/
Source:  %name.tar

%description
Allow to view list of files in *.torrent file from command line with
controllable output (only files, files and catalogs, files with
relative paths, etc).

%prep
%setup -n %name

%build
%make

%install
mkdir -p %buildroot/%_bindir
install -m 755 test %buildroot/%_bindir/%name

%files
%_bindir/%name
%doc man_pages

%changelog
* Sun Mar 17 2013 Terechkov Evgenii <evg@altlinux.org> 0.0.1-alt1
- Initial build for ALT Linux Sisyphus
