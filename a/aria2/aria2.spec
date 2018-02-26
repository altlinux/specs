Name: aria2
Version: 1.15.1
Release: alt1

Summary: aria2 - a simple utility for downloading files faster.
License: GPL
Group: Networking/File transfer
Url: http://aria2.sourceforge.net/
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source: %{name}-%version.tar.bz2

# Automatically added by buildreq on Thu Mar 23 2006
BuildRequires: gcc-c++ libssl-devel libstdc++-devel

%description

aria2 is a download utility with resuming and segmented downloading.
Supported protocols are HTTP/HTTPS/FTP/BitTorrent. It also supports Metalink
version 3.0.

Currently it has following features:
- HTTP/HTTPS GET support
- HTTP Proxy support
- HTTP BASIC authentication support
- HTTP Proxy authentication support
- FTP support (active, passive mode)
- FTP through HTTP proxy (GET command or tunneling)
- Segmented download
- Cookie support
- It can run as a daemon process.
- BitTorrent protocol support with fast extension.
- Selective download in multi-file torrent
- Metalink version 3.0 support (HTTP/FTP/BitTorrent).
- Limiting download/upload speed



%prep
%setup -q -n %{name}-%version

%build
%configure
%make

%install
mkdir -p %buildroot%_bindir
%__install -pD -m755 src/aria2c %buildroot%_bindir/%name

%files
%doc AUTHORS ChangeLog README
%_bindir/%name

%changelog
* Wed May 30 2012 Ilya Mashkin <oddity@altlinux.ru> 1.15.1-alt1
- 1.15.1
- Update description

* Wed Feb 29 2012 Ilya Mashkin <oddity@altlinux.ru> 1.14.2-alt1
- 1.14.2

* Tue Dec 27 2011 Ilya Mashkin <oddity@altlinux.ru> 1.14.0-alt1
- 1.14.0

* Wed Aug 03 2011 Ilya Mashkin <oddity@altlinux.ru> 1.12.1-alt1
- 1.12.1

* Thu Jun 16 2011 Ilya Mashkin <oddity@altlinux.ru> 1.11.2-alt1
- 1.11.2

* Sat Apr 02 2011 Ilya Mashkin <oddity@altlinux.ru> 1.11.1-alt1
- 1.11.1

* Mon Dec 20 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.8-alt1
- 1.10.8

* Wed Dec 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.7-alt1
- 1.10.7

* Thu Nov 04 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.6-alt1
- 1.10.6

* Sat Oct 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.5-alt1
- 1.10.5

* Fri Oct 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.4-alt1
- 1.10.4

* Thu Sep 23 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.3-alt1
- 1.10.3

* Tue Aug 31 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.2-alt1
- 1.10.2

* Sun Aug 29 2010 Ilya Mashkin <oddity@altlinux.ru> 1.10.1-alt1
- 1.10.1

* Mon Jul 12 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.5-alt1
- 1.9.5

* Sat Jun 12 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.4-alt1
- 1.9.4

* Sat May 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.3-alt1
- 1.9.3

* Sun May 02 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.2-alt1
- 1.9.2

* Fri Apr 16 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.1-alt1
- 1.9.1

* Mon Mar 29 2010 Ilya Mashkin <oddity@altlinux.ru> 1.9.0-alt1
- 1.9.0

* Wed Feb 24 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.3-alt1
- 1.8.3

* Mon Feb 15 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Sun Jan 24 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Thu Jan 07 2010 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Dec 17 2009 Ilya Mashkin <oddity@altlinux.ru> 1.7.2-alt1
- 1.7.2

* Sun Nov 15 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.3-alt1
- 1.6.3

* Mon Oct 12 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Wed Oct 07 2009 Ilya Mashkin <oddity@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Wed Aug 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Thu Jul 29 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Tue Jul 21 2009 Ilya Mashkin <oddity@altlinux.ru> 1.5.0-alt1
- 1.5.0

* Tue Jun 16 2009 Ilya Mashkin <oddity@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon May 11 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.3-alt1
- 1.3.3

* Tue Apr 28 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Tue Apr 14 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.1-alt1
- 1.3.1

* Fri Apr 03 2009 Ilya Mashkin <oddity@altlinux.ru> 1.3.0-alt1
- 1.3.0

* Sat Feb 21 2009 Ilya Mashkin <oddity@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 1.1.2-alt1
- 1.1.2

* Wed Nov 26 2008 Ilya Mashkin <oddity@altlinux.ru> 1.0.1-alt1
- 1.0.1

* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 0.16.2-alt1
- 0.16.2

* Thu Oct 09 2008 Ilya Mashkin <oddity@altlinux.ru> 0.16.0-alt1
- 0.16.0

* Sat Sep 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.15.3-alt1
- 0.15.3

* Fri Aug 29 2008 Ilya Mashkin <oddity@altlinux.ru> 0.15.2-alt1
- 0.15.2

* Thu Jul 03 2008 Ilya Mashkin <oddity@altlinux.ru> 0.14.0-alt1
- 0.14.0+1

* Mon May 26 2008 Ilya Mashkin <oddity@altlinux.ru> 0.13.2-alt1
- 0.13.2

* Tue Mar 20 2008 Ilya Mashkin <oddity@altlinux.ru> 0.13.1-alt1
- 0.13.1+1

* Wed Mar 05 2008 Ilya Mashkin <oddity@altlinux.ru> 0.13.0-alt1
- 0.13.0

* Sun Feb 17 2008 Ilya Mashkin <oddity@altlinux.ru> 0.12.1-alt1
- 0.12.1+1

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.6.0-alt1.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Tue Jul 11 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Mon Jun 26 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.5.2-alt1
- 0.5.2

* Tue Jun 20 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Sat May 27 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.5.0-alt1
- 0.5.0

* Tue May 02 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.4.1-alt1
- 0.4.1

* Wed Apr 26 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.4.0-alt1
- 0.4.0

* Wed Apr 19 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.3.2-alt1
- 0.3.2

* Thu Mar 23 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Fri Feb 24 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.2.0-alt1
- 0.2.0

* Mon Feb 20 2006 Andrey Semenov <mitrofan@altlinux.ru> 0.1.0-alt1
- First version

