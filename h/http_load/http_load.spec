# Spec file for http_load utility

Name: http_load
 
Version: 20060312
Release: alt1.1.1
    
Summary: a throughput testing tool for web servers

License: %bsdstyle
Group: Networking/WWW
URL: http://acme.com/software/http_load/


BuildRequires(pre): rpm-build-licenses

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar.bz2
Patch0: %name-alt-20060312-enable_ssl.patch

AutoReqProv: yes

# Automatically added by buildreq on Sat May 24 2008
BuildRequires: libssl-devel

%description
http_load runs multiple http fetches in parallel, to test
the throughput of a web server. However unlike most such
test clients, it runs in a single process, so it doesn't
bog down the client machine. It can be configured to do
https fetches as well. 


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
%doc README make_test_files

%_bindir/%name
%_man1dir/*

%changelog
* Wed Dec 08 2010 Igor Vlasenko <viy@altlinux.ru> 20060312-alt1.1.1
- rebuild with new openssl and/or boost by request of git.alt administrator

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 20060312-alt1.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Sat May 31 2008 Nikolay A. Fetisov <naf@altlinux.ru> 20060312-alt1
- Initial build for ALT Linux Sisyphus
