%global _unpackaged_files_terminate_build 1

%define oname qrcodejs

Name: javascript-%oname
Summary: QRCode.js is javascript library for making QRCode.
Version: 0.0.1
Release: alt1
License: MIT
Group: Development/Other
Url: https://github.com/davidshimjs/qrcodejs
Source: %name-%version.tar
# Patch: %%name-%%version.patch
BuildArch: noarch
Provides: libjs-%oname = %EVR
Provides: %oname = %EVR

Requires: javascript-common
BuildRequires(pre): rpm-macros-javascript

%description
QRCode.js is javascript library for making QRCode.
QRCode.js supports Cross-browser with HTML5 Canvas and table tag in DOM.
QRCode.js has no dependencies.

%prep
%setup
# %%patch -p1

%build
%install

mkdir -p %buildroot%_jsdir/%oname
install -p -m644 qrcode.min.js %buildroot%_jsdir/%oname/

%files
%_jsdir/%oname

%changelog
* Tue Jan 25 2022 Alexey Shabalin <shaba@altlinux.org> 0.0.1-alt1
- Initial build.
