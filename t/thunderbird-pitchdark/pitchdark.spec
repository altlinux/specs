BuildRequires(pre): rpm-build-thunderbird

%define mname pitchdark
%define mcid \{42b649d0-62e0-11da-8cd6-0800200c9a66\}
%define mciddir %tbird_noarch_extensionsdir/%mcid
%define mworkdir %tbird_name-%mname-%mver

Name: %tbird_name-%mname
Version: 4.0.0
Release: alt1
Summary: Dark-colored minimalistic theme for Thunderbird
License: MPL or GPLv3
Group: Networking/Mail
Url: https://addons.mozilla.org/ru/thunderbird/addon/pitchdark-for-tb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %mname-%version.tar
BuildArch: noarch
Requires: %tbird_name >= %tbird_version

%description
Dark-colored minimalistic theme with emphasis on visibility, usability
and maximum screen real estate.

%prep
%setup

%install
install -d %buildroot%mciddir
cp -fR * %buildroot%mciddir/

%files
%mciddir

%changelog
* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1
- Version 4.0.0

* Mon Jan 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus

