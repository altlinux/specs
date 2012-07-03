Summary:      FMRadio plugin for xmms
Name:         xmms-fmradio
Version:      1.5
Release:      alt1.qa2
License:      GPL
Group:        Sound
Packager:     Alexey Shentzev <ashen@altlinux.org>
URL:          http://silicone.free.fr/xmms-FMRadio/
Source0:      %name-%version.tar.bz2
Patch0: xmms-fmradio-1.5-alt-v4l.patch
Provides:     xmms-fmradio
BuildRequires:	libxmms-devel libv4l-devel
Requires:     xmms 

%description
xmms-in-fmradio is a plugin with which you can use xmms as fm-radio receiver
create a file with the extension '.fmr', open this file and adjust the 
frequency by editing the file info. Enjoy !

%prep
%setup -q -n %name-%version
%patch0 -p2

%build
make

%install
mkdir -p %buildroot%_libdir/xmms/Input
cp libradio.so %buildroot/%_libdir/xmms/Input

%files
%defattr(-,root,root)
%doc INSTALL
%doc README
%_libdir/xmms/Input/libradio.so

%changelog
* Tue Jun 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5-alt1.qa2
- Fixed build

* Tue Nov 10 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.5-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for xmms-fmradio
  * postclean-05-filetriggers for spec file

* Wed Aug 15 2007 Alexey Shentzev <ashen@altlinux.ru> 1.5-alt1
- first build

