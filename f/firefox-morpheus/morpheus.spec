%define oname	morpheus
%define ocid jid1-hA782Yun5MXnyw@jetpack
%define ociddir 	%firefox_noarch_extensionsdir/%ocid

Name: firefox-%oname
Version: 0.2.5
Release: alt1
Summary: A simple morphological analyzer and dictionary for a latin language
Group: Networking/WWW
License: MPL 2.0
URL: https://addons.mozilla.org/ru/firefox/addon/diglossa/
Source: %name-%version.tar
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>
BuildArch: noarch
BuildRequires(pre): rpm-build-firefox

%description 
Morhpeus addon integrates your browser with Morpheus - a simple
morphological analyzer and dictionary for a latin language, which is
used as web-service on http://diglossa.org

%prep
%setup

%install
install -d %buildroot%ociddir
cp -fR * %buildroot%ociddir/

%files
%ociddir

%changelog
* Fri Jan 11 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.5-alt1
- Initial build for Sisyphus

