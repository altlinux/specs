Name:		kbookocr	
Version:	2.1.0
Release:	alt2
Summary:	Kbookocr - an intelligent system for recognition documents (OCR system)

License:	GPL
Group:		Graphics
URL:		http://kbookocr.blogspot.com/

Packager:	Andrey Cherepanov <cas@altlinux.org>

Source0:	KBookocr.tar.gz
Source1:	KBookocr.desktop
Patch1:		%name-fix-missing-libs.patch

BuildPreReq:    libksane4-devel
BuildRequires:  gcc-c++ 
BuildRequires:  libqt4-devel >= 4.7.0
BuildRequires:  libksane4
BuildRequires:  libpoppler-qt4-devel
#BuildRequires:  kde4graphics-devel # Only for p6

Requires: 	cuneiform tesseract

%description
Kbookocr - an intelligent system for recognition documents (OCR system).

%prep
%setup -q -n KBookocr
cp %SOURCE1 .
%patch1 -p2

%add_optflags -I%_K4includedir 
PREFIX=%prefix qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" "QMAKE_LFLAGS+=-L%_K4lib/devel" KBookocr.pro 

%build
%make_build

%install
make install INSTALL_ROOT=%buildroot
mkdir -p %buildroot%_bindir
install -m0755 KBookocr %buildroot%_bindir/%name
install -m0755 scripts/*.sh %buildroot%_bindir/
mkdir -p %buildroot%_desktopdir
install -m0644 KBookocr.desktop %buildroot%_desktopdir/KBookocr.desktop
mkdir -p %buildroot%_iconsdir
install -m0755 %name.png %buildroot%_iconsdir/%name.png

%files
%doc RoadMap.txt 
%_bindir/%name
%_bindir/*.sh
%_desktopdir/KBookocr.desktop
%_iconsdir/%name.png

%changelog
* Wed Jun 27 2012 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt2
- Fix build in Sisyphus

* Thu Oct 20 2011 Andrey Cherepanov <cas@altlinux.org> 2.1.0-alt1
- Initial build in Sisyphus

