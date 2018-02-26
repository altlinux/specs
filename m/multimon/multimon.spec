Summary:       Decodes a variety of digital transmission modes (DTMF,ZVEI,AX.25 etc)
Name:          multimon
Version:       0.1
Release:       alt1.1
License:       GPL v2
Group:         Sound
Source:        %name-%version.tar
URL:           http://www.baycom.org/~tom/ham/linux/multimon.html
BuildRequires: libX11-devel

%description
Decodes a variety of digital transmission modes (DTMF,ZVEI,AX.25 etc).

NOTE: renamed %_bindir/gen -> %_bindir/%name-gen

%prep
%setup 

%build
%make_build

%install
install -D -m 755 bin-$( uname -m )/multimon %buildroot/%_bindir/multimon
install -D -m 755 bin-$( uname -m )/gen %buildroot/%_bindir/%name-gen
install -D -m 755 bin-$( uname -m )/mkcostab %buildroot/%_bindir/mkcostab

%files
%_bindir/*

%changelog
* Sun Mar 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.1
- Renamed %_bindir/gen -> %_bindir/%name-gen

* Thu Feb 18 2010 Maxim Ivanov <redbaron at altlinux.org> 0.1-alt1
- Initial build for ALT Linux

