# Spec file for http_ping utility

Name: http_ping
 
Version: 20050629
Release: alt1.1.1
    
Summary: utility to send HTTP/HTTPS requests 

License: %bsdstyle
Group: Networking/WWW
URL: http://acme.com/software/http_ping/


BuildRequires(pre): rpm-build-licenses

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2
Patch0:  %name-alt-20050629-enable_ssl.patch

AutoReqProv: yes

# Automatically added by buildreq on Sat May 24 2008
BuildRequires: libssl-devel

%description
http_ping is like the regular ping command, except that it sends
HTTP requests instead of ICMP echo requests.

%prep
%setup
%patch0

%build
%make_build

%install
install -d %buildroot%_bindir
install -d %buildroot%_man1dir

install -m 0755 %name %buildroot%_bindir/
install -m 0644 %name.1 %buildroot%_man1dir/

%files
%doc README

%_bindir/%name
%_man1dir/*

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 20050629-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 20050629-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat May 31 2008 Nikolay A. Fetisov <naf@altlinux.ru> 20050629-alt1
- Initial build for ALT Linux Sisyphus
