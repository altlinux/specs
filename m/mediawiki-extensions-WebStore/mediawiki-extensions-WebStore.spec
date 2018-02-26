%define oname WebStore
%define major 1.15
%define revision r48763

Name: mediawiki-extensions-%oname
Version: %major.%revision
Release: alt1

BuildArch: noarch

Group: Networking/WWW
Summary: Web-only (non-NFS) file storage middleware. It is needed by the ProofreadPage extension.
Url: http://www.mediawiki.org/wiki/Extension:%oname

Packager: Vitaly Lipatov <lav@altlinux.ru>

License: GPL

BuildPreReq: rpm-build-mediawiki >= 0.2
Requires: mediawiki-common >= 1.15.1-alt4

# It is new feature etersoft-build-utils since 1.7.6: supports commented real url
# Source-url: http://upload.wikimedia.org/ext-dist/%oname-MW%major-%revision.tar.gz
Source: %name-%version.tar

%description
WebStore is intended to handle images and the generation of thumbnails in
a multiple-server environment. It includes a web-server error 404 handler;
if a thumbnail is requested that does not already exist on the local
server, the request is forwarded to another server so that the thumbnail
image may be automatically generated.  Communication between the multiple
servers is based on WWW protocols (http) only.  The WebStore extension
is needed by the ProofreadPage extension.

%prep
%setup

%install
%mediawiki_ext_install 50 %oname

%files -f %oname.files

%changelog
* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 1.15.r48763-alt1
- initial build for ALT Linux Sisyphus
