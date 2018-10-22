Name: sendemail
Version: 1.56
Release: alt2

Summary: Send email from a console near you!
License: GPLv2+
Group: Networking/Mail

Packager: Ilfat Aminov <aminov@altlinux.org>

URL: https://github.com/mogaal/sendemail
Source: %name-%version.tar

BuildRequires: perl-IO-Socket-INET6

Patch0: 00_fix_ssl_version.patch
Patch1: 01_add_ipv6_support.patch

BuildArch: noarch

%description
SendEmail is a lightweight, completly command line based,
SMTP email agent. If you have the need to send email from
the command line, this tool is perfect. It was designed to be used
in bash scripts, Perl programs, and web sites, but it is also quite
useful in many other contexts.  SendEmail is written in Perl
and is unique in that it requires NO SPECIAL MODULES.
It has an intuitive and flexible set of command-line options,
making it very easy to learn and use.

%prep
%setup

%patch0 -p1
%patch1 -p1

%build

%install
mkdir -pv %buildroot/%_bindir
cp -v sendEmail sendEmail.pl %buildroot/%_bindir/

%files
%doc CHANGELOG README README-BR.txt TODO
%_bindir/sendEmail*

%changelog
* Mon Oct 22 2018 Ilfat Aminov <aminov@altlinux.org> 1.56-alt2
- Backport to Sisyphus

* Mon Oct 22 2018 Ilfat Aminov <aminov@altlinux.org> 1.56-alt0.M70C.3
- Add ipv6 support

* Mon Oct 15 2018 Ilfat Aminov <aminov@altlinux.org> 1.56-alt0.M70C.2
- Add patch to fix fails when tls is enabled

* Fri Apr 13 2018 Lenar Shakirov <snejok@altlinux.ru> 1.56-alt0.M70C.1
- Backport to C7.1

* Thu Jun 23 2016 Lenar Shakirov <snejok@altlinux.ru> 1.56-alt1
- First build for Sisyphus
