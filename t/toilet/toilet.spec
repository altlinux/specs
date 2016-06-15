Name: toilet
Version: 0.3
Release: alt1

Summary: The Other Implementation's letters
License: DWTFYWTPL
Group: Text tools
Url: http://libcaca.zoy.org

# Repacked http://caca.zoy.org/raw-attachment/wiki/toilet/%name-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Wed Jun 15 2016
# optimized out: perl pkg-config python-base
BuildRequires: libcaca-devel zip

%description
TOIlet is in its very early development phase. It uses the powerful
libcucul library to achieve various text-based effects. TOIlet
implements or plans to implement the following features:
 * The ability to load FIGlet fonts
 * Support for Unicode input and output
 * Support for colour output
 * Support for various output formats: HTML, IRC, ANSI...

TOIlet also aims for full FIGlet compatibility. It is currently able to
load FIGlet fonts and perform horizontal smushing.

%prep
%setup -q -n %name-%version

%build
touch INSTALL
touch AUTHORS
%autoreconf

%configure

%make_build
%make_build fonts

%install
%make_install DESTDIR="%buildroot" install

%files
%_bindir/toilet
%_datadir/figlet
%_man1dir/toilet.*

%changelog
* Wed Jun 15 2016 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.3-alt1
- Updated to 0.3 (fixes FTBFS).

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.1-alt1.qa1
- NMU: rebuilt for debuginfo.

* Tue Nov 21 2006 Pavlov Konstantin <thresh@altlinux.ru> 0.1-alt1
- 0.1 release.


