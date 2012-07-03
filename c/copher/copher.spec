Name: copher
Version: 0.1.1
Release: alt1

Summary: copher submits file releases to SourceForge

License: GPL
Group: Development/Other
Url: http://copher.sourceforge.net/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://dl.sf.net/%name/%name-%version.tar.bz2

# Automatically added by buildreq on Sun Sep 10 2006 (-bi)
BuildRequires: perl-WWW-Mechanize

%description
copher is a script that submits file releases to a project hosted on
SourceForge, including adding a new release, uploading and adding files,
and editing an existing release.

%prep
%setup -q

%install
install -m 0755 -D %name.pl %buildroot%_bindir/%name

%files
%_bindir/%name

%changelog
* Fri Jan 18 2008 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt1
- fix Url, Source URL

* Sun Sep 10 2006 Vitaly Lipatov <lav@altlinux.ru> 0.1.1-alt0.1
- initial build for Sisyphus
