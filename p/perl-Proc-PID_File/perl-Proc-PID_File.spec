%define dist Proc-PID_File

Name: perl-%dist
Version: 0.05
Release: alt5

Summary: check whether a self process is already running
License: %perl_license
Group: Development/Perl

Source: %dist-%version.tar.gz

BuildArch: noarch

BuildPreReq: /proc rpm-build-licenses

# Automatically added by buildreq on Mon May 07 2007
BuildRequires: perl-devel

%description
Check whether a self process is already running. This package is predecessor
of Proc-PID-File but they are uncompatible. Proc-PID_File removed from CPAN
archive at this time.

%prep
%setup -q -n %dist-%version

#patch0 -p0
#patch1 -p0

%build
%perl_vendor_build

%__rm -f $RPM_BUILD_DIR/%dist-%version/blib/lib/Proc/*.pl

%install
%perl_vendor_install

%files
%doc README Changes

%perl_vendor_privlib/Proc/PID*

%changelog
* Wed Nov 17 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.05-alt5
- removed macro %%perl_vendor_man3dir from spec
- removed Packager from spec

* Wed May 12 2010 Sergey Y. Afonin <asy@altlinux.ru> 0.05-alt4
- updated description
- removed Url (package removed from CPAN archive)

* Sat Nov 15 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.05-alt3
- added packager

* Tue Sep 02 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.05-alt2
- fixed directory ownership violation

* Sat May 03 2008 Sergey Y. Afonin <asy@altlinux.ru> 0.05-alt1
- Initial build for ALTLinux 
