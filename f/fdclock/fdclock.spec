Name:		fdclock
Version:	20071208
Release:	alt3.1
Summary:	Freedesktop logo clock using cairo
Source:		%name-%version.tar
Patch: fdclock-20071208-alt-libpng15.patch
Group:		System/X11
License:	MIT

# Automatically added by buildreq on Mon Mar 14 2011
BuildRequires: libcairo-devel libpng-devel

%description
%summary

%prep
%setup
%patch -p0

%build
export FDCLOCK_LIBS="-lXrender -lcairo -lX11"
%autoreconf
%configure
%make_build

%install
%makeinstall

%files
%_bindir/*


%changelog
* Tue Dec 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 20071208-alt3.1
- Fixed build with libpng15

* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 20071208-alt3
- DSO list completion

* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 20071208-alt2
- Buildreq regenerated

* Tue May 25 2010 Fr. Br. George <george@altlinux.ru> 20071208-alt1
- Initial build

