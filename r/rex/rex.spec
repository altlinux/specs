# SPEC file for rex package

Name:    rex
Version: 0.34.1
Release: alt1

Summary: (R)?ex - Remote Execution Framework

License: Apache License 2.0
Group:   System/Configuration/Other
URL:     http://rexify.org/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch


BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Aug 12 2012
# optimized out: perl-Encode perl-HTTP-Date perl-IO-Stty perl-IO-Tty perl-Term-ANSIColor perl-XML-LibXML perl-XML-SAX perl-XML-SAX-Base perl-YAML
BuildRequires: perl-DBI perl-DBM perl-Digest-HMAC perl-Expect perl-JSON-XS perl-Net-SSH2 perl-XML-Simple perl-devel perl-libwww

%description
(R)?ex is a tool to ease the execution of commands on multiple
remote servers. It allows to manage all boxes from a central
point through the complete process of configuration management
and software deployment.

%prep
%setup
%patch0 -p1


%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README.pod doc/Rexfile-example1
%doc LICENSE

%_bindir/rex
%_bindir/rexify

%exclude %perl_vendor_privlib/README.pod

%perl_vendor_privlib/Rex*


%changelog
* Tue Nov 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.34.1-alt1
- New version

* Wed Nov 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.34.0-alt1
- New version

* Sun Oct 14 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.33.1-alt1
- New version

* Sat Aug 25 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.32.0-alt1
- New version

* Wed Aug 15 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.31.4-alt1
- New version

* Sun Aug 12 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.30.0-alt1
- Initial build for ALT Linux Sisyphus
