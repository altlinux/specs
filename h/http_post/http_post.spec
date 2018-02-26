# Spec file for http_post utility

Name: http_post
 
Version: 20050316
Release: alt1.1.1
    
Summary: utility to do POST to an HTTP/HTTPS URL

License: %bsdstyle
Group: Networking/WWW
URL: http://acme.com/software/http_post/


BuildRequires(pre): rpm-build-licenses

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2
Patch0:  %name-alt-20050316-enable_ssl.patch

AutoReqProv: yes

# Automatically added by buildreq on Sat May 24 2008
BuildRequires: libssl-devel

%description
Http_post does a POST operation to an HTTP URL and dumps the
results to stdout. It can do HTTPS POSTs as well.

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
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 20050316-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 20050316-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat May 31 2008 Nikolay A. Fetisov <naf@altlinux.ru> 20050316-alt1
- Initial build for ALT Linux Sisyphus
