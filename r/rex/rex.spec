# SPEC file for rex package

Name:    rex
Version: 0.43.7
Release: alt1

Summary: (R)?ex - Remote Execution Framework

License: Apache License 2.0
Group:   System/Configuration/Other
URL:     http://rexify.org/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source0: %name-%version.tar
Patch0:  %name-%version-%release.patch

Patch1:  %name-0.38.0-alt-update_system.patch
Patch2:  %name-0.41.2-sudo_backquotes.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Dec 01 2013
# optimized out: perl-Digest-SHA perl-Encode perl-Encode-Locale perl-HTTP-Date perl-HTTP-Message perl-IO-Stty perl-IO-Tty perl-Term-ANSIColor perl-Types-Serialiser perl-URI perl-YAML perl-common-sense perl-libwww
BuildRequires: perl-DBI perl-Digest-HMAC perl-Expect perl-JSON-XS perl-Net-SSH2 perl-String-Escape perl-XML-Simple perl-devel perl-Net-SFTP-Foreign subversion wget
BuildRequires: perl-libwww perl-Net-OpenSSH

# Template files does't contains a proper Perl code
%add_findreq_skiplist */Commands/templates/*

%description
(R)?ex is a tool to ease the execution of commands on multiple
remote servers. It allows to manage all boxes from a central
point through the complete process of configuration management
and software deployment.

%prep
%setup
%patch0 -p1

%patch1 -p0
%patch2 -p0

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
* Sun Dec 01 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.43.7-alt1
- New version

* Sun May 19 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.3-alt1
- New version

* Sun Apr 21 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.2-alt2
- Fix backquotes in remote sudo() calls

* Sun Apr 21 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.2-alt1
- New version

* Sun Apr 14 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.41.1-alt1
- New version

* Sat Feb 09 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.39.0-alt1
- New version

* Sun Feb 03 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.38.0-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.37.0-alt1
- New version

* Sat Dec 15 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.34.2-alt1
- New version

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
