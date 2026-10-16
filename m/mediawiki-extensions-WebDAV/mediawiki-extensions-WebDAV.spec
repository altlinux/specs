%define oname WebDAV
%define mwversion 1.46
%define commit 9f08d3c
%setup_mediawiki_ext %mwversion %oname

Name: mediawiki-extensions-%oname
Version: 3.1.0
Release: alt1

Summary: WebDAV / DeltaV / Subversion interface to MediaWiki articles

License: GPL-3.0-only
Group: Networking/WWW
Url: https://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch

BuildRequires(pre): rpm-macros-mediawiki >= 0.7

# Source-url: https://extdist.wmflabs.org/dist/extensions/%oname-%MWREL-%commit.tar.gz
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
%mediawiki_ext_install 50 %oname
# remove development files
rm -rv %buildroot%mediawiki_ext_dir/{Gruntfile.js,package.json,package-lock.json,composer.lock,vendor/bin}
rm -rv %buildroot%mediawiki_ext_dir/vendor/sabre/*/bin
# the entry point finds MediaWiki by the directory of the script, run it from the web root
ln -s extensions/%oname/entrypoints/webdav.php %buildroot%_mediawikidir/webdav.php

%files -f %oname.files
%_mediawikidir/webdav.php

%changelog
* Thu Oct 15 2026 Vitaly Lipatov <lav@altlinux.ru> 3.1.0-alt1
- update to REL1_46 snapshot 9f08d3c (MediaWiki 1.46)
- dependency on mediawiki-common >= 1.46 comes from the setup macro, no Requires: mediawiki
- new WebDAV extension on sabre/dav (extension.json format), vendor from the snapshot
- removed vendor binaries
- added the webdav.php entry point symlink in the MediaWiki root (the old package installed it there)
- BuildRequires(pre): rpm-macros-mediawiki (macros moved there from rpm-build-mediawiki)

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r37162-alt1
- initial build for ALT Linux Sisyphus
