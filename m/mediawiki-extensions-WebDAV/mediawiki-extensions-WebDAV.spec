%define oname WebDAV
%define major 1.15
%define revision r37162

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: WebDAV / DeltaV / Subversion interface to MediaWiki articles
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.15.1-alt4

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-MW%major-%revision.tar.gz
Source: %oname-%version.tar

%description
WebDAV is a set of extensions to HTTP to support distributed authoring
and versioning. It defines some request methods, message headers and XML
message bodies which at their most basic, add metadata and locking to
HTTP. Because it's based on HTTP and XML, it is quite easy to implement
a WebDAV server in CGI or PHP. WebDAV maps very cleanly to file system
primitives, so most modern operating systems support mounting WebDAV
resources as file systems.  The Wikipedia:WebDAV article and the WebDAV
home page describe WebDAV in more detail. WebDAV is formally defined in
RFC 4918. The WebDAV versioning extension, DeltaV, is defined in RFC 3253.

%prep
%setup -n %oname-%version

%install
mkdir -p %buildroot%_datadir/mediawiki/
cp -a * %buildroot%_datadir/mediawiki/

%files
%_datadir/mediawiki/*

%changelog
* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r37162-alt1
- initial build for ALT Linux Sisyphus
