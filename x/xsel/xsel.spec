Name:	 xsel
Version: 1.2.0.0.58.gef01f3c
Release: alt1
Summary: Command line clipboard and X selection tool

Group:   Graphical desktop/Other
License: MIT
URL:     http://www.vergenet.net/~conrad/software/xsel/

Source0: %name-%version.tar.gz

# Automatically added by buildreq on Mon Sep 28 2015
# optimized out: gnu-config libICE-devel libX11-devel xorg-xproto-devel
BuildRequires: imake libXt-devel xorg-cf-files

%description
XSel is a command line or script utility, similar to xclip, that can
copy the primary and secondary X selection, or any highlighted text, to
or from a file, stdin or stdout. It can also append to and delete the
clipboard or buffer that you would paste with the middle mouse button.

%prep
%setup -q

%build
%autoreconf
%configure
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog *txt README release_notes
%_bindir/%name
%_man1dir/%{name}.1x*

%changelog
* Thu Dec 19 2019 Fr. Br. George <george@altlinux.ru> 1.2.0.0.58.gef01f3c-alt1
- Update from upstream git

* Mon Sep 28 2015 Fr. Br. George <george@altlinux.ru> 1.2.0-alt2.git9674445
- Update from upstream git

* Mon Sep 28 2015 Fr. Br. George <george@altlinux.ru> 1.2.0-alt1
- Initial build from scratch (thanks to cas@ for the spec)

